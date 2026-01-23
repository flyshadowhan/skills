import pdfplumber
import json
import sys
import argparse
from typing import Dict, List, Any

def extract_layout_data(pdf_path: str) -> Dict[str, Any]:
    """
    Extracts structured data from a PDF including text with layout info and tables.
    This helps in preserving the context of complex forms.
    """
    structured_data = {
        "pages": []
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_data = {
                    "page_number": page_num + 1,
                    "width": page.width,
                    "height": page.height,
                    "text_blocks": [],
                    "tables": []
                }

                # Extract text words with bounding boxes for precise location
                # We group them into blocks generally, but getting raw words helps with specific alignment
                words = page.extract_words(keep_blank_chars=True)
                page_data["text_blocks"] = words

                # Extract tables
                # Using multiple settings to try and catch different table styles
                tables = page.extract_tables({
                    "vertical_strategy": "lines", 
                    "horizontal_strategy": "lines",
                    "intersection_y_tolerance": 10
                })
                
                # If lines method fails, try text-based correlation for whitespace-separated tables
                if not tables:
                     tables = page.extract_tables({
                        "vertical_strategy": "text", 
                        "horizontal_strategy": "text"
                    })

                page_data["tables"] = tables
                structured_data["pages"].append(page_data)

    except Exception as e:
        return {"error": str(e)}

    return structured_data

def main():
    parser = argparse.ArgumentParser(description="Extract structured layout data from PDF.")
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    parser.add_argument("--output", help="Path to save the JSON output.", default=None)
    
    args = parser.parse_args()

    data = extract_layout_data(args.pdf_path)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {args.output}")
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
