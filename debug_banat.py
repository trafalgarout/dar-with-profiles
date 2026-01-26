import os

folder_path = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main\THUMBNAILS\BANAT"

try:
    files = os.listdir(folder_path)
    print(f"Files found: {len(files)}")
    if len(files) > 0:
        print(f"Sample: {files[:3]}")
        first = files[0]
        name, ext = os.path.splitext(first)
        print(f"Split test: '{first}' -> name='{name}', ext='{ext}'")
except Exception as e:
    print(f"Error: {e}")
