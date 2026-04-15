#!/usr/bin/env python3
"""
Generate a flat Markdown Obsidian vault from normalized tag data + raw prompts.

Usage:
    python3 scripts/generate-vault.py image [--min-group=5]
    python3 scripts/generate-vault.py video [--min-group=5]
"""

import argparse
import json
import os
import re
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
        "output_dir": "prompts_imgae",  # intentionally misspelled
        "vault_title": "Nano Banana Pro Prompts",
    },
    "video": {
        "raw_json": "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json",
        "normalized_json": "tmp/normalized_video.json",
        "output_dir": "prompts_video",
        "vault_title": "Seedance 2.0 Video Prompts",
    },
}


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def strip_link_brackets(s: str) -> str:
    """Remove [[ and ]] wrappers if present."""
    s = s.strip()
    if s.startswith("[[") and s.endswith("]]"):
        return s[2:-2].strip()
    return s


def to_kebab_case(s: str) -> str:
    """Convert a topic name to a kebab-case filename stem."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    s = re.sub(r"[\s]+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s


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
        return "Unknown"
    if isinstance(author, dict):
        return author.get("name", "Unknown")
    return str(author)


def get_author_link(author) -> str:
    if not author:
        return ""
    if isinstance(author, dict):
        return author.get("link", "")
    return ""


def get_media_urls(prompt: dict) -> list:
    """Extract media URLs from image prompt (handles str or dict items)."""
    media = prompt.get("media") or []
    urls = []
    for item in media:
        if isinstance(item, str):
            urls.append(item)
        elif isinstance(item, dict):
            url = item.get("url") or item.get("src") or ""
            if url:
                urls.append(url)
    return urls


def get_video_items(prompt: dict) -> list:
    """Extract video items from video prompt."""
    videos = prompt.get("videos") or []
    result = []
    for v in videos:
        if isinstance(v, dict):
            watch_url = v.get("watchUrl") or v.get("sourceUrl") or ""
            thumb_url = v.get("thumbnailUrl") or v.get("thumbnail") or ""
            if watch_url or thumb_url:
                result.append({"watchUrl": watch_url, "thumbnailUrl": thumb_url})
    return result


# ──────────────────────────────────────────────────────────────────────────────
# Markdown generation
# ──────────────────────────────────────────────────────────────────────────────

def render_prompt_block(idx: int, prompt: dict, pipeline: str) -> str:
    """Render a single prompt entry within a topic file."""
    title = prompt.get("title") or "(Untitled)"
    description = prompt.get("description") or ""
    content = prompt.get("content") or ""
    source_link = prompt.get("sourceLink") or ""
    date = format_date(prompt.get("sourcePublishedAt") or "")
    language = prompt.get("language") or ""
    author = prompt.get("author")
    author_name = get_author_name(author)
    author_link = get_author_link(author)

    lines = []
    lines.append(f"### {idx}. {title}")
    lines.append("")

    # Meta line
    meta_parts = []
    if author_name and author_link:
        meta_parts.append(f"**Author**: [{author_name}]({author_link})")
    elif author_name:
        meta_parts.append(f"**Author**: {author_name}")
    if date:
        meta_parts.append(f"**Date**: {date}")
    if language:
        meta_parts.append(f"**Language**: {language}")
    if meta_parts:
        lines.append("  ".join(meta_parts))
        lines.append("")

    # Description blockquote
    if description:
        lines.append(f"> {description}")
        lines.append("")

    if pipeline == "image":
        media_urls = get_media_urls(prompt)
        for url in media_urls:
            lines.append(f"![{title}]({url})")
        if media_urls:
            lines.append("")
    else:
        video_items = get_video_items(prompt)
        for v in video_items:
            if v["watchUrl"]:
                lines.append(f"**Video**: [Watch]({v['watchUrl']})")
            if v["thumbnailUrl"]:
                lines.append(f"![Thumbnail]({v['thumbnailUrl']})")
        if video_items:
            lines.append("")

    # Content fenced code block
    if content:
        lines.append("```")
        lines.append(content)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def render_topic_file(topic_name: str, prompts: list, tag_records: list, pipeline: str) -> str:
    """Render a complete topic Markdown file."""
    lines = []
    lines.append(f"# {topic_name}")
    lines.append("")
    lines.append(f"Total: {len(prompts)} prompts")
    lines.append("")

    for idx, (prompt, tag_record) in enumerate(zip(prompts, tag_records), start=1):
        lines.append(render_prompt_block(idx, prompt, pipeline))

        # Bidirectional links (from tag record)
        raw_links = tag_record.get("links") or []
        clean_links = [strip_link_brackets(lk) for lk in raw_links]
        # Remove duplicates while preserving order; exclude empty
        seen = set()
        deduped = []
        for lk in clean_links:
            if lk and lk not in seen:
                seen.add(lk)
                deduped.append(lk)
        if deduped:
            link_str = " ".join(f"[[{lk}]]" for lk in deduped)
            lines.append(link_str)
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def render_index(vault_title: str, groups: dict, group_links: dict) -> str:
    """Render 00-Index.md."""
    total_prompts = sum(len(v) for v in groups.values())
    total_topics = len(groups)

    lines = []
    lines.append(f"# {vault_title}")
    lines.append("")
    lines.append(f"Total: {total_prompts} prompts, {total_topics} topic pages")
    lines.append("")
    lines.append("## Index")
    lines.append("")
    lines.append("| Topic | Count | Related Links |")
    lines.append("|-------|-------|---------------|")

    # Sort by count descending
    for topic, prompts in sorted(groups.items(), key=lambda x: -len(x[1])):
        count = len(prompts)
        # Top 5 related links (excluding topic name itself)
        link_counter = group_links.get(topic, Counter())
        top_links = [
            lk for lk, _ in link_counter.most_common(10)
            if lk.lower() != topic.lower()
        ][:5]
        related = ", ".join(f"[[{lk}]]" for lk in top_links)
        lines.append(f"| [[{topic}]] | {count} | {related} |")

    lines.append("")
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Main pipeline
# ──────────────────────────────────────────────────────────────────────────────

def run_pipeline(pipeline: str, min_group: int):
    cfg = PIPELINE_CONFIG[pipeline]

    raw_path = os.path.join(BASE_DIR, cfg["raw_json"])
    norm_path = os.path.join(BASE_DIR, cfg["normalized_json"])
    out_dir = os.path.join(BASE_DIR, cfg["output_dir"])
    vault_title = cfg["vault_title"]

    print(f"[{pipeline}] Loading raw prompts from {raw_path} ...")
    with open(raw_path, encoding="utf-8") as f:
        raw_data = json.load(f)
    raw_prompts_list = raw_data.get("prompts", [])
    raw_by_id = {p["id"]: p for p in raw_prompts_list}
    print(f"[{pipeline}] Loaded {len(raw_by_id)} raw prompts")

    print(f"[{pipeline}] Loading normalized tags from {norm_path} ...")
    with open(norm_path, encoding="utf-8") as f:
        norm_data = json.load(f)
    print(f"[{pipeline}] Loaded {len(norm_data)} tag records")

    # Build groups: primary → list of (prompt, tag_record)
    groups_raw: dict[str, list] = defaultdict(list)
    missing_ids = 0
    for record in norm_data:
        pid = record.get("id")
        primary = strip_link_brackets(record.get("primary") or "Miscellaneous")
        prompt = raw_by_id.get(pid)
        if prompt is None:
            missing_ids += 1
            continue
        groups_raw[primary].append((prompt, record))

    if missing_ids:
        print(f"[{pipeline}] Warning: {missing_ids} tag records had no matching raw prompt")

    # Merge small groups into Miscellaneous
    final_groups: dict[str, list] = {}
    misc_items = []
    misc_tag_records = []

    for topic, items in groups_raw.items():
        if len(items) < min_group and topic != "Miscellaneous":
            misc_items.extend(items)
        else:
            final_groups[topic] = items

    if misc_items:
        existing_misc = final_groups.get("Miscellaneous", [])
        final_groups["Miscellaneous"] = existing_misc + misc_items

    # Print distribution report
    print(f"\n[{pipeline}] Distribution report (top 20, min_group={min_group}):")
    sorted_groups = sorted(final_groups.items(), key=lambda x: -len(x[1]))
    for topic, items in sorted_groups[:20]:
        print(f"  {len(items):5d}  {topic}")
    if len(sorted_groups) > 20:
        print(f"  ... and {len(sorted_groups) - 20} more topics")
    print(f"  Total topics: {len(final_groups)}")
    print(f"  Total prompts: {sum(len(v) for v in final_groups.values())}")

    # Build group link counters for index
    group_links: dict[str, Counter] = {}
    for topic, items in final_groups.items():
        ctr = Counter()
        for _, record in items:
            for lk in record.get("links") or []:
                clean = strip_link_brackets(lk)
                if clean:
                    ctr[clean] += 1
        group_links[topic] = ctr

    # Clean output directory
    if os.path.exists(out_dir):
        print(f"\n[{pipeline}] Cleaning output directory {out_dir} ...")
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    # Write topic files
    print(f"[{pipeline}] Writing {len(final_groups)} topic files ...")
    for topic, items in final_groups.items():
        prompts = [p for p, _ in items]
        records = [r for _, r in items]
        content = render_topic_file(topic, prompts, records, pipeline)
        filename = to_kebab_case(topic) + ".md"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Write index
    # Convert final_groups to {topic: prompts_list} for index renderer
    groups_for_index = {topic: [p for p, _ in items] for topic, items in final_groups.items()}
    index_content = render_index(vault_title, groups_for_index, group_links)
    index_path = os.path.join(out_dir, "00-Index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)

    # Verify
    written = [f for f in os.listdir(out_dir) if f.endswith(".md")]
    print(f"[{pipeline}] Done. {len(written)} .md files written to {out_dir}/")
    print(f"[{pipeline}]   (including 00-Index.md)")


def main():
    parser = argparse.ArgumentParser(description="Generate Obsidian vault from normalized prompts")
    parser.add_argument("pipeline", choices=["image", "video"], help="Pipeline to run")
    parser.add_argument("--min-group", type=int, default=5, help="Min prompts per group (default: 5)")
    args = parser.parse_args()

    run_pipeline(args.pipeline, args.min_group)


if __name__ == "__main__":
    main()
