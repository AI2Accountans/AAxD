import os
import sys

pdf_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Nicolas Figay\2026-08-01.pdf"
out_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Nicolas Figay\pdf_text.txt"

print(f"Checking libraries to read {pdf_path}...")

try:
    import pypdf
    print("Using pypdf")
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for i, page in enumerate(reader.pages):
        text += f"\n--- Page {i+1} ---\n"
        text += page.extract_text() or ""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted text with pypdf")
    sys.exit(0)
except ImportError:
    print("pypdf not available")

try:
    import pdfplumber
    print("Using pdfplumber")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text += f"\n--- Page {i+1} ---\n"
            text += page.extract_text() or ""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted text with pdfplumber")
    sys.exit(0)
except ImportError:
    print("pdfplumber not available")

try:
    import fitz # PyMuPDF
    print("Using fitz")
    doc = fitz.open(pdf_path)
    text = ""
    for i, page in enumerate(doc):
        text += f"\n--- Page {i+1} ---\n"
        text += page.get_text()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted text with fitz")
    sys.exit(0)
except ImportError:
    print("fitz not available")

try:
    from pdfminer.high_level import extract_text
    print("Using pdfminer")
    text = extract_text(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted text with pdfminer")
    sys.exit(0)
except ImportError:
    print("pdfminer not available")

print("No PDF extraction library available. Trying to install pypdf via pip...")
