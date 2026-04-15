# Prompt Vault Reclassification Design

## Problem

Current regex-based categorization forces each prompt into a single hierarchical category. The keyword `cinematic` alone causes 65% of prompts to collapse into one dominant category ("人像摄影" for images, "电影感与叙事" for videos). Single-category assignment fundamentally conflicts with how prompts work — a "surreal cinematic portrait with cyberpunk lighting" belongs to multiple dimensions simultaneously.

## Design Decision Summary

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Classification method | LLM (via subagents in Claude Code) | Semantic understanding > regex keywords |
| Organization model | Flat files + `[[bidirectional links]]` | Multi-dimensional discovery; no forced hierarchy |
| Link language | English only | e.g. `[[Cinematic Portrait]]` |
| Tag vocabulary | Open generation + post-hoc normalization | Let concepts emerge from data |
| File granularity | Determined by subagent output distribution | Run first, merge small files after |
| Search model | Index-first (Karpathy llm-wiki pattern) | LLM reads index → drills into files |
| Maintenance | Periodic lint (Karpathy pattern) | Manual trigger, incremental improvement |

## Architecture

Image and video prompts are processed as **two independent pipelines**. They have different source models (Nano Banana Pro vs Seedance 2.0), different content characteristics (static image descriptions vs multi-shot video scripts), and will produce different link vocabularies. Each pipeline runs the full Step 1-4 sequence independently.

```
Pipeline 1: Image Prompts (prompts_imgae/)
Raw JSON ──→ Batch Subagents ──→ Normalize ──→ Distribute ──→ Generate MD

Pipeline 2: Video Prompts (prompts_video/)
Raw JSON ──→ Batch Subagents ──→ Normalize ──→ Distribute ──→ Generate MD
```

Cross-pipeline links are allowed (e.g. a video prompt can link to `[[Cyberpunk]]` which also appears in image prompts), but normalization and file generation are independent per pipeline.

## Data Sources

- Image prompts: `40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json` (12465 prompts)
- Video prompts: `40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json` (1753 prompts)

## Step 1: Subagent Batch Processing

### Batching

Two independent batch sequences, processed sequentially (complete image pipeline first, then video pipeline):

**Image pipeline:** 12465 prompts ÷ 200 = ~63 batches, 5-6 parallel subagents, ~11 rounds
**Video pipeline:** 1753 prompts ÷ 200 = ~9 batches, 5-6 parallel subagents, ~2 rounds

### Subagent Input

Each subagent receives a JSON array of prompts with fields: `title`, `description`, `content`, `translatedContent`, `_id`.

### Subagent Output

Each subagent returns a JSON array:

```json
[
  {
    "id": "<prompt _id>",
    "primary": "Cinematic Portrait",
    "links": ["Cinematic Portrait", "Double Exposure", "Urban Scene", "Conceptual Art"]
  }
]
```

- `primary`: The single most representative concept — determines which file this prompt is stored in.
- `links`: All relevant `[[bidirectional links]]`, including the primary. English only. Generated freely without a fixed vocabulary.

### Subagent Prompt Guidelines

- Primary should be the most *specific* match, not the most *common* (prefer "Double Exposure Portrait" over "Portrait")
- Links should cover: subject matter, visual style, technique, mood/atmosphere, medium (where distinctive)
- Avoid generic links that would apply to nearly everything (e.g. `[[High Quality]]`, `[[Detailed]]`)
- Use consistent naming conventions: Title Case, noun phrases (e.g. `[[Street Photography]]` not `[[street photo style]]`)

## Step 2: Link Normalization

After all subagents complete:

1. Collect all unique link strings across all results
2. Cluster synonyms and merge (e.g. `[[Cyber Punk]]` → `[[Cyberpunk]]`, `[[Sci-fi]]` → `[[Sci-Fi]]`)
3. Apply merges to all prompt records
4. Output: a normalized link vocabulary + updated prompt records

Normalization is done independently per pipeline by a dedicated subagent that reviews the full link list for that pipeline.

## Step 3: Distribution Analysis & File Grouping

1. Group prompts by `primary` link
2. Analyze distribution:
   - Groups with < 5 prompts: merge into nearest larger related group
   - Groups with > 500 prompts: consider if subagent was too generic; may re-process that batch with stricter instructions
3. Final file list determined by this step

## Step 4: Markdown Generation

### File Structure

All files flat in output directory (no subdirectories):

```
prompts_imgae/
  00-Index.md
  cinematic-portrait.md
  surreal-art.md
  street-photography.md
  ...

prompts_video/
  00-Index.md
  cinematic-short-film.md
  martial-arts.md
  ...
```

File names: kebab-case derived from primary link name.

### 00-Index.md Format (Karpathy pattern)

```markdown
# Nano Banana Pro Prompts

Total: 12465 prompts, {N} topic pages

## Index

| Topic | Count | Links | Summary |
|-------|-------|-------|---------|
| [[Cinematic Portrait]] | 850 | [[Portrait]], [[Film Style]] | Portraits with cinematic lighting and film aesthetics |
| [[Surreal Art]] | 320 | [[Conceptual Art]], [[Fantasy]] | Dreamlike and surreal visual compositions |
| ... | ... | ... | ... |
```

LLM search path: read Index → identify candidate topics → read specific files.

### Prompt Entry Format

```markdown
### {index}. {title}

{author/date/language metadata}

> {description}

{image/video embeds}

```
{prompt content}
```

[[Cinematic Portrait]] [[Double Exposure]] [[Urban Scene]] [[Conceptual Art]]

---
```

Links placed after the prompt content, before the separator.

## Step 5: Lint Mechanism

Add to project CLAUDE.md:

```markdown
## Wiki Lint
To lint the prompt vault:
1. Read 00-Index.md, iterate topic files
2. For each prompt, verify [[links]] are accurate and complete
3. Fix inaccurate links, add missing links
4. Update 00-Index.md summaries
5. Append changes to log.md
```

Triggered manually. Operates incrementally on individual files.

## Output Artifacts

| Artifact | Purpose |
|----------|---------|
| `prompts_imgae/00-Index.md` | Rich index for LLM search entry point |
| `prompts_imgae/{topic}.md` | Topic pages with prompts and bidirectional links |
| `prompts_video/00-Index.md` | Same for video prompts |
| `prompts_video/{topic}.md` | Same for video prompts |
| `log.md` | Chronological record of processing |
| Updated `CLAUDE.md` | Lint workflow instructions |

## What Changes From Current State

| Aspect | Before | After |
|--------|--------|-------|
| Classification | Regex, single category | LLM, multi-dimensional links |
| File structure | Nested folders (category/subcategory) | Flat files per topic |
| Links | Cross-category related (max 3) | Unlimited bidirectional links |
| Link language | Chinese | English |
| Index | Category tree with counts | Rich table with summaries and links |
| Search model | Browse folder → read file | Read index → drill into topic |
| Maintenance | Re-run script | Incremental lint |

## What Happens to Existing Scripts

- `scripts/categorize-prompts.py` — kept for reference, no longer used for output generation
- `scripts/categorize-video-prompts.py` — same
- New generation logic lives in the subagent prompts + a collection/output script

## Risks

1. **Subagent inconsistency**: Different subagents may use different link phrasings for the same concept. Mitigated by normalization step.
2. **Primary assignment too granular**: May produce hundreds of tiny files. Mitigated by distribution analysis and merging.
3. **Token cost**: ~72 subagent calls processing ~200 prompts each. Significant but one-time.
4. **Large files**: Some topics may still have many prompts. Acceptable — LLM can grep within a file.
