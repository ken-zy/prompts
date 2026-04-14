#!/usr/bin/env python3
"""Convert YouMind prompts JSON to a structured Markdown document."""

import json
import sys
import time

INPUT_FILE = "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json"
OUTPUT_FILE = "40_Reference/Articles/20260414/nano-banana-pro-prompts-complete.md"


def format_prompt(p: dict, index: int) -> str:
    lines = []
    # Title
    title = p.get("title", f"Prompt #{index}")
    lines.append(f"### {index}. {title}")
    lines.append("")

    # Meta info
    author = p.get("author", {})
    author_name = author.get("name", "Unknown")
    author_link = author.get("link", "")
    source_link = p.get("sourceLink", "")
    published = p.get("sourcePublishedAt", "")[:10]
    featured = p.get("featured", False)
    likes = p.get("likes", 0)
    categories = p.get("promptCategories", [])

    meta_parts = []
    if author_link:
        meta_parts.append(f"**Author**: [{author_name}]({author_link})")
    elif author_name:
        meta_parts.append(f"**Author**: {author_name}")
    if published:
        meta_parts.append(f"**Date**: {published}")
    if featured:
        meta_parts.append("**Featured**")
    if likes:
        meta_parts.append(f"**Likes**: {likes}")
    if categories:
        cat_names = [c.get("name", c) if isinstance(c, dict) else str(c) for c in categories]
        meta_parts.append(f"**Categories**: {', '.join(cat_names)}")
    if source_link:
        meta_parts.append(f"**Source**: [Link]({source_link})")

    lines.append(" | ".join(meta_parts))
    lines.append("")

    # Description
    desc = p.get("description", "")
    if desc:
        lines.append(f"> {desc}")
        lines.append("")

    # Images
    media = p.get("media", [])
    if media:
        for i, img_url in enumerate(media):
            alt = f"{title}" if len(media) == 1 else f"{title} - {i+1}"
            lines.append(f"![{alt}]({img_url})")
        lines.append("")

    # Prompt content
    content = p.get("content", "")
    if content:
        lines.append("**Prompt:**")
        lines.append("")
        lines.append("```")
        lines.append(content)
        lines.append("```")
        lines.append("")

    # Reference images
    ref_images = p.get("referenceImages", [])
    if ref_images:
        lines.append("**Reference Images:**")
        for i, img_url in enumerate(ref_images):
            lines.append(f"![Reference {i+1}]({img_url})")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    prompts = data["prompts"]
    total = data["total"]
    fetched_at = data.get("fetched_at", "")

    print(f"Loaded {len(prompts)} prompts (total declared: {total})")

    lines = []
    # YAML front matter
    lines.append("---")
    lines.append(f'url: "https://youmind.com/zh-CN/nano-banana-pro-prompts"')
    lines.append(f'title: "Nano Banana Pro Prompts Complete Collection"')
    lines.append(f'description: "All {len(prompts)} Nano Banana Pro AI image generation prompts from YouMind"')
    lines.append(f'total_prompts: {len(prompts)}')
    lines.append(f'captured_at: "{fetched_at}"')
    lines.append("---")
    lines.append("")

    # Header
    lines.append(f"# Nano Banana Pro Prompts Complete Collection")
    lines.append("")
    lines.append(f"Total: **{len(prompts)}** prompts")
    lines.append(f"Source: [YouMind](https://youmind.com/zh-CN/nano-banana-pro-prompts)")
    lines.append(f"Captured: {fetched_at}")
    lines.append("")

    # Table of Contents - Featured prompts
    featured = [p for p in prompts if p.get("featured")]
    if featured:
        lines.append(f"## Featured Prompts ({len(featured)})")
        lines.append("")

    # All prompts
    lines.append("## All Prompts")
    lines.append("")

    for i, p in enumerate(prompts, 1):
        lines.append(format_prompt(p, i))
        if i % 1000 == 0:
            print(f"Formatted {i}/{len(prompts)}")

    content = "\n".join(lines)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    import os
    size_mb = os.path.getsize(OUTPUT_FILE) / 1024 / 1024
    print(f"\nDone! Saved {len(prompts)} prompts to {OUTPUT_FILE}")
    print(f"File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
