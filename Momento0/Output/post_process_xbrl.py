import os
import sys
from lxml import etree

def main():
    # Paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = os.path.join(script_dir, "GS2XBRLGL2JSONLD.xbrl")
    schema_path = os.path.join(script_dir, "..", "Taxonomy", "gl", "plt", "case-c-b-m-u-t-s", "gl-plt-all-2015-03-25.xsd")
    
    if not os.path.exists(xml_path):
        print(f"Error: Output file not found at {xml_path}")
        sys.exit(1)
        
    print(f"Post-processing file: {xml_path}")
    
    # Parse the XML
    parser = etree.XMLParser(remove_blank_text=True)
    doc = etree.parse(xml_path, parser)
    root = doc.getroot()
    
    # Namespaces
    ns = {
        "xbrli": "http://www.xbrl.org/2003/instance",
        "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25",
        "gl-bus": "http://www.xbrl.org/int/gl/bus/2015-03-25",
        "gl-muc": "http://www.xbrl.org/int/gl/muc/2015-03-25"
    }
    
    # Create new root with injected namespaces natively
    new_nsmap = root.nsmap.copy()
    new_nsmap["iso639"] = "http://www.xbrl.org/2005/iso639"
    new_nsmap["iso4217"] = "http://www.xbrl.org/2003/iso4217"
    
    new_root = etree.Element(root.tag, attrib=root.attrib, nsmap=new_nsmap)
    for child in list(root):
        new_root.append(child)
    doc._setroot(new_root)
    root = new_root
    
    # Check if unit "Shares" exists, if not create it
    shares_unit = root.find(".//xbrli:unit[@id='Shares']", ns)
    if shares_unit is None:
        print("-> Creating unit 'Shares'...")
        shares_unit = etree.Element(f"{{{ns['xbrli']}}}unit")
        shares_unit.set("id", "Shares")
        measure = etree.SubElement(shares_unit, f"{{{ns['xbrli']}}}measure")
        measure.text = "xbrli:shares"
        
        # Insert shares_unit after existing units or at the beginning of root
        units = root.findall(".//xbrli:unit", ns)
        if units:
            units[-1].addnext(shares_unit)
        else:
            root.insert(0, shares_unit)
            
    # Check if documentInfo exists under accountingEntries, if not create it
    ae = root.find(".//gl-cor:accountingEntries", ns)
    if ae is not None:
        doc_info = ae.find(".//gl-cor:documentInfo", ns)
        if doc_info is None:
            print("-> Creating documentInfo header...")
            doc_info = etree.Element(f"{{{ns['gl-cor']}}}documentInfo")
            
            entries_type = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}entriesType")
            entries_type.set("contextRef", "ctx1")
            entries_type.text = "other"
            
            unique_id = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}uniqueID")
            unique_id.set("contextRef", "ctx1")
            unique_id.text = "GENESIS-001"
            
            language = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}language")
            language.set("contextRef", "ctx1")
            language.text = "iso639:es"
            
            creation_date = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}creationDate")
            creation_date.set("contextRef", "ctx1")
            creation_date.text = "2005-06-01"
            
            creator = etree.SubElement(doc_info, f"{{{ns['gl-bus']}}}creator")
            creator.set("contextRef", "ctx1")
            creator.text = "Notaria Veinticinco de Medellin"
            
            entries_comment = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}entriesComment")
            entries_comment.set("contextRef", "ctx1")
            entries_comment.text = "Constitucion de Sociedad de Responsabilidad Limitada"
            
            period_start = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}periodCoveredStart")
            period_start.set("contextRef", "ctx1")
            period_start.text = "2005-06-01"
            
            period_end = etree.SubElement(doc_info, f"{{{ns['gl-cor']}}}periodCoveredEnd")
            period_end.set("contextRef", "ctx1")
            period_end.text = "2005-06-01"
            
            default_currency = etree.SubElement(doc_info, f"{{{ns['gl-muc']}}}defaultCurrency")
            default_currency.set("contextRef", "ctx1")
            default_currency.text = "iso4217:COP"
            
            # Insert at the beginning of accountingEntries
            ae.insert(0, doc_info)
            
    # Process details and measurables
    details = root.findall(".//gl-cor:entryDetail", ns)
    for detail in details:
        measurable = detail.find(".//gl-bus:measurable", ns)
        if measurable is not None:
            if len(measurable) == 0:
                print(f"-> Removing empty measurable element from detail line {detail.find('gl-cor:lineNumber', ns).text}...")
                detail.remove(measurable)
            else:
                # Correct measurableCode from ORD to SP
                code = measurable.find("gl-bus:measurableCode", ns)
                if code is not None and code.text == "ORD":
                    print(f"-> Correcting measurableCode in detail line {detail.find('gl-cor:lineNumber', ns).text} to 'SP'...")
                    code.text = "SP"
                
                # Correct measurableQuantity
                qty = measurable.find("gl-bus:measurableQuantity", ns)
                if qty is not None:
                    # check if unitRef is already set and correct, otherwise set it
                    if qty.get("unitRef") != "Shares":
                        print(f"-> Adding unitRef='Shares' and decimals='0' to measurableQuantity in detail line {detail.find('gl-cor:lineNumber', ns).text}...")
                        qty.set("unitRef", "Shares")
                        qty.set("decimals", "0")

    # Write out the corrected file
    with open(xml_path, "wb") as f:
        doc.write(f, pretty_print=True, xml_declaration=True, encoding="utf-8")
    print(f"-> Corrected file saved back to {xml_path}")
    
    # Run schema validation if taxonomy is available
    if os.path.exists(schema_path):
        print(f"-> Schema found at {schema_path}. Running validation...")
        xmlschema_doc = etree.parse(schema_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        
        final_doc = etree.parse(xml_path)
        is_valid = xmlschema.validate(final_doc)
        if is_valid:
            print("-> XML is 100% VALID against the schema.")
        else:
            print("-> XML is INVALID. Errors:")
            for error in xmlschema.error_log:
                print(f"   Line {error.line}: {error.message}")
    else:
        print(f"-> Warning: Schema not found at {schema_path}. Skipping validation.")

if __name__ == "__main__":
    main()
