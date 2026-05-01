"""
Checkpoint: persistent record of which items the agent has already processed.

Stored as data/processed_ids.json — a flat list of composite IDs ("source:id"),
sorted for clean git diffs. Read into a set at runtime for O(1) membership checks.
"""

import json
import os
from pathlib import Path

# Where the checkpoint lives. Path() handles slashes correctly across OSes.
CHECKPOINT_PATH = Path("data/processed_ids.json")


def _composite_id(item):
    """
    Build the composite ID used as the memory key.
    
    Items keep their source-native id (e.g., "2604.26999"), but memory
    is indexed by source:id so that the same arxiv id appearing in
    arxiv and hf_papers are tracked separately.
    """
    return f"{item['source']}:{item['id']}"


def load_processed_ids():
    """
    Load the set of already-processed composite IDs.
    
    Returns an empty set if the file doesn't exist (first run) or is
    malformed (defensive: better to start fresh than crash the workflow).
    """
    if not CHECKPOINT_PATH.exists():
        print(f"  No checkpoint found at {CHECKPOINT_PATH}. Starting fresh.")
        return set()
    
    try:
        with open(CHECKPOINT_PATH, "r") as f:
            data = json.load(f)
        # Expect a list of strings. Convert to set for fast lookups.
        return set(data)
    except (json.JSONDecodeError, TypeError) as e:
        # Corrupted file. Log and start over rather than crash.
        print(f"  Warning: checkpoint at {CHECKPOINT_PATH} is corrupted ({e}). Starting fresh.")
        return set()


def filter_unseen(items, processed_ids):
    """
    Return only items whose composite ID is not in the processed set.
    
    Pure function: doesn't modify the input set, doesn't write anything.
    The caller decides what to do with the unseen items.
    """
    unseen = []
    for item in items:
        if _composite_id(item) not in processed_ids:
            unseen.append(item)
    return unseen


def save_processed_ids(processed_ids, newly_processed_items):
    """
    Add newly-processed items' composite IDs to the set, write back to disk.
    
    Sorted for stable git diffs — when the file changes, you can see exactly
    which IDs were added in any given commit.
    """
    # Make sure the data/ directory exists.
    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Add the new IDs to the existing set.
    updated = set(processed_ids)
    for item in newly_processed_items:
        updated.add(_composite_id(item))
    
    # Serialize as a sorted list. JSON has no native set type.
    with open(CHECKPOINT_PATH, "w") as f:
        json.dump(sorted(updated), f, indent=2)
    
    print(f"  Checkpoint updated: {len(updated)} total IDs ({len(newly_processed_items)} new this run).")
  
if __name__ == "__main__":
    # Quick self-test. Simulates two runs.
    
    print("=== Checkpoint self-test ===\n")
    
    # Pretend these are items from a fetcher.
    fake_items_run1 = [
        {"id": "2604.26999", "source": "arxiv"},
        {"id": "2604.27085", "source": "hf_papers"},
        {"id": "post-abc", "source": "interconnects"},
    ]
    
    fake_items_run2 = [
        {"id": "2604.26999", "source": "arxiv"},      # already seen
        {"id": "2604.27500", "source": "arxiv"},      # new
        {"id": "post-abc", "source": "interconnects"}, # already seen
        {"id": "post-xyz", "source": "interconnects"}, # new
    ]
    
    # --- Run 1 ---
    print("Run 1:")
    processed = load_processed_ids()
    print(f"  Loaded {len(processed)} processed IDs")
    
    unseen = filter_unseen(fake_items_run1, processed)
    print(f"  {len(unseen)} unseen out of {len(fake_items_run1)} fetched")
    
    save_processed_ids(processed, unseen)
    
    # --- Run 2 ---
    print("\nRun 2:")
    processed = load_processed_ids()
    print(f"  Loaded {len(processed)} processed IDs")
    
    unseen = filter_unseen(fake_items_run2, processed)
    print(f"  {len(unseen)} unseen out of {len(fake_items_run2)} fetched")
    
    for item in unseen:
        print(f"    new: {item['source']}:{item['id']}")
    
    save_processed_ids(processed, unseen)
    
    print("\n=== Self-test complete ===")
