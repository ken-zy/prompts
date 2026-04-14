# Prompt Categorization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Classify 12,465 Nano Banana Pro prompts into a two-level taxonomy and generate an Obsidian vault with bidirectional `[[wiki-links]]`.

**Architecture:** Single Python script (`scripts/categorize-prompts.py`) reads the JSON data, classifies each prompt via keyword rules, then generates ~75 Markdown files organized into 14 category folders under `prompts/`. A separate validation pass checks link integrity and quality thresholds.

**Tech Stack:** Python 3 (stdlib only: json, os, re, collections)

---

## File Structure

```
scripts/
  categorize-prompts.py          # Main script: classify + generate Markdown vault
prompts/                          # Generated output (Obsidian vault)
  00-Index.md
  人像摄影/
    _人像摄影.md
    电影感肖像.md
    ...
  ... (14 category folders)
```

---

### Task 1: Define taxonomy data structure and keyword rules

**Files:**
- Create: `scripts/categorize-prompts.py`

This task creates the script with the complete taxonomy definition and keyword mapping. No classification logic yet — just the data structures.

- [ ] **Step 1: Create the script with taxonomy and keyword rules**

Create `scripts/categorize-prompts.py` containing:

1. Constants: `INPUT_FILE`, `OUTPUT_DIR`
2. `TAXONOMY` dict: `{ category_name: [subcategory_names] }` with all 14 categories and ~60 subcategories as defined in the spec.
3. `SUBCATEGORY_RULES` dict: `{ subcategory_name: [regex_patterns] }` — keyword patterns matched case-insensitively against concatenated prompt text. Rules are ordered by specificity (more specific subcategories first within each category group). Key patterns:

   - 人像摄影: `镜面自拍|mirror|selfie`, `电影感|cinematic.*portrait`, `街拍|street.*photo`, `证件照|id.*photo`, `群像|group.*photo|多人`, fallback `肖像|portrait`
   - 时尚与造型: `cosplay`, `婚纱|wedding`, `运动|sport|gym`, `时装|fashion|haute couture`, fallback `穿搭|outfit`
   - 产品与广告: `食品|饮料|food|drink|burger|coffee`, `科技产品|tech.*product|smartphone|laptop`, `美妆|makeup|skincare`, `品牌|brand|广告|commercial`, fallback `产品|product`
   - 艺术风格: `浮世绘|ukiyo|woodblock`, `水彩|watercolor`, `油画|oil.*paint|impressionist`, `像素|pixel.*art`, `手绘|sketch|pencil|chalkboard`, fallback `艺术|art.*style|painting|illustration`
   - 3D与微缩: `蒸汽朋克|steampunk|clockwork`, `微缩|miniature|diorama|tilt.*shift`, `3d.*render|blender|c4d|isometric`, fallback `3d|sculpt|雕塑`
   - 信息图表: `bento.*grid|网格.*信息|液态玻璃.*信息`, `数据可视化|data.*viz|chart|dashboard`, `地图|map|geographic`, fallback `信息图|infograph|diagram`
   - 海报与设计: `电影海报|movie.*poster`, `海报|poster|flyer|banner`, `名片|business.*card|logo|badge`, `贴纸|sticker|emoji`, fallback `设计|design|graphic|typography`
   - 建筑与空间: `室内|interior|家居|furniture`, `建筑|architect|building|skyscraper`, `城市场景|cityscape|skyline|nightcity`, fallback `空间|environment`
   - 动漫与卡通: `line贴图|line.*sticker`, `q版|chibi|kawaii|mascot`, `动漫|anime|manga.*character|二次元`, `漫画|manga|comic`, fallback `卡通|cartoon|character.*design`
   - 节日与主题: `圣诞|christmas|santa`, `新年|new.*year|元旦|春节`, `万圣|halloween|pumpkin`, `情人节|valentine`, fallback `节日|festival|birthday|party`
   - 奇幻与科幻: `赛博朋克|cyberpunk|neon.*city`, `奇幻|fantasy|magic|dragon|medieval`, `超现实|surreal|dreamlike`, `概念艺术|concept.*art|sci.*fi|space|mech`, fallback `幻想|fictional`
   - 食物与生活: `美食|food.*photography|cuisine|restaurant`, `宠物|pet|cat|dog|animal`, `旅行|travel|landscape|beach|sunset`, fallback `生活|lifestyle|daily`
   - 工具与模板: `json|structured.*prompt|\{.*scene.*subject`, `风格迁移|style.*transfer|image.*to.*image|reimagin`, `修复|restore|enhance|upscale|coloriz`, `模板|template|batch|parameteriz|\[插入`, fallback `工具|tool|tutorial|guide`

4. `RELATED_PAIRS` list: ~23 curated bidirectional pairs between subcategories (e.g. `("电影感肖像", "电影海报")`, `("Cosplay", "日系动漫")`, `("赛博朋克", "城市场景")`).
5. Derived lookups: `SUB_TO_CAT` (subcategory -> category), `RELATED_MAP` (bidirectional), `ALL_SUBCATEGORIES` set.

- [ ] **Step 2: Run syntax check**

Run: `python3 -c "exec(open('scripts/categorize-prompts.py').read()); print(f'Taxonomy: {len(TAXONOMY)} categories, {len(SUB_TO_CAT)} subcategories'); print(f'Rules: {len(SUBCATEGORY_RULES)} subcategories with rules'); print(f'Related pairs: {len(RELATED_PAIRS)}')"`

Expected: `Taxonomy: 14 categories, ~60 subcategories`, no errors.

- [ ] **Step 3: Commit**

```
git add scripts/categorize-prompts.py
git commit -m "feat(categorize): define taxonomy, keyword rules, and related links"
```

---

### Task 2: Implement classification function

**Files:**
- Modify: `scripts/categorize-prompts.py`

Add the `classify_prompt()` function and the cross-category Related link detection.

- [ ] **Step 1: Add classification functions**

Add these functions:

1. `get_match_text(prompt)` — concatenate `title + description + content + translatedContent`, lowercased.
2. `classify_prompt(prompt)` — iterate `SUBCATEGORY_RULES` in order, collect all matching subcategories, assign primary = first match, collect cross-category matches (different parent category) as Related links (max 3). Return `(category, subcategory, related_list)`. No match → `("其他", "未分类", [])`.

- [ ] **Step 2: Add test harness**

Add `test_classification()` function with 5 synthetic test cases covering: exact match, combo match, cross-category detection, translatedContent matching, and no-match fallback. Guard with `if __name__ == "__main__"` and `sys.argv[1] == "test"`.

- [ ] **Step 3: Run test**

Run: `python3 scripts/categorize-prompts.py test`

Expected: All 5 test cases PASS.

- [ ] **Step 4: Commit**

```
git add scripts/categorize-prompts.py
git commit -m "feat(categorize): implement classification function with cross-category linking"
```

---

### Task 3: Implement Markdown generation

**Files:**
- Modify: `scripts/categorize-prompts.py`

Add functions that generate: subcategory files, category index files, and the master index.

- [ ] **Step 1: Add Markdown generation functions**

Add these functions:

1. `format_prompt_entry(prompt, index)` — format one prompt as Markdown with:
   - `### {index}. {title}`
   - Meta line: Author (linked if sourceLink exists, plain text otherwise), Date (from sourcePublishedAt[:10]), Language
   - Blockquote description (if exists)
   - Images from `media` array (omit block entirely if empty/missing)
   - Prompt content in fenced code block (use ```````` to avoid conflicts)
   - Fallbacks: no media → skip images, no sourceLink → plain author, no author → omit

2. `format_prompt_related(related_subs)` — format `**Related**: [[sub1]]、[[sub2]]` line, validating each against `ALL_SUBCATEGORIES`. Return empty string if no valid links.

3. `generate_subcategory_file(cat, sub, prompts_in_sub, related_subs)` — generate full subcategory .md with:
   - YAML frontmatter (category, subcategory, count)
   - `# {sub}` heading
   - `所属大类：[[_{cat}]]` upward link
   - `相关分类：[[...]]` horizontal links from `RELATED_MAP` (controlled vocabulary)
   - All prompt entries with separator `---`

4. `generate_category_index(cat, subcategory_counts)` — generate `_{cat}.md` with heading, total count, list of `[[subcategory]] (count)` links.

5. `generate_master_index(category_stats)` — generate `00-Index.md` with total, then for each category: `### [[_{cat}]] (count)` with subcategory list.

- [ ] **Step 2: Commit**

```
git add scripts/categorize-prompts.py
git commit -m "feat(categorize): add Markdown generation functions"
```

---

### Task 4: Implement main pipeline and validation

**Files:**
- Modify: `scripts/categorize-prompts.py`

Wire everything together: load data, classify, generate files, validate quality thresholds, print statistics report.

- [ ] **Step 1: Add `run_pipeline()` function**

Implement main pipeline:

1. Load JSON: `data["prompts"]` from INPUT_FILE
2. Classify all prompts into `classified = { cat: { sub: [(prompt, related)] } }`
3. Compute `category_stats = { cat: { sub: count } }`
4. Print statistics report: each category with subcategory counts and percentages, flag 综合 > 40%
5. Validate quality thresholds:
   - 未分类 < 8% of total
   - No 综合 subcategory > 40% of parent category
   - If fail → print errors and exit without generating files
6. Generate output:
   - Create category directories under OUTPUT_DIR
   - Write category index files (`_{cat}.md`)
   - Write subcategory files with all prompts
   - Write master index (`00-Index.md`)
   - Track all generated file names as link targets
7. Validate links: scan all `[[...]]` in generated files against link target set, report dangling links
8. Print summary: file count, link target count, dangling count

Update `if __name__` to call `run_pipeline()` by default, `test_classification()` with `test` arg.

- [ ] **Step 2: Run the full pipeline**

Run: `python3 scripts/categorize-prompts.py`

Expected output:
- Classification statistics for all 14 categories
- Quality check PASSED (未分类 < 8%, no 综合 > 40%)
- ~70 files generated
- No dangling links

- [ ] **Step 3: Spot-check generated files**

Run: `head -30 prompts/人像摄影/电影感肖像.md` and `head -20 prompts/00-Index.md` and `ls prompts/*/`

Verify: YAML frontmatter correct, `[[links]]` present, prompt content renders properly.

- [ ] **Step 4: Commit all generated files**

```
git add scripts/categorize-prompts.py prompts/
git commit -m "feat: generate categorized Obsidian vault with 12465 prompts and bidirectional links"
```

---

### Task 5: Iterate on keyword rules if quality thresholds fail

**Files:**
- Modify: `scripts/categorize-prompts.py` (SUBCATEGORY_RULES only)

This task is **conditional** — only needed if Task 4 Step 2 reports quality check failures.

- [ ] **Step 1: Analyze failures**

If 未分类 > 8%: sample 50 uncategorized prompts, print their titles, identify missing keyword patterns.

- [ ] **Step 2: Add missing keyword patterns to SUBCATEGORY_RULES**

Based on the sampled titles, add new regex patterns to existing subcategories or broaden existing patterns.

- [ ] **Step 3: Re-run pipeline and verify quality passes**

Run: `python3 scripts/categorize-prompts.py`

- [ ] **Step 4: Commit updated rules**

```
git add scripts/categorize-prompts.py prompts/
git commit -m "fix(categorize): refine keyword rules to reduce uncategorized prompts"
```

---

### Task 6: Clean up temporary files

**Files:**
- Delete: `40_Reference/Articles/20260414/世界上最大的-nano-banana-pro-免费提示词库持续更新-youmind.md`
- Delete: `40_Reference/Articles/20260414/nano-banana-pro-prompts-complete.md`
- Keep: `40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json`

- [ ] **Step 1: Remove obsolete files**

```
rm "40_Reference/Articles/20260414/世界上最大的-nano-banana-pro-免费提示词库持续更新-youmind.md"
rm "40_Reference/Articles/20260414/nano-banana-pro-prompts-complete.md"
rm -f /tmp/prompts_*.json
```

- [ ] **Step 2: Commit cleanup**

```
git add -A
git commit -m "chore: remove obsolete prompt files, keep source JSON and categorized vault"
```
