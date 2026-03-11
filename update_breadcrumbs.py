import os
import re

target_dir = './ai-tools'
files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

# Match both old and new breadcrumb styles to be robust
breadcrumb_pattern = re.compile(r'<nav class="breadcrumb[^"]*">.*?</nav>', re.DOTALL)

for filename in files:
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the tool name
    title_match = re.search(r'<h1>(.*?)</h1>', content)
    if not title_match:
        title_match = re.search(r'<title>(.*?)</title>', content)
    
    if title_match:
        full_title = title_match.group(1).split('–')[0].split('بالذكاء')[0].strip()
        
        if filename == 'index.html':
            new_breadcrumb = f"""        <nav class="breadcrumb-nav">
            <ul class="breadcrumb">
                <li class="breadcrumb-item"><a href="../index.html"><span class="breadcrumb-icon">🏠</span> الرئيسية</a></li>
                <li class="breadcrumb-sep">/</li>
                <li class="breadcrumb-item active">أدوات الذكاء الاصطناعي</li>
            </ul>
        </nav>"""
        else:
            new_breadcrumb = f"""        <nav class="breadcrumb-nav">
            <ul class="breadcrumb">
                <li class="breadcrumb-item"><a href="../index.html"><span class="breadcrumb-icon">🏠</span> الرئيسية</a></li>
                <li class="breadcrumb-sep">/</li>
                <li class="breadcrumb-item"><a href="index.html">أدوات الذكاء الاصطناعي</a></li>
                <li class="breadcrumb-sep">/</li>
                <li class="breadcrumb-item active">{full_title}</li>
            </ul>
        </nav>"""
        
        if breadcrumb_pattern.search(content):
            new_content = breadcrumb_pattern.sub(new_breadcrumb, content)
        else:
            # Inject after the header
            new_content = content.replace('</header>', f'</header>\n{new_breadcrumb}')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Refined breadcrumbs to premium style in {len(files)} files.")
