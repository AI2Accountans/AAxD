import urllib.request
import re
import os
import html

def clean_html(html_content):
    # Find post body
    post_body_match = re.search(r"<div[^>]*class=['\"]post-body[^'\"]*['\"][^>]*>(.*?)</div>\s*(?:<div|<footer)", html_content, re.DOTALL | re.IGNORECASE)
    if post_body_match:
        content = post_body_match.group(1)
    else:
        body_match = re.search(r"<body[^>]*>(.*?)</body>", html_content, re.DOTALL | re.IGNORECASE)
        content = body_match.group(1) if body_match else html_content

    # Strip style, script and some specific elements
    content = re.sub(r"<style.*?</style>", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r"<script.*?</script>", "", content, flags=re.DOTALL | re.IGNORECASE)
    
    # Replace paragraphs and line breaks with double newlines
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.IGNORECASE)
    content = re.sub(r"</p>", "\n\n", content, flags=re.IGNORECASE)
    content = re.sub(r"</div>", "\n", content, flags=re.IGNORECASE)
    content = re.sub(r"<li>", "\n- ", content, flags=re.IGNORECASE)
    content = re.sub(r"</li>", "", content, flags=re.IGNORECASE)
    content = re.sub(r"<h1>", "\n# ", content, flags=re.IGNORECASE)
    content = re.sub(r"</h2>|<h3>|<h4>", "\n## ", content, flags=re.IGNORECASE)
    content = re.sub(r"</h1>|</h2>|</h3>|</h4>", "\n", content, flags=re.IGNORECASE)

    # Strip remaining HTML tags
    content = re.sub(r"<[^>]+>", " ", content)
    
    # Unescape HTML entities
    content = html.unescape(content)
    
    # Clean up spaces
    lines = []
    for line in content.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line:
            lines.append(line)
        else:
            lines.append("")
            
    # Remove excessive blank lines
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()

def main():
    blogs = {
        "1_essence_of_accounting": "https://seattlemethod.blogspot.com/2026/02/essence-of-accounting.html",
        "2_industrial_process": "https://seattlemethod.blogspot.com/2026/03/industrial-process.html",
        "3_fundamental_capability": "https://seattlemethod.blogspot.com/2026/05/fundamental-capability-xbrl-enables.html",
        "4_core_pattern": "https://seattlemethod.blogspot.com/2025/11/core-pattern.html",
        "5_poka_yoke": "https://digitalfinancialreporting.blogspot.com/2025/06/poka-yoke-mistake-proofing.html"
    }

    out_dir = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\scratch"
    os.makedirs(out_dir, exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for name, url in blogs.items():
        print(f"Fetching {name} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                html_data = response.read().decode('utf-8', errors='ignore')
            
            cleaned = clean_html(html_data)
            
            out_file = os.path.join(out_dir, f"{name}.md")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# Source: {url}\n\n" + cleaned)
            print(f"Saved to {out_file} (length: {len(cleaned)} chars)")
        except Exception as e:
            print(f"Error fetching {name}: {e}")

if __name__ == "__main__":
    main()
