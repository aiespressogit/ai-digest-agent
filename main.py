"""
Agent 1 — daily orchestration.

Sequence:
  1. Load checkpoint of processed item IDs
  2. Fetch from arXiv, HF Daily Papers, Interconnects
  3. Filter out items already in checkpoint
  4. Classify new items via the LLM filter
  5. Write today's CSV
  6. Regenerate rolling 7-day digest
  7. Save checkpoint
"""

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from fetcher import fetch_arxiv_all, fetch_hf_daily, fetch_interconnects
from checkpoint import load_processed_ids, filter_unseen, save_processed_ids
from filter import classify_items


# Where outputs land. Match the directory layout we set up earlier.
DATA_DIR = Path("data")
DIGESTS_DIR = Path("digests")

# Rolling window for the digest. 7 days = one week of context.
DIGEST_WINDOW_DAYS = 7


def fetch_all():
    """Run every source's fetcher, combine, dedupe within this run."""
    print("Fetching arXiv...")
    arxiv_items = fetch_arxiv_all()
    print(f"  Total unique arXiv items: {len(arxiv_items)}")

    print("Fetching Hugging Face Daily Papers...")
    hf_items = fetch_hf_daily()
    print(f"  Total HF items: {len(hf_items)}")

    print("Fetching Interconnects...")
    ic_items = fetch_interconnects()
    print(f"  Total Interconnects items: {len(ic_items)}")

    all_items = arxiv_items + hf_items + ic_items

    # Dedupe within this run by composite source:id key.
    # (Cross-source dups can happen — same paper in arXiv and HF.)
    seen = set()
    deduped = []
    for item in all_items:
        key = f"{item['source']}:{item['id']}"
        if key not in seen:
            seen.add(key)
            deduped.append(item)

    print(f"Combined unique items this run: {len(deduped)}")
    return deduped


def write_run_csv(classified_items, run_date):
    """
    Write today's classified items to data/items_YYYY-MM-DD.csv.

    Drops the verbose 'raw' field — it's useful for debugging but not
    for analysis, and including it would bloat the CSV.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = DATA_DIR / f"items_{run_date}.csv"

    # Strip 'raw' field; keep everything else.
    rows = []
    for item in classified_items:
        row = {k: v for k, v in item.items() if k != "raw"}
        # Authors is a list — flatten to a single semicolon-separated string for CSV.
        if isinstance(row.get("authors"), list):
            row["authors"] = "; ".join(row["authors"])
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)
    print(f"  Wrote {len(df)} rows to {csv_path}")
    return csv_path


def build_digest():
    """
    Read recent CSVs, build a rolling N-day markdown digest.

    Items are grouped into tiers:
      - Read deeply: relevance >= 4 AND depth >= 3
      - Worth knowing: relevance >= 3
      - Skim if time: relevance == 2 (currently dropped — adjust if useful)

    Items below relevance 3 are excluded from the digest entirely.
    """
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)

    # Find CSVs in the last N days.
    cutoff = datetime.now(timezone.utc).date() - timedelta(days=DIGEST_WINDOW_DAYS - 1)
    csv_files = sorted(DATA_DIR.glob("items_*.csv"))

    recent_dfs = []
    for csv_path in csv_files:
        try:
            # Filename format: items_2026-05-01.csv -> extract date.
            date_str = csv_path.stem.replace("items_", "")
            file_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if file_date >= cutoff:
                recent_dfs.append(pd.read_csv(csv_path))
        except (ValueError, pd.errors.EmptyDataError) as e:
            print(f"  Skipping {csv_path}: {e}")

    if not recent_dfs:
        print("  No recent CSVs to build digest from.")
        return None

    df = pd.concat(recent_dfs, ignore_index=True)

    # Defensive: drop rows where the filter errored out.
    df = df[df["filter_error"].isna()]

    # Score columns can be float (NaN-coerced) or int. Cast safely.
    df["relevance_score"] = pd.to_numeric(df["relevance_score"], errors="coerce")
    df["depth_score"] = pd.to_numeric(df["depth_score"], errors="coerce")

    # Build tiers.
    read_deeply = df[(df["relevance_score"] >= 4) & (df["depth_score"] >= 3)]
    worth_knowing = df[(df["relevance_score"] >= 3) & ~df.index.isin(read_deeply.index)]

    # Sort each tier by relevance then depth, descending.
    read_deeply = read_deeply.sort_values(
        ["relevance_score", "depth_score"], ascending=False
    )
    worth_knowing = worth_knowing.sort_values(
        ["relevance_score", "depth_score"], ascending=False
    )

    # Format as markdown.
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        f"# AI digest — {today}",
        f"",
        f"Rolling {DIGEST_WINDOW_DAYS}-day window. Generated automatically.",
        f"",
        f"---",
        f"",
        f"## Read deeply ({len(read_deeply)} items)",
        f"",
        f"_High relevance and substantial depth — worth full attention._",
        f"",
    ]
    lines.extend(_format_items(read_deeply))

    lines.extend([
        f"",
        f"## Worth knowing ({len(worth_knowing)} items)",
        f"",
        f"_On-criterion but lower depth, or peripheral relevance._",
        f"",
    ])
    lines.extend(_format_items(worth_knowing))

    digest_path = DIGESTS_DIR / "digest_latest.md"
    digest_path.write_text("\n".join(lines))
    print(f"  Wrote digest with {len(read_deeply)} deep + {len(worth_knowing)} worth-knowing items to {digest_path}")
    return digest_path


def _format_items(df):
    """Render a DataFrame of items as markdown."""
    if len(df) == 0:
        return ["_(none)_", ""]
    lines = []
    for _, row in df.iterrows():
        authors = row.get("authors", "")
        # Truncate long author lists.
        if isinstance(authors, str) and len(authors) > 100:
            authors = authors[:100] + "..."
        lines.append(f"### [{row['title']}]({row['url']})")
        lines.append(f"**Source:** {row['source']} | **Authors:** {authors}")
        lines.append(f"**Relevance:** {int(row['relevance_score'])}/5 — {row['relevance_why']}")
        lines.append(f"**Depth:** {int(row['depth_score'])}/5 — {row['depth_why']}")
        lines.append("")
    return lines


def main():
    """Run the agent's daily routine."""
    run_date = datetime.now(timezone.utc).date().isoformat()
    print(f"=== Agent 1 daily run — {run_date} ===\n")

    # 1. Load checkpoint.
    print("Loading checkpoint...")
    processed_ids = load_processed_ids()
    print(f"  {len(processed_ids)} previously-processed IDs loaded.\n")

    # 2. Fetch.
    all_items = fetch_all()

    # 3. Filter against checkpoint.
    new_items = filter_unseen(all_items, processed_ids)
    print(f"\n{len(new_items)} items new since last run (out of {len(all_items)} fetched).\n")

    if not new_items:
        print("Nothing new to classify. Rebuilding digest from existing CSVs anyway.")
        build_digest()
        return

    # 4. Classify.
    print("Classifying new items...\n")
    classified = classify_items(new_items)
    print()

    # 5. Write CSV.
    print("Writing today's CSV...")
    write_run_csv(classified, run_date)

    # 6. Rebuild digest.
    print("\nBuilding rolling digest...")
    build_digest()

    # 7. Save checkpoint. Only mark items as processed if the filter
    #    actually ran (not budget-capped, not errored). This way a
    #    failed item gets retried next run rather than being silently lost.
    successfully_processed = [
        item for item in classified if item.get("filter_error") is None
    ]
    save_processed_ids(processed_ids, successfully_processed)

    print(f"\n=== Run complete ===")


if __name__ == "__main__":
    main()
