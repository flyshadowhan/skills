import sys
import re

def aggregate_stats(content):
    stats = {
        "🔴 Critical": 0,
        "🟡 Medium": 0,
        "🔵 Minor": 0
    }
    
    # Process line by line to avoid issues with large files
    lines = content.split('\n')
    for line in lines:
        # Match lines that start with a pipe and have a numeric ID
        # Format: | ID | Path | Anchor | Level | Desc | Suggest |
        if not re.match(r'^\s*\|\s*\d+', line):
            continue
            
        # Split by pipes, but be careful with pipes inside backticks
        # A simple way is to find all content between pipes
        # This regex matches content between pipes, accounting for escaped pipes
        parts = re.findall(r'\|\s*((?:\\\||[^|])*?)\s*(?=\||$)', line)
        
        if len(parts) >= 4:
            # Column 0 is ID, 1 is Path, 2 is Anchor, 3 is Level
            level = parts[3].strip()
            if "Critical" in level or "🔴" in level:
                stats["🔴 Critical"] += 1
            elif "Medium" in level or "🟡" in level:
                stats["🟡 Medium"] += 1
            elif "Minor" in level or "🔵" in level:
                stats["🔵 Minor"] += 1
            
    total = sum(stats.values())
    
    summary = f"| 级别 | 数量 |\n| :--- | :--- |\n"
    summary += f"| 🔴 Critical | {stats['🔴 Critical']} |\n"
    summary += f"| 🟡 Medium | {stats['🟡 Medium']} |\n"
    summary += f"| 🔵 Minor | {stats['🔵 Minor']} |\n"
    summary += f"| **总计** | **{total}** |"
    
    return summary

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                print(aggregate_stats(f.read()))
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print(aggregate_stats(sys.stdin.read()))
