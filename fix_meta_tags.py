import os
import re
import urllib.parse

def fix_meta_tags(directory):
    updated_count = 0
    pattern_miss_count = 0
    for filename in os.listdir(directory):
        if not filename.startswith('quiz_') or not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title from <h1>
        h1_match = re.search(r'<h1>(.*?)</h1>', content)
        if h1_match:
            title_text = h1_match.group(1).strip()
            title_text = re.sub(r'<[^>]+>', '', title_text)
        else:
            # try to see if title already has something useful
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match and "اختبار سريع" not in title_match.group(1):
                title_text = title_match.group(1).strip()
            else:
                title_text = "كويزات عربية | اكتشف شخصيتك"
            
        if "|" not in title_text and "-" not in title_text:
            title_text += " | كويزات عربية"
            
        # Extract description from the first <p> after <h1>
        seo_p_match = re.search(r'<div class="seo-intro"[^>]*>.*?<h1>.*?</h1>\s*<p>(.*?)</p>', content, re.DOTALL)
        if not seo_p_match:
            seo_p_match = re.search(r'<div class="seo-intro"[^>]*>\s*<p>(.*?)</p>', content, re.DOTALL)
            
        if seo_p_match:
            description = seo_p_match.group(1).strip()
            description = re.sub(r'<[^>]+>', '', description)
            description = description.replace('\n', ' ').replace('\r', '')
            description = re.sub(r'\s+', ' ', description)
        else:
            description = "اختبار ممتع من كويزات عربية. اكتشف المزيد عن شخصيتك الآن!"
            
        if len(description) > 160:
            description = description[:157] + "..."
            
        # Extract image from quiz-hero-img
        img_match = re.search(r'<img[^>]+class="quiz-hero-img"[^>]+src="(.*?)"', content)
        if not img_match:
            img_match = re.search(r'<img[^>]+src="(.*?)"[^>]+class="quiz-hero-img"', content)
            
        if img_match:
            img_src = img_match.group(1)
        else:
            img_src = "THUMBNAILS/MEN QUIZZES/quiz_quick_deep_test.jpeg"
            
        # Encode spaces in image URL
        # Unquote first to avoid double encoding (e.g., %20 becoming %2520)
        unquoted_img_src = urllib.parse.unquote(img_src)
        # Use safe='/' so we don't encode the directory slashes, which Github Pages dislikes
        img_url = "https://www.darlma3rifa.com/" + urllib.parse.quote(unquoted_img_src, safe='/')
        page_url = "https://www.darlma3rifa.com/" + filename
        
        # Replace the <head> meta tags.
        # Sometimes there's spaces or different tags. Use a broad pattern from <!-- SEO & Social Meta Tags --> to </title>
        meta_block_pattern = re.compile(r'<!-- SEO & Social Meta Tags -->.*?</title>', re.DOTALL | re.IGNORECASE)
        
        new_meta_block = f"""<!-- SEO & Social Meta Tags -->
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{page_url}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title_text}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{img_url}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:site_name" content="كويزات عربية">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_text}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{img_url}">

    <meta name="description" content="{description}">
    <title>{title_text}</title>"""

        new_content, count = meta_block_pattern.subn(new_meta_block, content)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
        else:
            # Handle case where "<!-- SEO & Social Meta Tags -->" might not exist
            pattern_miss_count += 1
            print(f"Missed pattern for {filename}")

    print(f"Successfully updated {updated_count} files.")
    print(f"Missed {pattern_miss_count} files.")

if __name__ == "__main__":
    fix_meta_tags(r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\dar-with-profiles")
