# Propuesta de Correo para Charles Hoffman

**De**: Richard Gasca / Equipo A&AD (Accounting & Audit by Design)  
**Para**: Charles Hoffman (carlos.hoffman@gmail.com / charles.hoffman@xbrl.org)  
**Fecha**: 12 de Agosto de 2026  
**Asunto**: End-to-End Declarative Shift-Left Architecture: From Trial Balance to JSON-LD Knowledge Graph & Automated Financial Statements (MINI Model Alignment)

---

## English Version (Recommended for Email Dispatch)

Dear Charles,

I hope this email finds you well.

Following our recent interaction regarding the alignment of our **Accounting & Audit by Design (A&AD)** architecture with your **MINI Accounting Information System (MINI AIS)** model, I wanted to share a concrete, end-to-end working demonstration that proves how declarative programming shifts audit validation and financial statement synthesis all the way to the left ($1 prevention principle).

We have operationalized a 6-stage declarative pipeline that ingests real-world trial balances and emits fully balanced, NIIF/IFRS-compliant financial statements via Linked Data (JSON-LD):

### 1. Stage 1: Source (Real Entity Trial Balances - Confidential)
We ingest raw, multi-entity transactional trial balances (CSV/Siesa) containing historical and current period balances across multiple economic entities. *(Note: This dataset contains real, non-anonymized financial data provided strictly for demonstration, validation, and conceptual understanding purposes).*  
* **Shift-Left Vision Note**: While this current demonstration starts from trial balances, our overarching Shift-Left goal is to move even further to the left—originating directly from transactional Journal Entries (`entriesHeader` / `entriesDetail`) at the moment of genesis.

### 2. Stage 2: Semantic Taxonomy Tags (SRCD/XBRL GL Mapping)
We map account numbers to formal semantic categories using SRCD (Standardized Report Component Definitions) tags, assigning ontological concepts such as `gsk:CashAndCashEquivalents`, `gsk:TradeAndOtherReceivables`, `gsk:Assets`, and `gsk:EquityAndLiabilities`. *(Note: These are the exact semantic tags currently used in active practice to enrich our chart of accounts and automate financial statement reporting).*

### 3. Stage 3: Declarative XQuery Merge (3.Merge 1 y 2)
We execute a purely declarative XQuery script in a NoSQL database engine to merge the raw trial balance data (`1.Source`) with the semantic tags (`2.Tags`).

### 4. Stage 4: XBRL GL Transmutation to JSON-LD Knowledge Graph (4.Output)
The merged dataset produces an intermediate **XBRL Global Ledger (XBRL GL)** XML instance, which is then transmuted semantically into a native **JSON-LD Knowledge Graph** (`CSV2XBRLGL2JSONLD.json`), preserving full ontological relations, `@id` URI nodes, `@type` class definitions (`EntryHeader`, `EntryDetail`), and `@context` ontologies.  
* **DFRNT Integration Readiness**: This JSON-LD payload is 100% structured and validated to be directly ingested into **DFRNT** (TerminusDB semantic graph engine) for rich graph query analysis and immutable audit trails.

### 5. Stage 5: Declarative JSON-LD to HTML Projection (XQuery 3.1)
Using a second XQuery script (`generate_financial_statements.xq`), we query the JSON-LD Knowledge Graph natively via `parse-json()`. The script aggregates balances by double-entry accounting rules (PUC Classes 1, 2, 3) and projects comparative period columns (June 2026 vs. December 2025).

### 6. Stage 6: Reporting Output (Automated Financial Statements)
The output is a self-contained, audit-ready HTML report (`Estados_Financieros_Paladin.html`). The accounting equation $\text{Assets} = \text{Liabilities} + \text{Equity}$ balances perfectly to $\$0.00$ difference across both comparative periods without a single hardcoded constant or arbitrary multiplier.

---

### Alignment with Your MINI AIS Framework

This operational flow maps 1:1 with your 5 MINI AIS phases:
1. **Reporting Framework** $\rightarrow$ SRCD & NIIF Ontologies (`2.Tags`)
2. **Source Documentation** $\rightarrow$ Multi-entity Trial Balances (`1.Source`)
3. **Business Events & Transactions** $\rightarrow$ Reified XBRL GL Graph (`4.Output`)
4. **Financial Statements** $\rightarrow$ XQuery 3.1 Declarative Projections (`5.Xquery JsonLD 2 HTML` $\rightarrow$ `6.Reporting`)

By keeping every stage 100% declarative, we eliminate black-box procedural code, ensure complete audit traceability, and achieve true **Accounting & Audit by Design**.

I would welcome your feedback on this demonstration and any suggestions for refining the MINI AIS alignment further.

Warm regards,

**Richard Gasca**  
*Accounting & Audit by Design (A&AD) Research Group*  
DFRNT & GSKM Project  

---

## Versión en Español (Para Revisión Interna)

Estimado Charles,

Espero que se encuentre muy bien.

En seguimiento a nuestra reciente interacción sobre la alineación de la arquitectura **Accounting & Audit by Design (A&AD)** con su modelo **MINI AIS (MINI Accounting Information System)**, quiero compartirle una demostración práctica funcional que prueba cómo la programación declarativa desplaza la validación de auditoría y la síntesis de estados financieros totalmente a la izquierda (principio de prevención $1).

Hemos puesto en marcha una canalización declarativa de 6 etapas que ingiere balances de comprobación reales de múltiples entidades y genera estados financieros auditables y balanceados bajo NIIF/IFRS mediante Linked Data (JSON-LD):

1. **Etapa 1: Fuente (1.Source - Confidencial)**: Ingesta del balance de comprobación real de múltiples entidades a fechas de corte comparativas. *(Nota: Esta información corresponde a datos financieros reales no anonimizados y se comparte únicamente con fines ilustrativos, de validación y entendimiento técnico del modelo).*  
   * **Visión Shift-Left**: Aunque en esta ocasión partimos del balance de comprobación, nuestro objetivo para desplazarnos aún más hacia la izquierda es salir directamente desde las **entradas de diario** (`entriesHeader` / `entriesDetail`) en su punto de génesis transaccional.
2. **Etapa 2: Etiquetas Ontológicas (2.Tags)**: Mapeo de cuentas a conceptos semánticos estandarizados (SRCD) (`gsk:CashAndCashEquivalents`, `gsk:Assets`, `gsk:EquityAndLiabilities`). *(Nota: Estas corresponden a las etiquetas que utilizo en la actualidad para enriquecer el catálogo de cuentas y automatizar la generación de reportes).*
3. **Etapa 3: Consolidación XQuery (3.Merge 1 y 2)**: Ejecución de una consulta declarativa XQuery en una base de datos NoSQL para realizar la fusión (merge) del balance de comprobación (`1.Source`) con las etiquetas ontológicas (`2.Tags`).
4. **Etapa 4: Transmutación XBRL GL a Grafo JSON-LD (4.Output)**: A partir de la consolidación se genera una instancia intermedia **XBRL Global Ledger (XBRL GL)** en XML, la cual es transmutada semánticamente hacia un **Grafo de Conocimiento JSON-LD** (`CSV2XBRLGL2JSONLD.json`), preservando URIs (`@id`), clases ontológicas (`@type`) y contextos semánticos (`@context`).  
   * **Integración con DFRNT**: Esta instancia JSON-LD se encuentra 100% estructurada y lista para ser inyectada directamente en **DFRNT** (motor de grafos semánticos sobre TerminusDB) para análisis ontológico de auditoría.
5. **Etapa 5: Proyección Declarativa (5.Xquery JsonLD 2 HTML)**: Consulta XQuery 3.1 que parsea el JSON-LD de forma nativa (`parse-json()`) agregando saldos por partida doble.
6. **Etapa 6: Reporte Final (6.Reporting)**: Generación automática del Estado de Situación Financiera en HTML (`Estados_Financieros_Paladin.html`) con Ecuación Patrimonial cuadrada a $0,00 de diferencia.

Todo el flujo opera bajo programación declarativa pura, asegurando auditabilidad completa y eliminación de valores quemados o scripts de código procedimental opaco.

Quedo atento a sus valiosos comentarios sobre esta demostración y su alineación con el modelo MINI AIS.

Un cordial saludo,

**Richard Gasca**  
*Grupo de Investigación Accounting & Audit by Design (A&AD)*  
Proyecto DFRNT / GSKM
