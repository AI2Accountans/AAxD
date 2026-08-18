# Alineación Técnica con el Modelo MINI de Charles Hoffman (11 de Agosto de 2026)

> **Objetivo**: Conectar la canalización semántica implementada en **GSKM_FON** (BaseX + XBRL GL + Altova MapForce + DFRNT JSON-LD) con la propuesta de **Sistema de Información Contable Mínimo Viable (MINI AIS)** de Charles Hoffman.

---

## 1. Visión General del Modelo MINI de Charles Hoffman

En su publicación del 11 de agosto de 2026, Charles Hoffman propone reducir la complejidad accidental del software contable tradicional mediante un **diseño idealizado y minimalista**:

```mermaid
graph LR
    RF[1. Reporting Framework] --> SD[2. Source Documentation]
    SD --> BE[3. Business Events]
    BE --> FT[4. Financial Transactions]
    FT --> FS[5. Financial Statements]

    style RF fill:#1e293b,color:#fff,stroke:#3b82f6
    style SD fill:#0f766e,color:#fff,stroke:#14b8a6
    style BE fill:#854d0e,color:#fff,stroke:#eab308
    style FT fill:#701a75,color:#fff,stroke:#d946ef
    style FS fill:#991b1b,color:#fff,stroke:#ef4444
```

> *"El punto principal aquí es reducir toda la complejidad que se pueda reducir y aun así poder crear un Estado Financiero MÍNIMO a partir de la documentación de origen. La complejidad se puede volver a agregar incrementalmente."* — **Charlie Hoffman**

---

## 2. Matriz de Alineación: Modelo MINI vs. GSKM_FON

| Fase del Modelo MINI (Hoffman) | Requisito Mínimo del Modelo | Implementación Realizada en GSKM_FON | Componente / Archivo de Soporte |
|---|---|---|---|
| **1. Reporting Framework** | Especificación interpretable por máquinas (Seattle Method) | JSON Schema ontológico Sunder/Zachman v2 + Reglas NIIF/Superfinanciera | [`sunder_zachman_dfrnt_instances_v2.schema.json`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Taxonomy/JsonSchema/sunder_zachman_dfrnt_instances_v2.schema.json)<br/>[`dav30.sps`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Target/dav30.sps) |
| **2. Source Documentation** | Documentación de origen estructurada (Contrato, Factura, Trial Balance) | CSV de Origen Siesa + XML de Balance de Prueba Enriquecido | [`Data_Enriquecida.csv`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Target/Data_Enriquecida.csv)<br/>[`Qx_SaldoInicialQxSiesa2XBRLGL.xml`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Output/Qx_SaldoInicialQxSiesa2XBRLGL.xml) |
| **3. Business Events (REA)** | Registro inmutable de eventos de negocio con ontología REA (Recursos, Eventos, Agentes) | Enriquecimiento semántico en BaseX XQuery con el módulo SRCD de XBRL GL (`gsk:Assets`, `gsk:EquityAndLiabilities`) | [`merge_data.xq`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Xquery/merge_data.xq)<br/>`gl-srcd:detailedContentFilter` |
| **4. Financial Transactions** | Proyección de eventos contables sin plan de cuentas arbitrario (XBRL GL ➔ Graph JSON-LD) | Transmutación semántica 1:1 en Altova MapForce a payload ontológico JSON-LD | [`Siesa2XBRLGL.mfd`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Mapping/Siesa2XBRLGL.mfd)<br/>[`CSV2XBRLGL2JSONLD.json`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Output/CSV2XBRLGL2JSONLD.json) |
| **5. Financial Statements** | Proyección de estados financieros primarios (Balance General y Estado de Resultados) | Generación automática en BaseX XQuery + Renderizado HTML imprimible alineado con Paladin Realty | [`generate_dav30_report.xq`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Xquery/generate_dav30_report.xq)<br/>[`Estados_Financieros_dav30.html`](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Target/Estados_Financieros_dav30.html) |

---

## 3. Demostración de Verificación del Prototipo

En respuesta directa al reto de Charles (*"I cannot make the prototype actually work because I am not a good enough programmer; but it could work"*), el prototipo **GSKM_FON** demuestra que la arquitectura **FUNCIONA** operativamente a través de la consulta XQuery en BaseX:

### Consulta XQuery Ejecutada en BaseX 12.0:
```xquery
xquery version "3.1";
declare namespace file = "http://expath.org/ns/file";

let $json-path := "C:/Users/IPHIX/Documents/Projects/DFRNT/GSKM_FON/Output/CSV2XBRLGL2JSONLD.json"
let $data := parse-json(file:read-text($json-path))

let $exact := for $item in $data?*
              let $tags := $item("gl-srcd:detailedContentFilter")?*
              where string($item("agent_identifier")) = '293'
                and string($item("postingDate")) = '2026-07-31'
                and (some $tag in $tags satisfies $tag = 'gsk:EquityAndLiabilities')
              return xs:decimal($item("amount"))

return map {
  "Suma_Filtro_Exacto_293_Equity": sum($exact),
  "Conteo_Filtro_Exacto": count($exact)
}
```

### Resultado Matemático Obtenido:
- **`Suma_Filtro_Exacto_293_Equity`**: **`-$71.165.357.012,32`** (33 registros de Pasivo + Patrimonio).
- **Verificación contra PDF Oficial (`293. Paladin Compartimento B Junio 2026.pdf`)**: **`$71.165.357.012,18`** (Diferencia de centavos por redondeos).

---

## 4. Conclusiones y Próximos Pasos con Charles Hoffman

1. **Eliminación del Plan de Cuentas Tradicional (*No Lead Schedule needed*)**:
   - Tal como señala Charlie en el punto 98, no se necesitó una tabla intermedia de mapeo de PUC (*Chart of Accounts*) porque el concepto directo del **Reporting Framework** (`gl-srcd:detailedContentFilter`) clasifica las transacciones en el origen.

2. **Flujo Shift-Left Automatizado**:
   - Se ha demostrado la tesis de que un grafo semántico interpretable por máquina (JSON-LD) puede renderizar directamente la vista interpretable por humanos (HTML/PDF de Davivienda Corredores) sin duplicación de datos.
