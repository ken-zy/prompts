# Project: Nano Banana Pro Prompts

## 项目说明
- 从 YouMind 抓取的 12465 条 Nano Banana Pro AI 图像生成提示词
- 分类为 14 大类 ~60 子分类的 Obsidian vault，带 `[[双向链接]]`

## 目录结构
- `prompts_imgae/` — Obsidian vault 输出目录（目录名拼写如此，勿改）
- `scripts/categorize-prompts.py` — 分类脚本，可重新生成 vault：`python3 scripts/categorize-prompts.py`
- `scripts/categorize-prompts.py test` — 运行分类规则测试
- `40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json` — 原始数据（86MB, 12465 条）

## YouMind API
- `POST https://youmind.com/youhome-api/prompts` — 提示词分页接口
- 必须带 `Referer: https://youmind.com/zh-CN/nano-banana-pro-prompts` 和 `Origin: https://youmind.com`，否则 403
- 参数：`{model, page, limit(max 100), locale}`
- 并发请求容易超时，建议串行 + 0.3s 间隔

## 注意事项
- 长时间 API 批量请求脚本建议分批执行（每批 25 页），避免单次运行超时
- 分类脚本内置质量阈值：未分类 < 8%，综合类 < 40%
