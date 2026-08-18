import xml.etree.ElementTree as ET
import os

bak_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd.bak"
mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

ET.register_namespace('', '')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

tree = ET.parse(bak_path)
root = tree.getroot()

comp_map = root.find(".//component[@name='defaultmap']")
struct = comp_map.find("structure")
children = struct.find("children")
graph = struct.find("graph")
vertices = graph.find("vertices")

# 1. Update defaultmap properties SelectedLanguage to builtin
properties = comp_map.find("properties")
if properties is not None:
    properties.set('SelectedLanguage', 'builtin')

# 2. Remove old QName components
to_remove = []
for comp in children.findall("component[@name='QName']"):
    to_remove.append(comp)
for comp in to_remove:
    children.remove(comp)

# 3. Add outkeys to source XBRL component (gl-plt-all-2015-03-25)
comp_xbrl = children.find("component[@name='gl-plt-all-2015-03-25']")
if comp_xbrl is not None:
    detail = comp_xbrl.find(".//entry[@name='entryDetail']")
    if detail is not None:
        ident_ref = detail.find(".//entry[@name='identifierReference']")
        if ident_ref is not None:
            ident_ref.set('outkey', '1070') # GistPerson loop
            code = ident_ref.find("entry[@name='identifierCode']")
            if code is not None:
                code.set('outkey', '1071') # identifierCode outkey
            desc = ident_ref.find("entry[@name='identifierDescription']")
            if desc is not None:
                desc.set('outkey', '1072')
            itype = ident_ref.find("entry[@name='identifierType']")
            if itype is not None:
                itype.set('outkey', '1073')
                
    org_idents = comp_xbrl.find(".//entry[@name='organizationIdentifiers']")
    if org_idents is not None:
        org_ident = org_idents.find("entry[@name='organizationIdentifier']")
        if org_ident is not None:
            org_ident.set('outkey', '1090')
            
    doc_info = comp_xbrl.find(".//entry[@name='documentInfo']")
    if doc_info is not None:
        doc_info.set('outkey', '1080')

# Helper function to clear a property and add its type child 'string' with the inpkey
def set_string_inpkey(parent_node, name, inpkey):
    node = parent_node.find(f"entry[@name='{name}']")
    if node is not None:
        node.clear()
        node.attrib.update({'name': name, 'type': 'json-property', 'expanded': '1'})
        ET.SubElement(node, 'entry', {'name': 'string', 'inpkey': str(inpkey)})

# 4. Update target JSON component (uid=43)
comp_json = children.find("component[@uid='43']")
if comp_json is not None:
    json_data = comp_json.find("data/json")
    if json_data is not None:
        json_data.set('outputinstance', r"..\Output\GS2XBRLGL2JSONLD.jsonld")
        
    obj_entry = comp_json.find(".//entry[@name='object']")
    if obj_entry is not None:
        # anyOf0 (FIBO_StockCorporation)
        anyOf0 = obj_entry.find("entry[@name='anyOf0']")
        if anyOf0 is not None:
            set_string_inpkey(anyOf0, '@type', 1001)
            set_string_inpkey(anyOf0, '@id', 1002)
            set_string_inpkey(anyOf0, 'artifact_name', 1003)
            set_string_inpkey(anyOf0, 'identifierCode', 1004)
            set_string_inpkey(anyOf0, 'identifierDescription', 1005)
            set_string_inpkey(anyOf0, 'identifierType', 1006)
            
            # Array item nexus
            nexus = anyOf0.find("entry[@name='nexus']")
            if nexus is not None:
                nexus.clear()
                nexus.attrib.update({'name': 'nexus', 'type': 'json-property', 'expanded': '1'})
                arr = ET.SubElement(nexus, 'entry', {'name': 'array', 'expanded': '1'})
                item = ET.SubElement(arr, 'entry', {'name': 'item', 'type': 'json-item', 'expanded': '1'})
                ET.SubElement(item, 'entry', {'name': 'string', 'inpkey': '1007'})
                
        # anyOf1 (SourceDocument)
        anyOf1 = obj_entry.find("entry[@name='anyOf1']")
        if anyOf1 is not None:
            anyOf1.set('inpkey', '1081') # loop from documentInfo (target inpkey 1081)
            set_string_inpkey(anyOf1, '@type', 1011)
            set_string_inpkey(anyOf1, '@id', 1012)
            set_string_inpkey(anyOf1, 'artifact_name', 1013)
            
            # Array item engaged_agents
            engaged = anyOf1.find("entry[@name='engaged_agents']")
            if engaged is not None:
                engaged.clear()
                engaged.attrib.update({'name': 'engaged_agents', 'type': 'json-property', 'expanded': '1'})
                arr = ET.SubElement(engaged, 'entry', {'name': 'array', 'expanded': '1'})
                item = ET.SubElement(arr, 'entry', {'name': 'item', 'type': 'json-item', 'expanded': '1'})
                ET.SubElement(item, 'entry', {'name': 'string', 'inpkey': '1014'})

        # anyOf2 (GistPerson)
        anyOf2 = obj_entry.find("entry[@name='anyOf2']")
        if anyOf2 is None:
            anyOf2 = ET.Element('entry', {'name': 'anyOf2', 'type': 'json-subtype', 'inpkey': '1082', 'expanded': '1'})
            # We define properties with child 'string'
            for name, inpkey in [('@type', 1021), ('@id', 1022), ('identifierCode', 1023), ('identifierDescription', 1024), ('identifierType', 1025), ('artifact_name', 1026)]:
                p_node = ET.SubElement(anyOf2, 'entry', {'name': name, 'type': 'json-property', 'expanded': '1'})
                ET.SubElement(p_node, 'entry', {'name': 'string', 'inpkey': str(inpkey)})
            
            idx_anyOf1 = list(obj_entry).index(anyOf1)
            obj_entry.insert(idx_anyOf1 + 1, anyOf2)

        # anyOf3 (Account)
        anyOf3 = obj_entry.find("entry[@name='anyOf3']")
        if anyOf3 is not None:
            anyOf3.set('inpkey', '1083') # loop from account (target inpkey 1083)
            set_string_inpkey(anyOf3, '@type', 1031)
            set_string_inpkey(anyOf3, '@id', 1032)
            set_string_inpkey(anyOf3, 'mainAccountType', 1033)
            set_string_inpkey(anyOf3, 'artifact_name', 1034)

        # anyOf4 (EntryHeader)
        anyOf4 = obj_entry.find("entry[@name='anyOf4']")
        if anyOf4 is not None:
            set_string_inpkey(anyOf4, '@type', 1041)
            set_string_inpkey(anyOf4, '@id', 1042)
            set_string_inpkey(anyOf4, 'artifact_name', 1043)
            set_string_inpkey(anyOf4, 'posting_date', 1044)
            set_string_inpkey(anyOf4, 'source_document', 1045)

        # anyOf5 (EntryDetail)
        anyOf5 = obj_entry.find("entry[@name='anyOf5']")
        if anyOf5 is not None:
            set_string_inpkey(anyOf5, '@type', 1051)
            set_string_inpkey(anyOf5, '@id', 1052)
            set_string_inpkey(anyOf5, 'artifact_name', 1053)
            set_string_inpkey(anyOf5, 'header', 1054)
            
            # account/string
            account_node = anyOf5.find("entry[@name='account']")
            if account_node is not None:
                account_node.find("entry[@name='string']").set('inpkey', '1055')
                
            set_string_inpkey(anyOf5, 'resource', 1056)
            set_string_inpkey(anyOf5, 'agent_identifier', 1057)
            set_string_inpkey(anyOf5, 'agent', 1058)
            set_string_inpkey(anyOf5, 'duality', 1059)

# 5. Add custom components
# Constants (UID 1001-1030, keys 5001-5030)
def add_constant(uid, key, value, ltx, lty):
    c = ET.Element('component', {'name': 'constant', 'library': 'core', 'uid': str(uid), 'kind': '2'})
    targets = ET.SubElement(c, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key)})
    ET.SubElement(c, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+150), 'rby': str(lty+17)})
    data = ET.SubElement(c, 'data')
    ET.SubElement(data, 'constant', {'value': str(value), 'datatype': 'string'})
    children.append(c)

add_constant(1001, 5001, "FIBO_StockCorporation", 1120, -100)
add_constant(1002, 5002, "FIBO_StockCorporation/", 1120, -80)
add_constant(1003, 5003, "Sociedad Génesis Ltda.", 1120, -60)
add_constant(1004, 5004, "NIT", 1120, -40)
add_constant(1005, 5005, "SourceDocument", 1120, -20)
add_constant(1006, 5006, "SourceDocument/", 1120, 0)
add_constant(1009, 5009, "GistPerson", 1120, 60)
add_constant(1010, 5010, "GistPerson/", 1120, 80)
add_constant(1011, 5011, "Account", 1120, 100)
add_constant(1012, 5012, "Account/", 1120, 120)
add_constant(1013, 5013, "EntryHeader", 1120, 140)
add_constant(1014, 5014, "EntryHeader/Header_Genesis_1", 1120, 160)
add_constant(1015, 5015, "Asiento de Constitución de la Sociedad", 1120, 180)
add_constant(1016, 5016, "SourceDocument/Escritura_Publica_25_2005", 1120, 200)
add_constant(1017, 5017, "EntryDetail", 1120, 220)
add_constant(1018, 5018, "EntryDetail/Line_", 1120, 240)
add_constant(1019, 5019, "Linea Asiento ", 1120, 260)
add_constant(1020, 5020, " - ", 1120, 280)
add_constant(1021, 5021, " Account ", 1120, 300)
add_constant(1022, 5022, "EntryDetail/Line_1", 1120, 320)
add_constant(1023, 5023, "C", 1120, 340)
add_constant(1024, 5024, "110505", 1120, 360)
add_constant(1025, 5025, "Asset", 1120, 380)
add_constant(1026, 5026, "Equity", 1120, 400)
add_constant(1027, 5027, "", 1120, 420)
add_constant(1028, 5028, "iso639:es", 1120, 440)
add_constant(1029, 5029, "iso4217:COP", 1120, 460)
add_constant(1030, 5030, "xbrli:shares", 1120, 480)

# Concat functions (UID 1101-1110, keys 5101-5134)
def add_concat(uid, key_in1, key_in2, key_out, ltx, lty, key_in3=None, key_in4=None, key_in5=None, key_in6=None):
    c = ET.Element('component', {'name': 'concat', 'library': 'core', 'uid': str(uid), 'kind': '5', 'growable': '1', 'growablebasename': 'value'})
    sources = ET.SubElement(c, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_in1)})
    ET.SubElement(sources, 'datapoint', {'pos': '1', 'key': str(key_in2)})
    if key_in3 is not None:
        ET.SubElement(sources, 'datapoint', {'pos': '2', 'key': str(key_in3)})
    if key_in4 is not None:
        ET.SubElement(sources, 'datapoint', {'pos': '3', 'key': str(key_in4)})
    if key_in5 is not None:
        ET.SubElement(sources, 'datapoint', {'pos': '4', 'key': str(key_in5)})
    if key_in6 is not None:
        ET.SubElement(sources, 'datapoint', {'pos': '5', 'key': str(key_in6)})
    targets = ET.SubElement(c, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(c, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+54)})
    children.append(c)

add_concat(1101, 5101, 5102, 5103, 1150, 440) # FIBO Stock Corp ID
add_concat(1102, 5104, 5105, 5106, 1150, 490)  # FIBO Stock Corp Nexus
add_concat(1103, 5107, 5108, 5109, 1150, 540)  # SourceDocument ID
add_concat(1104, 5110, 5111, 5112, 1150, 590) # SourceDocument engaged_agents item
add_concat(1105, 5113, 5114, 5115, 1150, 640) # GistPerson ID
add_concat(1106, 5116, 5117, 5118, 1150, 690)  # Account ID
add_concat(1107, 5119, 5120, 5121, 1150, 740)  # EntryDetail ID
add_concat(1108, 5122, 5123, 5124, 1150, 790)  # EntryDetail account & resource Concat
add_concat(1109, 5125, 5126, 5127, 1150, 840) # EntryDetail agent & agent_identifier Concat
add_concat(1110, 5128, 5129, 5134, 1150, 890, 5130, 5131, 5132, 5133) # EntryDetail artifact_name

# Equal functions (UID 1201, 1203, keys 5201-5206)
def add_equal(uid, key_in1, key_in2, key_out, ltx, lty):
    eq = ET.Element('component', {'name': 'equal', 'library': 'core', 'uid': str(uid), 'kind': '5'})
    sources = ET.SubElement(eq, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_in1)})
    ET.SubElement(sources, 'datapoint', {'pos': '1', 'key': str(key_in2)})
    targets = ET.SubElement(eq, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(eq, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+54)})
    children.append(eq)

add_equal(1201, 5201, 5202, 5203, 1150, 950)
add_equal(1203, 5204, 5205, 5206, 1150, 1080)

# If-Else components (UID 1202, 1204, keys 5301-5308, kind="4"!)
def add_ifelse(uid, key_cond, key_true, key_false, key_out, ltx, lty):
    ifelse = ET.Element('component', {'name': 'if-else', 'library': 'core', 'uid': str(uid), 'kind': '4'})
    sources = ET.SubElement(ifelse, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_cond)})
    ET.SubElement(sources, 'datapoint', {'pos': '1', 'key': str(key_true)})
    ET.SubElement(sources, 'datapoint', {'pos': '2', 'key': str(key_false)})
    targets = ET.SubElement(ifelse, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(ifelse, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+72)})
    children.append(ifelse)

add_ifelse(1202, 5301, 5302, 5303, 5304, 1150, 1000)
add_ifelse(1204, 5305, 5306, 5307, 5308, 1150, 1130)

# first-items components (UID 1301-1303, keys 5401-5406)
def add_first_items(uid, key_in, key_out, ltx, lty):
    fi = ET.Element('component', {'name': 'first-items', 'library': 'core', 'uid': str(uid), 'kind': '5'})
    sources = ET.SubElement(fi, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_in)})
    targets = ET.SubElement(fi, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(fi, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+54)})
    children.append(fi)

add_first_items(1301, 5401, 5402, 1150, -400) # first-items for documentType
add_first_items(1302, 5403, 5404, 1150, -350) # first-items for documentNumber
add_first_items(1303, 5405, 5406, 1150, -300) # first-items for documentDate
add_first_items(1304, 5407, 5408, 1150, -250) # first-items for postingDate

# 6. Rebuild graph vertices/edges
# 6.1 Clean up old QName vertices/edges
keys_to_remove = {'120', '121', '122', '124', '125', '126', '127', '128', '129'}
vertices_to_remove = []
for v in vertices.findall("vertex"):
    v_key = v.attrib.get('vertexkey')
    if v_key in keys_to_remove:
        vertices_to_remove.append(v)
    else:
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

keys_with_edges_to_clean = {'97', '123', '99', '130', '131'}
for v_key in keys_with_edges_to_clean:
    v = vertices.find(f"vertex[@vertexkey='{v_key}']")
    if v is not None:
        edges = v.find("edges")
        if edges is not None:
            for e in list(edges):
                if e.attrib.get('vertexkey') in keys_to_remove:
                    edges.remove(e)
            if len(list(edges)) == 0:
                vertices.remove(v)

# 6.2 Clean up the loop and obsolete connections of target JSON component
# Remove edge 153 from vertex 134 (since we changed anyOf1 loop to 1081)
v_134 = vertices.find("vertex[@vertexkey='134']")
if v_134 is not None:
    edges = v_134.find("edges")
    if edges is not None:
        e_153 = edges.find("edge[@vertexkey='153']")
        if e_153 is not None:
            edges.remove(e_153)

# Remove edge 162 from vertex 136 (since we changed account ref key to 1055)
v_136 = vertices.find("vertex[@vertexkey='136']")
if v_136 is not None:
    edges = v_136.find("edges")
    if edges is not None:
        e_162 = edges.find("edge[@vertexkey='162']")
        if e_162 is not None:
            edges.remove(e_162)

# Remove original direct connections from 142 -> 154, 143 -> 155, 144 -> 156
for vk in ['142', '143', '144']:
    v = vertices.find(f"vertex[@vertexkey='{vk}']")
    if v is not None:
        edges = v.find("edges")
        if edges is not None:
            for target_key in ['154', '155', '156']:
                e = edges.find(f"edge[@vertexkey='{target_key}']")
                if e is not None:
                    edges.remove(e)

# 6.3 Add all new edges for our custom components
def add_vertex_edge(v_key, target_keys):
    v_elem = vertices.find(f"vertex[@vertexkey='{v_key}']")
    if v_elem is None:
        v_elem = ET.SubElement(vertices, 'vertex', {'vertexkey': str(v_key)})
    edges = v_elem.find("edges")
    if edges is None:
        edges = ET.SubElement(v_elem, 'edges')
    for t_key in target_keys:
        if edges.find(f"edge[@vertexkey='{t_key}']") is None:
            ET.SubElement(edges, 'edge', {'vertexkey': str(t_key)})

# Connect constants
add_vertex_edge(5001, [1001]) # FIBO_StockCorporation -> type
add_vertex_edge(5002, [5101]) # FIBO_StockCorporation/ -> concat_fibo_id
add_vertex_edge(5003, [1005]) # Sociedad Génesis Ltda -> anyOf0/identifierDescription
add_vertex_edge(5004, [1006]) # NIT -> anyOf0/identifierType
add_vertex_edge(5005, [1011]) # SourceDocument -> anyOf1/@type
add_vertex_edge(5006, [5104, 5107]) # SourceDocument/ -> concats
add_vertex_edge(5009, [1021]) # GistPerson -> anyOf2/@type
add_vertex_edge(5010, [5110, 5113, 5125]) # GistPerson/ -> concats
add_vertex_edge(5011, [1031]) # Account -> anyOf3/@type
add_vertex_edge(5012, [5116, 5122]) # Account/ -> concats
add_vertex_edge(5013, [1041]) # EntryHeader -> anyOf4/@type
add_vertex_edge(5014, [1042, 1054]) # Header_Genesis_1 -> EntryHeader/@id, EntryDetail/header
add_vertex_edge(5015, [1043]) # Asiento... -> EntryHeader/artifact_name
add_vertex_edge(5016, [1045]) # SourceDocument/Escritura... -> EntryHeader/source_document
add_vertex_edge(5017, [1051]) # EntryDetail -> anyOf5/@type
add_vertex_edge(5018, [5119]) # EntryDetail/Line_ -> concat
add_vertex_edge(5019, [5128]) # Linea Asiento  -> concat
add_vertex_edge(5020, [5130]) #  -  -> concat
add_vertex_edge(5021, [5132]) #  Account  -> concat
add_vertex_edge(5022, [5306]) # EntryDetail/Line_1 -> ifelse true
add_vertex_edge(5023, [5205]) # C -> equal credit
add_vertex_edge(5024, [5202]) # 110505 -> equal cash
add_vertex_edge(5025, [5302]) # Asset -> ifelse true
add_vertex_edge(5026, [5303]) # Equity -> ifelse false
add_vertex_edge(5027, [5307]) # empty -> ifelse false
add_vertex_edge(5028, [103])  # iso639:es -> language
add_vertex_edge(5029, [109])  # iso4217:COP -> defaultCurrency
add_vertex_edge(5030, [92])   # xbrli:shares -> measure

# Connect XBRL sources to first-items (to resolve sequence cardinality issue)
add_vertex_edge(142, [5401]) # documentType -> first_doc_type input
add_vertex_edge(143, [5403]) # documentNumber -> first_doc_num input
add_vertex_edge(144, [5405]) # documentDate -> first_doc_date input

# Connect first-items outputs to target JSON fields and concats
add_vertex_edge(5402, [154]) # first documentType -> anyOf1/documentType/string
add_vertex_edge(5404, [155, 5105, 5108, 1013]) # first documentNumber -> target documentNumber, fibo stock corp nexus, SourceDocument ID concat, artifact_name
add_vertex_edge(5406, [156]) # first documentDate -> anyOf1/documentDate/string

# Connect remaining XBRL sources
add_vertex_edge(1090, [5102, 1003, 1004]) # organizationIdentifier -> concat, artifact_name, identifierCode
add_vertex_edge(1071, [5111, 5126, 5114, 1023]) # identifierCode -> concats, GistPerson code
add_vertex_edge(1072, [1024, 1026])        # identifierDescription -> GistPerson description, artifact_name
add_vertex_edge(1073, [1025])              # identifierType -> GistPerson identifierType
add_vertex_edge(137, [5117, 5123, 5133, 5201]) # accountMainID -> concats, equal
add_vertex_edge(138, [1034])               # accountMainDescription -> Account/artifact_name
add_vertex_edge(141, [5407, 165])          # postingDate -> first-items input, Detail postingDate
add_vertex_edge(5408, [1044])              # first postingDate -> EntryHeader posting_date
add_vertex_edge(135, [5120, 5129])         # lineNumberCounter -> concats
add_vertex_edge(140, [5131, 5204])         # debitCreditCode -> concat, equal

# Connect loop sources
add_vertex_edge(132, [152]) # organizationIdentifiers loop
add_vertex_edge(1080, [1081]) # documentInfo loop -> anyOf1 loop
add_vertex_edge(1070, [1082]) # identifierReference loop -> anyOf2 loop
add_vertex_edge(136, [1083])  # account loop -> anyOf3 loop

# Connect concat outputs
add_vertex_edge(5103, [1002]) # FIBO Stock Corp ID
add_vertex_edge(5106, [1007]) # FIBO Stock Corp Nexus
add_vertex_edge(5109, [1012]) # SourceDocument ID
add_vertex_edge(5112, [1014]) # SourceDocument engaged_agents
add_vertex_edge(5115, [1022]) # GistPerson ID
add_vertex_edge(5118, [1032]) # Account ID
add_vertex_edge(5121, [1052]) # EntryDetail ID
add_vertex_edge(5124, [1055, 1056]) # Detail account, resource
add_vertex_edge(5127, [1057, 1058]) # Detail agent, agent_identifier
add_vertex_edge(5134, [1053]) # Detail desc

# Connect equal outputs to ifelse condition inputs
add_vertex_edge(5203, [5301]) # eq_cash output -> ifelse condition
add_vertex_edge(5206, [5305]) # eq_credit output -> ifelse condition

# Connect ifelse outputs
add_vertex_edge(5304, [1033]) # mainAccountType
add_vertex_edge(5308, [1059]) # duality

tree.write(mfd_path, encoding='utf-8', xml_declaration=True)
print("Cleanly rebuilt mapping file with string type nodes for JSON target component!")
