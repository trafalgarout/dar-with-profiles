import os
from collections import defaultdict

folder_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\THUMBNAILS\BANAT"
report_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\banat_analysis_report.md"

files = os.listdir(folder_path)
extensions = defaultdict(int)
base_names = defaultdict(list)

for f in files:
    name, ext = os.path.splitext(f)
    extensions[ext.lower()] += 1
    base_names[name].append(ext)

with open(report_path, "w", encoding="utf-8") as report:
    report.write("# BANAT Folder Analysis\n\n")
    report.write(f"**Total files:** {len(files)}\n\n")
    
    report.write("## File Types\n")
    for ext, count in extensions.items():
        report.write(f"- **{ext}**: {count}\n")
    
    duplicates = {name: exts for name, exts in base_names.items() if len(exts) > 1}
    
    report.write("\n## Conflicts (Same Name, Different Extensions)\n")
    if duplicates:
        report.write(f"Found {len(duplicates)} conflicts.\n\n")
        report.write("| Base Name | Extensions Found |\n")
        report.write("|---|---|\n")
        for name, exts in sorted(duplicates.items()):
            report.write(f"| {name} | {', '.join(sorted(exts))} |\n")
    else:
        report.write("No naming conflicts found.\n")

print("Report generated.")
