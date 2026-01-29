import argparse
import re
import json
import sys
from collections import Counter

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                content = f.read()
        except Exception as e:
            return {"error": f"Could not read file: {e}"}
    except Exception as e:
        return {"error": f"Could not read file: {e}"}

    analysis = {}

    # 1. Structure Analysis (Markdown focus)
    analysis['structure'] = {
        'total_lines': len(content.splitlines()),
        'headers': len(re.findall(r'^#+\s', content, re.MULTILINE)),
        'header_depth_distribution': dict(Counter(len(m.group(0).strip()) for m in re.finditer(r'^(#+)\s', content, re.MULTILINE))),
        'list_items': len(re.findall(r'^\s*[-*+]\s', content, re.MULTILINE)),
        'numbered_list_items': len(re.findall(r'^\s*\d+\.\s', content, re.MULTILINE)),
        'code_blocks': len(re.findall(r'```', content)),
        'links': len(re.findall(r'\[.*?\]\(.*?\)', content)),
        'images': len(re.findall(r'!\[.*?\]\(.*?\)', content)),
    }

    # 2. Text Statistics
    words = re.findall(r'\b\w+\b', content)
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if s.strip()]

    if words:
        analysis['stats'] = {
            'word_count': len(words),
            'avg_word_length': sum(len(w) for w in words) / len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length_words': len(words) / len(sentences) if sentences else 0,
        }
    else:
        analysis['stats'] = {'word_count': 0}

    # 3. Snippets (for Tone/Vocabulary context)
    # Return start and random middle snippet to give LLM a taste of the actual text
    analysis['sample_start'] = content[:500]
    
    return analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a text/markdown file for style extraction.")
    parser.add_argument("file_path", help="Path to the file to analyze")
    args = parser.parse_args()

    result = analyze_file(args.file_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
