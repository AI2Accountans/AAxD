mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

with open(mfd_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change SelectedLanguage to builtin to avoid Java generation warning
content = content.replace('SelectedLanguage="java"', 'SelectedLanguage="builtin"')

with open(mfd_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("MFD SelectedLanguage changed to builtin!")
