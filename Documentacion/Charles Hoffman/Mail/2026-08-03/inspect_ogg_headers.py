import os

ogg_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\Charlie.ogg"

with open(ogg_path, "rb") as f:
    data = f.read()

print("File size:", len(data))
# Look for printable ASCII strings of length > 4 in data
import re
strings = re.findall(b'[\x20-\x7e]{5,}', data)
print("Extracted strings in OGG binary:")
for s in strings:
    print(s.decode('ascii', errors='ignore'))
