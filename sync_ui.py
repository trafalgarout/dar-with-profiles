import os
import re

# Full Header extracted from index.html (with paths adjusted for ai-tools subdirectory)
full_header = r'''    <header class="main-header">
        <div class="container header-content">
            <a href="../index.html" class="logo">
                <img src="../LOGO.png" alt="كويزات عربية" style="height: 45px; width: auto;">
            </a>

            <nav class="nav-menu">
                <a href="../index.html" class="nav-link">الرئيسية</a>

                <div class="nav-item dropdown">
                    <span class="nav-link" style="cursor: pointer; display: flex; align-items: center; gap: 5px;">
                        كويزات <span style="font-size: 0.8em;">▾</span>
                    </span>
                    <div class="dropdown-content">
                        <a href="../index.html#men">للشباب</a>
                        <a href="../index.html#women">للبنات</a>
                        <a href="../index.html#entertainment">ترفيه</a>
                    </div>
                </div>

                <div class="nav-item dropdown">
                    <span class="nav-link" style="cursor: pointer; display: flex; align-items: center; gap: 5px;">
                        الذكاء الاصطناعي <span style="font-size: 0.8em;">▾</span>
                    </span>
                    <div class="dropdown-content">
                        <a href="index.html">أدوات الذكاء الاصطناعي</a>
                        <a href="username-generator.html">مولد أسماء المستخدمين</a>
                        <a href="business-name-generator.html">مولد أسماء شركات</a>
                        <a href="name-compatibility.html">اختبار توافق الأسماء</a>
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
                        <a href="../gulf_saudi.html">🇸🇦 السعودية</a>
                        <a href="../gulf_uae.html">🇦🇪 الإمارات</a>
                        <a href="../gulf_qatar.html">🇶🇦 قطر</a>
                        <a href="../gulf_kuwait.html">🇰🇼 الكويت</a>
                        <a href="../gulf_bahrain.html">🇧🇭 البحرين</a>
                        <a href="../gulf_oman.html">🇴🇲 عمان</a>
                    </div>
                </div>

                <a href="../wallpapers.html" class="nav-link">خلفيات متحركة</a>
                <a href="../index.html#banat" class="nav-link" style="color:#E91E63;font-weight:900;">🔥 تعارف بنات</a>
            </nav>

            <div class="header-actions">
                <div class="search-box">
                    <input type="text" placeholder="ابحث عن اختبار...">
                    <button class="search-btn" style="background:none;border:none;cursor:pointer;">🔍</button>
                </div>
                <a href="../index.html#men" class="cta-btn">ابدأ الآن</a>
            </div>

            <button class="mobile-menu-btn">☰</button>
        </div>
    </header>'''

# Full Footer extracted from index.html (with paths adjusted)
full_footer = r'''    <footer class="main-footer">
        <div class="container footer-grid">
            <div class="footer-col">
                <div class="logo" style="margin-bottom:15px;">
                    <img src="../FAVICON.png" alt="كويزات عربية" style="height: 50px; width: auto;">
                </div>
                <p style="color:#cbd5e1;line-height:1.6;">منصة ترفيهية تعليمية تساعدك على اكتشاف نفسك وفهم علاقاتك بشكل أفضل من خلال اختبارات ممتعة ودقيقة.</p>
            </div>

            <div class="footer-col">
                <h3>اكتشف</h3>
                <ul class="footer-links">
                    <li><a href="../index.html#men">الأكثر رواجاً</a></li>
                    <li><a href="../index.html#men">جديدنا</a></li>
                    <li><a href="../index.html#men">اختبارات الحب</a></li>
                    <li><a href="../index.html#men">تحليل الشخصية</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h3>معلومات</h3>
                <ul class="footer-links">
                    <li><a href="../about.html">من نحن</a></li>
                    <li><a href="../privacy.html">سياسة الخصوصية</a></li>
                    <li><a href="../terms.html">شروط الاستخدام</a></li>
                    <li><a href="../contact.html">تواصل معنا</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h3>تابعنا</h3>
                <div class="social-icons">
                    <a href="#" class="social-icon">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z" />
                        </svg>
                    </a>
                    <a href="#" class="social-icon">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
                        </svg>
                    </a>
                    <a href="#" class="social-icon">
                        <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z" />
                        </svg>
                    </a>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <div class="container">
                <p>&copy; 2026 كويزات عربية — جميع الحقوق محفوظة</p>
                <p class="disclaimer">لأغراض الترفيه واكتشاف الذات فقط</p>
            </div>
        </div>
    </footer>'''

# Mobile Menu Script
mobile_script = r'''    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.querySelector('.mobile-menu-btn');
            const menu = document.querySelector('.nav-menu');
            if (btn && menu) {
                btn.addEventListener('click', () => {
                    menu.classList.toggle('active');
                    btn.textContent = menu.classList.contains('active') ? '✕' : '☰';
                });
            }
            const dropdowns = document.querySelectorAll('.nav-item.dropdown');
            dropdowns.forEach(dropdown => {
                const trigger = dropdown.querySelector('.nav-link');
                if (trigger) {
                    trigger.addEventListener('click', (e) => {
                        if (window.innerWidth <= 900) {
                            e.preventDefault();
                            dropdown.classList.toggle('open');
                        }
                    });
                }
            });
            const searchBtn = document.querySelector('.search-btn');
            const searchInput = document.querySelector('.search-box input');
            if (searchBtn && searchInput) {
                searchBtn.addEventListener('click', () => {
                    const query = searchInput.value.trim();
                    if (query) { alert('جاري البحث عن: ' + query); }
                });
            }
        });
    </script>'''

target_dir = './ai-tools'
files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

for filename in files:
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Header
    content = re.sub(r'<header class="main-header">.*?</header>', full_header, content, flags=re.DOTALL)
    # Replace Footer
    content = re.sub(r'<footer class="main-footer">.*?</footer>', full_footer, content, flags=re.DOTALL)
    
    # Replace/Inject Script before </body>
    if '<script>' in content and 'mobile-menu-btn' in content:
        # Replace existing simplified script
        content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',.*?<\/script>', mobile_script, content, flags=re.DOTALL)
    else:
        # Inject script before </body>
        content = content.replace('</body>', f'{mobile_script}\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully synchronized header/footer for {len(files)} files.")
