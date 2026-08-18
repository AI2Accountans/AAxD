import xml.etree.ElementTree as ET

mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"
tree = ET.parse(mfd_path)
root = tree.getroot()

# Let's find all components of name 'QName'
qnames = []
for comp in root.findall(".//component[@name='QName']"):
    uid = comp.attrib.get('uid')
    qnames.append(uid)
    print("Found QName component with UID:", uid)
    # Print targets and sources keys
    for dp in comp.findall(".//datapoint"):
        print("  Datapoint key:", dp.attrib.get('key'), "pos:", dp.attrib.get('pos'))

# Let's check which vertices/edges refer to these keys
# The keys of QName targets/sources are:
# uid 40: sources key 120, 121; target key 122
# uid 41: sources key 124, 125; target key 126
# uid 42: sources key 127, 128; target key 129
