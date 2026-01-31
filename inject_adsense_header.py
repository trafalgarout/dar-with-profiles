
import os
import re

adsense_script = '''    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6865939387108271"
        crossorigin="anonymous"></script>'''

def inject_adsense():
    root_dir = "."
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check if script already exists
                    if 'ca-pub-6865939387108271' in content:
                        # Even if it exists, let's make sure it's at the top of head if it's a restored file
                        # Actually, better to just check if it's in the first 10 lines of <head>
                        head_match = re.search(r'<head>', content, re.IGNORECASE)
                        if head_match:
                            head_start = head_match.end()
                            first_part = content[head_start:head_start+500]
                            if 'ca-pub-6865939387108271' not in first_part:
                                # Not at the top, let's insert it
                                new_content = content[:head_start] + "\n" + adsense_script + content[head_start:]
                                with open(file_path, 'w', encoding='utf-8') as f:
                                    f.write(new_content)
                                print(f"Injected AdSense at top of head in: {file_path}")
                                count += 1
                        continue

                    # If not found at all
                    new_content = content.replace('<head>', f'<head>\n{adsense_script}', 1)
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Injected AdSense in: {file_path}")
                        count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"Total files updated with AdSense: {count}")

if __name__ == "__main__":
    inject_adsense()
