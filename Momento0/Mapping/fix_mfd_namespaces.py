mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

with open(mfd_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace root element to restore namespace definition if missing
if 'xmlns:xsi' not in content:
    content = content.replace('<mapping version="29">', '<mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="29">')

# Let's save it back
with open(mfd_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("MFD namespaces fixed!")
