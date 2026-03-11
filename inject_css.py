import os
import re

target_dir = './ai-tools'

# Read global CSS
with open('style.css', 'r', encoding='utf-8') as f:
    global_css = f.read()

# Read local CSS
local_css_path = os.path.join(target_dir, 'style.css')
with open(local_css_path, 'r', encoding='utf-8') as f:
    local_css = f.read()

# Combined style block
combined_css = f'<style>\n{global_css}\n{local_css}\n</style>'

files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

for filename in files:
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find and replace existing style block containing our marker
    # We look for a style block that contains '/* ai-tools/style.css */'
    style_block_pattern = re.compile(r'<style>.*?\/\* ai-tools/style\.css \*\/.*?</style>', re.DOTALL)
    
    if style_block_pattern.search(content):
        new_content = style_block_pattern.sub(combined_css, content)
    else:
        # Fallback to link tags if not yet replaced
        new_content = re.sub(r'<link[^>]*href="\.\./style\.css"[^>]*>\s*<link[^>]*href="style\.css"[^>]*>', combined_css, content)
        
        # If still same, try replacing by </head>
        if new_content == content:
             # Even if there's a style tag, if it's NOT our combined one, we might want to keep it or replace it.
             # For safety, if our marker isn't there, and link tags aren't there, just inject before </head> if not already present
             if '/* ai-tools/style.css */' not in content:
                 new_content = content.replace('</head>', f'{combined_css}\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Updated CSS injection in {len(files)} files.")
