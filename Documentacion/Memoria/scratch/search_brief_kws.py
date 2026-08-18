import os

es_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrativa_ES.md"
en_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrative_EN.md"

def find_kw(path, kw):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if kw.lower() in line.lower():
                print(f"[{os.path.basename(path)}:L{i}]: {line.strip()[:100]}...")

for p in [es_path, en_path]:
    print(f"\n--- Keywords in {os.path.basename(p)} ---")
    find_kw(p, "CFO")
    find_kw(p, "First Mile")
    find_kw(p, "Philippe")
    find_kw(p, "Schmidt")
    find_kw(p, "fusing")
    find_kw(p, "fusión")
