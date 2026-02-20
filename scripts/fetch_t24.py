import json
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

AUTHOR_URL = "https://m.t24.com.tr/yazarlar/ozancan-ozdemir"
OUT_PATH = "_data/t24.json"
LIMIT = 6

def clean(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()

def main():
    r = requests.get(AUTHOR_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    items = []
    for a in soup.select('a[href*="/yazarlar/ozancan-ozdemir/"]'):
        href = a.get("href") or ""
        title = clean(a.get_text(" ", strip=True))
        if not title:
            continue

        url = href if href.startswith("http") else f"https://t24.com.tr{href}"
        # T24 yazı linkleri genelde %2C içeriyor ama her zaman şart koşmayalım
        if "/yazarlar/ozancan-ozdemir/" in url:
            items.append({"title": title, "url": url})

    # URL’e göre tekilleştir + ilk LIMIT
    seen = set()
    uniq = []
    for it in items:
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        uniq.append(it)
        if len(uniq) >= LIMIT:
            break

    payload = {
        "source": AUTHOR_URL,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "items": uniq,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(uniq)} items to {OUT_PATH}")

if __name__ == "__main__":
    main()
