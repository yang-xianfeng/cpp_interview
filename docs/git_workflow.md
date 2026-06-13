# Git Workflow

这个文档说明当前仓库的标准 Git 提交流程。

## 适用范围

适用于本仓库内所有内容更新，包括：

- `notes/`
- `docs/`
- `tools/`
- 根目录导航文档

## 基本规则

每次完成一轮明确的整理、清洗、重命名、结构调整或文档更新后，都要至少提交一次 Git。

推荐原则：

- 一轮完整操作，对应一次提交。
- 提交信息必须描述本次真实改动，不能长期复用一个泛化说明。
- 如果远端已配置且认证可用，提交后立即推送。

## 标准命令

```bash
cd /home/ub/cx_ws
git status
git add .
git commit -m "<根据本次改动填写说明>"
git push
```

## 提交信息建议

提交信息要按本次改动内容具体写，推荐使用“动作 + 对象”的方式：

```bash
git commit -m "Refine notes structure and navigation"
git commit -m "Refresh cleaned notes and SOP"
git commit -m "Rename notes files and update references"
git commit -m "Update git workflow and project docs"
```

不要这样写：

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "submit files"
```

## 说明

- 如果只是本地留档，至少要完成 `git add` 和 `git commit`。
- 如果要同步到 GitHub，继续执行 `git push`。
- 当前仓库已配置 `origin` 并可通过 SSH 推送。
