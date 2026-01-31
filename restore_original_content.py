
import os
import shutil

source_dir = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\ARAB QUIZZES"
target_dir = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\darlma3rifa-quizzes-2-main"

def restore_files():
    count = 0
    # List files in source
    source_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]
    
    for filename in source_files:
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)
        
        # Only restore if it exists in target (to avoid copying unrelated files if any)
        if os.path.exists(target_path):
            try:
                shutil.copy2(source_path, target_path)
                print(f"Restored: {filename}")
                count += 1
            except Exception as e:
                print(f"Error restoring {filename}: {e}")
        else:
            # If it's a quiz file but doesn't exist in target for some reason, maybe we should still restore it?
            # User said "ALL QUIZZES IN THE WEBSITE", so if it's in ARAB QUIZZES it's probably intended.
            # But safer to match what was already there or just restore all quiz files.
            if filename.startswith("quiz_"):
                 shutil.copy2(source_path, target_path)
                 print(f"Restored (New): {filename}")
                 count += 1

    print(f"Total files restored: {count}")

if __name__ == "__main__":
    restore_files()
