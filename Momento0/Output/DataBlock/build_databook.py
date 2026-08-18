import json
import os
from datetime import datetime

# Rutas de archivos
input_file = "DataBook_Target.json"
output_file = "output.databook.md"

def build_databook():
    if not os.path.exists(input_file):
        print(f"Error: No se encontro el archivo {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. YAML Frontmatter Estático
    yaml_frontmatter = f"""---
id: urn:uuid:dbk-escritura-constitucion-001
type: DataBook
title: "Escritura Pública de Constitución - Asignación de Capital"
version: 1.0.0
created: "{datetime.now().strftime('%Y-%m-%d')}"
provenance:
  source: "DFRNT MapForce Pipeline"
  method: "Automated Semantic Transmutation"
manifest:
  entrypoints:
    - block: dataset
  blocks:
    dataset:
      type: json-ld
      description: "XBRL GL / REA Semantic Graph (Inline)"
---

# Escritura Pública de Constitución

El siguiente documento detalla la asignación de capital inicial (Momento 0), unificando la narrativa legal con los holones semánticos inyectables en TerminusDB.
"""

    blocks_markdown = ""

    # 2. Generación Inline Markdown + JSON-LD
    for idx, block in enumerate(data.get("inline_blocks", [])):
        socio_nombre = block.get("narrative_markdown", "Desconocido")
        json_data = block.get("json_ld_data", {})
        
        # Agregamos el context y el type que MapForce omitió por simplicidad
        json_ld = {
            "@context": {
                "terminus": "terminusdb:///",
                "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#"
            },
            "@type": "gl-cor:EntryDetail",
            **json_data
        }

        # Extraemos variables para la narrativa humana
        cantidad = json_data.get("gl-cor:measurable", {}).get("gl-cor:measurableQuantity", "???")
        unidad = json_data.get("gl-cor:measurable", {}).get("gl-cor:measurableUnitOfMeasure", "Cuotas")
        monto = json_data.get("gl-cor:amount", "???")
        cuenta = json_data.get("gl-cor:account", {}).get("gl-cor:accountMainID", "311505")

        blocks_markdown += f"\n### {socio_nombre}\n"
        blocks_markdown += f"El accionista **{socio_nombre}** suscribe y paga un total de **{cantidad} {unidad}** por un valor monetario de **${monto} COP**, registrado en la cuenta **{cuenta}**.\n\n"
        blocks_markdown += "```json-ld\n"
        blocks_markdown += json.dumps(json_ld, indent=2, ensure_ascii=False)
        blocks_markdown += "\n```\n"

    # 3. Escribir archivo final
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(yaml_frontmatter)
        f.write(blocks_markdown)

    print(f"DataBook generado exitosamente: {output_file}")

if __name__ == "__main__":
    build_databook()
