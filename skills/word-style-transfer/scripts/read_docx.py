import argparse
import sys
from docx import Document

def extract_text(docx_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def main():
    parser = argparse.ArgumentParser(description='Extract text from a DOCX file.')
    parser.add_argument('file', help='Path to the DOCX file.')
    args = parser.parse_args()

    try:
        text = extract_text(args.file)
        # Print to stdout so the agent can read it
        print(text)
    except Exception as e:
        print(f"Error reading file: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

