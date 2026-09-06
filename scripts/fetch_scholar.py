#!/usr/bin/env python3
"""Fetch Google Scholar metrics and write _data/scholar.yml.

Runs on GitHub Actions (see .github/workflows/scholar-metrics.yml).
Uses the `scholarly` package, which needs no API key. Google Scholar
occasionally rate-limits/CAPTCHAs datacenter IPs; the script retries a
few times and, if it still cannot get a real citation count, exits
non-zero WITHOUT touching scholar.yml so a bad run never wipes the
numbers already on the site.
"""

import datetime
import os
import sys
import time

from scholarly import scholarly

SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "JnC6fesAAAAJ")
OUT_PATH = os.environ.get("SCHOLAR_OUT", "_data/scholar.yml")
MAX_TRIES = 4


def fetch():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices"])
    return (
        int(author.get("citedby", 0) or 0),
        int(author.get("hindex", 0) or 0),
        int(author.get("i10index", 0) or 0),
    )


def main():
    citations = hindex = i10 = 0
    for attempt in range(1, MAX_TRIES + 1):
        try:
            citations, hindex, i10 = fetch()
            if citations > 0:
                break
            print(f"[try {attempt}] Empty result, retrying...", file=sys.stderr)
        except Exception as exc:  # network / CAPTCHA / parse
            print(f"[try {attempt}] {type(exc).__name__}: {exc}", file=sys.stderr)
        time.sleep(15 * attempt)

    if citations <= 0:
        print(
            "Could not retrieve a valid citation count after "
            f"{MAX_TRIES} tries. Leaving {OUT_PATH} unchanged.",
            file=sys.stderr,
        )
        sys.exit(1)

    today = datetime.date.today().isoformat()
    content = (
        "# Auto-updated by .github/workflows/scholar-metrics.yml — do not edit by hand.\n"
        f"citations: {citations}\n"
        f"h_index: {hindex}\n"
        f"i10_index: {i10}\n"
        f'updated: "{today}"\n'
    )
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(content)


if __name__ == "__main__":
    main()
