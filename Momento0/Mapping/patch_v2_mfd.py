import xml.etree.ElementTree as ET
import os

v2_mfd = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V2.mfd"

with open(v2_mfd, 'r', encoding='utf-8') as f:
    content = f.read()

# Ensure V2 schema and CSV references are explicitly set in the MFD XML
content = content.replace("sunder_zachman_dfrnt_instances.schema.json", "sunder_zachman_dfrnt_instances_v2.schema.json")
content = content.replace("Constitucion_Input.csv", "Constitucion_Input_V2.csv")
content = content.replace("GS2XBRLGL2JSONLD.jsonld", "GS2XBRLGL2JSONLD_V2.jsonld")

with open(v2_mfd, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {v2_mfd} with V2 references.")
