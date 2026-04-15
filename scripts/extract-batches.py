#!/usr/bin/env python3
"""
Extract lightweight batch files from raw prompt JSON for subagent processing.

Usage:
    python3 scripts/extract-batches.py image
    python3 scripts/extract-batches.py video
"""

import json
import math
import os
import sys

BATCH_SIZE = 300

PIPELINES = {
    "image": "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json",
    "video": "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json",
}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in PIPELINES:
        print(f"Usage: {sys.argv[0]} <pipeline>")
        print(f"  pipeline: {' | '.join(PIPELINES.keys())}")
        sys.exit(1)

    pipeline = sys.argv[1]
    json_path = PIPELINES[pipeline]

    # Resolve relative to repo root (script lives in scripts/)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_abs = os.path.join(repo_root, json_path)

    print(f"Reading {json_abs} ...")
    with open(json_abs, encoding="utf-8") as f:
        data = json.load(f)

    prompts = data["prompts"]
    total = len(prompts)
    num_batches = math.ceil(total / BATCH_SIZE)
    print(f"Total prompts: {total}, batch size: {BATCH_SIZE}, batches: {num_batches}")

    out_dir = os.path.join(repo_root, f"tmp/batches_{pipeline}")
    os.makedirs(out_dir, exist_ok=True)

    for i in range(num_batches):
        start = i * BATCH_SIZE
        end = min(start + BATCH_SIZE, total)
        batch = [
            {
                "id": p["id"],
                "title": p.get("title", ""),
                "description": p.get("description", ""),
            }
            for p in prompts[start:end]
        ]
        batch_file = os.path.join(out_dir, f"batch_{i:03d}.json")
        with open(batch_file, "w", encoding="utf-8") as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)
        print(f"  Wrote {batch_file} ({len(batch)} prompts)")

    print(f"Done. {num_batches} batch files written to {out_dir}/")


if __name__ == "__main__":
    main()
