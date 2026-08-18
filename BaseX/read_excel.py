import pandas as pd
import json

excel_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\BaseX\Índice BaseX-Talk Digest_2026-07-31..xlsx"
df = pd.read_excel(excel_path)

print(f"Total filas: {len(df)}")
print("Columnas:", df.columns.tolist())

# Mostrar los temas tratados
output = []
for idx, row in df.iterrows():
    fecha = str(row.iloc[0])
    asunto = str(row.iloc[1])
    temas = str(row.iloc[2])
    output.append({
        "fecha": fecha,
        "asunto": asunto,
        "temas": temas
    })

with open(r"C:\Users\IPHIX\Documents\Projects\DFRNT\BaseX\temas_extracted.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Extraídos {len(output)} registros a temas_extracted.json")
