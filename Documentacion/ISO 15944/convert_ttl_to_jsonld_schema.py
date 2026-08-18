import os
import json
import re

def convert_ttl_to_schemas():
    ttl_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\ISO 15944\ontologias\valueflows_all_vf.ttl"
    out_dir = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\ISO 15944\ontologias"
    
    with open(ttl_path, "r", encoding="utf-8") as f:
        ttl_content = f.read()

    # Extract all classes and properties defined in valueflows
    classes = re.findall(r'vf:(\w+)\s+a\s+owl:Class', ttl_content)
    properties = re.findall(r'vf:(\w+)\s+a\s+owl:(?:ObjectProperty|DatatypeProperty)', ttl_content)
    
    classes = sorted(list(set(classes)))
    properties = sorted(list(set(properties)))
    
    print(f"[*] Found {len(classes)} classes and {len(properties)} properties in Valueflows TTL.")

    # 1. Generate JSON-LD @context
    context_dict = {
        "@context": {
            "vf": "https://w3id.org/valueflows/ont/vf#",
            "owl": "http://www.w3.org/2002/07/owl#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "xsd": "http://www.w3.org/2001/XMLSchema#"
        }
    }
    
    for cls in classes:
        context_dict["@context"][cls] = f"vf:{cls}"
    for prop in properties:
        context_dict["@context"][prop] = {"@id": f"vf:{prop}"}
        
    jsonld_context_path = os.path.join(out_dir, "valueflows_context.jsonld")
    with open(jsonld_context_path, "w", encoding="utf-8") as f:
        json.dump(context_dict, f, indent=2)
    print(f"[✓] Generated JSON-LD Context: {jsonld_context_path}")

    # 2. Generate JSON Schema (for Altova XMLSpy / MapForce JSON Schema Viewer)
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Valueflows JSON Schema (Derived from TTL)",
        "description": "JSON Schema representation of Valueflows ontology for Altova XMLSpy / MapForce",
        "type": "object",
        "properties": {
            "@context": { "type": ["object", "string"] },
            "@id": { "type": "string" },
            "@type": {
                "type": "array",
                "items": { "type": "string" }
            }
        },
        "definitions": {}
    }
    
    for cls in classes:
        json_schema["definitions"][cls] = {
            "type": "object",
            "properties": {
                "@id": { "type": "string" },
                "@type": { "const": f"vf:{cls}" }
            }
        }
        
    json_schema_path = os.path.join(out_dir, "valueflows_schema.json")
    with open(json_schema_path, "w", encoding="utf-8") as f:
        json.dump(json_schema, f, indent=2)
    print(f"[✓] Generated JSON Schema: {json_schema_path}")

    # 3. Generate XSD (XML Schema for Altova StyleVision / MapForce)
    xsd_content = ['<?xml version="1.0" encoding="UTF-8"?>',
                   '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"',
                   '           targetNamespace="https://w3id.org/valueflows/ont/vf#"',
                   '           xmlns:vf="https://w3id.org/valueflows/ont/vf#"',
                   '           elementFormDefault="qualified">',
                   '']
    
    for cls in classes:
        xsd_content.append(f'  <xs:element name="{cls}">')
        xsd_content.append('    <xs:complexType>')
        xsd_content.append('      <xs:sequence>')
        xsd_content.append('        <xs:element name="id" type="xs:string" minOccurs="0"/>')
        for prop in properties[:10]: # Include common properties
            xsd_content.append(f'        <xs:element name="{prop}" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>')
        xsd_content.append('      </xs:sequence>')
        xsd_content.append('    </xs:complexType>')
        xsd_content.append('  </xs:element>')
    
    xsd_content.append('</xs:schema>')
    
    xsd_path = os.path.join(out_dir, "valueflows_schema.xsd")
    with open(xsd_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xsd_content))
    print(f"[✓] Generated XSD Schema: {xsd_path}")

if __name__ == "__main__":
    convert_ttl_to_schemas()
