import os
import re
import html

steps_dir = r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps"
output_file = r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\scratch\extracted_blogs.txt"

blog_paths = {
    "Essence of Accounting": r"C:\Users\IPHIX\.gemini\antigravity\brain\f7f2b34c-de1e-40cd-8bfd-1d153ea585fe\.system_generated\steps\644\content.md", # We just saved this one at step 644
}

# Let's search the steps directory for other content.md files that might have been downloaded in previous turns
for root, dirs, files in os.walk(steps_dir):
    for f in files:
        if f == "content.md":
            full_path = os.path.join(root, f)
            # Read first few lines to detect title
            try:
                with open(full_path, "r", encoding="utf-8") as file:
                    head = [file.readline() for _ in range(30)]
                content_str = "".join(head)
                if "Essence of Accounting" in content_str:
                    blog_paths["Essence of Accounting"] = full_path
                elif "Industrial Process" in content_str:
                    blog_paths["Industrial Process"] = full_path
                elif "Fundamental Capability" in content_str:
                    blog_paths["Fundamental Capability"] = full_path
                elif "Core Pattern" in content_str:
                    blog_paths["Core Pattern"] = full_path
                elif "Poka Yoke" in content_str:
                    blog_paths["Poka Yoke"] = full_path
            except Exception as e:
                pass

print("Found blog paths:", blog_paths)

# Clean HTML helper
def clean_html(html_content):
    # Extract only post content if possible
    # In Blogger, post content is usually inside <div class='post-body entry-content' ...> ... </div>
    match = re.search(r"<div[^>]*class=['\"]post-body[^'\"]*['\"][^>]*>(.*?)</div>\s*<div", html_content, re.DOTALL)
    if match:
        body = match.group(1)
    else:
        # Fallback to whole body
        body = html_content
    
    # Strip script and style tags
    body = re.sub(r"<style.*?</style>", "", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r"<script.*?</script>", "", body, flags=re.DOTALL | re.IGNORECASE)
    
    # Replace common tags with newlines
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.IGNORECASE)
    body = re.sub(r"</p>", "\n\n", body, flags=re.IGNORECASE)
    body = re.sub(r"</div>", "\n", body, flags=re.IGNORECASE)
    body = re.sub(r"<li>", "\n- ", body, flags=re.IGNORECASE)
    body = re.sub(r"</tr>", "\n", body, flags=re.IGNORECASE)
    body = re.sub(r"</td>", " | ", body, flags=re.IGNORECASE)
    
    # Strip all other HTML tags
    body = re.sub(r"<[^>]+>", "", body)
    
    # Decode HTML entities
    body = html.unescape(body)
    
    # Clean up whitespace
    body = re.sub(r"\n\s*\n+", "\n\n", body)
    return body.strip()

with open(output_file, "w", encoding="utf-8") as out:
    for title, path in blog_paths.items():
        out.write("=" * 80 + "\n")
        out.write(f"BLOG POST: {title}\n")
        out.write(f"Source Path: {path}\n")
        out.write("=" * 80 + "\n\n")
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            cleaned = clean_html(content)
            out.write(cleaned)
            out.write("\n\n\n")
            print(f"Extracted {title} successfully.")
        except Exception as e:
            out.write(f"Error reading path: {e}\n\n\n")
            print(f"Error extracting {title}: {e}")

print(f"Extraction complete! Saved to {output_file}")
