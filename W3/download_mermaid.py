import urllib.request
import zlib
import base64

mermaid_code = """
flowchart TD
    %% Styling
    classDef genesis fill:#e1f5fe,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    classDef graphdb fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    classDef transmute fill:#fff3e0,stroke:#fbc02d,stroke-width:2px,color:#f57f17
    classDef wrapper fill:#fce4ec,stroke:#e65100,stroke-width:2px,color:#e65100
    classDef audit fill:#f3e5f5,stroke:#c2185b,stroke-width:2px,color:#880e4f
    
    subgraph Layer1 ["3.1 The Operational Graph Engine"]
        direction TB
        A1[Moment 0 Genesis: Contracts / UBL]:::genesis --> B1[(TerminusDB: REA Knowledge Graph)]:::graphdb
        B1 --> C1{{DFRNT: QOWL Semantic Extraction}}:::transmute
    end

    subgraph Layer2 ["3.2 The Semantic Transmutation Layer"]
        direction TB
        D1([Altova XMLSpy: SHACL Constraints]):::transmute -.-> D2[[Altova MapForce: XBRL GL Mapping]]:::transmute
    end

    subgraph Layer3 ["3.3 The Living Knowledge Wrapper"]
        direction TB
        E1[\DataBook: Markdown + JSON-LD Holon/]:::wrapper
        E1 --> F1((LLM & SKOS Autonomous Audit)):::audit
        E1 --> F2((SPARQL Deterministic Audit)):::audit
    end

    %% Cross-layer connections
    C1 -->|Raw Operational Payload| D2
    D2 -->|Transmuted JSON-LD Instance| E1
"""

# Compress and encode for Kroki API
graphbytes = mermaid_code.encode("utf-8")
compressed = zlib.compress(graphbytes, 9)
encoded = base64.urlsafe_b64encode(compressed).decode('ascii')

# API URL
url = f"https://kroki.io/mermaid/png/{encoded}"

print("Fetching PNG from Kroki API...")

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        with open("aad_architecture.png", "wb") as f:
            f.write(response.read())
    print("Success: aad_architecture.png saved.")
except Exception as e:
    print(f"Error: {e}")
