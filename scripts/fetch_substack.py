import json
from datetime import datetime
import requests
import xml.etree.ElementTree as ET

# Eğer bu URL çalışmazsa, Substack yayın adresini yaz:
# örn: https://YOURPUBLICATION.substack.com/feed
FEED_URL = "https://ozancanozdemir.substack.com/feed"
OUT_PATH = "_data/substack.json"
LIMIT = 6

def strip(tag: str) -> str:
    return tag.split("}", 1)[-1]  # namespaced tag'leri temizler

def main():
    r = requests.get(FEED_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()

    root = ET.fromstring(r.text)
    channel = None
    for child in root:
        if strip(child.tag) == "channel":
            channel = child
            break
    if channel is None:
        raise RuntimeError("RSS channel not found. Feed URL doğru mu?")

    items = []
    for item in channel:
        if strip(item.tag) != "item":
            continue
        title = link = pubDate = None
        for x in item:
            t = strip(x.tag)
            if t == "title":
                title = (x.text or "").strip()
            elif t == "link":
                link = (x.text or "").strip()
            elif t == "pubDate":
                pubDate = (x.text or "").strip()

        if title and link:
            items.append({"title": title, "url": link, "date": pubDate})

        if len(items) >= LIMIT:
            break

    payload = {
        "source": FEED_URL,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "items": items
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(items)} items to {OUT_PATH}")

if __name__ == "__main__":
    main()
