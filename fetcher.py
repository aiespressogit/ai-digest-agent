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

def _clean_arxiv_summary(summary):
    """
    arXiv RSS descriptions start with metadata like:
      'arXiv:2604.26091v1 Announce Type: new \nAbstract: <real abstract>'
    Strip everything before 'Abstract:' so 'text' contains just the abstract.
    Falls back to the raw summary if the marker isn't found.
    """
    marker = "Abstract:"
    if marker in summary:
        return summary.split(marker, 1)[1].strip()
    return summary.strip()

def fetch_hf_daily():
    """Fetch papers from Hugging Face's daily papers feed."""
    url = "https://huggingface.co/api/daily_papers"
    
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    # HF returns JSON directly. .json() parses it into a Python list of dicts.
    data = response.json()
    
    items = []
    for entry in data:
        # The actual paper object is nested under "paper".
        paper = entry.get("paper", {})
        
        # Skip entries without a paper object (shouldn't happen, but defensive).
        if not paper:
            continue
        
        paper_id = paper.get("id", "")
        if not paper_id:
            continue
        
        # Authors are a list of objects like [{"name": "..."}, ...]. Extract names.
        authors_raw = paper.get("authors", [])
        authors = [a.get("name", "").strip() for a in authors_raw if a.get("name")]
        
        item = {
            "id": paper_id,
            "source": "hf_papers",
            "title": paper.get("title", "").strip(),
            "authors": authors,
            "url": f"https://huggingface.co/papers/{paper_id}",
            "published_at": paper.get("publishedAt", ""),
            "fetched_at": datetime.utcnow().isoformat(),
            "text": paper.get("summary", "").strip(),
            "raw": entry,
            
            # HF-specific extra: community upvote count. Useful signal later.
            "upvotes": paper.get("upvotes", 0),
            
            # Filter fields, populated later.
            "relevant": None,
            "relevance_score": None,
            "relevance_why": None,
            "depth_score": None,
            "depth_why": None,
        }
        items.append(item)
    
    return items
    
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
            "text": _clean_arxiv_summary(entry.summary),
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
    arxiv_items = fetch_arxiv_all()
    print(f"  Total unique arXiv items: {len(arxiv_items)}")
    
    print("\nFetching Hugging Face Daily Papers...")
    hf_items = fetch_hf_daily()
    print(f"  Total HF items: {len(hf_items)}")
    
    # Combine all items.
    all_items = arxiv_items + hf_items
    
    # Deduplicate across sources by id. arXiv and HF can point to the same paper.
    seen_ids = set()
    deduped = []
    for item in all_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            deduped.append(item)
    
    print(f"\nCombined unique items: {len(deduped)}")
    
    # Show one sample from each source so we can confirm both are working.
    print("\n--- Sample arXiv item ---")
    for item in deduped:
        if item["source"] == "arxiv":
            print(f"[{item['id']}] {item['title']}")
            print(f"  Abstract preview: {item['text'][:200]}...")
            break
    
    print("\n--- Sample HF item ---")
    for item in deduped:
        if item["source"] == "hf_papers":
            print(f"[{item['id']}] {item['title']}")
            print(f"  Upvotes: {item['upvotes']}")
            print(f"  Abstract preview: {item['text'][:200]}...")
            break
