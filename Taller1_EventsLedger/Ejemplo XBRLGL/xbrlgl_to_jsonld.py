import xml.etree.ElementTree as ET
import json
import uuid
import os

XML_FILE = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Output\QxSiesa2XBRLGL.xml"
OUTPUT_JSONLD = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Output\EEFF_Fondos_Holon.jsonld"

NAMESPACES = {
    'xbrli': 'http://www.xbrl.org/2003/instance',
    'gl-cor': 'http://www.xbrl.org/int/gl/cor/2015-03-25',
    'gl-bus': 'http://www.xbrl.org/int/gl/bus/2015-03-25',
    'gl-srcd': 'http://www.xbrl.org/int/gl/srcd/2015-03-25'
}

def parse_xbrl_gl(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    nodes = []

    # 1. Reporting Entity
    entity_node = {
        "@type": "FIBO_StockCorporation",
        "@id": "https://www.davivienda.com",
        "artifact_name": "EEFF Fondos Davivienda Ledger",
        "identifierCode": "Davivienda",
        "identifierDescription": "FONDO DE CAPITAL PRIVADO TC LATAM / DAVIVIENDA",
        "identifierType": "NIT"
    }
    nodes.append(entity_node)

    # 2. Source Document (Momento 0 / Trial Balance)
    source_doc = {
        "@type": "SourceDocument",
        "@id": "SourceDocument/TrialBalance-20250731",
        "artifact_name": "QxSiesa2XBRLGL.xml",
        "documentType": "TrialBalance",
        "documentDate": "2025-07-31T00:00:00Z"
    }
    nodes.append(source_doc)

    # Process accountingEntries
    entries = root.findall('gl-cor:accountingEntries', NAMESPACES)
    
    header_id = "JE-DAV-2025-07"
    entry_header = {
        "@type": "EntryHeader",
        "@id": f"EntryHeader/{header_id}",
        "artifact_name": "QxSiesa2XBRLGL",
        "posting_date": "2025-07-31T00:00:00Z",
        "source_document": "SourceDocument/TrialBalance-20250731",
        "economic_event": f"EconomicEvent/{header_id}"
    }
    nodes.append(entry_header)

    line_counter = 1

    for entry in entries:
        detail = entry.find('.//gl-cor:entryDetail', NAMESPACES)
        if detail is None:
            continue

        account_elem = detail.find('gl-cor:account', NAMESPACES)
        acc_id = account_elem.find('gl-cor:accountMainID', NAMESPACES).text if account_elem is not None and account_elem.find('gl-cor:accountMainID', NAMESPACES) is not None else ""
        acc_desc = account_elem.find('gl-cor:accountMainDescription', NAMESPACES).text if account_elem is not None and account_elem.find('gl-cor:accountMainDescription', NAMESPACES) is not None else ""

        amount_elem = detail.find('gl-cor:amount', NAMESPACES)
        amount = float(amount_elem.text) if amount_elem is not None and amount_elem.text else 0.0

        dc_elem = detail.find('gl-cor:debitCreditCode', NAMESPACES)
        dc_code = dc_elem.text if dc_elem is not None else "D"

        date_elem = detail.find('gl-cor:postingDate', NAMESPACES)
        posting_date = date_elem.text if date_elem is not None else "2025-07-31"

        id_ref = detail.find('gl-cor:identifierReference', NAMESPACES)
        agent_id = id_ref.find('gl-cor:identifierCode', NAMESPACES).text if id_ref is not None and id_ref.find('gl-cor:identifierCode', NAMESPACES) is not None else ""
        agent_desc = id_ref.find('gl-cor:identifierDescription', NAMESPACES).text if id_ref is not None and id_ref.find('gl-cor:identifierDescription', NAMESPACES) is not None else ""

        # Extract gsk semántica inyectada
        gsk_labels = []
        for xbrl_info in detail.findall('gl-cor:xbrlInfo', NAMESPACES):
            filter_elem = xbrl_info.find('gl-srcd:detailedContentFilter', NAMESPACES)
            if filter_elem is not None and filter_elem.text:
                gsk_labels.append(filter_elem.text)

        account_node_id = f"Account/{acc_id}"
        
        # Add Account if not existing
        if not any(n.get("@id") == account_node_id for n in nodes):
            nodes.append({
                "@type": "Account",
                "@id": account_node_id,
                "accountMainID": acc_id,
                "accountMainDescription": acc_desc,
                "mini_lineItem": gsk_labels[-1] if gsk_labels else "",
                "artifact_name": "Siesa Account"
            })

        # Add EntryDetail
        detail_node = {
            "@type": ["EntryDetail", "prov:Entity"],
            "@context": {
                "prov": "http://www.w3.org/ns/prov#",
                "dca": "https://xbrlsite.azurewebsites.net/seattlemethod/dca/",
                "gsk": "https://davivienda.com/gskm/taxonomy#"
            },
            "@id": f"EntryDetail/{header_id}-{line_counter}",
            "artifact_name": "EEFF Fondos EntryDetail",
            "header": f"EntryHeader/{header_id}",
            "lineNumberCounter": line_counter,
            "account": account_node_id,
            "amount": amount,
            "debitCreditCode": dc_code,
            "postingDate": f"{posting_date}T00:00:00Z",
            "agent_identifier": agent_desc,
            "mini_lineItem": gsk_labels[-1] if gsk_labels else "",
            "xbrlInfo": {
                "detailedContentFilter": gsk_labels
            }
        }
        nodes.append(detail_node)
        line_counter += 1

    return nodes

if __name__ == '__main__':
    print(f"Parsing XBRL GL from {XML_FILE}...")
    nodes = parse_xbrl_gl(XML_FILE)
    print(f"Generated {len(nodes)} graph nodes.")

    with open(OUTPUT_JSONLD, 'w', encoding='utf-8') as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)
    
    print(f"JSON-LD Holon successfully written to: {OUTPUT_JSONLD}")
