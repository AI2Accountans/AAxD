import re
import os

def clean_html(html_content):
    # Find text inside <div class='post-body ...'>...</div> or just extract readable text
    # A simple regex to find the post body
    post_body_match = re.search(r"<div[^>]*class=['\"]post-body[^'\"]*['\"][^>]*>(.*?)</div>\s*<div", html_content, re.DOTALL | re.IGNORECASE)
    if post_body_match:
        content = post_body_match.group(1)
    else:
        # Fallback to anything inside body
        body_match = re.search(r"<body[^>]*>(.*?)</body>", html_content, re.DOTALL | re.IGNORECASE)
        content = body_match.group(1) if body_match else html_content

    # Strip HTML tags
    content = re.sub(r"<style.*?</style>", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r"<script.*?</script>", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r"<[^>]+>", " ", content)
    # Replace multiple spaces/newlines
    content = re.sub(r"\s+", " ", content)
    # Unescape HTML entities
    content = content.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'").replace("&quot;", '"')
    return content.strip()

def main():
    steps = {
        "Essence of Accounting": r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps\518\content.md",
        "Industrial Process": r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps\520\content.md",
        "Fundamental Capability": r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps\522\content.md",
        "Core Pattern": r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps\524\content.md"
    }

    for name, path in steps.items():
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                html = f.read()
            text = clean_html(html)
            print("="*40)
            print(f"BLOG: {name}")
            print("="*40)
            # Print the first 2500 characters
            print(text[:2500] + "\n... [TRUNCATED] ...\n" if len(text) > 2500 else text)
            print("\n")
        else:
            print(f"Path not found for {name}: {path}")

if __name__ == "__main__":
    main()
