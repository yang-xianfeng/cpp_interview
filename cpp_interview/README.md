# cpp_interview

这个目录把原来的 `CppNotes/`、`CppNotes_refined/` 和 `tools/` 合并成一个统一项目。

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
- `notes/source/`
  - 原始版笔记。
- `notes/cleaned/`
  - 清洗整理后的主用笔记。
- `tools/`
  - 笔记清洗和辅助脚本。
- `docs/`
  - 清洗 SOP、LLM 工作单等项目文档。
- `archive/`
  - 原始资料压缩归档。

## 放置结论

`CppNotes/` 和 `CppNotes_refined/` 中的 `ROLE.md` 与 `AGENT.md` 内容一致，没有版本差异，因此不应该继续各放一份。更合理的做法是：

1. 把 `ROLE.md` 和 `AGENT.md` 提升到 `cpp_interview/` 根目录。
2. 把 `notes/source/` 和 `notes/cleaned/` 只当作内容目录，不再放项目级角色说明。
3. 只有在某个子目录需要独立工作规则时，才在该子目录额外新增一份局部 `AGENT.md` 或 `ROLE.md`。

## 为什么这样放

- `ROLE.md` 约束的是整个项目的导师身份，不依赖原始笔记还是 refined 笔记。
- `AGENT.md` 约束的是整个项目的推进方式，也不应绑定到某一套笔记副本。
- `notes/source/` 和 `notes/cleaned/` 的差别是内容状态，不是角色状态。
- `PROJECT_GUIDE.md` 负责统一导航，因此也应该放在项目根目录。
- `docs/` 中的流程文档属于项目文档，也应随项目一起管理，而不是留在工作区根目录。

## 以后怎么扩展

如果后续你希望：

- `source` 侧重“保真存档”；
- `cleaned` 侧重“结构清洗与主用复习”；

那么可以保留根目录公共 `ROLE.md`，再只给特定子目录补一份局部 `AGENT.md`，作为覆盖规则，而不是复制两份完全相同的项目级文件。

## 清理策略

项目完成合并后，工作区根目录的旧 `CppNotes/`、`CppNotes_refined/`、`tools/` 可以清理。

建议保留方式：

1. 在 `cpp_interview/archive/` 中保留一份最初 `CppNotes/` 的 zip 归档。
2. 项目日常使用统一切换到 `cpp_interview/` 目录。
3. SOP 和工作单统一放在 `cpp_interview/docs/`。
