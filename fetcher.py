"""
Agent 1 — arXiv fetcher (v0.1).

Fetches new submissions from cs.AI, cs.LG, and cs.CL,
deduplicates by arXiv ID, and prints a summary.

This is the fetcher only — no filtering, no LLM. That comes later.
"""

import feedparser
import requests
from bs4 import BeautifulSoup
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

def _html_to_text(html, max_chars=2000):
    """
    Strip HTML to plain text and truncate to a preview length.
    
    Substack post bodies are full essays; the filter only needs the opening
    to decide relevance. Truncating saves tokens on every filter call.
    """
    if not html:
        return ""
    
    # Parse the HTML and extract plain text.
    # get_text(separator=" ") joins block elements with spaces so paragraphs
    # don't run together as one wall of text.
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    
    # Truncate. ~2000 chars is roughly 500 tokens — plenty for relevance classification.
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
    
    return text

def fetch_interconnects():
    """Fetch recent posts from Interconnects (Nathan Lambert's Substack)."""
    url = "https://www.interconnects.ai/feed"
    
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    feed = feedparser.parse(response.text)
    
    items = []
    for entry in feed.entries:
        # Substack item identifier — the post URL is stable and unique.
        # We hash-friendly it by stripping the protocol and trailing slash.
        post_url = entry.link
        post_id = post_url.replace("https://", "").replace("http://", "").rstrip("/")
        
        # Substack puts the full post HTML in 'content' (richer) or 'summary' (shorter).
        # Prefer content if present.
        if hasattr(entry, "content") and entry.content:
            html_body = entry.content[0].value
        else:
            html_body = entry.get("summary", "")
        
        # Author is usually a single string for Substack.
        author = entry.get("author", "Nathan Lambert")
        authors = [author.strip()] if author else []
        
        item = {
            "id": post_id,
            "source": "interconnects",
            "title": entry.title,
            "authors": authors,
            "url": post_url,
            "published_at": entry.get("published", ""),
            "fetched_at": datetime.utcnow().isoformat(),
            "text": _html_to_text(html_body),
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
    
    print("\nFetching Interconnects...")
    ic_items = fetch_interconnects()
    print(f"  Total Interconnects items: {len(ic_items)}")
    
    # Combine.
    all_items = arxiv_items + hf_items + ic_items
    
    # Deduplicate by id.
    seen_ids = set()
    deduped = []
    for item in all_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            deduped.append(item)
    
    print(f"\nCombined unique items: {len(deduped)}")
    
    # Show one sample from each source.
    for source_name in ["arxiv", "hf_papers", "interconnects"]:
        print(f"\n--- Sample {source_name} item ---")
        for item in deduped:
            if item["source"] == source_name:
                print(f"[{item['id']}] {item['title']}")
                print(f"  Text preview: {item['text'][:250]}...")
                break
        else:
            print(f"  (no items from {source_name} this run)")
            print(f"  Abstract preview: {item['text'][:200]}...")
            break
