---
name: pdf-content-validator
description: Validates PDF content against business rules, checks for compliance, diffs versions, and generates reports. Use when you need to deep-read a PDF, verify its contents against a schema or specific requirements, or check for missing information.
---

# PDF Content Validator

## Overview

This skill provides a workflow for parsing, validating, and auditing PDF documents. It is designed to handle complex business scenarios such as contract review, invoice processing, and technical document compliance checking.

## Setup

Before using this skill, ensure you have the required dependencies installed:

```bash
pip install -r skills/pdf-content-validator/requirements.txt
```

## Workflow

The validation process follows these four steps:

1.  **Intent Recognition & Parsing**: Extract text, tables, and metadata from the PDF to understand its structure.
2.  **Rule Selection**: Choose the appropriate validation rules (e.g., from the `rules/` directory) based on the document type (Invoice, Contract, etc.).
3.  **Ambiguity Resolution**: Check for missing context (e.g., missing tax IDs for invoice validation) and ask the user for clarification if needed.
4.  **Validation & Reporting**: Compare the PDF content against the selected rules and generate a structured pass/fail report.

## Usage

### 1. Extract & Analyze (Read)

First, understand the content of the PDF. Use `validate_pdf.py` for automated checking or `pdfplumber` (via python script) for ad-hoc analysis.

```python
# Ad-hoc text extraction for understanding context
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(text)
```

### 2. Validate Against Rules (Validate)

Use the provided script to check the PDF against a JSON rule set.

**Command:**
```bash
python scripts/validate_pdf.py <pdf_path> <rules_path> <report_path>
```

**Example:**
```bash
python scripts/validate_pdf.py invoice_123.pdf rules/example_invoice_rules.json report.json
```

**Rule Format (`rules/*.json`):**
```json
{
  "name": "Invoice Rules",
  "required_strings": ["Invoice", "Total"],
  "regex_patterns": [
    {
      "name": "Date",
      "pattern": "\\d{4}-\\d{2}-\\d{2}"
    }
  ]
}
```

### 3. Generate Report (Write)

After validation, read the generated JSON report and summarize it for the user.

**Example Report Output:**
```json
{
  "status": "FAIL",
  "details": [
    {
      "check": "Required String",
      "item": "Total",
      "status": "PASS"
    },
    {
      "check": "Regex Pattern",
      "item": "Date",
      "status": "FAIL",
      "message": "Pattern for 'Date' not found."
    }
  ]
}
```

## Advanced Capabilities

### Complex Layouts & Tables
For multi-column layouts or cross-page tables, use `pdfplumber`'s explicit table extraction settings in a custom script or ad-hoc analysis.

```python
# Example for table extraction
with pdfplumber.open("table_doc.pdf") as pdf:
    tables = pdf.pages[0].extract_tables()
    for table in tables:
        print(table)
```

### Compliance & Diffing
To compare two PDFs (Diffing):
1. Extract text from both PDFs.
2. Use a diff library (like `difflib` in Python) to find differences.
3. Report changes in text or structure.