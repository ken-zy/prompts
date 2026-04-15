# Prompt Vault Reclassification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace regex-based single-category classification with LLM-generated multi-dimensional `[[bidirectional links]]` for 14218 prompts across two independent pipelines (image + video).

**Architecture:** A Python orchestration script reads raw JSON, splits into batches, dispatches subagents for semantic tagging, collects results into intermediate JSON, then a generation script produces flat Markdown files with `[[links]]` and a rich `00-Index.md`. Image and video pipelines are fully independent.

**Tech Stack:** Python 3, Claude Code subagents (Agent tool), JSON for intermediate data, Markdown for output.

---

### Task 1: Create the batch extraction script

**Files:**
- Create: `scripts/extract-batches.py`

This script reads raw JSON and produces lightweight batch files containing only `id`, `title`, `description` per prompt. These batch files will be fed to subagents.

- [ ] **Step 1: Write `scripts/extract-batches.py`**

```python
"""
extract-batches.py

Reads raw prompt JSON and splits into batch files for subagent processing.

Usage:
    python3 scripts/extract-batches.py image   # process image prompts
    python3 scripts/extract-batches.py video   # process video prompts
"""

import json
import math
import os
import sys

BATCH_SIZE = 300

CONFIGS = {
    "image": {
        "input": "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json",
        "output_dir": "tmp/batches_image",
    },
    "video": {
        "input": "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json",
        "output_dir": "tmp/batches_video",
    },
}


def extract_batches(pipeline: str) -> None:
    config = CONFIGS[pipeline]
    with open(config["input"]) as f:
        data = json.load(f)

    prompts = data["prompts"]
    print(f"Total prompts: {len(prompts)}")

    os.makedirs(config["output_dir"], exist_ok=True)

    total_batches = math.ceil(len(prompts) / BATCH_SIZE)

    for i in range(total_batches):
        batch = []
        for p in prompts[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]:
            batch.append({
                "id": p["id"],
                "title": p.get("title") or "",
                "description": p.get("description") or "",
            })

        batch_path = os.path.join(config["output_dir"], f"batch_{i:03d}.json")
        with open(batch_path, "w") as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)

    print(f"Wrote {total_batches} batches to {config['output_dir']}/")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CONFIGS:
        print("Usage: python3 scripts/extract-batches.py [image|video]")
        sys.exit(1)
    extract_batches(sys.argv[1])
```

- [ ] **Step 2: Run for image pipeline**

Run: `python3 scripts/extract-batches.py image`
Expected: `Wrote 42 batches to tmp/batches_image/`

- [ ] **Step 3: Run for video pipeline**

Run: `python3 scripts/extract-batches.py video`
Expected: `Wrote 6 batches to tmp/batches_video/`

- [ ] **Step 4: Verify batch content**

Run: `python3 -c "import json; d=json.load(open('tmp/batches_image/batch_000.json')); print(len(d)); print(json.dumps(d[0], ensure_ascii=False, indent=2))"`
Expected: 300 items, each with `id`, `title`, `description` fields.

- [ ] **Step 5: Commit**

```bash
git add scripts/extract-batches.py
git commit -m "feat(scripts): add batch extraction script for subagent processing"
```

---

### Task 2: Process image batches with subagents

**Files:**
- Read: `tmp/batches_image/batch_*.json` (42 batch files)
- Create: `tmp/results_image/batch_*.json` (42 result files)

This task is executed by dispatching subagents in parallel. Each subagent reads one batch file and outputs a JSON result file.

- [ ] **Step 1: Process batches in parallel rounds**

For each round, dispatch up to 6 subagents in parallel. Each subagent receives this prompt (with batch file path substituted):

```
You are a prompt tagging specialist. Read the batch file at {batch_path}.
It contains an array of AI image generation prompts, each with id, title, description.

For EACH prompt, output:
1. "primary": The most SPECIFIC concept this prompt belongs to. This determines which file it will be stored in. Use English, Title Case, noun phrases. Prefer specific over generic (e.g. "Double Exposure Portrait" over "Portrait").
2. "links": ALL relevant [[bidirectional links]] for this prompt. Include the primary. Cover: subject matter, visual style, technique, mood, medium. Use English, Title Case, noun phrases. Do NOT include generic links like "High Quality", "Detailed", "AI Generated".

Write the result as a JSON array to {result_path}. Format:
[
  {"id": 123, "primary": "Double Exposure Portrait", "links": ["Double Exposure Portrait", "Cinematic Portrait", "Urban Scene", "Silhouette Art"]},
  ...
]

IMPORTANT:
- Output ONLY the JSON file. No commentary.
- Every prompt in the batch must appear in the output.
- Use consistent naming: Title Case, English, noun phrases.
```

Round scheduling: batches 0-5 in round 1, 6-11 in round 2, etc. ~7 rounds for 42 batches.

- [ ] **Step 2: Verify all result files exist**

Run: `ls tmp/results_image/ | wc -l`
Expected: 42 files

- [ ] **Step 3: Validate result completeness**

Run:
```bash
python3 -c "
import json, glob
total = 0
for f in sorted(glob.glob('tmp/results_image/batch_*.json')):
    data = json.load(open(f))
    total += len(data)
    for item in data:
        assert 'id' in item and 'primary' in item and 'links' in item, f'Bad item in {f}: {item}'
print(f'Total tagged prompts: {total}')
"
```
Expected: `Total tagged prompts: 12465`

- [ ] **Step 4: Spot-check quality**

Read 5 random results and verify links make sense:
```bash
python3 -c "
import json, random
data = json.load(open('tmp/results_image/batch_020.json'))
for item in random.sample(data, 5):
    print(f\"Title: {item.get('title', item['id'])}\")
    print(f\"Primary: {item['primary']}\")
    print(f\"Links: {item['links']}\")
    print()
"
```

---

### Task 3: Process video batches with subagents

**Files:**
- Read: `tmp/batches_video/batch_*.json` (6 batch files)
- Create: `tmp/results_video/batch_*.json` (6 result files)

Same as Task 2, but for video prompts. Use the same subagent prompt with one change: replace "AI image generation prompts" with "AI video generation prompts (for Seedance 2.0)".

- [ ] **Step 1: Process all 6 batches in one round (parallel)**

Dispatch 6 subagents, one per batch.

- [ ] **Step 2: Validate result completeness**

Run:
```bash
python3 -c "
import json, glob
total = 0
for f in sorted(glob.glob('tmp/results_video/batch_*.json')):
    data = json.load(open(f))
    total += len(data)
print(f'Total tagged prompts: {total}')
"
```
Expected: `Total tagged prompts: 1753`

---

### Task 4: Normalize links

**Files:**
- Create: `scripts/normalize-links.py`
- Read: `tmp/results_image/batch_*.json`, `tmp/results_video/batch_*.json`
- Create: `tmp/normalized_image.json`, `tmp/normalized_video.json`
- Create: `tmp/link_vocab_image.json`, `tmp/link_vocab_video.json`

This task collects all unique links, dispatches a subagent to merge synonyms, then applies the merge map.

- [ ] **Step 1: Write `scripts/normalize-links.py`**

```python
"""
normalize-links.py

Collects all links from subagent results, applies a merge map, outputs normalized data.

Usage:
    python3 scripts/normalize-links.py image [merge_map.json]
    python3 scripts/normalize-links.py video [merge_map.json]

Without merge_map: outputs unique link list to stdout for review.
With merge_map: applies merges and writes normalized output.
"""

import json
import glob
import sys
from collections import Counter


def load_results(pipeline: str) -> list[dict]:
    results = []
    for f in sorted(glob.glob(f"tmp/results_{pipeline}/batch_*.json")):
        results.extend(json.load(open(f)))
    return results


def collect_links(results: list[dict]) -> Counter:
    counter = Counter()
    for item in results:
        for link in item["links"]:
            counter[link] += 1
    return counter


def apply_merge_map(results: list[dict], merge_map: dict) -> list[dict]:
    for item in results:
        item["primary"] = merge_map.get(item["primary"], item["primary"])
        item["links"] = list(dict.fromkeys(
            merge_map.get(link, link) for link in item["links"]
        ))
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("image", "video"):
        print("Usage: python3 scripts/normalize-links.py [image|video] [merge_map.json]")
        sys.exit(1)

    pipeline = sys.argv[1]
    results = load_results(pipeline)

    if len(sys.argv) < 3:
        # Phase 1: output link vocabulary for review
        counter = collect_links(results)
        vocab = [{"link": link, "count": count} for link, count in counter.most_common()]
        out_path = f"tmp/link_vocab_{pipeline}.json"
        with open(out_path, "w") as f:
            json.dump(vocab, f, ensure_ascii=False, indent=2)
        print(f"Unique links: {len(vocab)}")
        print(f"Vocabulary written to {out_path}")
        print(f"\nTop 30 links:")
        for item in vocab[:30]:
            print(f"  {item['count']:>5}  {item['link']}")
    else:
        # Phase 2: apply merge map
        merge_map = json.load(open(sys.argv[2]))
        results = apply_merge_map(results, merge_map)
        out_path = f"tmp/normalized_{pipeline}.json"
        with open(out_path, "w") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"Normalized {len(results)} prompts -> {out_path}")
```

- [ ] **Step 2: Extract image link vocabulary**

Run: `python3 scripts/normalize-links.py image`
Expected: Outputs unique link count and top 30 links.

- [ ] **Step 3: Generate image merge map via subagent**

Dispatch a subagent with the link vocabulary. Prompt:

```
Read the file tmp/link_vocab_image.json. It contains a list of [[bidirectional link]] names with their usage counts, generated by multiple independent agents.

Your task: identify synonyms, near-duplicates, and inconsistent naming that should be merged. Output a JSON merge map where keys are the link names to replace and values are the canonical name to keep.

Rules:
- Merge only TRUE synonyms (e.g. "Sci-Fi" and "Science Fiction", "Cyber Punk" and "Cyberpunk")
- Do NOT merge distinct concepts (e.g. "Street Photography" and "Urban Scene" are different)
- Keep the most common/standard spelling as the canonical name
- Use Title Case, English, noun phrases

Write the merge map to tmp/merge_map_image.json. Format:
{"Cyber Punk": "Cyberpunk", "Sci-Fi": "Science Fiction", ...}
```

- [ ] **Step 4: Apply image merge map**

Run: `python3 scripts/normalize-links.py image tmp/merge_map_image.json`
Expected: `Normalized 12465 prompts -> tmp/normalized_image.json`

- [ ] **Step 5: Repeat steps 2-4 for video pipeline**

Run: `python3 scripts/normalize-links.py video`
Then subagent generates `tmp/merge_map_video.json`.
Then: `python3 scripts/normalize-links.py video tmp/merge_map_video.json`

- [ ] **Step 6: Commit**

```bash
git add scripts/normalize-links.py
git commit -m "feat(scripts): add link normalization script"
```

---

### Task 5: Analyze distribution and generate Markdown

**Files:**
- Create: `scripts/generate-vault.py`
- Read: `tmp/normalized_image.json`, `tmp/normalized_video.json`
- Read: raw JSON files (for full prompt content)
- Write: `prompts_imgae/*.md`, `prompts_video/*.md`

- [ ] **Step 1: Write `scripts/generate-vault.py`**

```python
"""
generate-vault.py

Reads normalized link data + raw prompts, generates flat Markdown vault.

Usage:
    python3 scripts/generate-vault.py image [--min-group=5]
    python3 scripts/generate-vault.py video [--min-group=5]
"""

import json
import os
import re
import shutil
import sys
from collections import defaultdict

CONFIGS = {
    "image": {
        "raw": "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json",
        "normalized": "tmp/normalized_image.json",
        "output_dir": "prompts_imgae",
        "vault_title": "Nano Banana Pro Prompts",
    },
    "video": {
        "raw": "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json",
        "normalized": "tmp/normalized_video.json",
        "output_dir": "prompts_video",
        "vault_title": "Seedance 2.0 Video Prompts",
    },
}


def to_filename(topic: str) -> str:
    """Convert topic name to kebab-case filename."""
    name = topic.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = name.strip("-")
    return name + ".md"


def format_prompt_entry(prompt: dict, index: int, links: list[str]) -> str:
    """Format one prompt as a Markdown entry with [[links]]."""
    lines = []
    title = prompt.get("title") or "Untitled"
    lines.append(f"### {index}. {title}")
    lines.append("")

    # Meta line
    meta_parts = []
    author_obj = prompt.get("author") or {}
    author_name = author_obj.get("name") or "" if isinstance(author_obj, dict) else ""
    source_link = prompt.get("sourceLink") or ""
    if author_name:
        if source_link:
            meta_parts.append(f"**Author**: [{author_name}]({source_link})")
        else:
            meta_parts.append(f"**Author**: {author_name}")

    published_at = prompt.get("sourcePublishedAt") or ""
    if published_at:
        meta_parts.append(f"**Date**: {published_at[:10]}")

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

    # Media (images)
    for m in prompt.get("media") or []:
        url = m if isinstance(m, str) else m.get("url", "")
        if url:
            lines.append(f"![{title}]({url})")
    if prompt.get("media"):
        lines.append("")

    # Videos
    for v in prompt.get("videos") or []:
        if isinstance(v, dict):
            watch = v.get("watchUrl") or v.get("url") or ""
            thumb = v.get("thumbnailUrl") or ""
            if watch:
                lines.append(f"**Video**: [Watch]({watch})")
            if thumb:
                lines.append(f"![Thumbnail]({thumb})")
    if prompt.get("videos"):
        lines.append("")

    # Prompt content
    content = prompt.get("content") or ""
    if content:
        lines.append("```")
        lines.append(content.strip())
        lines.append("```")
        lines.append("")

    # Bidirectional links
    link_str = " ".join(f"[[{link}]]" for link in links)
    lines.append(link_str)
    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate(pipeline: str, min_group: int = 5) -> None:
    config = CONFIGS[pipeline]

    # Load raw prompts (keyed by id)
    with open(config["raw"]) as f:
        raw_data = json.load(f)
    raw_by_id = {p["id"]: p for p in raw_data["prompts"]}

    # Load normalized tagging results
    with open(config["normalized"]) as f:
        tagged = json.load(f)

    # Group by primary
    groups = defaultdict(list)
    tag_map = {}  # id -> links
    for item in tagged:
        groups[item["primary"]].append(item["id"])
        tag_map[item["id"]] = item["links"]

    # Merge small groups into "Miscellaneous"
    final_groups = {}
    misc_ids = []
    for topic, ids in groups.items():
        if len(ids) < min_group:
            misc_ids.extend(ids)
        else:
            final_groups[topic] = ids
    if misc_ids:
        final_groups["Miscellaneous"] = misc_ids

    # Distribution report
    print(f"=== {pipeline} distribution ===")
    print(f"Total topics: {len(final_groups)}")
    for topic in sorted(final_groups, key=lambda t: -len(final_groups[t])):
        print(f"  {len(final_groups[topic]):>5}  {topic}")

    # Clean output dir
    output_dir = config["output_dir"]
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Generate topic files
    all_topics = []
    for topic, ids in sorted(final_groups.items(), key=lambda t: -len(t[1])):
        filename = to_filename(topic)
        filepath = os.path.join(output_dir, filename)

        lines = []
        lines.append(f"# {topic}")
        lines.append("")
        lines.append(f"Total: {len(ids)} prompts")
        lines.append("")

        for idx, pid in enumerate(ids, 1):
            raw = raw_by_id.get(pid, {})
            links = tag_map.get(pid, [])
            lines.append(format_prompt_entry(raw, idx, links))

        with open(filepath, "w") as f:
            f.write("\n".join(lines))

        # Collect top links for index
        link_counter = defaultdict(int)
        for pid in ids:
            for link in tag_map.get(pid, []):
                if link != topic:
                    link_counter[link] += 1
        top_links = [l for l, _ in sorted(link_counter.items(), key=lambda x: -x[1])[:5]]

        all_topics.append({
            "topic": topic,
            "filename": filename,
            "count": len(ids),
            "top_links": top_links,
        })

    # Generate 00-Index.md
    index_lines = []
    index_lines.append(f"# {config['vault_title']}")
    index_lines.append("")
    total = sum(t["count"] for t in all_topics)
    index_lines.append(f"Total: {total} prompts, {len(all_topics)} topic pages")
    index_lines.append("")
    index_lines.append("## Index")
    index_lines.append("")
    index_lines.append("| Topic | Count | Related Links |")
    index_lines.append("|-------|-------|---------------|")
    for t in sorted(all_topics, key=lambda x: -x["count"]):
        links_str = ", ".join(f"[[{l}]]" for l in t["top_links"])
        index_lines.append(f"| [[{t['topic']}]] | {t['count']} | {links_str} |")
    index_lines.append("")

    with open(os.path.join(output_dir, "00-Index.md"), "w") as f:
        f.write("\n".join(index_lines))

    print(f"\nGenerated {len(all_topics)} topic files + 00-Index.md in {output_dir}/")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CONFIGS:
        print("Usage: python3 scripts/generate-vault.py [image|video] [--min-group=N]")
        sys.exit(1)

    pipeline = sys.argv[1]
    min_group = 5
    for arg in sys.argv[2:]:
        if arg.startswith("--min-group="):
            min_group = int(arg.split("=")[1])

    generate(pipeline, min_group)
```

- [ ] **Step 2: Run for image pipeline**

Run: `python3 scripts/generate-vault.py image`
Expected: Distribution report + generated files in `prompts_imgae/`

- [ ] **Step 3: Run for video pipeline**

Run: `python3 scripts/generate-vault.py video`
Expected: Distribution report + generated files in `prompts_video/`

- [ ] **Step 4: Verify output**

```bash
ls prompts_imgae/*.md | wc -l   # topic files + index
ls prompts_video/*.md | wc -l
head -30 prompts_imgae/00-Index.md
```

- [ ] **Step 5: Commit**

```bash
git add scripts/generate-vault.py prompts_imgae/ prompts_video/
git commit -m "feat: regenerate prompt vault with LLM-tagged bidirectional links"
```

---

### Task 6: Update CLAUDE.md with lint workflow

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add lint workflow section to CLAUDE.md**

Append to CLAUDE.md:

```markdown
## Wiki Lint Workflow
To lint the prompt vault:
1. Read `00-Index.md` in target directory (`prompts_imgae/` or `prompts_video/`)
2. For each topic file, review prompts and verify `[[links]]` are accurate and complete
3. Fix inaccurate links, add missing links
4. Update `00-Index.md` related links column
5. Record changes in commit message

Trigger: manual, run periodically or when quality issues are noticed.
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add wiki lint workflow to CLAUDE.md"
```

---

### Task 7: Cleanup

**Files:**
- Remove: `tmp/` directory (intermediate batch and result files)
- Keep: `scripts/extract-batches.py`, `scripts/normalize-links.py`, `scripts/generate-vault.py` (for future re-runs)

- [ ] **Step 1: Remove tmp directory**

```bash
rm -rf tmp/
```

- [ ] **Step 2: Add tmp/ to .gitignore**

```bash
echo "tmp/" >> .gitignore
git add .gitignore
git commit -m "chore: add tmp/ to gitignore"
```
