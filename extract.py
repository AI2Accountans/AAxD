from bs4 import BeautifulSoup

path = r"C:\Users\IPHIX\.gemini\antigravity-ide\brain\eb9fa28d-4223-48ed-a4c1-7c59e0f211b2\.system_generated\steps\121\content.md"
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
out_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\extracted.txt"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(soup.get_text(separator='\n', strip=True))
