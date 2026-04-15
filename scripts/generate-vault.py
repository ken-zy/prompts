#!/usr/bin/env python3
"""
Generate chunk-based Obsidian vault optimized for LLM retrieval.

Reads normalized tag data + raw prompts, produces:
- chunk-{NNN}.md files (~200 prompts each, semantically sorted)
- 00-Index.md (topic inverted index, ~70 rows)

Usage:
    python3 scripts/generate-vault.py image
    python3 scripts/generate-vault.py video
"""

import argparse
import json
import os
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime


# ──────────────────────────────────────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PIPELINE_CONFIG = {
    "image": {
        "raw_json": "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json",
        "normalized_json": "tmp/normalized_image.json",
        "output_dir": "prompts_imgae",  # intentional misspelling, do not change
        "vault_title": "Nano Banana Pro Prompts",
        "chunk_size": 200,
        "anchor_min_freq": 50,
        "search_link_min_freq": 5,
        "search_link_max": 4,
    },
    "video": {
        "raw_json": "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json",
        "normalized_json": "tmp/normalized_video.json",
        "output_dir": "prompts_video",
        "vault_title": "Seedance 2.0 Video Prompts",
        "chunk_size": 200,
        "anchor_min_freq": 10,  # video has lower link freq; top link is 29
        "search_link_min_freq": 3,
        "search_link_max": 4,
    },
}


# ──────────────────────────────────────────────────────────────────────────────
# Link analysis
# ──────────────────────────────────────────────────────────────────────────────

def build_link_freq(tagged_data: list[dict]) -> Counter:
    """Count global frequency of every link across all prompts."""
    freq = Counter()
    for item in tagged_data:
        for link in item.get("links", []):
            freq[link] += 1
    return freq


def select_search_links(
    links: list[str],
    freq_table: Counter,
    min_freq: int,
    max_links: int,
) -> list[str]:
    """Select search_links for one prompt.

    Rules:
    1. Keep only links with global freq >= min_freq
    2. Sort by frequency descending
    3. Truncate to max_links
    4. Fallback: if empty, keep 1 link with highest frequency from original set
    """
    candidates = [(lk, freq_table.get(lk, 0)) for lk in links if freq_table.get(lk, 0) >= min_freq]
    candidates.sort(key=lambda x: -x[1])
    result = [lk for lk, _ in candidates[:max_links]]

    if not result and links:
        best = max(links, key=lambda lk: freq_table.get(lk, 0))
        result = [best]

    return result


def assign_anchor(search_links: list[str], anchor_set: set[str], freq_table: Counter) -> str:
    """Pick the best anchor for a prompt from its search_links.

    Returns the highest-frequency link that is in the anchor set, or "" if none.
    """
    best = ""
    best_freq = -1
    for lk in search_links:
        if lk in anchor_set and freq_table.get(lk, 0) > best_freq:
            best = lk
            best_freq = freq_table[lk]
    return best


# ──────────────────────────────────────────────────────────────────────────────
# Markdown rendering
# ──────────────────────────────────────────────────────────────────────────────

def format_date(iso_str: str) -> str:
    """Format ISO date string to YYYY-MM-DD."""
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return iso_str[:10] if len(iso_str) >= 10 else iso_str


def get_author_name(author) -> str:
    if not author:
        return ""
    if isinstance(author, dict):
        return author.get("name", "")
    return str(author)


def get_author_link(author) -> str:
    if not author:
        return ""
    if isinstance(author, dict):
        return author.get("link", "")
    return ""


def render_prompt_entry(idx: int, prompt: dict, search_links: list[str], pipeline: str) -> str:
    """Render one prompt as a Markdown entry."""
    lines = []
    title = prompt.get("title") or "(Untitled)"
    lines.append(f"### {idx}. {title}")
    lines.append("")

    # Meta line
    meta_parts = []
    author = prompt.get("author")
    author_name = get_author_name(author)
    author_link = get_author_link(author)
    if author_name and author_link:
        meta_parts.append(f"**Author**: [{author_name}]({author_link})")
    elif author_name:
        meta_parts.append(f"**Author**: {author_name}")

    date = format_date(prompt.get("sourcePublishedAt") or "")
    if date:
        meta_parts.append(f"**Date**: {date}")

    language = prompt.get("language") or ""
    if language:
        meta_parts.append(f"**Language**: {language}")

    if meta_parts:
        lines.append("  ".join(meta_parts))
        lines.append("")

    # Description
    description = prompt.get("description") or ""
    if description:
        for desc_line in description.strip().splitlines():
            lines.append(f"> {desc_line}")
        lines.append("")

    # Media (image pipeline)
    if pipeline == "image":
        media = prompt.get("media") or []
        for item in media:
            url = item if isinstance(item, str) else (item.get("url") or item.get("src") or "")
            if url:
                lines.append(f"![{title}]({url})")
        if media:
            lines.append("")
    else:
        # Video pipeline
        videos = prompt.get("videos") or []
        for v in videos:
            if isinstance(v, dict):
                watch_url = v.get("watchUrl") or v.get("sourceUrl") or ""
                thumb_url = v.get("thumbnailUrl") or v.get("thumbnail") or ""
                if watch_url:
                    lines.append(f"**Video**: [Watch]({watch_url})")
                if thumb_url:
                    lines.append(f"![Thumbnail]({thumb_url})")
        has_video_content = any(
            isinstance(v, dict) and (v.get("watchUrl") or v.get("sourceUrl") or v.get("thumbnailUrl") or v.get("thumbnail"))
            for v in videos
        )
        if has_video_content:
            lines.append("")

    # Prompt content
    content = prompt.get("content") or ""
    if content:
        lines.append("```")
        lines.append(content.strip())
        lines.append("```")
        lines.append("")

    # search_links
    if search_links:
        lines.append(" ".join(f"[[{lk}]]" for lk in search_links))
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def render_chunk_file(chunk_num: int, entries: list[dict], pipeline: str) -> str:
    """Render a complete chunk Markdown file.

    Each entry in `entries` is: {"prompt": raw_prompt, "search_links": [...]}
    """
    lines = []
    lines.append(f"# Chunk {chunk_num:03d}")
    lines.append("")
    lines.append(f"Total: {len(entries)} prompts")
    lines.append("")

    for idx, entry in enumerate(entries, start=1):
        lines.append(render_prompt_entry(idx, entry["prompt"], entry["search_links"], pipeline))

    return "\n".join(lines)


def render_index(vault_title: str, total_prompts: int, total_chunks: int, topic_index: list[dict]) -> str:
    """Render 00-Index.md.

    topic_index: [{"topic": str, "chunks": [int], "count": int}, ...]
    """
    lines = []
    lines.append(f"# {vault_title}")
    lines.append("")
    lines.append(f"Total: {total_prompts} prompts, {total_chunks} chunk files")
    lines.append("")
    lines.append("## Index")
    lines.append("")
    lines.append("| Topic | Chunks | Count |")
    lines.append("|-------|--------|-------|")

    for entry in topic_index:
        chunk_strs = ", ".join(f"{c:03d}" for c in entry["chunks"])
        lines.append(f"| [[{entry['topic']}]] | {chunk_strs} | {entry['count']} |")

    lines.append("")
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Main pipeline
# ──────────────────────────────────────────────────────────────────────────────

def run_pipeline(pipeline: str):
    cfg = PIPELINE_CONFIG[pipeline]

    raw_path = os.path.join(BASE_DIR, cfg["raw_json"])
    norm_path = os.path.join(BASE_DIR, cfg["normalized_json"])
    out_dir = os.path.join(BASE_DIR, cfg["output_dir"])

    chunk_size = cfg["chunk_size"]
    anchor_min_freq = cfg["anchor_min_freq"]
    search_link_min_freq = cfg["search_link_min_freq"]
    search_link_max = cfg["search_link_max"]

    # Load data
    print(f"[{pipeline}] Loading raw prompts from {raw_path} ...")
    with open(raw_path, encoding="utf-8") as f:
        raw_data = json.load(f)
    raw_by_id = {p["id"]: p for p in raw_data["prompts"]}
    print(f"[{pipeline}] Loaded {len(raw_by_id)} raw prompts")

    print(f"[{pipeline}] Loading normalized tags from {norm_path} ...")
    with open(norm_path, encoding="utf-8") as f:
        tagged = json.load(f)
    print(f"[{pipeline}] Loaded {len(tagged)} tag records")

    # Step 1: Build link frequency
    freq_table = build_link_freq(tagged)
    print(f"[{pipeline}] Unique links: {len(freq_table)}")
    print(f"[{pipeline}] Links freq >= {search_link_min_freq}: {sum(1 for c in freq_table.values() if c >= search_link_min_freq)}")
    print(f"[{pipeline}] Links freq >= {anchor_min_freq}: {sum(1 for c in freq_table.values() if c >= anchor_min_freq)}")

    # Step 2: Build anchor set
    anchor_set = {lk for lk, c in freq_table.items() if c >= anchor_min_freq}
    print(f"[{pipeline}] Anchor topics: {len(anchor_set)}")

    # Step 3: For each prompt, compute search_links and anchor
    entries = []
    missing_ids = 0
    for record in tagged:
        pid = record.get("id")
        if pid is None:
            missing_ids += 1
            continue
        prompt = raw_by_id.get(pid)
        if prompt is None:
            missing_ids += 1
            continue

        s_links = select_search_links(record.get("links", []), freq_table, search_link_min_freq, search_link_max)
        anchor = assign_anchor(s_links, anchor_set, freq_table)

        entries.append({
            "prompt": prompt,
            "search_links": s_links,
            "anchor": anchor,
        })

    if missing_ids:
        print(f"[{pipeline}] Warning: {missing_ids} tag records had no matching raw prompt")

    # Step 4: Sort — anchored first (by anchor name), then unanchored
    anchored = [e for e in entries if e["anchor"]]
    unanchored = [e for e in entries if not e["anchor"]]
    anchored.sort(key=lambda e: e["anchor"])
    sorted_entries = anchored + unanchored

    if not sorted_entries:
        print(f"[{pipeline}] Error: no prompts matched. Check that raw and normalized files are aligned.")
        sys.exit(1)

    anchored_count = len(anchored)
    print(f"[{pipeline}] Anchored: {anchored_count} ({anchored_count/len(sorted_entries)*100:.1f}%)")
    print(f"[{pipeline}] Unanchored: {len(unanchored)} ({len(unanchored)/len(sorted_entries)*100:.1f}%)")

    # Step 5: Slice into chunks
    chunks = []
    for i in range(0, len(sorted_entries), chunk_size):
        chunks.append(sorted_entries[i:i + chunk_size])

    print(f"[{pipeline}] Chunks: {len(chunks)} (chunk_size={chunk_size})")

    # Step 6: Clean output directory and write chunks
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    for chunk_idx, chunk_entries in enumerate(chunks, start=1):
        content = render_chunk_file(chunk_idx, chunk_entries, pipeline)
        filepath = os.path.join(out_dir, f"chunk-{chunk_idx:03d}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Step 7: Build inverted index
    topic_chunk_map: dict[str, Counter] = defaultdict(Counter)
    for chunk_idx, chunk_entries in enumerate(chunks, start=1):
        for entry in chunk_entries:
            for lk in entry["search_links"]:
                if lk in anchor_set:
                    topic_chunk_map[lk][chunk_idx] += 1

    topic_index = []
    for topic in sorted(topic_chunk_map.keys(), key=lambda t: -sum(topic_chunk_map[t].values())):
        chunk_counts = topic_chunk_map[topic]
        total_count = sum(chunk_counts.values())
        chunk_nums = sorted(chunk_counts.keys())
        topic_index.append({
            "topic": topic,
            "chunks": chunk_nums,
            "count": total_count,
        })

    # Write 00-Index.md
    index_content = render_index(
        cfg["vault_title"],
        len(sorted_entries),
        len(chunks),
        topic_index,
    )
    with open(os.path.join(out_dir, "00-Index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)

    # Summary
    print(f"\n[{pipeline}] Done:")
    print(f"  {len(chunks)} chunk files + 00-Index.md written to {out_dir}/")
    print(f"  Index topics: {len(topic_index)}")
    print(f"  Total prompts: {len(sorted_entries)}")


def main():
    parser = argparse.ArgumentParser(description="Generate chunk-based Obsidian vault for LLM retrieval")
    parser.add_argument("pipeline", choices=["image", "video"], help="Pipeline to run")
    args = parser.parse_args()

    run_pipeline(args.pipeline)


if __name__ == "__main__":
    main()
