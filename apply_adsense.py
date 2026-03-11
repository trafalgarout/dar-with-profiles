import os
import re

tools_dir = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\dar-with-profiles\ai-tools"

ad_script = """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6865939387108271"
        crossorigin="anonymous"></script>"""

for filename in os.listdir(tools_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(tools_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        head_match = re.search(r'<head>(.*?)</head>', content, re.IGNORECASE | re.DOTALL)
        if head_match:
            head_content = head_match.group(1)
            # Only add if it's missing (checking the publisher ID)
            if "ca-pub-6865939387108271" not in head_content:
                # Replace the first <head> tag with <head> + ad script
                content = re.sub(r'(<head>)', r'\1' + ad_script, content, count=1, flags=re.IGNORECASE)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Added AdSense to {filename}")
            else:
                print(f"ℹ️ AdSense already exists in {filename}")
        else:
            print(f"⚠️ No <head> tag found in {filename}")
