
import os

# Gulf Countries Data
countries = [
    {"name": "السعودية", "flag": "🇸🇦", "filename": "gulf_saudi.html", "title": "أموال الخليج: السعودية"},
    {"name": "الإمارات", "flag": "🇦🇪", "filename": "gulf_uae.html", "title": "أموال الخليج: الإمارات"},
    {"name": "قطر", "flag": "🇶🇦", "filename": "gulf_qatar.html", "title": "أموال الخليج: قطر"},
    {"name": "الكويت", "flag": "🇰🇼", "filename": "gulf_kuwait.html", "title": "أموال الخليج: الكويت"},
    {"name": "البحرين", "flag": "🇧🇭", "filename": "gulf_bahrain.html", "title": "أموال الخليج: البحرين"},
    {"name": "عمان", "flag": "🇴🇲", "filename": "gulf_oman.html", "title": "أموال الخليج: عمان"}
]

# Grid Categories
categories = [
    {"name": "بطاقات الائتمان", "icon": "💳", "desc": "أفضل العروض والمزايا لبطاقات الائتمان."},
    {"name": "القروض الشخصية", "icon": "💵", "desc": "تمويل شخصي مرن يناسب احتياجاتك."},
    {"name": "كراء وتمويل السيارات", "icon": "🚗", "desc": "طريقك الأسهل لامتلاك سيارة أحلامك."},
    {"name": "التأمين", "icon": "🛡️", "desc": "خطط تأمين شاملة لراحة بالك ومستقبلك."},
    {"name": "الحسابات البنكية", "icon": "🏦", "desc": "خيارات بنكية متنوعة لادخار وإدارة أموالك."},
    {"name": "الاستثمار", "icon": "📈", "desc": "فرص استثمارية ذكية لتنمية ثروتك."},
    {"name": "التمويل العقاري", "icon": "🏠", "desc": "حلول تمويلية لامتلاك منزلك الخاص."},
    {"name": "الأعمال وريادة المشاريع", "icon": "🚀", "desc": "دعم وتمويل لرواد الأعمال والمشاريع الناشئة."}
]

# HTML Template (Using parts of index.html structure)
html_template = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | كويزات عربية</title>
    <meta name="description" content="دليل {name} الشامل للمال والأعمال: بطاقات الائتمان، القروض، الاستثمار، والمزيد.">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <link rel="shortcut icon" href="FAVICON.png" type="image/png">
    <style>
        :root {{
            --primary: #c2185b;
            --secondary: #7b1fa2;
            --dark: #1e293b;
            --light: #f8fafc;
            --surface: #ffffff;
            --accent: #ffd700;
        }}
        
        body {{
            font-family: 'Cairo', sans-serif;
            background-color: var(--light);
            color: var(--dark);
            margin: 0;
            padding: 0;
        }}

        /* Reuse Header Styles */
        .main-header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 15px 0;
        }}

        .header-content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        .logo img {{ height: 50px; width: auto; }}

        .nav-menu {{ display: flex; gap: 25px; align-items: center; }}
        .nav-link {{ text-decoration: none; color: var(--dark); font-weight: 700; transition: color 0.3s; }}
        .nav-link:hover {{ color: var(--primary); }}

        /* Dropdown Styles */
        .nav-item.dropdown {{ position: relative; }}
        .dropdown-content {{
            display: none;
            position: absolute;
            top: 100%;
            right: 0;
            background-color: white;
            min-width: 220px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            z-index: 1000;
            border-radius: 12px;
            padding: 10px 0;
            flex-direction: column;
        }}
        .nav-item.dropdown:hover .dropdown-content {{ display: flex; }}
        .dropdown-content a {{
            padding: 12px 20px;
            text-decoration: none;
            color: var(--dark);
            font-weight: 600;
            display: block;
            text-align: right;
        }}
        .dropdown-content a:hover {{ background-color: #f1f5f9; color: var(--primary); }}

        .country-hero {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 80px 20px;
            text-align: center;
            border-radius: 0 0 50px 50px;
            margin-bottom: 50px;
        }}

        .country-hero h1 {{ font-size: 2.5rem; margin-bottom: 10px; }}
        .country-flag {{ font-size: 4rem; display: block; margin-bottom: 20px; }}
        
        .grid-container {{
            max-width: 1100px;
            margin: 0 auto 80px;
            padding: 0 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }}

        .category-card {{
            background: white;
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            border: 1px solid rgba(0,0,0,0.05);
        }}

        .category-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
            border-color: var(--primary);
        }}

        .cat-icon {{ font-size: 3rem; margin-bottom: 15px; display: block; }}
        .cat-title {{ font-size: 1.25rem; font-weight: 800; margin-bottom: 10px; color: var(--dark); }}
        .cat-desc {{ font-size: 0.95rem; color: #64748b; line-height: 1.6; }}

        .cta-btn {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 10px 25px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 800;
        }}
          /* Mobile Menu - Minimal for layout consistency */
        @media (max-width: 900px) {{
            .nav-menu {{ display: none; }}
        }}
        
         /* Footer */
        .main-footer {{
            background: var(--dark);
            color: white;
            padding: 60px 0 20px;
            border-top-left-radius: 40px;
            border-top-right-radius: 40px;
            text-align: center;
        }}
        
        .footer-bottom {{ border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; margin-top: 40px; color: #94a3b8; }}

    </style>
</head>

<body>

    <header class="main-header">
        <div class="header-content">
            <a href="index.html" class="logo">
                <img src="LOGO.png" alt="كويزات عربية">
            </a>

            <!-- NAV MENU PLACEHOLDER - Will be updated by script -->
            <nav class="nav-menu">
                <a href="index.html" class="nav-link">الرئيسية</a>
                 <!-- Placeholder for script update -->
                  <div class="nav-item dropdown">
                    <span class="nav-link">كويزات ▾</span>
                  </div>
            </nav>

            <a href="index.html#men" class="cta-btn">ابدأ الآن</a>
            <button class="mobile-menu-btn" style="background:none;border:none;font-size:1.5rem;cursor:pointer;">☰</button>
        </div>
    </header>

    <section class="country-hero">
        <span class="country-flag">{flag}</span>
        <h1>دليل المال والأعمال في {name}</h1>
        <p>كل ما تحتاج معرفته عن التمويل والاستثمار في {name}</p>
    </section>

    <div class="grid-container">
        {grid_items}
    </div>

    <footer class="main-footer">
        <div class="container">
             <div class="logo" style="margin-bottom:15px;">
                <img src="FAVICON.png" alt="كويزات عربية" style="height: 50px; width: auto;">
            </div>
            <p>منصة ترفيهية تعليمية تساعدك على اكتشاف نفسك وفهم علاقاتك.</p>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 كويزات عربية — جميع الحقوق محفوظة</p>
        </div>
    </footer>

</body>
</html>
'''

def generate_grid_html():
    items_html = ""
    for cat in categories:
        items_html += f'''
        <div class="category-card">
            <span class="cat-icon">{cat["icon"]}</span>
            <div class="cat-title">{cat["name"]}</div>
            <div class="cat-desc">{cat["desc"]}</div>
        </div>
        '''
    return items_html

def create_pages():
    grid_html = generate_grid_html()
    
    for country in countries:
        content = html_template.format(
            title=country["title"],
            name=country["name"],
            flag=country["flag"],
            grid_items=grid_html
        )
        
        with open(country["filename"], 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {country['filename']}")

if __name__ == "__main__":
    create_pages()
