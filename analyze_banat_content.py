import os
import hashlib
from collections import defaultdict

folder_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\THUMBNAILS\BANAT"
report_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\banat_content_analysis.md"

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

files = os.listdir(folder_path)
hashes = defaultdict(list)
extensions = defaultdict(int)

for f in files:
    full_path = os.path.join(folder_path, f)
    if os.path.isfile(full_path):
        _, ext = os.path.splitext(f)
        extensions[ext.lower()] += 1
        file_hash = get_file_hash(full_path)
        hashes[file_hash].append(f)

duplicates = {k: v for k, v in hashes.items() if len(v) > 1}

with open(report_path, "w", encoding="utf-8") as report:
    report.write("# BANAT Content Analysis\n\n")
    report.write(f"**Total files:** {len(files)}\n\n")
    report.write("## File Extensions\n")
    for ext, count in extensions.items():
        report.write(f"- **{ext}**: {count}\n")
    
    report.write("\n## Content Duplicates (Identical Files)\n")
    if duplicates:
        report.write(f"Found {len(duplicates)} sets of duplicates.\n\n")
        report.write("| Hash | Files |\n")
        report.write("|---|---|\n")
        for h, file_list in duplicates.items():
            report.write(f"| {h[:8]}... | {', '.join(file_list)} |\n")
    else:
        report.write("No content duplicates found.\n")

print("Content analysis complete.")
