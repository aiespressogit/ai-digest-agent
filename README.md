# AI Digest Agent

An automated pipeline that reads the day's new AI research and writes a ranked weekly digest, so the papers worth reading surface without a daily manual trawl.

Every day, a few hundred new papers and posts land across arXiv, Hugging Face, and the major AI newsletters. Only a handful matter for a given focus, which here is **LLM-based agents and the frontier model capabilities behind them**. The agent fetches everything, has an LLM score each item against that focus, and keeps a rolling 7-day digest of the ones worth attention.

## How it works

```
GitHub Actions (daily cron)
   │
   ├─ 1. Fetch        arXiv cs.AI, cs.LG, cs.CL (RSS) · Hugging Face Daily Papers (API) · Interconnects (Substack RSS)
   ├─ 2. Dedupe       within the run (source:id key) and across runs (checkpoint of processed IDs)
   ├─ 3. Classify     Claude Haiku scores each new item 1–5 for relevance and 1–5 for depth, each with a one-line reason
   ├─ 4. Store        one CSV per day in data/items_YYYY-MM-DD.csv
   ├─ 5. Digest       rolling 7-day markdown digest in digests/digest_latest.md
   └─ 6. Commit       the workflow commits outputs back to the repo
```

**Digest tiers**
- **Read deeply:** relevance ≥ 4 and depth ≥ 3
- **Worth knowing:** relevance ≥ 3
- Everything else stays in the daily CSV and is left out of the digest.

## Design choices

- **Criterion in code.** The relevance criterion is a single versioned prompt in `filter.py`, so every change to what counts as relevant is tracked in git.
- **Cost guardrails.** A hard cap of 200 LLM calls per run, about $0.26 at worst, with token-based cost tracking. This sits on top of the provider-level spend cap.
- **No silent data loss.** Items are checkpointed only after a successful classification, so a failed or budget-capped item is retried on the next run.
- **Pinned model snapshot.** The model is pinned to a dated snapshot, not an alias, so scores stay comparable over time.
- **Defensive parsing.** The model's JSON output is validated, and a malformed response is logged as an error rather than crashing the run.

## Repo layout

| Path | What it holds |
|---|---|
| `main.py` | Daily orchestration: checkpoint → fetch → dedupe → classify → CSV → digest |
| `fetcher.py` | Source fetchers for arXiv, Hugging Face, and Interconnects |
| `filter.py` | LLM relevance and depth classifier, criterion, cost cap |
| `checkpoint.py` | Processed-ID store for cross-run deduplication |
| `.github/workflows/daily.yml` | Scheduled run (06:30 UTC) plus manual trigger |
| `data/` | Daily classified items (CSV) and the checkpoint |
| `digests/` | Latest rolling digest |

## Run it

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
python main.py
```

On GitHub, add `ANTHROPIC_API_KEY` as a repository secret. The workflow runs daily, or on demand from the Actions tab.

## Stack

Python 3.11 · pandas · feedparser · BeautifulSoup · Anthropic API (Claude Haiku 4.5) · GitHub Actions
