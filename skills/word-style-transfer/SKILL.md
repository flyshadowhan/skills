---
name: word-style-transfer
description: Analyzes Word document styles and generates new documents with matching formatting and tone. Use this skill when you need to create a new .docx file that strictly mimics the visual style and writing voice of an existing template or sample document.
---

# Word Style Transfer

## Overview

This skill allows you to "clone" the style of an existing Word document. It performs two types of transfer:
1.  **Visual Style Transfer**: Applies fonts, spacing, margins, and styles (Headings, Normal, Lists) from a source DOCX to new content.
2.  **Writing Style Transfer**: Analyzes the voice, tone, and vocabulary of the source text to ensure the new content "sounds" like the original.

## Usage Workflow

Follow this 3-step process to transfer style:

### 1. Extraction (Analyze Tone & Style)

First, read the source document to understand its writing style.

```bash
python skills/word-style-transfer/scripts/read_docx.py "path/to/template.docx"
```

**Analyze the output for:**
- **Tone**: Is it formal, conversational, technical, or persuasive?
- **Vocabulary**: Does it use industry jargon, simple words, or academic language?
- **Structure**: How is information organized (short paragraphs, bullet points, numbered lists)?

### 2. Content Generation (Drafting)

Draft the new content based on the user's request, strictly adhering to the analyzed **Writing Style**.

**Format Requirement**: You MUST draft the content in **Markdown**.
- Use `#` for Title/Heading 1
- Use `##` for Heading 2
- Use `###` for Heading 3
- Use `-` or `*` for Bulleted Lists
- Use `1.` for Numbered Lists
- Standard paragraphs for Normal text

**Save the draft**:
Write this markdown content to a temporary file (e.g., `content_draft.md`).

```python
# Example of saving content using write_file (conceptual)
write_file(file_path="content_draft.md", content="# New Title\n\nNew paragraph in the style of the original...")
```

### 3. Synthesis (Build DOCX)

Combine the **Source Template** (for visual styles) and your **Drafted Content** (for text) into the final document.

Use the `generate_docx.py` script. This script clears the content of the template (preserving styles) and injects your markdown content using the correct Word styles.

```bash
python skills/word-style-transfer/scripts/generate_docx.py --template "path/to/template.docx" --content "content_draft.md" --output "path/to/final_output.docx"
```

### 4. Verification

Confirm the output file was generated successfully.

## Tips

- **Templates**: The `template` file serves as the "Style Source". The script will modify a *copy* of it (in memory) and save to `output`, so the original template is safe.
- **Complex Formatting**: The script handles standard Markdown elements. Complex tables or custom XML features might not transfer perfectly via Markdown; focus on text flow and hierarchical structure.
- **Tone consistency**: The most important part of "style transfer" is your generation of the text. If the template is a legal contract, do not write the new content like a blog post.

---