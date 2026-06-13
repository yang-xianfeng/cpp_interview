# cpp_interview Guide

这个文件作为 `cpp_interview/` 的统一入口，优先回答“先看什么、从哪里开始用”。

## 先看哪里

如果你是第一次进入这个项目，建议按下面顺序：

1. [README.md](/home/ub/cx_ws/cpp_interview/README.md:1)
   - 先理解项目结构和文件职责。
2. [ROLE.md](/home/ub/cx_ws/cpp_interview/ROLE.md:1)
   - 明确导师角色、工作视角和目标边界。
3. [AGENT.md](/home/ub/cx_ws/cpp_interview/AGENT.md:1)
   - 明确执行方式、输出格式和推进规则。
4. `notes/cleaned/`
   - 默认优先使用这套清洗后的笔记做复习和面试准备。
5. `notes/source/`
   - 遇到内容丢失、清洗过度或需要回查原文时，再回到原始笔记。

## 怎么使用这套内容

按用途划分，入口如下：

- 复习主线
  - 从 `notes/cleaned/13-CPP基础.md`、`14-类与对象.md`、`19-STL.md`、`05-Linux系统编程.md`、`08-线程.md`、`10-网络编程.md` 开始。
- 项目包装
  - 重点看 `notes/cleaned/23-搜索引擎项目.md` 和 `26-Workflow重写NetDisk.md`。
- 简历与面试
  - 重点看 `notes/cleaned/30-面试经验.md`、`31-面试简历.md`、`32-15天复习计划.md`。
- 清洗工具
  - 脚本在 `tools/clean_notes.py`。
- 项目文档
  - 统一从 `docs/README.md` 进入。

## 目录职责

- `ROLE.md`
  - 项目级角色定义。
- `AGENT.md`
  - 项目级执行规则。
- `notes/source/`
  - 原始笔记副本。
- `notes/cleaned/`
  - 当前主用笔记。
- `tools/`
  - 清洗和辅助脚本。
- `docs/`
  - 项目流程文档。
- `archive/`
  - 原始资料压缩归档。

## 当前推荐规则

- 日常复习默认只看 `notes/cleaned/`。
- 只有在需要校对原文时，才回看 `notes/source/` 或 `archive/source_notes_backup.zip`。
- 不再使用工作区根目录的旧 `CppNotes/`、`CppNotes_refined/`、`tools/`。
