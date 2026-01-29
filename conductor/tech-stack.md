# 技术栈

## 核心标准
- **Agent Skills:** 使用 YAML frontmatter 和 Markdown 编写的标准化指令集，作为所有技能的基础。

## 脚本与自动化
- **脚本语言:** Python (主要用于复杂逻辑处理，如 PDF 解析、数据提取等)。
- **包管理:** `uv` (用于高效管理 Python 环境和依赖)。
- **安装脚本:** Windows Batch (.bat) (用于本地环境的技能安装)。

## 兼容性与集成
- **多模型兼容:** 技能设计必须同时兼容 Gemini Cli、Claude Code 及其他支持 Agent Skills 标准的 AI 代理环境。
- **配置管理:** 灵活适配不同环境的配置文件（如 `.claude-plugin` 等），确保跨平台可用性。
