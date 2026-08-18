import xml.etree.ElementTree as ET

mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

# Register namespaces
ET.register_namespace('', '')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

tree = ET.parse(mfd_path)
root = tree.getroot()

comp_map = root.find(".//component[@name='defaultmap']")
struct = comp_map.find("structure")
children = struct.find("children")
graph = struct.find("graph")
vertices = graph.find("vertices")

# 1. Remove QName components
to_remove = []
for comp in children.findall("component[@name='QName']"):
    to_remove.append(comp)
for comp in to_remove:
    children.remove(comp)
    print("Removed QName component:", comp.attrib.get('uid'))

# 2. Add new constants replacing the QName outputs
# Constant "iso639:es" (uid 1060, key 2060)
c1 = ET.Element('component', {'name': 'constant', 'library': 'core', 'uid': '1060', 'kind': '2'})
targets1 = ET.SubElement(c1, 'targets')
ET.SubElement(targets1, 'datapoint', {'pos': '0', 'key': '2060'})
ET.SubElement(c1, 'view', {'ltx': '500', 'lty': '-290', 'rbx': '650', 'rby': '-273'})
data1 = ET.SubElement(c1, 'data')
ET.SubElement(data1, 'constant', {'value': 'iso639:es', 'datatype': 'string'})
children.append(c1)

# Constant "iso4217:COP" (uid 1061, key 2061)
c2 = ET.Element('component', {'name': 'constant', 'library': 'core', 'uid': '1061', 'kind': '2'})
targets2 = ET.SubElement(c2, 'targets')
ET.SubElement(targets2, 'datapoint', {'pos': '0', 'key': '2061'})
ET.SubElement(c2, 'view', {'ltx': '500', 'lty': '-260', 'rbx': '650', 'rby': '-243'})
data2 = ET.SubElement(c2, 'data')
ET.SubElement(data2, 'constant', {'value': 'iso4217:COP', 'datatype': 'string'})
children.append(c2)

# Constant "xbrli:shares" (uid 1062, key 2062)
c3 = ET.Element('component', {'name': 'constant', 'library': 'core', 'uid': '1062', 'kind': '2'})
targets3 = ET.SubElement(c3, 'targets')
ET.SubElement(targets3, 'datapoint', {'pos': '0', 'key': '2062'})
ET.SubElement(c3, 'view', {'ltx': '500', 'lty': '-230', 'rbx': '650', 'rby': '-213'})
data3 = ET.SubElement(c3, 'data')
ET.SubElement(data3, 'constant', {'value': 'xbrli:shares', 'datatype': 'string'})
children.append(c3)

# 3. Modify graph/vertices
# Remove vertices that are inputs or outputs of QNames (keys 120, 121, 122, 124, 125, 126, 127, 128, 129)
keys_to_remove = {'120', '121', '122', '124', '125', '126', '127', '128', '129'}
vertices_to_remove = []
for v in vertices.findall("vertex"):
    v_key = v.attrib.get('vertexkey')
    if v_key in keys_to_remove:
        vertices_to_remove.append(v)
    else:
        # Also check and remove edges that point to these keys
        edges = v.find("edges")
        if edges is not None:
            edges_to_remove = []
            for e in edges.findall("edge"):
                if e.attrib.get('vertexkey') in keys_to_remove:
                    edges_to_remove.append(e)
            for e in edges_to_remove:
                edges.remove(e)

for v in vertices_to_remove:
    vertices.remove(v)
    print("Removed vertex:", v.attrib.get('vertexkey'))

# Remove references to QNames from other vertices (e.g. constant 97 -> 120, constant 123 -> 121, etc.)
# Let's clean up edges of:
# key 97 (points to 120), key 123 (points to 121), key 99 (points to 124), key 130 (points to 127), key 131 (points to 128)
keys_with_edges_to_clean = {'97', '123', '99', '130', '131'}
for v_key in keys_with_edges_to_clean:
    v = vertices.find(f"vertex[@vertexkey='{v_key}']")
    if v is not None:
        edges = v.find("edges")
        if edges is not None:
            for e in list(edges):
                if e.attrib.get('vertexkey') in keys_to_remove:
                    edges.remove(e)
            # If no edges left, remove the vertex altogether
            if len(list(edges)) == 0:
                vertices.remove(v)
                print("Cleaned empty vertex:", v_key)

# Add vertices/edges for the new constants
# Constant "iso639:es" (key 2060) -> language in documentInfo (key 103)
v1 = ET.SubElement(vertices, 'vertex', {'vertexkey': '2060'})
edges1 = ET.SubElement(v1, 'edges')
ET.SubElement(edges1, 'edge', {'vertexkey': '103'})

# Constant "iso4217:COP" (key 2061) -> defaultCurrency in documentInfo (key 109)
v2 = ET.SubElement(vertices, 'vertex', {'vertexkey': '2061'})
edges2 = ET.SubElement(v2, 'edges')
ET.SubElement(edges2, 'edge', {'vertexkey': '109'})

# Constant "xbrli:shares" (key 2062) -> measure in unit (key 92)
v3 = ET.SubElement(vertices, 'vertex', {'vertexkey': '2062'})
edges3 = ET.SubElement(v3, 'edges')
ET.SubElement(edges3, 'edge', {'vertexkey': '92'})

tree.write(mfd_path, encoding='utf-8', xml_declaration=True)
print("QName components replaced with compatible string constants!")
