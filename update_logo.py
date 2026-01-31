
import os
import glob

# Define the old and new logo HTML for Footer
# Note: The spacing and attributes must match exactly what is in the files to be robust.

old_footer_logo_patterns = [
    '<div class="logo" style="color:white;margin-bottom:15px;">كويزات<span class="highlight">عربية</span>\n                </div>',
    '<div class="logo" style="color:white;margin-bottom:15px;">كويزات<span class="highlight">عربية</span></div>',
    '<div class="logo" style="color:white;margin-bottom:15px;">كويزات <span class="highlight">عربية</span>\n                </div>'
]

new_footer_logo = '''<div class="logo" style="margin-bottom:15px;">
                    <img src="FAVICON.png" alt="كويزات عربية" style="height: 50px; width: auto;">
                </div>'''

def update_files():
    root_dir = "."
    files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                files.append(os.path.join(dirpath, filename))
    
    count = 0
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            updated = False
            
            # Footer Logo Replacement
            for pattern in old_footer_logo_patterns:
                # We normalize whitespace slightly to match potential variations if strict match failed
                # But python verify works best with exact strings.
                if pattern in content:
                    content = content.replace(pattern, new_footer_logo)
                    updated = True
            
            # Retry with looser match if needed (regex would be better but simple replace is safer for now)
            if not updated and 'class="logo" style="color:white;margin-bottom:15px;">كويزات' in content:
                 # Fallback for slight whitespace diffs
                 pass 

            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated footer in: {file_path}")
                count += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Total files updated with footer logo: {count}")

if __name__ == "__main__":
    update_files()
