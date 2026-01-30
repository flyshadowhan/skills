# Specification: Text Style Transfer Skill

## Goal
创建一个 AI 技能，能够分析用户提供的 Markdown 或纯文本样本，提取其写作风格、结构模式和语法规范，并利用这些特征生成新的、风格高度一致的 .md 或 .txt 内容。

## Core Features
1.  **风格分析 (Style Analysis):**
    -   能够读取 .md 和 .txt 格式的样本文件。
    -   分析文本的语气（Tone）、词汇选择（Vocabulary）、句式结构（Sentence Structure）。
    -   识别文档的结构模式（如标题层级、列表使用、段落长度）。
2.  **内容生成 (Content Generation):**
    -   接受用户的主题或大纲输入。
    -   应用分析得出的风格特征生成新内容。
    -   确保生成的文档符合 Markdown 语法规范（如果适用）。
3.  **一致性验证 (Consistency Check):**
    -   (可选) 提供机制对比生成内容与源文档的相似度。

## User Interaction
-   用户通过 `SKILL.md` 指令调用此功能。
-   用户需提供：
    1.  样本文件路径（或内容）。
    2.  新内容的主题、大纲或原始素材。

## Success Criteria
-   生成的文档在视觉结构和阅读体验上与样本高度相似。
-   Markdown 语法正确无误。
-   技能成功通过 Claude/Gemini 的调用测试。