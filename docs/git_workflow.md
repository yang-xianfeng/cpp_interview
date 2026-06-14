# Git Workflow

这个文档定义 `cpp_interview/` 项目的标准 Git 提交流程。

## 默认位置

- 工作空间：`~/cx_ws`
- 项目根目录：`~/cx_ws/cpp_interview`
- Git 目录：`~/cx_ws/cpp_interview/.git`
- 远端仓库：`origin -> git@github.com:yang-xianfeng/cpp_interview.git`

## 基本规则

- `cx_ws/` 只是工作空间，不是当前项目的 Git 根目录。
- `cpp_interview/` 是默认工作目录，也是 Git 命令默认执行位置。
- 每完成一个明确批次，就提交一次 Git。
- 提交信息必须描述本次真实改动。
- 远端认证可用时，提交后立即推送。

## 标准命令

```bash
cd ~/cx_ws/cpp_interview
git status
git add .
git commit -m "<根据本次改动填写说明>"
git push
```

## 提交信息建议

提交信息按“动作 + 对象”写，优先用下面这些常用模板：

```bash
git commit -m "Refine project docs and navigation"
git commit -m "Refresh cleaned notes and index"
git commit -m "Rename notes files and update references"
git commit -m "Update tools and cleaning workflow"
git commit -m "Polish interview notes and project writeups"
```

不要这样写：

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "submit files"
```

## 适用范围

适用于当前项目的所有常规更新，包括 `notes/`、`docs/`、`tools/` 和项目根目录文档。
