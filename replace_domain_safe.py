import os
import io

def replace_domain(directory):
    updated_count = 0
    
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        # Skip git directory
        if '.git' in root:
            continue
            
        for file in files:
            if not file.endswith(('.html', '.css', '.js')):
                continue
                
            filepath = os.path.join(root, file)
            
            try:
                # Read with explicit UTF-8 encoding
                with io.open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # The explicit goal is to replace `https://darlma3rifa.com` with `https://www.darlma3rifa.com/`
                # but ONLY if it's not already correct (or if it doesn't already have www).
                # Simple strategy: replace all `https://darlma3rifa.com` with a temporary string,
                # assuming we don't accidentally replace `https://www.darlma3rifa.com` inside it
                
                original_content = content
                
                # First, normalize everything to NOT have www temporarily to avoid double www.
                # Just replace EXACTLY 'https://darlma3rifa.com' -> 'https://www.darlma3rifa.com'
                # but take care of trailing slashes. 
                
                # A safer Regex or string replace:
                # Replace 'https://darlma3rifa.com' -> 'https://www.darlma3rifa.com'
                # Wait, if we replace "https://darlma3rifa.com", we might accidentally replace inside "https://www.darlma3rifa.com".
                # But actually "https://darlma3rifa.com" doesn't match "https://www.darlma3rifa.com" exactly because of the.
                content = content.replace("https://darlma3rifa.com", "https://www.darlma3rifa.com")
                
                # Fix double www if it accidentally happened
                content = content.replace("https://www.www.darlma3rifa.com", "https://www.darlma3rifa.com")
                
                if content != original_content:
                    with io.open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_count += 1
                    
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")

    print(f"Successfully updated {updated_count} files with utf-8 preservation.")

if __name__ == '__main__':
    replace_domain(r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\dar-with-profiles")
