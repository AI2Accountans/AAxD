import os

v1_mfd = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"
v2_mfd = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V2.mfd"

with open(v1_mfd, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace references to V1 schema and files with V2
content_v2 = content.replace("sunder_zachman_dfrnt_instances.schema.json", "sunder_zachman_dfrnt_instances_v2.schema.json")
content_v2 = content_v2.replace("Constitucion_Input.csv", "Constitucion_Input_V2.csv")
content_v2 = content_v2.replace("GS2XBRLGL2JSONLD.jsonld", "GS2XBRLGL2JSONLD_V2.jsonld")

with open(v2_mfd, 'w', encoding='utf-8') as f:
    f.write(content_v2)

print(f"GS2XBRLGL2JSONLD_V2.mfd successfully generated. Size: {os.path.getsize(v2_mfd)} bytes.")
