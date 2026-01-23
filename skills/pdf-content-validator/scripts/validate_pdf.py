import sys
import json
import re

try:
    import pdfplumber
except ImportError:
    print(json.dumps({
        "error": "Missing dependency 'pdfplumber'.", 
        "message": "Please install required packages: pip install -r requirements.txt"
    }))
    sys.exit(1)

def validate_pdf(pdf_path, rules_path, output_path):
    # Load rules
    try:
        with open(rules_path, 'r', encoding='utf-8') as f:
            rules = json.load(f)
    except Exception as e:
        print(json.dumps({"error": f"Failed to load rules: {str(e)}"}))
        return

    # Extract text
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
    except Exception as e:
        print(json.dumps({"error": f"Failed to read PDF: {str(e)}"}))
        return

    report = {
        "status": "PASS",
        "details": [],
        "text_summary": {
            "length": len(full_text),
            "preview": full_text[:200] + "..." if len(full_text) > 200 else full_text
        }
    }

    # Check required strings
    if "required_strings" in rules:
        for req in rules["required_strings"]:
            if req not in full_text:
                report["status"] = "FAIL"
                report["details"].append({
                    "check": "Required String",
                    "item": req,
                    "status": "FAIL",
                    "message": f"String '{req}' not found in document."
                })
            else:
                report["details"].append({
                    "check": "Required String",
                    "item": req,
                    "status": "PASS"
                })

    # Check regex patterns
    if "regex_patterns" in rules:
        for pattern_obj in rules["regex_patterns"]:
            pattern = pattern_obj.get("pattern")
            name = pattern_obj.get("name", "Unknown Pattern")
            if pattern:
                match = re.search(pattern, full_text)
                if not match:
                    report["status"] = "FAIL"
                    report["details"].append({
                        "check": "Regex Pattern",
                        "item": name,
                        "status": "FAIL",
                        "message": f"Pattern for '{name}' not found."
                    })
                else:
                    report["details"].append({
                        "check": "Regex Pattern",
                        "item": name,
                        "status": "PASS",
                        "match_preview": match.group(0)
                    })

    # Write report
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"Validation complete. Report written to {output_path}")
    except Exception as e:
        print(json.dumps({"error": f"Failed to write report: {str(e)}"}))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python validate_pdf.py <pdf_path> <rules_json_path> <output_json_path>")
    else:
        validate_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
