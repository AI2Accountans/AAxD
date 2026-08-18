mfd_bak_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd.bak"

with open(mfd_bak_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f, 1):
        if 'selectedlanguage' in line.lower():
            print(f"Line {idx}: {line.strip()}")
