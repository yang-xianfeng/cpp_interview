# cpp_interview

本地工作空间根目录是 `/home/ub/cx_ws`，当前项目目录是 `/home/ub/cx_ws/cpp_interview`。

`cpp_interview/` 本身就是 Git 仓库根目录，GitHub 远端仓库也直接对应这一层项目内容。

这意味着远端仓库中只保留一层项目内容：

- 本地 `cx_ws/cpp_interview/README.md` -> 远端 `README.md`
- 本地 `cx_ws/cpp_interview/notes/` -> 远端 `notes/`
- 本地 `cx_ws/cpp_interview/docs/` -> 远端 `docs/`

远端不会出现 `cx_ws/`，也不会出现二层 `cpp_interview/cpp_interview/`。

## 标准形态

对刚开始使用 Codex/CC 的场景，更推荐的标准形态是：

- `cx_ws/` 只是你的本地工作空间，不承担 Git 仓库根的角色
- `cx_ws/cpp_interview/` 才是项目根目录
- `.git` 也位于 `cx_ws/cpp_interview/`
- 平时在项目根直接执行 `git add`、`git commit`、`git push`

这样本地项目名和远端仓库名一致时，确实可以直接推送，不需要 `subtree`。

历史上如果把 `.git` 放在 `cx_ws/` 这一层，那么 `cpp_interview/` 会被当成子目录，直接 `git push` 时远端就会多出一层 `cpp_interview/`。当前项目已经完成标准化，不再采用这种结构。

## Codex/CC 使用建议

- `cx_ws/` 只作为本地工作空间，用来容纳多个项目。
- `cpp_interview/` 才是当前项目的工作根目录。
- 日常打开 Codex/CC、执行 Git、阅读项目文档、修改文件时，都应以 `cx_ws/cpp_interview/` 作为当前目录。
- 只有在你明确要管理多个项目时，才在 `cx_ws/` 这一层工作；否则容易再次混淆工作空间和项目根目录。

这个项目把原来的 `CppNotes/`、`CppNotes_refined/` 和 `tools/` 合并成一个统一项目。

## 目录结构

- `ROLE.md`
  - 项目级角色定义。
  - 负责回答“你是谁、站在什么视角辅导”。
- `AGENT.md`
  - 项目级执行规范。
  - 负责回答“你如何推进任务、每次输出什么结构、如何纠偏”。
- `PROJECT_GUIDE.md`
  - 项目统一入口。
  - 负责回答“先看什么、从哪里开始使用”。
- `notes/README.md`
  - 按主题分类的总目录。
  - 用来快速定位语言、Linux、网络、数据库、项目、面试相关笔记。
- `notes/source/`
  - 原始版笔记。
- `notes/cleaned/`
  - 清洗整理后的主用笔记。
- `tools/`
  - 笔记清洗和辅助脚本。
- `docs/`
  - 清洗 SOP、LLM 工作单等项目文档。
  - 也包含 Git 提交流程说明。
- `archive/`
  - 原始资料压缩归档。

## 放置结论

`CppNotes/` 和 `CppNotes_refined/` 中的 `ROLE.md` 与 `AGENT.md` 内容一致，没有版本差异，因此不应该继续各放一份。更合理的做法是：

1. 把 `ROLE.md` 和 `AGENT.md` 放到项目根目录 `cx_ws/cpp_interview/`。
2. 把 `notes/source/` 和 `notes/cleaned/` 只当作内容目录，不再放项目级角色说明。
3. 只有在某个子目录需要独立工作规则时，才在该子目录额外新增一份局部 `AGENT.md` 或 `ROLE.md`。

## 为什么这样放

- `ROLE.md` 约束的是整个项目的导师身份，不依赖原始笔记还是 refined 笔记。
- `AGENT.md` 约束的是整个项目的推进方式，也不应绑定到某一套笔记副本。
- `notes/source/` 和 `notes/cleaned/` 的差别是内容状态，不是角色状态。
- `PROJECT_GUIDE.md` 负责统一导航，因此也应该放在项目根目录。
- `docs/` 中的流程文档属于项目文档，也应与项目内容同级管理。

## 以后怎么扩展

如果后续你希望：

- `source` 侧重“保真存档”；
- `cleaned` 侧重“结构清洗与主用复习”；

那么可以保留项目根目录公共 `ROLE.md`，再只给特定子目录补一份局部 `AGENT.md`，作为覆盖规则，而不是复制两份完全相同的项目级文件。

## 清理策略

项目完成合并后，工作空间中的旧 `CppNotes/`、`CppNotes_refined/`、`tools/` 可以清理。

建议保留方式：

1. 在 `archive/` 中保留一份最初 `CppNotes/` 的 zip 归档。
2. 项目日常使用统一切换到 `cx_ws/cpp_interview/`。
3. 本地 Git 直接在项目根目录 `cx_ws/cpp_interview/` 管理，日常不再维护额外兼容发布流程。
4. SOP、工作单和 Git 流程说明统一放在 `docs/`。
