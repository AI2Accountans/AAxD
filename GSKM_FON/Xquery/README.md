# Guía de Enriquecimiento de Datos Contables y Conversión XBRL GL a JSON-LD

Este proyecto contiene los scripts **XQuery 3.1** diseñados para realizar el cruce de datos contables a nivel de 9 a 6 dígitos y la posterior transformación de la instancia **XBRL GL 2015** (con el módulo **SRCD**) hacia la ontología en **JSON-LD**.

---

## 📁 Estructura del Proyecto

```text
GSKM_FON/
├── Mapping/
│   └── Siesa2XBRLGL.mfd                # Mapeo MapForce (ERP Siesa -> XBRL GL)
├── Output/
│   ├── Qx_SaldoInicialQxSiesa2XBRLGL.xml # Instancia XML en XBRL GL 2015 (con módulo SRCD)
│   └── Qx_SaldoInicialQxSiesa2XBRLGL.jsonld # Ontología JSON-LD enriquecida (Salida)
├── Source/
│   └── Data - Hoja 1.csv              # Fuente de datos contables (Auxiliar a 9 dígitos)
├── Tags/
│   └── Tags.csv                       # Etiquetas contables (Cuenta a 6 dígitos)
├── Target/
│   ├── Data_Enriquecida.csv           # Tabla plana enriquecida a 19 columnas
│   └── Data_Enriquecida.xml           # Salida XML enriquecida
└── Xquery/                            # Scripts XQuery para BaseX
    ├── merge_data.xq                  # Cruce 9 -> 6 dígitos (Genera Target/ CSV y XML)
    ├── xbrlgl_to_jsonld.xq            # Transformación XBRL GL (SRCD) -> JSON-LD
    ├── merge_to_csv.xq                # Salida directa CSV
    ├── merge_to_xml.xq                # Salida directa XML
    └── README.md                      # Esta documentación
```

---

## 💡 Flujo de Datos y Módulo SRCD (`gl-srcd:detailedContentFilter`)

1. **Enriquecimiento del Módulo SRCD en XBRL GL**:
   - Durante la construcción del XML XBRL GL (`Output/Qx_SaldoInicialQxSiesa2XBRLGL.xml`), cada detalle de asiento (`gl-cor:entryDetail`) almacena las etiquetas de taxonomía contable en el elemento:
     ```xml
     <gl-cor:xbrlInfo>
       <gl-srcd:detailedContentFilter contextRef="ctx1">gsk:Assets</gl-srcd:detailedContentFilter>
     </gl-cor:xbrlInfo>
     ```

2. **Propagación al Grafo Ontológico JSON-LD**:
   - El script **`xbrlgl_to_jsonld.xq`** lee el documento XML XBRL GL y extrae en cada nodo `EntryDetail` un arreglo JSON con los valores de `gl-srcd:detailedContentFilter`:
     ```json
     {
       "@type": "EntryDetail",
       "@id": "EntryDetail/111505003_1",
       "accountMainID": "111505003",
       "accountMainDescription": "(FI) PICHINCHA Cta No, 410216321",
       "amount": 55919562.97,
       "debitCreditCode": "D",
       "gl-srcd:detailedContentFilter": [
         "gsk:Assets",
         "gsk:CashAndCashEquivalents",
         "gsk:BalancesWithBanks",
         "gsk:Cash",
         "gsk:NetAssetsLiabilities"
       ],
       "prov:wasDerivedFrom": "xbrl_gl:entryDetail"
     }
     ```

---

## 🚀 Ejecución en BaseX

### Opción 1: Generar la Ontología JSON-LD desde XBRL GL (SRCD)
1. En **BaseX GUI**, abra el archivo **[xbrlgl_to_jsonld.xq](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Xquery/xbrlgl_to_jsonld.xq)** (`Ctrl + O`).
2. Presione **F5** (o el botón ▶️ Ejecutar).
3. Se generará automáticamente el archivo ontológico **`Output/Qx_SaldoInicialQxSiesa2XBRLGL.jsonld`**.

### Opción 2: Ejecución desde Consola (BaseX CLI)
```bash
cd GSKM_FON/Xquery
basex xbrlgl_to_jsonld.xq
```

---

## 🛠️ Requisitos del Sistema
- **BaseX**: Versión 12.0 o superior (compatible con XQuery 3.1, funciones `file:base-dir()`, `file:resolve-path()` y módulo `file` con namespace EXPath `http://expath.org/ns/file`).
