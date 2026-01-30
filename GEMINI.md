# Anthropic Agent Skills 仓库

本项目是 Anthropic "Agent Skills" 标准的参考实现与技能集合库。其核心目标是提供一系列高质量、开箱即用的 AI 代理技能，使用户能够通过标准化的指令和资源扩展 AI 代理（如 Claude、Gemini 等）的功能。

核心特性：
- **即插即用：** 提供包括 PDF 处理、文档样式迁移、企业办公自动化以及软件开发辅助在内的现成工具。
- **标准化示例：** 所有技能开发均遵循 Agent Skills 规范，作为构建自定义技能的参考标杆。

## 项目结构

*   **`skills/`**: 包含所有可用技能的主目录。每个子目录代表一个独立的技能。
*   **`conductor/`**: 项目上下文和管理文档，包含产品定义、技术栈和工作流指南。
*   **`spec/`**: 包含 Agent Skills 标准的规范文档。
*   **`template/`**: 用于创建新技能的启动模板。
*   **`install_skills.bat`**: 一个 Windows 批处理脚本，用于将技能安装到本地代理的环境中。
*   **`.claude-plugin/`**: Claude Code 市场的元数据。

## 技能结构 (Skill Anatomy)

一个技能由一个包含 `SKILL.md` 文件的目录定义。通常结构如下：

```
skills/<skill-name>/
├── SKILL.md          # 核心定义（YAML frontmatter + 指令）
├── assets/           # (可选) 技能使用的静态文件
├── scripts/          # (可选) 用于自动化的 Python 或 JS 脚本
└── rules/            # (可选) 用于重逻辑技能的规则文件
```

### `SKILL.md` 格式

`SKILL.md` 文件是技能的核心。它必须以 YAML frontmatter 开头，后跟 Markdown 指令：

```markdown
---
name: my-skill-name
description: 清晰描述该技能的功能。
---

# 技能名称

[给 AI 代理的详细指令...]

## Examples (示例)
...

## Guidelines (指南)
...
```

## 使用与安装

### 安装技能

要在本地环境中使用技能，必须将其安装到 `%USERPROFILE%\.gemini\skills`。请使用提供的批处理脚本：

```batch
install_skills.bat "skills\<skill-name>"
```

**示例：**
```batch
install_skills.bat "skills\pdf-data-extractor"
```

此命令会将技能目录复制到当前代理的技能文件夹中。

### 创建新技能

1.  将 `template/` 目录复制为 `skills/<new-skill-name>`。
2.  编辑 `skills/<new-skill-name>/SKILL.md`。
    *   更新 YAML frontmatter 中的 `name`（名称）和 `description`（描述）。
    *   在 Markdown 正文中编写具体的指令、示例和指南。
3.  向技能文件夹添加任何必要的资源或脚本。
4.  使用 `install_skills.bat` 安装技能进行测试。

## 开发标准与规范

*   **语言：** 本项目中的所有对话和文档均应使用 **中文** 进行。
*   **Python 环境：** 使用 **`uv`** 进行 Python 环境和包管理。
*   **独立性：** 每个技能应完全包含在其文件夹内。
*   **描述性命名：** 技能目录名称使用 kebab-case（例如 `pdf-data-extractor`）。
*   **清晰的指令：** `SKILL.md` 中的 Markdown 内容是给 AI 的提示词。编写清晰、明确的指令、“人设”（例如，“你是一名专家...”）和操作工作流。
*   **元数据：** 确保 YAML frontmatter 中的 `name` 与目录名称匹配，以保持一致性。