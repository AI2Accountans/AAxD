import urllib.request
import base64

mermaid_code = """
graph LR
    subgraph Step1 [Paso 1: Ingesta y Transmutacion]
        A1[Google Sheets CSV] --> M1[MapForce: GS2XBRLGL2JSONLD.mfd]
        M1 --> M1_B[Mapeo XBRL GL]
        M1_B --> G1[JSON-LD Schema TerminusDB]
    end

    subgraph Step2 [Paso 2: Generacion de DataBook]
        G2[Extraccion DFRNT] --> M2[MapForce: Markdown.mfd]
        M2 --> O1[Markdown DataBook]
    end
    
    G1 -.-> G2
"""

# Simple Base64 encoding for Mermaid.ink API
graphbytes = mermaid_code.encode("utf-8")
base64_string = base64.urlsafe_b64encode(graphbytes).decode('ascii')

# API URL
url = f"https://mermaid.ink/img/{base64_string}"

print("Fetching PNG from Mermaid.ink API...")

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        with open("mapforce_pipeline.png", "wb") as f:
            f.write(response.read())
    print("Success: mapforce_pipeline.png saved.")
except Exception as e:
    print(f"Error: {e}")
