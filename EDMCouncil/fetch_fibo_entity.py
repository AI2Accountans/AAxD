import urllib.request
import urllib.parse
import json

def get_entity_details(base_url: str, iri: str):
    """
    Realiza una petición al endpoint del onto-viewer para recuperar
    la información de una entidad por su IRI.
    """
    url = f"{base_url}/api/entity?iri={urllib.parse.quote(iri)}"
    
    try:
        # Se realiza la petición HTTP GET
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data
            else:
                print(f"Error: Código de estado {response.status}")
    except Exception as e:
        print(f"Ocurrió un error al realizar la consulta: {e}")
        
    return None

def main():
    # URL base del onto-viewer (por defecto localhost:8080 si lo ejecutas con docker compose o java -jar)
    base_url = "http://localhost:8080"
    
    # El IRI de la clase LegalEntity en la ontología de FIBO
    legal_entity_iri = "https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegalEntity"
    
    print(f"Consultando detalles para: {legal_entity_iri}\n")
    details = get_entity_details(base_url, legal_entity_iri)
    
    if details:
        # El endpoint EntityApiController devuelve un `SearcherResult<OwlDetails>`
        # En el JSON resultante, la info interesante suele estar en la llave 'result'
        result = details.get("result", {})
        properties = result.get("properties", {})
        
        print("--- Propiedades devueltas por el visor ---")
        
        # Iteramos por las propiedades (las llaves suelen ser los IDs de visualización que le da el backend,
        # como axiomas, definiciones de skos:definition, anotaciones, rdfs:label, etc.)
        for key, value_list in properties.items():
            print(f"Propiedad: {key}")
            # value_list es una lista de OwlAxiomPropertyValue / OwlAnnotationPropertyValue 
            for item in value_list:
                # Cada item suele tener la llave 'value' o 'fullRenderedString' con el texto extraído
                val = item.get("value") or item.get("fullRenderedString")
                print(f"  -> {val}")
            print("-" * 40)
            
if __name__ == "__main__":
    main()
