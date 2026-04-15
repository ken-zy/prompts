#!/usr/bin/env python3
"""
normalize-links.py — Link vocabulary extractor and normalizer.

Usage:
    python3 scripts/normalize-links.py image              # extract vocab
    python3 scripts/normalize-links.py image merge.json   # apply merge map
    python3 scripts/normalize-links.py video              # extract vocab
    python3 scripts/normalize-links.py video merge.json   # apply merge map

Result files are read from:
    tmp/results_image/batch_*.json
    tmp/results_video/batch_*.json

Outputs:
    tmp/link_vocab_{pipeline}.json   — {link: count} sorted by count desc
    tmp/normalized_{pipeline}.json   — items with links replaced by merged names
"""

import json
import sys
import glob
import os
from collections import Counter


def strip_brackets(link: str) -> str:
    """Remove surrounding [[ and ]] from a link string."""
    s = link.strip()
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2]
    return s.strip()


def load_all_results(pipeline: str) -> list[dict]:
    """Load all batch JSON files for a pipeline and return a flat list of items."""
    pattern = os.path.join("tmp", f"results_{pipeline}", "batch_*.json")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"ERROR: no batch files found for pattern: {pattern}", file=sys.stderr)
        sys.exit(1)

    all_items = []
    for path in files:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        all_items.extend(data)

    print(f"Loaded {len(files)} batch files, {len(all_items)} total items for pipeline '{pipeline}'")
    return all_items


def extract_vocab(items: list[dict]) -> dict[str, int]:
    """Count occurrences of every link across all items."""
    counter: Counter = Counter()
    for item in items:
        for raw_link in item.get("links", []):
            link = strip_brackets(raw_link)
            if link:
                counter[link] += 1
    # Sort by count descending, then alphabetically for ties
    sorted_vocab = dict(sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))
    return sorted_vocab


def apply_merge_map(items: list[dict], merge_map: dict[str, str]) -> list[dict]:
    """
    Apply a merge map to all items.

    merge_map format: {"OldName": "CanonicalName", ...}
    Links not in the merge map are kept as-is.
    Duplicate links after merging are deduplicated while preserving order.
    """
    normalized = []
    for item in items:
        seen = []
        seen_set: set[str] = set()
        for raw_link in item.get("links", []):
            link = strip_brackets(raw_link)
            if not link:
                continue
            canonical = merge_map.get(link, link)
            if canonical not in seen_set:
                seen.append(canonical)
                seen_set.add(canonical)

        new_item = dict(item)
        new_item["links"] = seen
        # Also normalize primary if it appears in merge map
        new_item["primary"] = merge_map.get(item.get("primary", ""), item.get("primary", ""))
        normalized.append(new_item)
    return normalized


def ensure_tmp_dir() -> None:
    os.makedirs("tmp", exist_ok=True)


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pipeline = sys.argv[1]
    if pipeline not in ("image", "video"):
        print(f"ERROR: pipeline must be 'image' or 'video', got: {pipeline!r}", file=sys.stderr)
        sys.exit(1)

    merge_map_path = sys.argv[2] if len(sys.argv) >= 3 else None

    ensure_tmp_dir()
    items = load_all_results(pipeline)

    if merge_map_path is None:
        # --- Vocab extraction mode ---
        vocab = extract_vocab(items)
        out_path = os.path.join("tmp", f"link_vocab_{pipeline}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(vocab, f, ensure_ascii=False, indent=2)
        print(f"Wrote {len(vocab)} unique links to {out_path}")

        # Print top 30
        top30 = list(vocab.items())[:30]
        print(f"\nTop 30 links ({pipeline}):")
        for rank, (link, count) in enumerate(top30, 1):
            print(f"  {rank:>2}. {count:>5}  {link}")

    else:
        # --- Merge/normalize mode ---
        if not os.path.exists(merge_map_path):
            print(f"ERROR: merge map file not found: {merge_map_path}", file=sys.stderr)
            sys.exit(1)

        with open(merge_map_path, encoding="utf-8") as f:
            merge_map: dict[str, str] = json.load(f)
        print(f"Loaded merge map with {len(merge_map)} entries from {merge_map_path}")

        normalized = apply_merge_map(items, merge_map)
        out_path = os.path.join("tmp", f"normalized_{pipeline}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(normalized, f, ensure_ascii=False, indent=2)
        print(f"Wrote {len(normalized)} normalized items to {out_path}")


if __name__ == "__main__":
    main()
