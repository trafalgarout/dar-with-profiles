
import os
import re

def cleanup_files():
    root_dir = "."
    adsense_script_pattern = re.compile(r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-6865939387108271"\s+crossorigin="anonymous"></script>', re.IGNORECASE)
    uae_pattern_css = "background: url('UAE_PATTERN.png');"
    
    count_adsense = 0
    count_uae = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 1. Cleanup UAE_PATTERN.png
                    if uae_pattern_css in content:
                        new_content = content.replace(uae_pattern_css, "/* background: url('UAE_PATTERN.png'); */")
                        content = new_content
                        count_uae += 1
                        print(f"Commented out UAE_PATTERN in: {file_path}")

                    # 2. Cleanup redundant AdSense scripts
                    # Split content by </head> to only target the body
                    parts = re.split(r'</head>', content, maxsplit=1, flags=re.IGNORECASE)
                    if len(parts) == 2:
                        head, body = parts
                        # Count matches in head
                        head_matches = adsense_script_pattern.findall(head)
                        # Remove all matches in body
                        if adsense_script_pattern.search(body):
                            new_body = adsense_script_pattern.sub("", body)
                            content = head + "</head>" + new_body
                            count_adsense += 1
                            print(f"Removed redundant AdSense scripts in body of: {file_path}")
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"Total files updated (AdSense): {count_adsense}")
    print(f"Total files updated (UAE Pattern): {count_uae}")

if __name__ == "__main__":
    cleanup_files()
