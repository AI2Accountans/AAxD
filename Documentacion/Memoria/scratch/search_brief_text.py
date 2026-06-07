import os

es_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrativa_ES.md"
en_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrative_EN.md"

def search_text_in_file(path, search_str):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if search_str.lower() in line.lower():
                print(f"[{os.path.basename(path)}:L{i}]: {line.strip()}")

print("Searching in Spanish brief:")
search_text_in_file(es_path, "fusión del liderazgo")
search_text_in_file(es_path, "liderazgo operativo")

print("\nSearching in English brief:")
search_text_in_file(en_path, "fusing the operational")
search_text_in_file(en_path, "operational expertise")
