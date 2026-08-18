mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

with open(mfd_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f, 1):
        if 'java' in line.lower():
            print(f"Line {idx}: {line.strip()}")
