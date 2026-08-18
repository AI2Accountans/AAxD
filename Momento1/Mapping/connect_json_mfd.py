import xml.etree.ElementTree as ET
import os

mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento1\Mapping\Momento1.mfd"

ET.register_namespace('', '')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

print(f"Abriendo {mfd_path}...")
tree = ET.parse(mfd_path)
root = tree.getroot()

# Asegurar que exista <vertices>
vertices = root.find(".//vertices")
if vertices is None:
    graph = root.find(".//graph")
    vertices = ET.SubElement(graph, "vertices")

# Buscar la llave más alta para no chocar
max_key = 0
for el in root.iter():
    for attr in ['inpkey', 'outkey', 'key', 'vertexkey', 'edgekey']:
        val = el.attrib.get(attr)
        if val and val.isdigit():
            max_key = max(max_key, int(val))

def new_key():
    global max_key
    max_key += 1
    return str(max_key)

def get_or_create_key(node, key_type='inpkey'):
    if node is None: return None
    val = node.attrib.get(key_type)
    if not val:
        val = new_key()
        node.set(key_type, val)
    return val

def add_edge(v_out, v_in, desc=""):
    if v_out and v_in:
        v_out_str = str(v_out)
        v_in_str = str(v_in)
        vertex_node = vertices.find(f"vertex[@vertexkey='{v_out_str}']")
        if vertex_node is None:
            vertex_node = ET.SubElement(vertices, "vertex", {"vertexkey": v_out_str})
        edges_node = vertex_node.find("edges")
        if edges_node is None:
            edges_node = ET.SubElement(vertex_node, "edges")
        
        if edges_node.find(f"edge[@vertexkey='{v_in_str}']") is None:
            ET.SubElement(edges_node, "edge", {"vertexkey": v_in_str})
            print(f"  -> Conectado: {desc}")

csv_comp = root.find(".//component[@name='DataCDT']")
csv_keys = {}
if csv_comp is not None:
    for entry in csv_comp.findall(".//entry"):
        name = entry.attrib.get('name')
        outkey = entry.attrib.get('outkey')
        if name and outkey:
            csv_keys[name] = outkey

xbrl_comp = root.find(".//component[@name='gl-plt-all-2015-03-25']")
entry_detail_out = None
if xbrl_comp is not None:
    ed = xbrl_comp.find(".//entry[@name='entryDetail']")
    if ed is not None:
        entry_detail_out = get_or_create_key(ed, 'outkey')

json_comp = root.find(".//component[@name='sunder_zachman_dfrnt_instances_m1']")
if json_comp is not None:
    obj_entry = json_comp.find(".//entry[@name='object']")
    if obj_entry is not None:
        json_obj_in = get_or_create_key(obj_entry, 'inpkey')
        add_edge(entry_detail_out, json_obj_in, "Iterador: entryDetail -> JSON object")
        
        # Inyectar el nodo anyOf7 (ACTUS_Contract)
        anyOf7 = obj_entry.find("entry[@name='anyOf7']")
        if anyOf7 is None:
            anyOf7 = ET.SubElement(obj_entry, 'entry', {'name': 'anyOf7', 'type': 'json-subtype', 'expanded': '1'})
            
        anyOf7_in = get_or_create_key(anyOf7, 'inpkey')
        add_edge(entry_detail_out, anyOf7_in, "Iterador: entryDetail -> ACTUS_Contract (anyOf7)")
        
        def add_json_prop(parent, prop_name, prop_type='string', csv_key_name=None):
            prop = parent.find(f"entry[@name='{prop_name}']")
            if prop is None:
                prop = ET.SubElement(parent, 'entry', {'name': prop_name, 'type': 'json-property', 'expanded': '1'})
            
            val_node = prop.find(f"entry[@name='{prop_type}']")
            if val_node is None:
                val_node = ET.SubElement(prop, 'entry', {'name': prop_type})
                
            inpkey = get_or_create_key(val_node, 'inpkey')
            if csv_key_name and csv_key_name in csv_keys:
                add_edge(csv_keys[csv_key_name], inpkey, f"ACTUS: {csv_key_name} -> {prop_name}")
                
        print("\nMapeando variables ACTUS al JSON-LD:")
        add_json_prop(anyOf7, '@id', 'string', 'actus_ContractID')
        add_json_prop(anyOf7, 'actus_ContractType', 'string', 'actus_ContractType')
        add_json_prop(anyOf7, 'actus_NotionalPrincipal', 'number', 'actus_NotionalPrincipal')
        add_json_prop(anyOf7, 'actus_NominalInterestRate', 'number', 'actus_NominalInterestRate')
        add_json_prop(anyOf7, 'actus_InitialExchangeDate', 'string', 'actus_InitialExchangeDate')
        add_json_prop(anyOf7, 'actus_MaturityDate', 'string', 'actus_MaturityDate')

tree.write(mfd_path, encoding='UTF-8', xml_declaration=True)
print("\n¡Grafo inyectado en MapForce exitosamente!")
