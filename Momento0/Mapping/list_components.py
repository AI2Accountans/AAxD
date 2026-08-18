import xml.etree.ElementTree as ET

mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"
tree = ET.parse(mfd_path)
root = tree.getroot()

# Let's print all components, their library, name, kind, and uid
for comp in root.findall(".//component"):
    name = comp.attrib.get('name')
    lib = comp.attrib.get('library')
    uid = comp.attrib.get('uid')
    kind = comp.attrib.get('kind')
    if name or lib:
        print(f"UID {uid}: name={name}, library={lib}, kind={kind}")
