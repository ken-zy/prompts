# Vault Generation v2: Chunk-Based Organization for LLM Retrieval

## Problem

The v1 design (see `2026-04-15-prompt-reclassification-design.md`) used LLM-generated `primary` labels to group prompts into topic files. This failed: 12024 unique primaries for 12465 image prompts meant 99% of prompts fell into Miscellaneous. The `primary` field is too granular for grouping.

Additionally, the 44607 unique `links` have severe redundancy (43059 appear only 1-4 times) and incomplete normalization (250+ Celebrity variants, 200+ Identity variants).

## Design Decision Summary

| Decision | Choice | Rationale |
|----------|--------|-----------|
| File organization | Fixed-size chunks (~200 prompts) | Uniform file sizes, no grouping dependency |
| Intra-chunk ordering | Semantic sort by anchor topics | Clusters related prompts, improves grep locality |
| Index model | Topic inverted index (~70 rows) | Compact enough for single LLM read |
| Per-prompt links | search_links: freq >= 5, max 4 | Balance between noise reduction and recall (83.1% coverage) |
| Raw link preservation | Keep in source JSON, not in vault | Available for re-normalization, not in retrieval path |
| Primary use case | LLM retrieval | Not optimized for human browsing |

## Architecture

Same two independent pipelines as v1:

```
Pipeline 1: Image (prompts_imgae/)
normalized_image.json + raw JSON ──→ generate-vault.py ──→ 00-Index.md + chunk-{NNN}.md

Pipeline 2: Video (prompts_video/)
normalized_video.json + raw JSON ──→ generate-vault.py ──→ 00-Index.md + chunk-{NNN}.md
```

## Data Sources

- Image: `tmp/normalized_image.json` (12465 tagged prompts) + `40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json` (raw)
- Video: `tmp/normalized_video.json` (1753 tagged prompts) + `40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json` (raw)

## Configuration

```python
CHUNK_SIZE = 200          # prompts per chunk file
ANCHOR_MIN_FREQ = 50      # minimum link frequency to be an anchor topic
SEARCH_LINK_MIN_FREQ = 5  # minimum link frequency to be a search_link
SEARCH_LINK_MAX = 4       # max search_links per prompt
```

## Step 1: Build Link Frequency Table

Scan all prompts in `normalized_{pipeline}.json`, count global frequency of every link.

Output: `dict[str, int]` mapping link → count.

Key stats (image pipeline):
- freq >= 50: ~70 links (used as anchors + Index topics)
- freq >= 5: ~1548 links (used as search_links)
- freq < 5: ~43059 links (dropped from vault, kept in source JSON)

## Step 2: Select search_links Per Prompt

For each prompt's original links (4-7 items):

1. **Filter**: keep only links with global freq >= `SEARCH_LINK_MIN_FREQ` (5)
2. **Sort**: by frequency descending
3. **Truncate**: keep at most `SEARCH_LINK_MAX` (4)
4. **Fallback**: if empty after filtering, keep the 1 link with highest frequency from the original set

Guarantees: every prompt has at least 1 search_link. ~83% of prompts retain 2+ links.

## Step 3: Assign Anchor and Sort

### Anchor assignment

For each prompt, from its search_links pick the one with highest frequency that is also in the anchor set (freq >= `ANCHOR_MIN_FREQ`). If none qualifies, mark as "unanchored".

### Sort order

1. Anchored prompts: sorted by anchor name (alphabetical), then by original data order within same anchor
2. Unanchored prompts: appended at the end, in original data order

### Chunking

Slice the sorted list into groups of `CHUNK_SIZE`. Last chunk may be smaller.

Effect: prompts sharing the same anchor cluster together in 1-2 adjacent chunks. A grep for `[[Macro Photography]]` hits a concentrated region rather than scattering across all files.

## Step 4: Generate Chunk Files

### File naming

```
chunk-001.md, chunk-002.md, ..., chunk-063.md
```

### Chunk file format

```markdown
# Chunk 001

Total: 200 prompts

### 1. {title}

**Author**: [{author_name}]({author_link})  **Date**: {YYYY-MM-DD}  **Language**: {language}

> {description}

![{title}]({media_url})

\```
{prompt content}
\```

[[Link A]] [[Link B]] [[Link C]]

---

### 2. {title}
...
```

Each prompt entry contains:
- Title (h3 with index)
- Metadata line (author, date, language — only if present)
- Description blockquote (if present)
- Media embeds: images for image pipeline, video links + thumbnails for video pipeline
- Prompt content in fenced code block
- search_links as `[[bidirectional links]]`
- Horizontal rule separator

## Step 5: Generate 00-Index.md

### Format

```markdown
# {Vault Title}

Total: {N} prompts, {M} chunk files

## Index

| Topic | Chunks | Count |
|-------|--------|-------|
| Lifestyle Photography | 001, 002 | 266 |
| Celebrity Portrait | 002, 003 | 263 |
| Mirror Selfie | 003, 004 | 236 |
| ...（~70 rows） | ... | ... |
```

### Generation logic

1. Collect all anchor topics (freq >= `ANCHOR_MIN_FREQ`)
2. For each topic, scan all chunks: count how many prompts in that chunk have this topic as a search_link, record chunk numbers where count > 0
3. Sort topics by total count descending
4. Render table

### LLM retrieval path

```
Query: "macro photography prompts"
  → Read 00-Index.md (~70 rows) → find "Macro Photography → chunks 012, 013, count=118"
  → Read chunk-012.md → grep [[Macro Photography]]
  → Return matching prompts
```

Maximum 2 file reads to reach target prompts.

## Implementation Scope

### File changes

Only modify: `scripts/generate-vault.py`

### Functions to add

| Function | Purpose |
|----------|---------|
| `build_link_freq(tagged_data)` | Count global link frequencies, return dict |
| `select_search_links(links, freq_table)` | Filter + rank + truncate links per prompt |
| `assign_anchor(search_links, anchor_set)` | Pick best anchor for a prompt |

### Functions to modify

| Function | Change |
|----------|--------|
| `run_pipeline()` | Replace primary-grouping with: build freq → select links → assign anchors → sort → chunk → generate |

### Functions/logic to remove

- Primary-based grouping (`groups_raw`, `groups[primary]`)
- Miscellaneous merging logic
- `min_group` parameter

### Output

| Pipeline | Prompts | Expected chunks | Index rows |
|----------|---------|----------------|------------|
| Image | 12465 | ~63 | ~70 |
| Video | 1753 | ~9 | TBD (different link distribution) |

## What Changes From v1 Design

| Aspect | v1 | v2 |
|--------|----|----|
| File grouping | By `primary` label | Fixed-size chunks |
| File naming | `{topic}.md` | `chunk-{NNN}.md` |
| Intra-file order | Random within group | Semantic sort by anchor |
| Per-prompt links | All links (4-7) | search_links only (max 4, freq >= 5) |
| Index format | Topic → count + related links | Topic → chunk numbers + count |
| Miscellaneous handling | Catch-all file | No special handling (unanchored at end) |

## Risks

1. **Video pipeline anchor coverage**: Video prompts have different link distribution. The 70 anchors from image data won't apply; video anchors computed independently may be fewer. Mitigation: `ANCHOR_MIN_FREQ` can be tuned per pipeline.
2. **Chunk boundary splits topics**: A topic with 250 prompts may span 2 chunks due to fixed sizing. Acceptable — Index tells LLM which chunks to read.
3. **search_link quality depends on normalization**: The freq >= 5 filter inherits normalization gaps (e.g., "Identity Preservation" vs "Identity Lock" both survive as separate links). Mitigation: acceptable for v2; can re-normalize later using raw_links.
