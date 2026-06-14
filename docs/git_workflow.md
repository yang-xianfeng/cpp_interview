# Git Workflow

这个文档说明当前工作空间下 `cpp_interview/` 项目的标准 Git 提交流程。

## 本地与远端约定

- 本地工作空间根目录：`/home/ub/cx_ws`
- 当前项目目录：`/home/ub/cx_ws/cpp_interview`
- GitHub 远端仓库根目录：发布后的 `cpp_interview/` 子目录内容
- 远端目录层级：只保留一层项目内容，不出现 `cpp_interview/cpp_interview`
- 当前远端：`origin -> git@github.com:yang-xianfeng/cpp_interview.git`

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

## 本地提交命令

```bash
cd /home/ub/cx_ws
git status
git add cpp_interview
git commit -m "<根据本次改动填写说明>"
```

## 发布到 GitHub 远端根目录

本地 `master` 保留工作空间结构，远端 `master` 只发布 `cpp_interview/` 的内容。因此不要直接执行 `git push origin master`。

标准发布命令：

```bash
cd /home/ub/cx_ws
git subtree split --prefix=cpp_interview -b publish-cpp-interview
git push --force origin publish-cpp-interview:master
git branch -D publish-cpp-interview
```

说明：

- `git subtree split --prefix=cpp_interview` 会生成只包含项目子目录内容的发布分支。
- `git push --force origin publish-cpp-interview:master` 会把这个发布分支覆盖推送到 GitHub 远端根目录。
- 推送后的远端根目录应直接看到 `README.md`、`notes/`、`docs/`、`tools/`，而不是再出现一层 `cpp_interview/`。
- 如果未来远端默认分支改成 `main`，把最后一条命令中的 `master` 替换为 `main`。

## 一次完整操作

```bash
cd /home/ub/cx_ws
git status
git add cpp_interview
git commit -m "<根据本次改动填写说明>"
git subtree split --prefix=cpp_interview -b publish-cpp-interview
git push --force origin publish-cpp-interview:master
git branch -D publish-cpp-interview
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

- 如果只是本地留档，至少要完成 `git add cpp_interview` 和 `git commit`。
- 如果要同步到 GitHub，使用上面的 subtree 发布流程。
- 当前工作空间已配置 `origin` 并可通过 SSH 推送。
