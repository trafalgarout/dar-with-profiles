import os
import re

filepath = r'f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\dar-with-profiles\ai-tools\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS injection
css_to_add = '''
        .tool-thumbnail {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
        }
        .tool-card-custom:hover .tool-thumbnail {
            transform: scale(1.03);
        }
'''
if '.tool-thumbnail' not in content:
    content = content.replace('.tool-icon {', css_to_add.strip() + '\n        .tool-icon {')

# Replacements mapping
mapping = {
    'username-generator.html': 'username-generator.png',
    'business-name-generator.html': 'business-name-generator.jpeg',
    'instagram-bio-generator.html': 'instagram-bio-generator.jpeg',
    'blog-title-generator.html': 'blog-title-generator.jpeg',
    'youtube-title-generator.html': 'youtube-title-generator.jpeg',
    'hashtag-generator.html': 'hashtag-generator.jpeg',
    'startup-ideas-generator.html': 'startup-ideas-generator.jpeg',
    'study-plan-generator.html': 'study-plan-generator.jpeg',
    'resume-summary-generator.html': 'resume-summary-generator.jpeg',
    'password-generator.html': 'password-generator.jpeg'
}

for html_file, img_file in mapping.items():
    # Find the tool card and replace the emoji div
    pattern = r'(<a href="'+re.escape(html_file)+r'" class="tool-card-custom">\s*)<div class="tool-icon">[^<]+</div>'
    replacement = r'\1<img src="../THUMBNAILS/TOOLS/'+img_file+r'" alt="Tool Thumbnail" class="tool-thumbnail">'
    content = re.sub(pattern, replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Thumbnails added successfully to ai-tools/index.html")
