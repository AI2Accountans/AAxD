import os

es_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrativa_ES.md"
en_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrative_EN.md"

def inspect_file(path):
    if not os.path.exists(path):
        return
    print(f"\n================ STRUCTURE OF {os.path.basename(path)} ================")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("#"):
            print(f"L{i}: {line.strip()}")

inspect_file(es_path)
inspect_file(en_path)
