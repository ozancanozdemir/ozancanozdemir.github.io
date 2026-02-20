import json
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

AUTHOR_URL = "https://t24.com.tr/yazarlar/ozancan-ozdemir"
OUT_PATH = "_data/t24.json"
LIMIT = 6

def clean(s):
    return re.sub(r"\s+", " ", s).strip()

def main():
    r = requests.get(AUTHOR_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # T24 yazar sayfasında yazılar genelde liste halinde geliyor.
    # Bu seçiciler zamanla değişebilir; değişirse sadece burayı güncellersin.
    items = []
    for a in soup.select("a"):
        href = a.get("href") or ""
        txt = clean(a.get_text(" ", strip=True))
        # Yazar yazılarının URL pattern'i genelde: /yazarlar/ozancan-ozdemir/<slug>%2C<id>
        if "/yazarlar/ozancan-ozdemir/" in href and "%2C" in href and txt:
            url = href if href.startswith("http") else f"https://t24.com.tr{href}"
            items.append((txt, url))

    # tekilleştir
    seen = set()
    uniq = []
    for title, url in items:
        if url in seen:
            continue
        seen.add(url)
        uniq.append({"title": title, "url": url})

    # ilk gelenler genelde en yeni; yine de garanti değilse sonradan sıralama eklenebilir.
    uniq = uniq[:LIMIT]

    payload = {
        "source": AUTHOR_URL,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "items": uniq
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(uniq)} items to {OUT_PATH}")

if __name__ == "__main__":
    main()
