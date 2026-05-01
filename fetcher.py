"""
Agent 1 — arXiv fetcher (v0.1).

Fetches new submissions from cs.AI, cs.LG, and cs.CL,
deduplicates by arXiv ID, and prints a summary.

This is the fetcher only — no filtering, no LLM. That comes later.
"""

import feedparser
import requests
from datetime import datetime

# The three arXiv categories we monitor.
ARXIV_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL"]


def fetch_arxiv(category):
    """Fetch new submissions from one arXiv category."""
    url = f"https://rss.arxiv.org/rss/{category}"
    
    # Download the feed. 30s timeout so a hung connection doesn't freeze us.
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    # Parse the XML.
    feed = feedparser.parse(response.text)
    
    items = []
    for entry in feed.entries:
        # Skip revisions of existing papers — we only want new submissions.
        announce_type = entry.get("arxiv_announce_type", "")
        if announce_type != "new":
            continue
        
        # Extract the arXiv ID from the URL (e.g., "2404.12345" from ".../abs/2404.12345").
        arxiv_id = entry.link.split("/abs/")[-1]
        
        # Authors come as a comma-separated string. Split, strip, drop empties.
        authors_raw = entry.get("author", "")
        authors = [a.strip() for a in authors_raw.split(",") if a.strip()]
        
        item = {
            "id": arxiv_id,
            "source": "arxiv",
            "title": entry.title,
            "authors": authors,
            "url": entry.link,
            "published_at": entry.get("published", ""),
            "fetched_at": datetime.utcnow().isoformat(),
            "text": entry.summary,
            "raw": dict(entry),
            
            # Filter fields, populated later.
            "relevant": None,
            "relevance_score": None,
            "relevance_why": None,
            "depth_score": None,
            "depth_why": None,
        }
        items.append(item)
    
    return items


def fetch_arxiv_all():
    """Fetch from all categories, dedupe by id, return combined list."""
    all_items = []
    for category in ARXIV_CATEGORIES:
        category_items = fetch_arxiv(category)
        print(f"  {category}: {len(category_items)} new items")
        all_items.extend(category_items)
    
    # Deduplicate. Keep first occurrence of each arXiv ID.
    seen_ids = set()
    deduped = []
    for item in all_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            deduped.append(item)
    
    return deduped


# This block runs when the file is executed directly (which is what GitHub Actions does).
if __name__ == "__main__":
    print("Fetching arXiv...")
    items = fetch_arxiv_all()
    
    print(f"\nTotal unique items: {len(items)}")
    
    # Show the first 3 so we can sanity-check the data shape.
    print("\n--- Sample items ---")
    for item in items[:3]:
        print(f"\n[{item['id']}] {item['title']}")
        print(f"  Authors: {', '.join(item['authors'][:3])}{'...' if len(item['authors']) > 3 else ''}")
        print(f"  URL: {item['url']}")
        print(f"  Abstract preview: {item['text'][:200]}...")
