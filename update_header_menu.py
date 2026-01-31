
import os
import re

# New Header Menu Structure
# - Removed money bag emoji from "أموال الخليج" label based on user edit.
# - Added links to the new gulf country pages.
# - Preserved Quizzes dropdown.

new_nav_menu = '''<nav class="nav-menu">
                <a href="index.html" class="nav-link">الرئيسية</a>

                <div class="nav-item dropdown">
                    <span class="nav-link" style="cursor: pointer; display: flex; align-items: center; gap: 5px;">
                        كويزات <span style="font-size: 0.8em;">▾</span>
                    </span>
                    <div class="dropdown-content">
                        <a href="index.html#men">للشباب</a>
                        <a href="index.html#women">للبنات</a>
                        <a href="#entertainment">ترفيه</a>
                    </div>
                </div>

                <div class="nav-item dropdown">
                    <span class="nav-link" style="cursor: pointer; display: flex; align-items: center; gap: 5px;">
                        أموال الخليج <span style="font-size: 0.8em;">▾</span>
                    </span>
                    <div class="dropdown-content" style="min-width: 280px; padding-top:0;">
                        <div style="padding: 12px 15px; border-bottom: 1px solid #f1f5f9; font-size: 0.85rem; color: #64748b; background: #f8fafc; border-radius: 12px 12px 0 0; line-height: 1.5;">
                            كل ما تحتاج معرفته عن المال والتمويل في الخليج العربي
                        </div>
                        <a href="gulf_saudi.html">🇸🇦 السعودية</a>
                        <a href="gulf_uae.html">🇦🇪 الإمارات</a>
                        <a href="gulf_qatar.html">🇶🇦 قطر</a>
                        <a href="gulf_kuwait.html">🇰🇼 الكويت</a>
                        <a href="gulf_bahrain.html">🇧🇭 البحرين</a>
                        <a href="gulf_oman.html">🇴🇲 عمان</a>
                    </div>
                </div>

                <a href="wallpapers.html" class="nav-link">خلفيات متحركة</a>
                <a href="#banat" class="nav-link" style="color:#E91E63;font-weight:900;">🔥 تعارف بنات</a>
                <a href="name_compatibility.html" class="nav-link">💑 اختبار توافق الأسماء</a>
            </nav>'''

def update_files():
    root_dir = "."
    files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                files.append(os.path.join(dirpath, filename))
    
    count = 0
    # Regex to find <nav class="nav-menu"> ... </nav>
    # We use non-greedy .*?
    nav_pattern = re.compile(r'<nav class="nav-menu">.*?</nav>', re.DOTALL)

    for file_path in files:
        # We process ALL files including index.html to ensure consistency with links
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if nav_pattern.search(content):
                new_content = nav_pattern.sub(new_nav_menu, content)
                
                # Check if actually changed
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated nav in: {file_path}")
                    count += 1
                else:
                    pass
            else:
                print(f"Warning: No nav-menu found in {file_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Total files updated with new header: {count}")

if __name__ == "__main__":
    update_files()
