# Git Workflow

这个文档说明 `cpp_interview/` 项目的标准 Git 提交流程。

## 本地与远端约定

- 本地工作空间根目录：`/home/ub/cx_ws`
- 当前项目目录：`/home/ub/cx_ws/cpp_interview`
- GitHub 远端仓库根目录：发布后的 `cpp_interview/` 子目录内容
- 远端目录层级：只保留一层项目内容，不出现 `cpp_interview/cpp_interview`
- 当前远端：`origin -> git@github.com:yang-xianfeng/cpp_interview.git`

## 标准形态

对于刚开始使用 Codex/CC 的日常项目，推荐采用下面这套最简单的标准形态：

- `cx_ws/` 只是本地工作空间，用来放多个项目
- `cx_ws/cpp_interview/` 是项目根目录
- `.git` 位于 `cx_ws/cpp_interview/.git`
- Codex/CC 平时直接在 `cx_ws/cpp_interview/` 下工作
- 远端仓库直接对应这个项目根目录

在这个形态下，标准命令就是普通 Git：

```bash
cd /home/ub/cx_ws/cpp_interview
git status
git add .
git commit -m "<根据本次改动填写说明>"
git push
```

## 适用范围

适用于 `cpp_interview/` 项目内所有内容更新，包括：

- `notes/`
- `docs/`
- `tools/`
- 项目根目录导航文档

## 基本规则

每次完成一轮明确的整理、清洗、重命名、结构调整或文档更新后，都要至少提交一次 Git。

推荐原则：

- 一轮完整操作，对应一次提交。
- 提交信息必须描述本次真实改动，不能长期复用一个泛化说明。
- 如果远端已配置且认证可用，提交后立即推送。

## 标准命令

```bash
cd /home/ub/cx_ws/cpp_interview
git status
git add .
git commit -m "<根据本次改动填写说明>"
git push
```

说明：

- 推送后的远端根目录应直接看到 `README.md`、`notes/`、`docs/`、`tools/`。
- 如果远端默认分支是 `main`，就在本地跟随使用 `main`。

## 一次完整操作

```bash
cd /home/ub/cx_ws/cpp_interview
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

- `cx_ws/` 是工作空间，不是本项目的 Git 仓库根目录。
- `cpp_interview/` 才是项目根目录，也是 Git 命令的默认执行位置。
- 这个项目不再推荐维护额外的兼容发布流程。
