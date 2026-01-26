import os
from collections import defaultdict

folder_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\THUMBNAILS\BANAT"
report_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\banat_deep_analysis.md"

files = os.listdir(folder_path)
grouped = defaultdict(list)

for f in files:
    name, ext = os.path.splitext(f)
    full_path = os.path.join(folder_path, f)
    size = os.path.getsize(full_path)
    grouped[name].append({'ext': ext.lower(), 'size': size, 'filename': f})

with open(report_path, "w", encoding="utf-8") as report:
    report.write("# BANAT Deep Analysis\n\n")
    
    conflicts = {k: v for k, v in grouped.items() if len(v) > 1}
    
    if conflicts:
        report.write(f"Found {len(conflicts)} naming conflicts.\n\n")
        report.write("| Base Name | Variants (Extension: Size in Bytes) |\n")
        report.write("|---|---|\n")
        for name, variants in sorted(conflicts.items()):
            # Sort variants by size descending to highlight the highest quality potentially
            variants.sort(key=lambda x: x['size'], reverse=True)
            desc = ", ".join([f"**{v['ext']}**: {v['size']}" for v in variants])
            report.write(f"| {name} | {desc} |\n")
    else:
        report.write("No naming conflicts found.\n")

print("Deep analysis report generated.")
