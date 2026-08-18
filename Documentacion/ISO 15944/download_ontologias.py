import os
import urllib.request
import ssl

def download_file(url, target_path):
    try:
        print(f"[*] Downloading {url} -> {target_path}...")
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # Create unverified SSL context to bypass SSL certificate validation issues
        ssl_context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, context=ssl_context) as response, open(target_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"[✓] Saved to {target_path}")
    except Exception as e:
        print(f"[-] Failed to download {url}: {e}")

def main():
    base_dir = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\ISO 15944\ontologias"
    
    urls = {
        # RoboSystems (Joey French / Semantic Sovereignty)
        "robosystems_ontology.ttl": "https://raw.githubusercontent.com/RoboFinSystems/robosystems/main/frameworks/ontology/v1/ontology.ttl",
        "robosystems_shapes.ttl": "https://raw.githubusercontent.com/RoboFinSystems/robosystems/main/frameworks/ontology/v1/shapes.ttl",
        "fac_calculations.jsonld": "https://raw.githubusercontent.com/RoboFinSystems/robosystems/main/frameworks/fac/packages/fac-calculations/v1/taxonomy.jsonld",
        "fac_presentation.jsonld": "https://raw.githubusercontent.com/RoboFinSystems/robosystems/main/frameworks/fac/packages/fac-presentation/v1/taxonomy.jsonld",
        
        # Valueflows (REA / ISO 15944-4 Open-edi Implementation on Codeberg / Valueflo.ws)
        "valueflows_all_vf.ttl": "https://codeberg.org/valueflows/pages/raw/branch/main/assets/all_vf.TTL",
        
        # ACTUS Financial Contracts Data Dictionary
        "actus_dictionary.json": "https://raw.githubusercontent.com/actusfrf/actus-dictionary/master/actus-dictionary.json",
    }
    
    for filename, url in urls.items():
        target = os.path.join(base_dir, filename)
        download_file(url, target)

if __name__ == "__main__":
    main()
