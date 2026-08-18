import csv, sys, xml.etree.ElementTree as ET

CSV_FILE = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Source\EEFF_FONDOS_MERGED_WITH_GSKM_Mx.csv"
XML_FILE = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Output\QxSiesa2XBRLGL.xml"
XBRL_FILE = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Output\ReporteFondos.xbrl"

print("="*70)
print("1. CSV COLUMNS & FIRST 5 ROWS")
print("="*70)
try:
    for enc in ['utf-8-sig', 'latin-1', 'cp1252']:
        try:
            with open(CSV_FILE, encoding=enc, errors='replace') as f:
                reader = csv.reader(f, delimiter=';')
                rows = [row for i, row in enumerate(reader) if i < 6]
            print(f"Encoding: {enc}, Delimiter: semicolon")
            break
        except:
            with open(CSV_FILE, encoding=enc, errors='replace') as f:
                reader = csv.reader(f)
                rows = [row for i, row in enumerate(reader) if i < 6]
            print(f"Encoding: {enc}, Delimiter: comma")
            break
    
    if rows:
        headers = rows[0]
        print(f"\nTotal columns: {len(headers)}")
        print("COLUMNS:")
        for i, h in enumerate(headers):
            print(f"  [{i:02d}] {h}")
        print(f"\nROW 1: {rows[1] if len(rows)>1 else 'N/A'}")
        print(f"ROW 2: {rows[2] if len(rows)>2 else 'N/A'}")
except Exception as e:
    print(f"Error reading CSV: {e}")

print("\n" + "="*70)
print("2. XBRL GL XML STRUCTURE (first 60 lines)")
print("="*70)
try:
    with open(XML_FILE, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    for i, line in enumerate(lines[:60]):
        print(f"{i+1:03}: {line}", end='')
except Exception as e:
    print(f"Error reading XML: {e}")

print("\n" + "="*70)
print("3. REPORTE FONDOS .xbrl STRUCTURE")
print("="*70)
try:
    with open(XBRL_FILE, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    for i, line in enumerate(lines[:50]):
        print(f"{i+1:03}: {line}", end='')
except Exception as e:
    print(f"Error reading XBRL: {e}")
