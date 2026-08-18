import re
from bs4 import BeautifulSoup

file_path = r"C:\Users\IPHIX\.gemini\antigravity-ide\brain\33899917-1813-4b18-94dc-402eec984962\.system_generated\steps\163\content.md"
output_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\cdt_text.txt"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text(separator="\n")

# Limpiar saltos de línea excesivos
text = re.sub(r'\n\s*\n', '\n\n', text)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Texto extraído en {output_path}")
