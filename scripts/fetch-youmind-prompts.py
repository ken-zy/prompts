#!/usr/bin/env python3
"""Fetch all Nano Banana Pro prompts from YouMind API and save as JSON."""

import json
import time
import sys
import urllib.request

API_URL = "https://youmind.com/youhome-api/prompts"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://youmind.com/zh-CN/nano-banana-pro-prompts",
    "Origin": "https://youmind.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
}
OUTPUT_FILE = "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json"
LIMIT = 100  # max per page
MODEL = "nano-banana-pro"
LOCALE = "zh-CN"


def fetch_page(page: int) -> dict:
    payload = json.dumps({
        "model": MODEL,
        "page": page,
        "limit": LIMIT,
        "locale": LOCALE,
    }).encode()
    req = urllib.request.Request(API_URL, data=payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def main():
    all_prompts = []
    page = 1

    # First request to get total
    data = fetch_page(page)
    total = data["total"]
    total_pages = data["totalPages"]
    all_prompts.extend(data["prompts"])
    print(f"Total: {total}, Pages: {total_pages}, Got page 1 ({len(data['prompts'])} items)")

    page = 2
    while page <= total_pages:
        try:
            data = fetch_page(page)
            all_prompts.extend(data["prompts"])
            if page % 10 == 0 or page == total_pages:
                print(f"Page {page}/{total_pages}, collected {len(all_prompts)}/{total}")
            page += 1
            time.sleep(0.3)  # rate limit
        except Exception as e:
            print(f"Error on page {page}: {e}, retrying in 3s...")
            time.sleep(3)

    print(f"\nDone! Collected {len(all_prompts)} prompts total.")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "total": total,
            "prompts": all_prompts,
            "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }, f, ensure_ascii=False, indent=None)

    print(f"Saved to {OUTPUT_FILE}")
    # Print file size
    import os
    size_mb = os.path.getsize(OUTPUT_FILE) / 1024 / 1024
    print(f"File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
