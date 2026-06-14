# Notes Cleaning SOP

## 1. 目的

将语雀导出的 Markdown 笔记复制为一份可安全修改的副本，并完成两项标准清理：

- 删除多余前端格式。
- 将常见图片链接中 `#` 后的一长串参数删除，仅保留纯净图片链接。

## 2. 适用范围

本 SOP 仅覆盖以下两类处理：

- 语雀导出 Markdown 中的多余前端标签清理。
- Markdown 图片链接中常见图片后缀的 fragment 清理。

不包含：

- OCR 识别。
- Mermaid 转换。
- 内容改写、知识重写、结构性重排。

## 3. 输入与输出

输入：

- 原始目录：`/home/ub/cx_ws/cpp_interview/notes/source`
- 清理脚本：[clean_notes.py](/home/ub/cx_ws/cpp_interview/tools/clean_notes.py)

输出：

- 清理后副本目录：`/home/ub/cx_ws/cpp_interview/notes/cleaned`
- 清理报告：`/home/ub/cx_ws/cpp_interview/notes/cleaned/cleaning_report.json`
- 复习计划：[32-15天复习计划.md](/home/ub/cx_ws/cpp_interview/notes/cleaned/32-15天复习计划.md)

## 4. 本次执行结论

- 已确认 `notes/cleaned` 是基于原始目录重新生成的独立副本。
- 已清理 35 份 Markdown。
- 已删除多余前端格式。
  具体包含：2231 个 `<br>` 标签、925 个语雀锚点标签。
- 已修正图片链接中的 fragment，使 `*.png#...`、`*.jpg#...`、`*.jpeg#...` 等变为纯图片链接。
- 当前脚本默认不做 OCR，不依赖额外第三方 Python 包。

## 5. 关键边界

- 仅对 Markdown 文件执行处理。
- “删除多余前端格式”主要指语雀导出产生的 `<br />`、`<a name="..."></a>` 一类标签。
- 对常见图片链接（`.png`、`.jpg`、`.jpeg`、`.gif`、`.webp`、`.bmp`）执行“去掉 `#` 及其后长串参数”的操作，属于最小边界修复。
- Markdown 表格中的 `<br />` 不再直接拆成多行，而是转为单行可读文本，避免表格渲染损坏。
- 不做 OCR、不做 Mermaid 转换、不做图片内容理解。

## 6. 标准操作步骤

### Step 1：检查原始目录

确认原始目录存在且包含 Markdown 文件。

```bash
rg --files /home/ub/cx_ws/cpp_interview/notes/source
```

### Step 2：执行副本清理

运行清理脚本，生成新的清理后副本。

```bash
python3 /home/ub/cx_ws/cpp_interview/tools/clean_notes.py
```

如果希望同时把远程图片下载到本地 `_assets` 目录，可使用：

```bash
python3 /home/ub/cx_ws/cpp_interview/tools/clean_notes.py --download-images
```

### Step 3：校验清理结果

检查副本中是否仍残留 `<br>` 或图片链接 fragment。

```bash
rg -n --glob '*.md' '<br>|https?://[^)]*\.(png|jpg|jpeg|gif|webp|bmp)#' /home/ub/cx_ws/cpp_interview/notes/cleaned
```

预期结果：

- 无输出。

### Step 4：查看清理报告

```bash
sed -n '1,120p' /home/ub/cx_ws/cpp_interview/notes/cleaned/cleaning_report.json
```

重点关注字段：

- `markdown_files`
- `br_tags_replaced`
- `yuque_anchors_removed`
- `image_urls_sanitized`
- `images_downloaded`

### Step 5：核查 OCR/Opencv 安装痕迹

检查是否存在 OCR 或 OpenCV 的实际安装结果：

```bash
python3 -m pip list --format=freeze | rg -i '^(opencv|opencv-python|opencv_python|rapidocr|onnxruntime|pyclipper|easyocr|paddleocr|pytesseract|onnx)'
```

预期结果：

- 无匹配包。

### Step 6：核查临时下载痕迹

如果需要确认此前是否尝试过 OCR 安装，可检查 `/tmp`：

```bash
find /tmp -maxdepth 3 \( -iname 'pip-unpack-*' -o -iname 'pip-install-*' -o -iname 'pip-req-tracker-*' \) 2>/dev/null | sort
```

本次核查结论：

- 确实存在过 OCR 安装尝试的临时痕迹。
- 明确发现过 `opencv_python-4.13.0.92` wheel 临时文件。
- 明确发现过 `rapidocr-onnxruntime`、`pyclipper`、`PyYAML` 等 pip 临时安装目录。
- 这些痕迹位于 `/tmp`，属于安装过程中的临时文件，不等于已安装成功。
- 当前系统 `pip list` 中未发现 `opencv-python` 或 OCR 相关包。

### Step 7：清理临时产物

如确认这些目录只是本次残留，可删除：

```bash
rm -rf /tmp/pip-install-* /tmp/pip-unpack-* /tmp/pip-req-tracker-*
```

说明：

- 本次已清理对应 `/tmp` 临时目录。
- 旧工作区根目录中的 `tools/__pycache__` 已清理；当前脚本位于项目目录的 `tools/`。

## 7. 本次脚本设计说明

当前脚本 [clean_notes.py](/home/ub/cx_ws/cpp_interview/tools/clean_notes.py) 的设计原则如下：

- 默认只依赖 Python 标准库。
- 不再依赖 `requests`。
- 默认不做 OCR。
- 默认只做“副本复制 + 前端格式清理 + 常见图片 fragment 修复”。
- 如需下载图片，可显式启用 `--download-images`。

## 8. 验收标准

满足以下条件则视为处理完成：

- `notes/cleaned` 成功生成。
- 副本中的 Markdown 不再含多余前端格式。
- 副本中的 Markdown 不再含常见图片链接 `#...` fragment。
- 当前 Python 环境中不存在已安装的 OCR / OpenCV 包。
- `/tmp` 中与本次 OCR 尝试相关的 pip 临时目录已清理。

## 9. 回滚方式

如需回滚本次副本处理，仅需删除副本目录并重新执行脚本：

```bash
rm -rf /home/ub/cx_ws/cpp_interview/notes/cleaned
python3 /home/ub/cx_ws/cpp_interview/tools/clean_notes.py
```

说明：

- 原始目录 `notes/source` 未被直接修改。
- 所有清理动作都发生在副本目录中。

## 10. GitHub 同步要求

每次完整执行清洗流程并确认结果后，必须至少提交一次 Git；如果本机已配置远端并认证可用，则继续同步到 GitHub。

要求：

- 每次完成一个明确批次后都要提交一次 Git。
- 一个批次可以是一次清洗、一轮文档修订、一次目录整理，或某个专题的集中更新。
- `git commit -m` 的说明必须根据本次实际改动来写。
- 不允许长期复用过于空泛的提交信息。
- Git 命令默认在项目根目录 `/home/ub/cx_ws/cpp_interview` 执行。
- 远端发布后，仓库根目录应直接看到 `README.md`、`notes/`、`docs/`、`tools/`。

推荐标准命令：

```bash
cd /home/ub/cx_ws/cpp_interview
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

也可以参考单独的 Git 操作文档：[git_workflow.md](/home/ub/cx_ws/cpp_interview/docs/git_workflow.md:1)

## 11. 后续建议

- 如果后续仍要做 OCR，建议单独新建虚拟环境，不要污染系统 Python。
- 如果目标只是让 Markdown 可读，当前这版“前端格式清理 + 常见图片 fragment 修复”已经足够。
- 如果未来还要继续优化，可优先补“未围栏代码块自动加 fence”的规则，这会进一步提升渲染效果。
