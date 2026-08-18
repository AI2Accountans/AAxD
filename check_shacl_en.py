with open(r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrative_EN.md", 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer("SHACL", text)]
for m in matches:
    print(text[m-50:m+250])
    print("-" * 40)
