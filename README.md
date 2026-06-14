# cpp_interview

`cpp_interview/` 是当前项目根目录，也是 Git 仓库根目录。日常使用 Codex/CC、执行 Git、阅读文档、修改文件，都应以这个目录作为当前工作目录。

## 使用规则

- 工作空间：`/home/ub/cx_ws`
- 项目根目录：`/home/ub/cx_ws/cpp_interview`
- Git 根目录：`/home/ub/cx_ws/cpp_interview/.git`
- 远端仓库：`git@github.com:yang-xianfeng/cpp_interview.git`

标准 Git 流程：

```bash
cd /home/ub/cx_ws/cpp_interview
git status
git add .
git commit -m "<根据本次改动填写说明>"
git push
```

## 目录结构

- `PROJECT_GUIDE.md`：项目入口与导航。
- `ROLE.md`：项目角色定义。
- `AGENT.md`：项目执行规则。
- `notes/README.md`：笔记总目录。
- `notes/source/`：原始笔记。
- `notes/cleaned/`：主用笔记。
- `tools/`：清洗与辅助脚本。
- `docs/`：流程文档。
- `archive/`：归档资料。

## 文档入口

- 总览：`PROJECT_GUIDE.md`
- Git 流程：`docs/git_workflow.md`
- 清洗 SOP：`docs/notes_cleaning_sop.md`
- LLM 润色：`docs/llm_polish_workflow.md`
