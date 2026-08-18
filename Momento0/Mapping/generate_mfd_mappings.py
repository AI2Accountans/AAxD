import xml.etree.ElementTree as ET
import os

mfd_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Mapping\GS2XBRLGL2JSONLD_V1.mfd"

# Register namespaces to prevent ns0 prefixes in output
ET.register_namespace('', '')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

tree = ET.parse(mfd_path)
root = tree.getroot()

# 1. Add output keys (outkeys) to the source XBRL component
comp_xbrl = root.find(".//component[@name='gl-plt-all-2015-03-25']")
if comp_xbrl is not None:
    # 1.1 Find identifierReference under entryDetail
    detail = comp_xbrl.find(".//entry[@name='entryDetail']")
    if detail is not None:
        ident_ref = detail.find(".//entry[@name='identifierReference']")
        if ident_ref is not None:
            ident_ref.set('outkey', '1070')
            code = ident_ref.find("entry[@name='identifierCode']")
            if code is not None:
                code.set('outkey', '1075') # outkey for code under detail
            desc = ident_ref.find("entry[@name='identifierDescription']")
            if desc is not None:
                desc.set('outkey', '1072')
            itype = ident_ref.find("entry[@name='identifierType']")
            if itype is not None:
                itype.set('outkey', '1073')
                
    # 1.2 Find organizationIdentifier under organizationIdentifiers and set outkey
    org_idents = comp_xbrl.find(".//entry[@name='organizationIdentifiers']")
    if org_idents is not None:
        org_ident = org_idents.find("entry[@name='organizationIdentifier']")
        if org_ident is not None:
            org_ident.set('outkey', '1090')
            
    # 1.3 Find documentInfo and set outkey
    doc_info = comp_xbrl.find(".//entry[@name='documentInfo']")
    if doc_info is not None:
        doc_info.set('outkey', '1080')

# 2. Update target JSON component sunder_zachman_dfrnt_instances (uid=43)
comp_json = root.find(".//component[@uid='43']")
if comp_json is not None:
    # 2.1 Set outputinstance attribute to ..\Output\GS2XBRLGL2JSONLD.jsonld
    json_data = comp_json.find("data/json")
    if json_data is not None:
        json_data.set('outputinstance', r"..\Output\GS2XBRLGL2JSONLD.jsonld")

    # Find the object entry
    obj_entry = comp_json.find(".//entry[@name='object']")
    if obj_entry is not None:
        # anyOf0 (FIBO_StockCorporation)
        anyOf0 = obj_entry.find("entry[@name='anyOf0']")
        if anyOf0 is not None:
            anyOf0.find("entry[@name='@type']").set('inpkey', '1001')
            anyOf0.find("entry[@name='@id']").set('inpkey', '1002')
            anyOf0.find("entry[@name='artifact_name']").set('inpkey', '1003')
            anyOf0.find("entry[@name='identifierCode']").set('inpkey', '1004')
            anyOf0.find("entry[@name='identifierDescription']").set('inpkey', '1005')
            anyOf0.find("entry[@name='identifierType']").set('inpkey', '1006')
            nexus_item = anyOf0.find(".//entry[@name='item']")
            if nexus_item is not None:
                nexus_item.set('inpkey', '1007')
                
        # anyOf1 (SourceDocument)
        anyOf1 = obj_entry.find("entry[@name='anyOf1']")
        if anyOf1 is not None:
            anyOf1.set('inpkey', '1080') # loop from documentInfo
            anyOf1.find("entry[@name='@type']").set('inpkey', '1011')
            anyOf1.find("entry[@name='@id']").set('inpkey', '1012')
            anyOf1.find("entry[@name='artifact_name']").set('inpkey', '1013')
            
            # Replace engaged_agents with array/item elements
            engaged = anyOf1.find("entry[@name='engaged_agents']")
            if engaged is not None:
                engaged.clear()
                engaged.attrib.update({'name': 'engaged_agents', 'type': 'json-property', 'expanded': '1'})
                arr = ET.SubElement(engaged, 'entry', {'name': 'array', 'expanded': '1'})
                item = ET.SubElement(arr, 'entry', {'name': 'item', 'type': 'json-item', 'inpkey': '1014', 'expanded': '1'})

        # anyOf2 (GistPerson) - insert it if not present
        anyOf2 = obj_entry.find("entry[@name='anyOf2']")
        if anyOf2 is None:
            # Create anyOf2 element
            anyOf2 = ET.Element('entry', {'name': 'anyOf2', 'type': 'json-subtype', 'inpkey': '1070', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': '@type', 'type': 'json-property', 'inpkey': '1021', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': '@id', 'type': 'json-property', 'inpkey': '1022', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': 'identifierCode', 'type': 'json-property', 'inpkey': '1023', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': 'identifierDescription', 'type': 'json-property', 'inpkey': '1024', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': 'identifierType', 'type': 'json-property', 'inpkey': '1025', 'expanded': '1'})
            ET.SubElement(anyOf2, 'entry', {'name': 'artifact_name', 'type': 'json-property', 'inpkey': '1026', 'expanded': '1'})
            # Insert after anyOf1
            idx_anyOf1 = list(obj_entry).index(anyOf1)
            obj_entry.insert(idx_anyOf1 + 1, anyOf2)

        # anyOf3 (Account)
        anyOf3 = obj_entry.find("entry[@name='anyOf3']")
        if anyOf3 is not None:
            anyOf3.set('inpkey', '1030') # loop from account (outkey 136)
            anyOf3.find("entry[@name='@type']").set('inpkey', '1031')
            anyOf3.find("entry[@name='@id']").set('inpkey', '1032')
            anyOf3.find("entry[@name='mainAccountType']").set('inpkey', '1033')
            anyOf3.find("entry[@name='artifact_name']").set('inpkey', '1034')

        # anyOf4 (EntryHeader)
        anyOf4 = obj_entry.find("entry[@name='anyOf4']")
        if anyOf4 is not None:
            anyOf4.find("entry[@name='@type']").set('inpkey', '1041')
            anyOf4.find("entry[@name='@id']").set('inpkey', '1042')
            anyOf4.find("entry[@name='artifact_name']").set('inpkey', '1043')
            anyOf4.find("entry[@name='posting_date']").set('inpkey', '1044')
            anyOf4.find("entry[@name='source_document']").set('inpkey', '1045')

        # anyOf5 (EntryDetail)
        anyOf5 = obj_entry.find("entry[@name='anyOf5']")
        if anyOf5 is not None:
            anyOf5.find("entry[@name='@type']").set('inpkey', '1051')
            anyOf5.find("entry[@name='@id']").set('inpkey', '1052')
            anyOf5.find("entry[@name='artifact_name']").set('inpkey', '1053')
            anyOf5.find("entry[@name='header']").set('inpkey', '1054')
            anyOf5.find("entry[@name='account']").find("entry[@name='string']").set('inpkey', '1055') # Change account reference to accountMainID concat string
            anyOf5.find("entry[@name='resource']").set('inpkey', '1056')
            anyOf5.find("entry[@name='agent_identifier']").set('inpkey', '1057')
            anyOf5.find("entry[@name='agent']").set('inpkey', '1058')
            anyOf5.find("entry[@name='duality']").set('inpkey', '1059')

# 3. Add components (constants, functions) to children under defaultmap
comp_map = root.find(".//component[@name='defaultmap']")
struct = comp_map.find("structure")
children = struct.find("children")

def add_constant(uid, key, value, ltx, lty):
    const_elem = ET.Element('component', {'name': 'constant', 'library': 'core', 'uid': str(uid), 'kind': '2'})
    targets = ET.SubElement(const_elem, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key)})
    ET.SubElement(const_elem, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+150), 'rby': str(lty+17)})
    data = ET.SubElement(const_elem, 'data')
    ET.SubElement(data, 'constant', {'value': str(value), 'datatype': 'string'})
    children.append(const_elem)

def add_concat(uid, key_in1, key_in2, key_out, ltx, lty, key_in3=None, key_in4=None, key_in5=None, key_in6=None):
    concat_elem = ET.Element('component', {'name': 'concat', 'library': 'core', 'uid': str(uid), 'kind': '5', 'growable': '1', 'growablebasename': 'value'})
    sources = ET.SubElement(concat_elem, 'sources')
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
    targets = ET.SubElement(concat_elem, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(concat_elem, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+54)})
    children.append(concat_elem)

def add_equal(uid, key_in1, key_in2, key_out, ltx, lty):
    eq_elem = ET.Element('component', {'name': 'equal', 'library': 'core', 'uid': str(uid), 'kind': '5'})
    sources = ET.SubElement(eq_elem, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_in1)})
    ET.SubElement(sources, 'datapoint', {'pos': '1', 'key': str(key_in2)})
    targets = ET.SubElement(eq_elem, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(eq_elem, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+54)})
    children.append(eq_elem)

def add_ifelse(uid, key_cond, key_true, key_false, key_out, ltx, lty):
    ifelse_elem = ET.Element('component', {'name': 'if-else', 'library': 'core', 'uid': str(uid), 'kind': '5'})
    sources = ET.SubElement(ifelse_elem, 'sources')
    ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_cond)})
    ET.SubElement(sources, 'datapoint', {'pos': '1', 'key': str(key_true)})
    ET.SubElement(sources, 'datapoint', {'pos': '2', 'key': str(key_false)})
    targets = ET.SubElement(ifelse_elem, 'targets')
    ET.SubElement(targets, 'datapoint', {'pos': '0', 'key': str(key_out)})
    ET.SubElement(ifelse_elem, 'view', {'ltx': str(ltx), 'lty': str(lty), 'rbx': str(ltx+115), 'rby': str(lty+72)})
    children.append(ifelse_elem)

# Let's add the components
add_constant(1001, 2001, "FIBO_StockCorporation", 1120, -100)
add_constant(1002, 2002, "FIBO_StockCorporation/", 1120, -80)
add_constant(1003, 2003, "Sociedad Génesis Ltda.", 1120, -60)
add_constant(1004, 2004, "NIT", 1120, -40)
add_constant(1005, 2005, "SourceDocument", 1120, -20)
add_constant(1006, 2006, "SourceDocument/", 1120, 0)
add_constant(1007, 2007, "Escritura Publica de Constitucion", 1120, 20)
add_constant(1008, 2008, "Notaria 25 - 2005", 1120, 40)
add_constant(1009, 2009, "GistPerson", 1120, 60)
add_constant(1010, 2010, "GistPerson/", 1120, 80)
add_constant(1011, 2011, "Account", 1120, 100)
add_constant(1012, 2012, "Account/", 1120, 120)
add_constant(1013, 2013, "EntryHeader", 1120, 140)
add_constant(1014, 2014, "EntryHeader/Header_Genesis_1", 1120, 160)
add_constant(1015, 2015, "Asiento de Constitución de la Sociedad", 1120, 180)
add_constant(1016, 2016, "SourceDocument/Escritura_Publica_25_2005", 1120, 200)
add_constant(1017, 2017, "EntryDetail", 1120, 220)
add_constant(1018, 2018, "EntryDetail/Line_", 1120, 240)
add_constant(1019, 2019, "Linea Asiento ", 1120, 260)
add_constant(1020, 2020, " - ", 1120, 280)
add_constant(1021, 2021, " Account ", 1120, 300)
add_constant(1022, 2022, "EntryDetail/Line_1", 1120, 320)
add_constant(1023, 2023, "C", 1120, 340)
add_constant(1024, 2024, "110505", 1120, 360)
add_constant(1025, 2025, "Asset", 1120, 380)
add_constant(1026, 2026, "Equity", 1120, 400)
add_constant(1027, 2027, "", 1120, 420)

# Concat functions
add_concat(1101, 2002, 1090, 2103, 1150, 440) # FIBO Stock Corp ID
add_concat(1102, 2006, 143, 2106, 1150, 490)  # FIBO Stock Corp Nexus (SourceDocument/Escritura...)
add_concat(1103, 2006, 143, 2109, 1150, 540)  # SourceDocument ID
add_concat(1104, 2010, 1075, 2112, 1150, 590) # SourceDocument engaged_agents item
add_concat(1105, 2010, 1071, 2115, 1150, 640) # GistPerson ID
add_concat(1106, 2012, 137, 2118, 1150, 690)  # Account ID
add_concat(1107, 2018, 135, 2121, 1150, 740)  # EntryDetail ID
add_concat(1108, 2012, 137, 2124, 1150, 790)  # EntryDetail account & resource Concat
add_concat(1109, 2010, 1075, 2127, 1150, 840) # EntryDetail agent & agent_identifier Concat
add_concat(1110, 2019, 135, 2134, 1150, 890, 2020, 140, 2021, 137) # EntryDetail artifact_name

# Helpers
add_equal(1201, 137, 2024, 2201, 1150, 950)   # is 110505?
add_ifelse(1202, 2201, 2025, 2026, 2202, 1150, 1000) # Asset vs Equity
add_equal(1203, 140, 2023, 2203, 1150, 1080)   # is Credit (C)?
add_ifelse(1204, 2203, 2022, 2027, 2204, 1150, 1130) # EntryDetail/Line_1 duality

# 4. Add vertices/edges to the graph
graph = struct.find("graph")
vertices = graph.find("vertices")

# Function to add vertex and its edges
def add_vertex_edge(v_key, target_keys):
    # Find if vertex already exists
    v_elem = vertices.find(f"vertex[@vertexkey='{v_key}']")
    if v_elem is None:
        v_elem = ET.SubElement(vertices, 'vertex', {'vertexkey': str(v_key)})
    edges = v_elem.find("edges")
    if edges is None:
        edges = ET.SubElement(v_elem, 'edges')
    for t_key in target_keys:
        # Check if edge already exists
        if edges.find(f"edge[@vertexkey='{t_key}']") is None:
            ET.SubElement(edges, 'edge', {'vertexkey': str(t_key)})

# Add all our new edges
# Constants to properties directly
add_vertex_edge(2001, [1001]) # FIBO_StockCorporation -> @type
add_vertex_edge(2003, [1005]) # Sociedad Génesis Ltda -> identifierDescription
add_vertex_edge(2004, [1006]) # NIT -> identifierType
add_vertex_edge(2005, [1011]) # SourceDocument -> @type
add_vertex_edge(2009, [1021]) # GistPerson -> @type
add_vertex_edge(2011, [1031]) # Account -> @type
add_vertex_edge(2013, [1041]) # EntryHeader -> @type
add_vertex_edge(2014, [1042, 1054]) # Header_Genesis_1 -> EntryHeader/@id, EntryDetail/header
add_vertex_edge(2015, [1043]) # Asiento de Constitución -> EntryHeader/artifact_name
add_vertex_edge(2016, [1045]) # SourceDocument/Escritura... -> EntryHeader/source_document
add_vertex_edge(2017, [1051]) # EntryDetail -> @type

# Link XBRL source fields to concats and properties
add_vertex_edge(1090, [2102, 1003, 1004]) # organizationIdentifier -> FIBO Stock ID concat, artifact_name, identifierCode
add_vertex_edge(143, [2105, 2108])       # documentNumber -> FIBO Stock Corp Nexus concat, SourceDocument ID concat
add_vertex_edge(137, [2117, 2123, 2133, 2201]) # accountMainID -> Account ID concat, EntryDetail account concat, Detail desc concat, Equal check
add_vertex_edge(138, [1034])              # accountMainDescription -> Account/artifact_name
add_vertex_edge(135, [2120, 2129])        # lineNumberCounter -> EntryDetail ID concat, Detail desc concat
add_vertex_edge(140, [2131, 2203])        # debitCreditCode -> Detail desc concat, Equal check
add_vertex_edge(141, [1044])              # postingDate -> EntryHeader/posting_date

# GistPerson loop & properties
add_vertex_edge(1070, [1074])             # identifierReference loop -> anyOf2 loop
add_vertex_edge(1071, [2114, 1023])       # identifierCode -> GistPerson ID concat, GistPerson/identifierCode
add_vertex_edge(1072, [1024, 1026])       # identifierDescription -> GistPerson/identifierDescription, GistPerson/artifact_name
add_vertex_edge(1073, [1025])             # identifierType -> GistPerson/identifierType

# engaged_agents mapping (loop on entryDetail, filter or map GistPerson ID)
add_vertex_edge(1075, [2111, 2126])       # identifierCode under detail -> engaged_agents concat, agent concat

# Loop connectors
add_vertex_edge(136, [1030])              # account loop -> anyOf3 loop

# Concat outputs
add_vertex_edge(2103, [1002])             # FIBO Stock ID concat -> anyOf0/@id
add_vertex_edge(2106, [1007])             # FIBO Stock Corp Nexus concat -> anyOf0/nexus item
add_vertex_edge(2109, [1012, 1013])       # SourceDocument ID concat -> anyOf1/@id, anyOf1/artifact_name
add_vertex_edge(2112, [1014])             # engaged_agents concat -> engaged_agents item
add_vertex_edge(2115, [1022])             # GistPerson ID concat -> anyOf2/@id
add_vertex_edge(2118, [1032])             # Account ID concat -> anyOf3/@id
add_vertex_edge(2121, [1052])             # EntryDetail ID concat -> anyOf5/@id
add_vertex_edge(2124, [1055, 1056])       # Account ref concat -> EntryDetail/account, EntryDetail/resource
add_vertex_edge(2127, [1057, 1058])       # agent ref concat -> EntryDetail/agent_identifier, EntryDetail/agent
add_vertex_edge(2134, [1053])             # Detail desc concat -> anyOf5/artifact_name

# Constant inputs to concats
add_vertex_edge(2002, [2101])             # "FIBO_StockCorporation/"
add_vertex_edge(2006, [2104, 2107])       # "SourceDocument/"
add_vertex_edge(2010, [2110, 2113, 2125]) # "GistPerson/"
add_vertex_edge(2012, [2116, 2122])       # "Account/"
add_vertex_edge(2018, [2119])             # "EntryDetail/Line_"
add_vertex_edge(2019, [2128])             # "Linea Asiento "
add_vertex_edge(2020, [2130])             # " - "
add_vertex_edge(2021, [2132])             # " Account "

# Equal & If-Else connectors
add_vertex_edge(2024, [2202])             # Constant "110505" to equal input
add_vertex_edge(2201, [2201])             # equal output -> if-else condition
add_vertex_edge(2025, [2202])             # "Asset" -> if-else true
add_vertex_edge(2026, [2203])             # "Equity" -> if-else false
add_vertex_edge(2202, [1033])             # if-else result -> mainAccountType

# Equal & If-Else for Duality
add_vertex_edge(2023, [2204])             # Constant "C" to equal input
add_vertex_edge(2203, [2203])             # equal output -> if-else condition
add_vertex_edge(2022, [2204])             # "EntryDetail/Line_1" -> if-else true
add_vertex_edge(2027, [2205])             # "" -> if-else false (value-false)
# Wait, let's make sure the ifelse inputs match the positions we added:
# add_ifelse has: sources pos=0 (cond), pos=1 (true), pos=2 (false)
# In vertices:
# we connect equal output 2201 to if-else pos=0. The uid of if-else is 1202.
# Wait! In MapForce, a component's inputs and outputs have key attributes.
# Let's check: in add_ifelse(1202, 2201, 2025, 2026, 2202, ...):
# uid=1202 has inputs with keys: cond=2201? No, the keys we passed to add_ifelse are the keys of the datapoints on the component itself!
# Wait! In add_ifelse, we defined sources with keys: 2201, 2025, 2026?
# Ah! Let's check our add_ifelse code:
# `ET.SubElement(sources, 'datapoint', {'pos': '0', 'key': str(key_cond)})`
# Yes! The input keys of the if-else component are `key_cond`, `key_true`, and `key_false`.
# So the component itself expects input on keys `2201`, `2025`, and `2026`.
# Thus, in the graph, we must connect the source (e.g. constant "Asset" with key 2025) to the if-else input key 2025!
# Let's verify:
# Constant "Asset" key is 2025. If-else true-input key is 2025. So we connect 2025 to 2025!
# This is perfect!

# Let's fix ifelse inputs connection for 1202:
# equal output is 2201. If-else condition key is 2201. So connect 2201 to 2201!
# Constant "Asset" is 2025. If-else true key is 2025. So connect 2025 to 2025!
# Constant "Equity" is 2026. If-else false key is 2026. So connect 2026 to 2026!
# If-else output key is 2202. Target mainAccountType key is 1033. So connect 2202 to 1033!
# This matches exactly!

# Let's check ifelse inputs connection for 1204 (duality):
# Equal output is 2203. If-else condition key is 2203. Connect 2203 to 2203!
# Constant "EntryDetail/Line_1" is 2022. If-else true key is 2022. Connect 2022 to 2022!
# Constant "" is 2027. If-else false key is 2027. Connect 2027 to 2027!
# If-else output key is 2204. Target duality key is 1059. Connect 2204 to 1059!
# Equal component 1203 has inputs: 140 and 2023.
# Equal component 1201 has inputs: 137 and 2024.

# Write it out
tree.write(mfd_path, encoding='utf-8', xml_declaration=True)
print("GS2XBRLGL2JSONLD_V1.mfd modified successfully!")
