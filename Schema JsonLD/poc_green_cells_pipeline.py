import os
import sys
import json
import xml.etree.ElementTree as ET
from decimal import Decimal

# Absolute paths
BASE_DIR = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Schema JsonLD"
XML_FILE_PATH = os.path.join(BASE_DIR, "factura_dian_c4.xml")
CONTEXT_FILE_PATH = os.path.join(BASE_DIR, "xbrlgl_context.jsonld")
OUTPUT_FILE_PATH = os.path.join(BASE_DIR, "instancia_xbrlgl_output.json")

def print_banner(title):
    print("\n" + "=" * 80)
    print(f" {title.center(78)} ")
    print("=" * 80)

def main():
    # Force UTF-8 encoding for stdout on Windows to prevent UnicodeEncodeError
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            pass
    print_banner("INICIO: PRUEBA DE CONCEPTO - PIPELINE DE CASILLAS VERDES (ZACHMAN)")

    # 1. CELL C4: Raw physical document (XML Invoice in UBL 2.1 format)
    print("\n[🟢 Cell C4 - UBL Document (XML Invoice)]")
    if not os.path.exists(XML_FILE_PATH):
        print(f"❌ Error: No se encontro el archivo XML fisico en {XML_FILE_PATH}")
        sys.exit(1)
    
    print(f"  -> Archivo fisico de origen localizado en: {XML_FILE_PATH}")
    print("  -> Tamaño del archivo: {} bytes".format(os.path.getsize(XML_FILE_PATH)))
    
    # 2. CELL B4: Ingest Program (XML Parser & Database loader)
    print("\n[🟢 Cell B4 - Ingest Program (XML Ingestion & Parsing)]")
    try:
        tree = ET.parse(XML_FILE_PATH)
        root = tree.getroot()
        print("  -> XML cargado y parseado con exito en memoria.")
    except Exception as e:
        print(f"  ❌ Error al parsear el XML: {str(e)}")
        sys.exit(1)

    # Namespaces setup
    ns = {
        'inv': 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
        'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    }

    # 3. CELL B3: MapForce Mapping (Extraction of physical elements to logical keys)
    print("\n[🟢 Cell B3 - MapForce Mapping (Extracción y Mapeo Semántico)]")
    
    try:
        # Extract invoice header details
        invoice_id = root.find('cbc:ID', ns).text
        issue_date = root.find('cbc:IssueDate', ns).text
        currency = root.find('cbc:DocumentCurrencyCode', ns).text
        
        # Extract Supplier
        supplier_party = root.find('.//cac:AccountingSupplierParty/cac:Party', ns)
        supplier_name = supplier_party.find('.//cbc:Name', ns).text
        supplier_id = supplier_party.find('.//cbc:CompanyID', ns).text
        
        # Extract Customer
        customer_party = root.find('.//cac:AccountingCustomerParty/cac:Party', ns)
        customer_name = customer_party.find('.//cbc:Name', ns).text
        customer_id = customer_party.find('.//cbc:CompanyID', ns).text
        
        # Extract item details
        invoice_line = root.find('.//cac:InvoiceLine', ns)
        item_name = invoice_line.find('.//cac:Item/cbc:Name', ns).text
        line_amount = Decimal(invoice_line.find('cbc:LineExtensionAmount', ns).text)
        
        # Extract Tax totals
        tax_total = root.find('.//cac:TaxTotal', ns)
        tax_amount = Decimal(tax_total.find('cbc:TaxAmount', ns).text)
        tax_percent = Decimal(tax_total.find('.//cbc:Percent', ns).text)
        
        # Extract Legal total
        payable_amount = Decimal(root.find('.//cac:LegalMonetaryTotal/cbc:PayableAmount', ns).text)
        
        print(f"  -> Factura Nro: {invoice_id} | Fecha: {issue_date} | Moneda: {currency}")
        print(f"  -> Proveedor: {supplier_name} (NIT: {supplier_id})")
        print(f"  -> Cliente: {customer_name} (NIT: {customer_id})")
        print(f"  -> Linea 1: {item_name} | Monto Neto: {line_amount:,.2f} {currency}")
        print(f"  -> Impuesto IVA ({tax_percent}%): {tax_amount:,.2f} {currency}")
        print(f"  -> Total por Pagar (Payable): {payable_amount:,.2f} {currency}")
        
    except AttributeError as e:
        print(f"  ❌ Error de mapeo (estructura XML no coincide con el patron UBL esperado): {str(e)}")
        sys.exit(1)

    # 4. CELL B2: MapForce Transform (Double-Entry logic & Account routing)
    print("\n[🟢 Cell B2 - MapForce Transform (Reglas Conceptuales de Partida Doble)]")
    
    # conceptual rules:
    # 1. Invoice Subtotal (Net Line extension) -> Debit in selected general ledger expense account (510506 - Consultoría)
    # 2. Tax Amount -> Debit in VAT tax receivable account (240805 - IVA Descontable)
    # 3. Total Payable Amount -> Credit in Supplier Payable account (220505 - Proveedores Nacionales)
    
    expense_account = "510506"
    vat_account = "240805"
    payable_account = "220505"
    
    debits = [
        {"account": expense_account, "amount": line_amount, "desc": f"Gasto por Servicios: {item_name}", "agent": f"Supplier/{supplier_id}"},
        {"account": vat_account, "amount": tax_amount, "desc": "Impuesto sobre las Ventas por Pagar (Descontable)"}
    ]
    
    credits = [
        {"account": payable_account, "amount": payable_amount, "desc": f"Cuentas por Pagar - Proveedor {supplier_name}", "agent": f"Supplier/{supplier_id}"}
    ]
    
    # Arithmetic Verification (Pacioli Check)
    total_debits = sum(item["amount"] for item in debits)
    total_credits = sum(item["amount"] for item in credits)
    
    print(f"  -> Cuenta de Gasto: {expense_account} (Débito: {line_amount:,.2f} COP)")
    print(f"  -> Cuenta de Impuesto IVA: {vat_account} (Débito: {tax_amount:,.2f} COP)")
    print(f"  -> Cuenta por Pagar Proveedor: {payable_account} (Crédito: {payable_amount:,.2f} COP)")
    print(f"  -> 🔍 Verificando Aritmetica de Partida Doble:")
    print(f"     * Suma Débitos: {total_debits:,.2f} COP")
    print(f"     * Suma Créditos: {total_credits:,.2f} COP")
    
    if total_debits == total_credits:
        print("     ✅ ¡Balance Cuadrado Exitosamente! Débitos == Créditos.")
    else:
        print("     ❌ Error: El balance no cuadra. ¡La partida doble esta asimetrica!")
        sys.exit(1)

    # 5. CELLS C3 & C2: JSON-LD Logical Representation and XBRL GL / ESG Taxonomy integration
    print("\n[🟢 Cells C3 & C2 - JSON-LD Models & XBRL Taxonomies (Representación Lógica y Ontológica)]")
    
    # Read the fixed context file to verify it
    if not os.path.exists(CONTEXT_FILE_PATH):
        print(f"  ❌ Error: Contexto JSON-LD no encontrado en {CONTEXT_FILE_PATH}")
        sys.exit(1)
    
    # We build the JSON-LD structure matching the context and custom ontology
    json_ld_document = {
        "@context": "https://dfrnt.tu-dominio.com/Schema_JsonLD/xbrlgl_context.jsonld",
        "id": f"xbrlgl-instance:{invoice_id}",
        "type": "AccountingEntries",
        
        # Provenance Metadata linking logical to physical (W3C PROV-O)
        "documentInfo": {
            "id": f"doc:{invoice_id}",
            "type": "DocumentInfo",
            "dcat:keyword": ["factura", "servicio", "consultoria", "momento_cero"],
            "prov:wasDerivedFrom": f"file:///{XML_FILE_PATH.replace(chr(92), '/')}",
            "dcterms:creator": {
                "type": "foaf:Person",
                "foaf:name": "MapForce Automatic Pipeline Agent"
            }
        },
        
        # Source document contract detail (XBRL GL SRCD)
        "sourceDocument": {
            "id": f"SourceDocument/{invoice_id}",
            "type": "srcd:SummaryReportingData",
            "document_type": "Factura Electronica UBL 2.1",
            "engaged_agents": [
                {
                    "@id": f"Supplier/{supplier_id}",
                    "@type": "Supplier",
                    "artifact_name": supplier_name
                },
                {
                    "@id": f"Customer/{customer_id}",
                    "@type": "Customer",
                    "artifact_name": customer_name
                }
            ]
        },
        
        # Entry Header (C6 Journal Header)
        "entryHeader": {
            "id": f"journal:JRN-{invoice_id}",
            "type": "EntryHeader",
            "dcterms:issued": issue_date,
            "dcterms:description": f"Registro de factura por {item_name}",
            
            # Entry Details (Debits & Credits mapped explicitly)
            "entryDetail": [
                # Line 1: Expense Debit
                {
                    "id": f"detail:{invoice_id}-line1",
                    "type": "EntryDetail",
                    "account": expense_account,
                    "amount": float(line_amount),
                    "sign": "debit",
                    "agent_identifier": f"Supplier/{supplier_id}",
                    "linksToSummary": {
                        "type": "srcd:SummaryReportingData",
                        "summaryConcept": "GRI-201-1-Economic-Value-Distributed", # ESG Connection (GRI)
                        "contextRef": "PeriodoActual"
                    }
                },
                # Line 2: VAT Tax Debit
                {
                    "id": f"detail:{invoice_id}-line2",
                    "type": "EntryDetail",
                    "account": vat_account,
                    "amount": float(tax_amount),
                    "sign": "debit"
                },
                # Line 3: Supplier Credit
                {
                    "id": f"detail:{invoice_id}-line3",
                    "type": "EntryDetail",
                    "account": payable_account,
                    "amount": float(payable_amount),
                    "sign": "credit",
                    "agent_identifier": f"Supplier/{supplier_id}"
                }
            ]
        }
    }
    
    print("  -> Grafo JSON-LD estructurado en memoria exitosamente.")
    print("  -> Integra modulo SRCD (Contratos) y vincula cuentas a taxonomía ESG (GRI 201-1).")

    # 6. CELL C6: Running Graph Instances (Write back to database format / local file)
    print("\n[🟢 Cell C6 - Graph Instances (Grafo Contable en TerminusDB / Archivo Listo)]")
    
    try:
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(json_ld_document, f, indent=2, ensure_ascii=False)
        print(f"  ✅ ¡Prueba de concepto exitosa! Archivo JSON-LD generado con exito en:")
        print(f"     👉 {OUTPUT_FILE_PATH}")
        print("  -> Tamaño del archivo de salida: {} bytes".format(os.path.getsize(OUTPUT_FILE_PATH)))
    except Exception as e:
        print(f"  ❌ Error al guardar el archivo JSON-LD de salida: {str(e)}")
        sys.exit(1)

    print("\n" + "-" * 80)
    print(" RESUMEN DE LA PRUEBA DE CONCEPTO EN EL MARCO DE ZACHMAN ".center(80, "-"))
    print("-" * 80)
    print(" 1. [Cell C4] Entrada Fisica : Factura DIAN UBL 2.1 XML")
    print(" 2. [Cell B4] Ingesta        : Parser ET.parse() cargando y leyendo del disco.")
    print(" 3. [Cell B3] Mapeador RDF   : Mapeo de campos XML a propiedades semánticas del W3C.")
    print(" 4. [Cell B2] Partida Doble  : Distribución automatica en Cuentas T (Gasto, IVA, Proveedor).")
    print(" 5. [Cell C2] Taxonomías     : Alineación de cuentas con XBRL GL (SRCD) y ESG (GRI).")
    print(" 6. [Cell C3] Modelo Logico  : Estructuración en documento JSON-LD anidado y enlazado.")
    print(" 7. [Cell C6] Grafo Activo   : Generación del archivo final listo para inyección en TerminusDB.")
    print("=" * 80)

if __name__ == "__main__":
    main()
