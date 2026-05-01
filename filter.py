"""
Filter: classify each candidate item against the locked criterion.

For each item, makes one LLM call. Returns the item with relevance and
depth scores plus one-sentence reasons attached. Items that fail the
criterion get scores of 0.

Single-call design: applies Layer 1 (scope), Layer 2 (substance), and
Layer 3 (exclusions) jointly. Trade-off: lower cost and latency, less
visibility into which layer rejected an item. The reason field gives
us most of that visibility back.
"""

import json
import os
from anthropic import Anthropic

# Pinned snapshot. Use the snapshot ID, not the alias "claude-haiku-4-5".
# Snapshots give reproducible behavior; aliases drift when Anthropic updates the tier.
# Check https://docs.claude.com/en/docs/about-claude/models/overview before swapping.
MODEL = "claude-haiku-4-5-20251001"
MODEL = "claude-haiku-4-5-20251001"

# Initialize once. Reads ANTHROPIC_API_KEY from environment automatically.
_client = Anthropic()

# Cost-cap parameters. Hard-stops the filter run when limits are hit.
MAX_CALLS_PER_RUN = 200          # at ~$0.0013/call, ~$0.26 per run
HAIKU_INPUT_PER_MTOK = 1.00      # USD per million input tokens
HAIKU_OUTPUT_PER_MTOK = 5.00     # USD per million output tokens

# Module-level counters reset each Python invocation.
_call_count = 0
_total_input_tokens = 0
_total_output_tokens = 0


def _estimated_cost():
    """Cost so far this run, in USD."""
    return (
        _total_input_tokens / 1_000_000 * HAIKU_INPUT_PER_MTOK
        + _total_output_tokens / 1_000_000 * HAIKU_OUTPUT_PER_MTOK
    )


def _budget_exceeded():
    """True when we should stop calling the API."""
    return _call_count >= MAX_CALLS_PER_RUN

# The criterion, locked earlier. Lives here as a single string so changes
# to the criterion are tracked in version control alongside the code.
CRITERION = """\
You are filtering items for a learner tracking the frontier of AI research, \
specifically work on LLM-based agents and the model capabilities that enable them.

INCLUDE items that fall into either category:
  (a) LLM-based agents directly: reasoning, planning, tool use, memory, \
evaluation, deployment.
  (b) Frontier model capabilities, training methods, or releases that \
materially affect what agents can do: capability emergence, new training \
approaches, safety thresholds, major model launches from frontier labs.

REQUIRE that the item contains at least one of:
  - methodology (how something is built, what mechanisms work, why)
  - concrete results (specific evaluations, benchmark numbers, case studies)
  - explicit limitations of prior work that motivate the contribution

EXCLUDE:
  - sub-frontier work without architectural insight (e.g., specialized small-model results)
  - pure capability demos without methodology ("we built X, here's a video")
  - funding, hiring, and corporate news without technical substance
  - adjacent fields (image generation, robotics hardware, voice synthesis) \
unless directly tied to LLM agent capabilities

Use the term "agent" carefully: a paper using "agent" in a robotics/control \
sense (e.g., a mobile sensing agent) is NOT in scope unless the work is \
fundamentally about LLM-based reasoning."""


def _build_prompt(item):
    """
    Build the per-item user message.
    
    Keeps the criterion fixed (system) and the per-item content compact (user).
    This positions the criterion for prompt caching later if we want it.
    """
    return f"""Classify the following item.

Title: {item['title']}
Source: {item['source']}
Text: {item['text'][:2000]}

Return a JSON object with exactly these fields:
{{
  "relevance": <integer 0-5>,
  "relevance_why": "<one sentence>",
  "depth": <integer 0-5>,
  "depth_why": "<one sentence>"
}}

Scoring guide:
  relevance: 0 = clearly off-criterion (failed Layer 1 or 3); 1-2 = tangentially related;
             3 = on-topic but not central; 4 = squarely on-criterion; 5 = high-priority match.
  depth:     0 = no substance (failed Layer 2); 1-2 = thin / incremental;
             3 = solid contribution; 4 = substantial methodology or results; 5 = paradigm-shaping.

If the item fails Layer 1 (out of scope) or Layer 3 (exclusion), set both \
scores to 0 and explain in the reasons.
If the item is in scope but fails Layer 2 (no substance), set depth to 0 \
and relevance to at most 2.

Return ONLY the JSON object. No prose before or after."""


def classify_item(item):
    global _call_count, _total_input_tokens, _total_output_tokens
    
    # Hard stop if we're past the per-run cap.
    if _budget_exceeded():
        result = dict(item)
        result["relevance_score"] = None
        result["depth_score"] = None
        result["relevance_why"] = "SKIPPED: per-run call cap reached"
        result["depth_why"] = ""
        result["relevant"] = False
        result["filter_error"] = "budget_cap"
        return result
    
    try:
        response = _client.messages.create(
            model=MODEL,
            max_tokens=400,
            system=CRITERION,
            messages=[{"role": "user", "content": _build_prompt(item)}],
        )
        
        # Track cost.
        _call_count += 1
        _total_input_tokens += response.usage.input_tokens
        _total_output_tokens += response.usage.output_tokens
        
        # ... rest of the function unchanged
    """
    Send one item to the LLM, return the item with classification fields populated.
    
    Defensive: catches API errors, malformed JSON, and missing fields.
    On any failure, returns the item with relevance=None and an error in
    relevance_why so it's visible downstream.
    """
    try:
        response = _client.messages.create(
            model=MODEL,
            max_tokens=400,           # ~200 tokens for the JSON, with headroom
            system=CRITERION,
            messages=[{"role": "user", "content": _build_prompt(item)}],
        )
        
        # Response content is a list of blocks; we expect one text block.
        raw_text = response.content[0].text.strip()
        
        # Defensive: model may include surrounding prose despite "JSON only".
        # Find the first '{' and last '}' to extract the JSON.
        json_start = raw_text.find("{")
        json_end = raw_text.rfind("}") + 1
        if json_start == -1 or json_end <= json_start:
            raise ValueError(f"No JSON object found in response: {raw_text[:200]}")
        
        parsed = json.loads(raw_text[json_start:json_end])
        
        # Validate the shape. Missing keys would silently break downstream.
        for key in ("relevance", "relevance_why", "depth", "depth_why"):
            if key not in parsed:
                raise ValueError(f"Missing key '{key}' in response: {parsed}")
        
        # Attach to a copy of the item so we don't mutate the input.
        result = dict(item)
        result["relevance_score"] = int(parsed["relevance"])
        result["relevance_why"] = str(parsed["relevance_why"])
        result["depth_score"] = int(parsed["depth"])
        result["depth_why"] = str(parsed["depth_why"])
        result["relevant"] = result["relevance_score"] >= 3
        result["filter_error"] = None
        return result
        
    except Exception as e:
        # Don't crash the whole batch on one bad call. Mark and move on.
        result = dict(item)
        result["relevance_score"] = None
        result["depth_score"] = None
        result["relevance_why"] = f"FILTER ERROR: {type(e).__name__}: {str(e)[:200]}"
        result["depth_why"] = ""
        result["relevant"] = False
        result["filter_error"] = str(e)
        return result


def classify_items(items, verbose=True):
    """
    Classify a list of items. Sequential — one LLM call per item.
    
    Could be parallelized later (the Anthropic SDK supports async), but
    sequential is simpler to debug and the 300-item case takes ~5 minutes.
    """
    results = []
    for i, item in enumerate(items):
        if verbose:
            print(f"  [{i+1}/{len(items)}] {item['source']}:{item['id']} — {item['title'][:80]}")
        result = classify_item(item)
        results.append(result)
        if verbose and result["filter_error"] is None:
            print(f"      relevance={result['relevance_score']}, depth={result['depth_score']}")
        elif verbose:
            print(f"      ERROR: {result['filter_error'][:100]}")
    print(f"\n  --- Filter run summary ---")
    print(f"  API calls made: {_call_count}")
    print(f"  Input tokens:   {_total_input_tokens:,}")
    print(f"  Output tokens:  {_total_output_tokens:,}")
    print(f"  Estimated cost: ${_estimated_cost():.4f}")
    return results


# Self-test: classify three hand-picked items, print the results.
# We use the three IDs we flagged earlier as good test cases.
if __name__ == "__main__":
    test_items = [
        {
            "id": "2604.26091",
            "source": "arxiv",
            "title": "Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital",
            "text": "We study reliability in autonomous language-model agents that translate user mandates into validated tool actions under real capital. The setting is DX Terminal Pro, a 21-day deployment in which 3,505 user requests were processed by an LLM agent with operating-layer controls.",
        },
        {
            "id": "2604.26095",
            "source": "arxiv",
            "title": "Distill-Belief: Closed-Loop Inverse Source Localization and Characterization in Physical Fields",
            "text": "Closed-loop inverse source localization and characterization (ISLC) requires a mobile agent to select measurements that localize sources and infer latent field parameters under strict time constraints. We propose a distillation method that compresses belief updates into a compact policy.",
        },
        {
            "id": "2604.26106",
            "source": "arxiv",
            "title": "Evaluating Strategic Reasoning in Forecasting Agents",
            "text": "Forecasting benchmarks produce accuracy leaderboards but little insight into why some forecasters are more accurate than others. We introduce Bench to the Future 2 (BTF-2), 1,417 pastcasting questions designed to evaluate strategic reasoning in LLM-based forecasting agents.",
        },
    ]
    
    print("=== Filter self-test on three items ===\n")
    results = classify_items(test_items)
    
    print("\n=== Results ===")
    for r in results:
        print(f"\n[{r['source']}:{r['id']}] {r['title']}")
        print(f"  Relevance: {r['relevance_score']} — {r['relevance_why']}")
        print(f"  Depth:     {r['depth_score']} — {r['depth_why']}")
        print(f"  Verdict:   {'KEEP' if r['relevant'] else 'DROP'}")
