# Nano Banana Pro Prompts Categorization Design

## Overview

Categorize 12,465 Nano Banana Pro image generation prompts from YouMind into a two-level taxonomy with Obsidian-style `[[wiki-link]]` bidirectional links.

## Data Source

- `40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json` (86 MB)
- JSON root structure: `{ total: number, prompts: Array<Prompt>, fetched_at: string }`
- Prompt fields: id, title, description, content, translatedContent, media, mediaThumbnails, language, author, sourceLink, sourcePublishedAt, sourcePlatform, featured, likes, needReferenceImages, promptCategories
- No existing categories (`promptCategories` is empty for all prompts)
- Language distribution: en(10629), ja(1333), zh(461), ko(41), de(1)
- 451 prompts have no `media`, 4 have no `sourceLink`

## Output Structure

```
prompts/
├── 00-Index.md                          # Master index linking all categories
├── 人像摄影/
│   ├── _人像摄影.md                      # Category index page
│   ├── 电影感肖像.md                     # Subcategory file (contains all prompts)
│   ├── 镜面自拍.md
│   └── ...
├── 时尚与造型/
│   ├── _时尚与造型.md
│   └── ...
└── ...（14 categories total）
```

- Category index files prefixed with `_` to sort to top
- Each subcategory `.md` contains all prompts in that subcategory
- Estimated ~70-75 total `.md` files

## Category Taxonomy

| Category | Subcategories |
|----------|--------------|
| 人像摄影 | 电影感肖像, 镜面自拍, 街拍写真, 证件照与正式照, 群像与多人, 综合人像 |
| 时尚与造型 | 时装大片, 运动休闲, 婚纱婚礼, Cosplay, 综合时尚 |
| 产品与广告 | 食品饮料, 科技产品, 美妆护肤, 品牌广告, 综合产品 |
| 艺术风格 | 浮世绘与日本传统, 水彩, 油画, 像素艺术, 手绘素描, 综合艺术 |
| 3D与微缩 | 微缩模型与立体模型, 3D渲染, 蒸汽朋克机械, 综合3D |
| 信息图表 | Bento网格信息图, 数据可视化, 地图, 综合图表 |
| 海报与设计 | 电影海报, 活动海报, 名片与Logo, 贴纸, 综合设计 |
| 建筑与空间 | 室内设计, 建筑摄影, 城市场景, 综合建筑 |
| 动漫与卡通 | 日系动漫, Q版角色, LINE贴图, 漫画风, 综合动漫 |
| 节日与主题 | 圣诞节, 新年, 万圣节, 情人节, 综合节日 |
| 奇幻与科幻 | 赛博朋克, 奇幻世界, 超现实, 概念艺术, 综合奇幻 |
| 食物与生活 | 美食摄影, 宠物, 旅行, 综合生活 |
| 工具与模板 | JSON结构化提示, 批量模板, 风格迁移, 修复与增强, 综合工具 |
| 其他 | 未分类 |

## Classification Rules

Priority-based keyword matching on **title + description + content + translatedContent** (all four fields concatenated for matching, ensuring non-English prompts are classifiable via their Chinese translations):

1. **Exact match**: Title contains definitive keywords → direct classification
2. **Combo match**: Multiple keywords co-occurring → more specific subcategory
3. **Fallback match**: Only major category keywords → 综合 subcategory
4. **No match** → 其他/未分类

Each prompt is assigned to exactly ONE subcategory. Cross-category prompts are linked via `**Related**: [[other-subcategory]]`.

### Quality Thresholds

- 其他/未分类 must be < 8% of total (< ~1000 prompts)
- Any single 综合 subcategory must be < 40% of its parent category
- If thresholds exceeded, classification rules must be refined before output

## Bidirectional Link Format

### Related link vocabulary

All `[[wiki-links]]` MUST reference actual file names from the taxonomy. No free-form links. The generation script validates every `[[link]]` against the set of generated files and removes any that would be dangling.

### Subcategory file header
```markdown
---
category: 人像摄影
subcategory: 电影感肖像
count: 342
---

# 电影感肖像

所属大类：[[_人像摄影]]
相关分类：[[街拍写真]]、[[电影海报]]
```

### Individual prompt entry
```markdown
---

### 1. Prompt Title

**Author**: [name](link) | **Date**: 2025-11-21 | **Language**: en

> Description text

![Example](image_url)

**Prompt:**

\```
prompt content
\```

**Related**: [[镜面自拍]]、[[赛博朋克]]
```

### Missing field fallbacks

- No `media` → omit image block entirely
- No `sourceLink` → display author name and date as plain text (no link)
- No `author` → omit author field
- `Date` field is sourced from `sourcePublishedAt` (truncated to YYYY-MM-DD)

### Link rules
- Subcategory header → `[[_category-index]]` (upward link)
- Subcategory header → `[[related-subcategories]]` (horizontal link, controlled vocabulary only)
- Individual prompt → `[[cross-category-subcategory]]` (only when clearly cross-category, controlled vocabulary only)
- Category index → `[[all-subcategories]]` (downward link)
- Master index → `[[all-category-indexes]]`

## Implementation Approach

1. Write a Python classification script that:
   - Loads `data["prompts"]` from the JSON root object
   - Concatenates title + description + content + translatedContent for keyword matching
   - Applies keyword rules to classify each prompt
   - Detects cross-category keywords for Related links (controlled vocabulary only)
   - Validates all `[[links]]` against generated file set
   - Generates all `.md` files with proper formatting, fallbacks for missing fields
2. Run the script to generate the full Obsidian vault structure
3. Verify output:
   - File count matches expected subcategories
   - Sum of all prompt counts equals 12,465
   - No dangling `[[links]]`
   - 未分类 < 8% of total
   - No 综合 subcategory exceeds 40% of its parent category
   - Output a classification statistics report (category/subcategory counts)
