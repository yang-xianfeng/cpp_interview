# Notes Cleaning SOP

## 1. 目的

把 `notes/source/` 中的原始 Markdown 复制为可安全修改的副本，并完成标准清理。

- 删除多余前端格式。
- 清理常见图片链接里 `#` 后的 fragment 参数。

## 2. 适用范围

本 SOP 仅覆盖以下两类处理：

- 语雀导出 Markdown 中的多余前端标签清理。
- Markdown 图片链接中常见图片后缀的 fragment 清理。

不包含：

- OCR 识别。
- 内容改写、知识重写、结构性重排。
- Mermaid 转换。

## 3. 输入与输出

- 输入目录：`notes/source`
- 清理脚本：[clean_notes.py](../tools/clean_notes.py)
- 输出目录：`notes/cleaned`
- 清理报告：`notes/cleaned/cleaning_report.json`

## 4. 关键边界

- 仅对 Markdown 文件执行处理。
- “删除多余前端格式”主要指语雀导出产生的 `<br />`、`<a name="..."></a>` 一类标签。
- 对常见图片链接（`.png`、`.jpg`、`.jpeg`、`.gif`、`.webp`、`.bmp`）执行“去掉 `#` 及其后长串参数”的操作，属于最小边界修复。
- Markdown 表格中的 `<br />` 不再直接拆成多行，而是转为单行可读文本，避免表格渲染损坏。
- 默认不做 OCR，不依赖 OpenCV 一类额外图像能力。
- 不做图片内容理解，不做知识改写。

## 5. 标准操作步骤

所有命令默认在项目根目录执行：

```bash
cd ~/cx_ws/cpp_interview
```

### Step 1：检查原始目录

确认原始目录存在且包含 Markdown 文件。

```bash
rg --files notes/source
```

### Step 2：执行副本清理

运行清理脚本，生成新的清理后副本。

```bash
python3 tools/clean_notes.py
```

如果希望同时把远程图片下载到本地 `_assets` 目录，可使用：

```bash
python3 tools/clean_notes.py --download-images
```

### Step 3：校验清理结果

检查副本中是否仍残留 `<br>` 或图片链接 fragment。

```bash
rg -n --glob '*.md' '<br>|https?://[^)]*\.(png|jpg|jpeg|gif|webp|bmp)#' notes/cleaned
```

预期结果：

- 无输出。

### Step 4：查看清理报告

```bash
sed -n '1,120p' notes/cleaned/cleaning_report.json
```

重点关注字段：

- `markdown_files`
- `br_tags_replaced`
- `yuque_anchors_removed`
- `image_urls_sanitized`
- `images_downloaded`

## 6. 脚本约定

当前脚本 [clean_notes.py](../tools/clean_notes.py) 的设计原则如下：

- 默认只依赖 Python 标准库。
- 不再依赖 `requests`。
- 默认不做 OCR。
- 默认只做“副本复制 + 前端格式清理 + 常见图片 fragment 修复”。
- 如需下载图片，可显式启用 `--download-images`。

## 7. 验收标准

满足以下条件则视为处理完成：

- `notes/cleaned` 成功生成。
- 副本中的 Markdown 不再含多余前端格式。
- 副本中的 Markdown 不再含常见图片链接 `#...` fragment。
- 清理报告可正常读取，关键计数字段存在。

## 8. 回滚方式

如需回滚本次副本处理，仅需删除副本目录并重新执行脚本：

```bash
rm -rf notes/cleaned
python3 tools/clean_notes.py
```

说明：

- 原始目录 `notes/source` 未被直接修改。
- 所有清理动作都发生在副本目录中。

## 9. Git 同步要求

每次完整执行清洗流程并确认结果后，必须至少提交一次 Git；如果本机已配置远端并认证可用，则继续同步到 GitHub。

要求：

- 每次完成一个明确批次后都要提交一次 Git。
- 一个批次可以是一次清洗、一轮文档修订、一次目录整理，或某个专题的集中更新。
- `git commit -m` 的说明必须根据本次实际改动来写。
- 不允许长期复用过于空泛的提交信息。
- Git 命令默认在项目根目录执行。

推荐标准命令：

```bash
cd ~/cx_ws/cpp_interview
git status
git add .
git commit -m "<根据本次清洗内容填写说明>"
git push
```

如果本次只更新了某个专题，也可以把提交信息写得更具体，例如：

```bash
git commit -m "Refresh cleaned notes and SOP"
git commit -m "Refresh notes index and cleaning docs"
```

也可以参考单独的 Git 操作文档：[git_workflow.md](git_workflow.md)

## 10. 后续建议

- 如果后续要做 OCR，建议放到独立虚拟环境，不要污染默认环境。
- 如果目标只是让 Markdown 可读，当前这版清洗已经足够。
- 如果未来继续优化，可优先补“未围栏代码块自动加 fence”的规则。
