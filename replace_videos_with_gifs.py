import os
import json
import re
import random

def replace_videos_with_gifs(directory):
    gif_library_path = os.path.join(directory, 'gif_library.json')
    try:
        with open(gif_library_path, 'r', encoding='utf-8') as f:
            gifs = json.load(f)
    except Exception as e:
        print(f"Error loading gif_library.json: {e}")
        return

    if not gifs:
        print("No GIFs found in library.")
        return

    updated_count = 0
    
    for filename in os.listdir(directory):
        if not filename.startswith('quiz_') or not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content

        # 1. Replace the `.mp4` URLs inside the `questions` and `results` JavaScript objects.
        # It looks something like: "src":"https://res.cloudinary.com/...mp4"
        # We can find all unique video URLs and replace them.
        video_urls_1 = re.findall(r'"src"\s*:\s*"(https?://res\.cloudinary\.com/[^"]+\.mp4)"', content)
        video_urls_2 = re.findall(r'src\s*:\s*"(https?://res\.cloudinary\.com/[^"]+\.mp4)"', content)
        video_urls_3 = re.findall(r'"src"\s*:\s*"(https?://[^"]+\.mp4)"', content)
        video_urls_4 = re.findall(r'src\s*:\s*"(https?://[^"]+\.mp4)"', content)
        video_urls = list(set(video_urls_1 + video_urls_2 + video_urls_3 + video_urls_4))

        for v_url in video_urls:
            random_gif = random.choice(gifs)
            content = content.replace(v_url, random_gif)

        # 2. Replace the HTML rendering logic in calculateResult()
        # From: <div class="video-wrapper" style="margin-bottom:20px;"><video loop muted playsinline autoplay style="width:100%; border-radius:15px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"><source src="${r.video.src}" type="video/mp4"></video></div>
        # To: <div class="video-wrapper" style="margin-bottom:20px;"><img src="${r.video.src}" style="width:100%; max-width:350px; border-radius:15px; box-shadow:0 5px 15px rgba(0,0,0,0.1); display:block; margin: 0 auto;" alt="Result GIF"></div>
        result_video_pattern = re.compile(r'<div class="video-wrapper"[^>]*>\s*<video[^>]*>\s*<source src="\$\{r\.video\.src\}" type="video/mp4">\s*</video>\s*</div>', re.DOTALL)
        result_img_replacement = r'<div class="video-wrapper" style="margin-bottom:20px;"><img src="${r.video.src}" style="width:100%; max-width:350px; border-radius:15px; box-shadow:0 5px 15px rgba(0,0,0,0.1); display:block; margin: 0 auto;" alt="Result GIF"></div>'
        content = result_video_pattern.sub(result_img_replacement, content)

        # 3. Replace the HTML rendering logic in render()
        # From:
        # <div class="video-wrapper"><video loop muted playsinline
        #    poster="https://placehold.co/500x280/e0e0e0/333?text=Buffering...">
        #    <source src="${q.video.src}" type="video/mp4">
        # </video></div>
        # To:
        # <div class="video-wrapper"><img src="${q.video.src}" style="width:100%; max-width:350px; border-radius:15px; display:block; margin: 0 auto; box-shadow:0 5px 15px rgba(0,0,0,0.1);" alt="Question GIF"></div>
        question_video_pattern = re.compile(r'<div class="video-wrapper">\s*<video[^>]*>\s*<source src="\$\{q\.video\.src\}"[^>]*>\s*</video>\s*</div>', re.DOTALL)
        question_img_replacement = r'<div class="video-wrapper"><img src="${q.video.src}" style="width:100%; max-width:350px; border-radius:15px; display:block; margin: 0 auto 20px auto; box-shadow:0 5px 15px rgba(0,0,0,0.1);" alt="Question GIF"></div>'
        content = question_video_pattern.sub(question_img_replacement, content)

        # 4. Remove the IntersectionObserver for videos since we use GIFs now
        obs_pattern_1 = re.compile(r'const obs = new IntersectionObserver\(e => e\.forEach\(x => x\.isIntersecting \? x\.target\.play\(\) : x\.target\.pause\(\)\),\s*\{\s*threshold:\s*0\.5\s*\}\);', re.DOTALL)
        obs_pattern_2 = re.compile(r'document\.querySelectorAll\(\'video\'\)\.forEach\(v => obs\.observe\(v\)\);', re.DOTALL)
        
        content = obs_pattern_1.sub('', content)
        content = obs_pattern_2.sub('', content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1

    print(f"Successfully updated {updated_count} files.")

if __name__ == '__main__':
    fix_dir = r"f:\ANTIGRAVITY\QUIZAT ARABIC HTML\darlma3rifa-quizzes-2-main (1)\dar-with-profiles"
    replace_videos_with_gifs(fix_dir)
