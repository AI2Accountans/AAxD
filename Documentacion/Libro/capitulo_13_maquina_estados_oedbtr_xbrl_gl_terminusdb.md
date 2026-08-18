# Capítulo 13: La Máquina de Estados y el Grafo Multitaxonómico — De ISO/IEC 15944-21 (OeDBTR) al Mapeo XBRL GL SRCD en TerminusDB

## De la Dinámica de Transacciones Distribuidas a la Auditoría Multipropósito e Inmutable

---

*"Una transacción comercial no es un documento estático congelado en el tiempo; es un autómata de estados finitos donde cada evento económico gatilla la verdad contable en múltiples dimensiones regulatorias simultáneamente."*

---

## 1. Introducción: El Encuentro con la Visión OeDBTR de G. Ken Holman

En el desarrollo de la arquitectura **Accounting & Audit by Design (A&AD)**, un hito fundamental para la validación del modelo consistió en contrastar nuestros postulados con el trabajo pionero publicado por **G. Ken Holman**, Jonas Sveistrup Søgaard, Lasse Herskind y el **Prof. William E. McCarthy** (padre de la ontología REA).

En su ilustración práctica sobre la norma **ISO/IEC 15944-21** (*OeDBTR state machine scenario illustration*), Holman y McCarthy demostraron cómo las transacciones comerciales electrónicas deben gestionarse como **máquinas de estados finitos (*State Machines*)** dentro de un repositorio de transacciones distribuido e inmutable (**OeDBTR - Open-edi Distributed Business Transaction Repository**).

En dicho modelo, la transacción no se concibe como un archivo PDF estático o una fila pasiva en una base de datos relacional. Por el contrario:
1. Nace de un acuerdo inicial entre dos agentes (`provider` y `receiver`).
2. Evoluciona mediante **estímulos de negocio (*stimuli*)** —tales como la emisión de una orden, la recepción de mercancía o una notificación de pago.
3. Cada estímulo provoca una transición de estado auditable y gatilla asientos contables asociados en tiempo real.

Sin embargo, para que esta visión alcance el nivel de rigor exigido por las firmas de auditoría globales y los entes reguladores multinacionales, faltaba un puente técnico crucial: **¿Cómo conectar la dinámica de estados con el reporte contable multipropósito bajo múltiples marcos normativos (IFRS, US GAAP, TAX)?**

Este capítulo documenta la solución desarrollada por A&AD: la articulación completa de la familia de normas **ISO/IEC 15944** combinada con el módulo **SRCD de XBRL GL** y la inyección en grafos de conocimiento inmutables en **TerminusDB vía DFRNT**.

---

## 2. Desglosando la Familia ISO/IEC 15944: La Columna Vertebral de A&AD

Para comprender la potencia del modelo, es indispensable diferenciar las dos dimensiones fundamentales del estándar ISO/IEC 15944:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       FAMILIA ISO/IEC 15944 (BOV)                           │
├─────────────────────────────────────────────┬───────────────────────────────┤
│          ISO/IEC 15944-4 (OeBTO)            │    ISO/IEC 15944-21 (OeDBTR)  │
├─────────────────────────────────────────────┼───────────────────────────────┤
│              EL "QUÉ" SEMÁNTICO             │       EL "CÓMO" DINÁMICO      │
│  • Ontología Contable y Económica (REA)    │  • Máquinas de Estado Finitos │
│  • Definición de Recursos, Eventos, Agentes │  • Repositorio Distribuido    │
│  • Principio de Dualidad (Give & Take)      │  • Registro Inmutable (DLT)   │
└─────────────────────────────────────────────┴───────────────────────────────┘
```

Más allá de las Partes 4 y 21, la arquitectura A&AD se fundamenta en un ecosistema integrado de apartados de la norma ISO/IEC 15944:

### A. ISO/IEC 15944-1: El Desacoplamiento BOV vs. FSV
Establece la separación tajante entre la **Vista Operativa de Negocio (BOV - Business Operational View)** y la **Vista de Servicios Funcionales (FSV - Functional Service View)**. En A&AD, los contratos, las reglas contables y las intenciones de los agentes pertenecen estrictamente al BOV, garantizando que sean independientes de la tecnología de red, la base de datos o el lenguaje de programación (FSV).

### B. ISO/IEC 15944-4: La Ontología Económica Base (OeBTO)
Define el lenguaje conceptual unificado. Es la base de nuestro esquema `valueflows_schema.xsd`, donde cada entidad se mapea a conceptos REA puros: `Resource`, `Event`, `Agent`, `Commitment` y `Reciprocity`.

### C. ISO/IEC 15944-5: Dominios Jurisdiccionales y Restricciones Externas
Modela formalmente el impacto de las **restricciones externas** impuestas por legislaciones locales, códigos tributarios (DIAN, IRS) y marcos de información financiera (NIIF/IFRS). Este apartado es el soporte normativo que exige que la transacción no solo registre la física del intercambio, sino también su régimen fiscal y legal.

### D. ISO/IEC 15944-10: Dominios Codificados Habilitados por TI
Garantiza el uso de vocabularios estándar e interoperables (monedas ISO 4217, países ISO 3166, unidades de medida UN/CEFACT), eliminando la ambigüedad al serializar la información hacia tecnologías web de datos vinculados.

### E. ISO/IEC 15944-16: Reglas y Guías Consolidadas del BOV
Proporciona el catálogo unificado de reglas de validación de negocio. Es el conjunto de restricciones que ejecuta nuestro motor de ingesta en tiempo real en BaseX (`iso15944_ingest.xq`) para el cumplimiento estricto del enfoque *Shift Left*.

### F. ISO/IEC 15944-20 & 21: Repositorios Distribuidos y Smart Contracts (OeDBTR)
Gobierna la persistencia inmutable y la ejecución programática de contratos inteligentes. Es la especificación que respalda la inyección del libro mayor en bases de datos de grafos de conocimiento bitemporales como TerminusDB.

---

## 3. El Puente Semántico: Mapeo a XBRL GL con Módulo SRCD y `accountingPurposeCode`

La ontología REA (ISO 15944-4) explica con precisión la física del intercambio (quién entrega qué a quién y a cambio de qué). Sin embargo, la contabilidad corporativa requiere traducir este intercambio a los libros auxiliares y principales sin perder el nivel de detalle operativo.

Para lograr esto sin caer en la rigidez de las bases de datos relacionales, A&AD adopta el estándar **XBRL GL (Global Ledger)** e introduce dos innovaciones clave en el pipeline:

```
[Evento Económico REA (ISO 15944-4)]
                 │
                 ▼
[XBRL GL Base (gl-cor:account)] ──► Mapeo a la cuenta del Plan de Cuentas (PUC)
                 │
                 ├──────────────────────────────────────────────┐
                 ▼                                              ▼
[Módulo SRCD (XBRL GL)]                      [accountingPurposeCode]
  • Mapeo a Taxonomía IFRS / NIIF               • Código de Propósito Contable:
  • Mapeo a Taxonomía US GAAP                      - TAX (Fiscal / Tributario)
  • Mapeo a Taxonomía TAX (Fiscal)                 - FINANCIAL (NIIF / IFRS)
                                                   - MANAGEMENT (Gerencial)
```

### 1. El Módulo SRCD de XBRL GL (*Structure and Reporting Taxonomy Mapping*)
El módulo **SRCD** permite vincular la cuenta operativa (`gl-cor:account`) con elementos específicos de taxonomías externas de reporte financiero o tributario. De este modo, un único asiento contable derivado de la máquina de estados incluye explícitamente los conceptos de línea de reporte a los que contribuye:
* **Vinculación IFRS:** Conecta la línea operativa con el elemento exacto de la Taxonomía NIIF (ej. *Ingresos por actividades ordinarias procedentes de contratos con clientes*).
* **Vinculación TAX:** Conecta la línea operativa con la casilla correspondiente de la declaración tributaria o reporte de información exógena.

### 2. Atribución de Propósito con `accountingPurposeCode`
Para evitar la creación de asientos de ajuste duplicados o libros paralelos desconectados, A&AD califica cada entrada con el atributo nativo `accountingPurposeCode`:
* `TAX`: Registro computado bajo reglas fiscales locales.
* `FINANCIAL`: Registro computado bajo marcos NIIF/IFRS o US GAAP.
* `MANAGEMENT`: Registro computado para contabilidad analítica de costos y gestión interna.

Esto resuelve el problema histórico de las empresas multinacionales: **un solo evento transaccional genera la verdad contable multi-propósito en el instante mismo de su origen.**

---

## 4. El Contenedor Semántico: Named Graphs y la Metáfora del Reporte según Charles Hoffman

Al trasladar la información contable a un entorno de web semántica y grafos de conocimiento, surge un interrogante clave de auditoría: **¿Cómo se agrupan las afirmaciones contables individuales para formar un informe, un contrato o un estado financiero autocontenido?**

La respuesta la proporciona **Charles Hoffman** (padre del reporte financiero digital XBRL) a través del concepto de **Named Graph (Grafo Nombrado)**:

```
     RDF Triplas (S, P, O)                  RDF Cuádruplas (S, P, O, G)
┌──────────────────────────────┐       ┌───────────────────────────────────────┐
│ (Empresa, efectivo, 5000USD) │  ──►  │ (Empresa, efectivo, 5000USD, GrafoA)│
└──────────────────────────────┘       └───────────────────────────────────────┘
                                                           │
                                                           ▼
                                                Named Graph: GrafoA
                                         (Metadatos del Reporte / Contrato)
                                         • IRI: https://empresa.com/rep/2026/q2
                                         • Firma Criptográfica / Sello de Tiempo
                                         • Régimen: IFRS / TAX
```

### De las Triplas a las Cuádruplas (RDF Quads)
En la web semántica tradicional, los datos se expresan como triplas $(S, P, O) \rightarrow \text{(Sujeto, Predicado, Objeto)}$. Sin embargo, una tripla aislada carece de procedencia. Para dotar al dato de contexto contable y legal, el modelo evoluciona a **cuádruplas ($S, P, O, G$)**, donde **$G$ es el Named Graph**: un identificador internacionalizado (IRI/URI) que nombra al contenedor semántico.

### La Metáfora de Charles Hoffman: "Un Named Graph es como un Reporte"
Hoffman establece que en un almacenamiento de grafos (*RDF Store / Knowledge Graph*), un Named Graph actúa exactamente como un **informe financiero, un contrato o una declaración tributaria**:
* **Aislamiento y Límite Lógico:** Define la partición exacta de datos que constituyen un reporte sin que se mezclen con el resto del universo de datos de la empresa.
* **Metadatos del Contenedor:** Permite asociar atributos *al reporte completo* (quién lo emitió, el timestamp de sello de tiempo y la firma digital del auditor).
* **Control de Acceso Granular:** Un auditor externo puede recibir permisos de lectura exclusivos para el `Named Graph` del Balance 2025, sin exponer la información operativa o estratégica confidencial.

### El Santo Grial: Algoritmos de Proyección Globales (*Global Projection Algorithms*)
En la conclusión de su análisis, Charles Hoffman plantea una intuición técnica brillante sobre el futuro de la contabilidad digital:

> *"Parece que toda esta 'información' debería estar en una sola base de datos. Cada fuente, cada evento, el marco de reporte y luego, al crear los Named Graphs que deseas, todo es 'proyectado'. Algo así. Parece que los **algoritmos de proyección estándar globales** serían algo muy bueno."*  
> — **Charles Hoffman**

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │            UNICA BASE DE DATOS (Single Knowledge Graph Database)       │
 │   • Eventos Fuentes REA (ISO 15944-4)   • Contratos ACTUS / UBL        │
 │   • Asientos XBRL GL                    • Marcos de Reporte (IFRS/TAX)  │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │
                 ┌───────────────────┼───────────────────┐
                 ▼                   ▼                   ▼
          [Algoritmo NIIF]    [Algoritmo TAX]    [Algoritmo Costos]
                 │                   │                   │
                 ▼                   ▼                   ▼
          Named Graph NIIF   Named Graph TAX    Named Graph Gerencial
          (Proyección A)     (Proyección B)     (Proyección C)
```

Esta intuición de Hoffman es la confirmación exacta del paradigma **A&AD**:

1. **La Única Fuente de Verdad:** No existen ERPs aislados, sublibros o hojas de cálculo paralelas. Toda la realidad económica (fuentes, eventos, contratos y marcos de reporte) reside en una sola base de datos de grafos de conocimiento inmutable (**TerminusDB**).
2. **El Reporte como una "Proyección":** Los estados financieros ya no son "archivos" que se redactan a mano o tablas físicas que se duplican. Son **Proyecciones Semánticas (Projections)** generadas dinámicamente mediante la aplicación de un algoritmo sobre el grafo base.
3. **Algoritmos de Proyección Estándar:** En A&AD, los filtros basados en el módulo **SRCD de XBRL GL** y el código `accountingPurposeCode` operan como estos **algoritmos estándar globales de proyección**. Al ejecutar la regla de proyección `TAX`, la base de datos "proyecta" el *Named Graph Tributario*; al ejecutar la regla `FINANCIAL`, "proyecta" el *Named Graph NIIF*.

---

## 5. El Pipeline de Transmutación End-to-End: De la Interfaz al Grafo

El flujo completo de información en la arquitectura A&AD se sintetiza en cinco fases secuenciales:

```
 1. Captura Shift Left       2. Ingesta & Validaciones     3. Normalización & SRCD
┌──────────────────────┐    ┌─────────────────────────┐    ┌──────────────────────┐
│ Altova StyleVision   │ ──►│ BaseX RESTXQ            │ ──►│ Mapeo XBRL GL        │
│ Authentic eForm      │    │ (Rules ISO 15944-16)    │    │ SRCD + Purpose Code  │
└──────────────────────┘    └─────────────────────────┘    └──────────┬───────────┘
                                                                      │
 5. Grafo Inmutable (OeDBTR) 4. Serialización Semántica              │
┌──────────────────────┐    ┌─────────────────────────┐               │
│ TerminusDB via DFRNT │ ◄──│ JSON-LD Payload / Quad  │ ◄─────────────┘
│ (ISO 15944-21 / DLT) │    │ (Named Graph ISO 15944) │
└──────────────────────┘    └─────────────────────────┘
```

1. **Captura Shift Left (`ISO 15944-4`):** El usuario o sistema emisor interactúa con la interfaz gráfica en Altova StyleVision (`.sps` / Authentic eForm). Se capturan las partes (`seller`/`buyer`) y la dualidad recíproca (`vf:commitment`).
2. **Ingesta y Validación (`ISO 15944-16`):** El script `iso15944_ingest.xq` en BaseX intercepta la instancia XML. Si no cumple las restricciones ontológicas y de esquema, es rechazada inmediatamente (*Shift Left*).
3. **Mapeo a XBRL GL Enriquecido (`ISO 15944-5`):** La transacción se traduce a XBRL GL, asociando las cuentas base con el módulo **SRCD** (IFRS/USGAAP/TAX) y asignando el `accountingPurposeCode`.
4. **Serialización a JSON-LD (`ISO 15944-10` / Named Graph):** El documento XML se transmuta a un pasaporte semántico **JSON-LD** (`@context`, `@type`, `@id`, `@graph`), estructurado como un **Named Graph** con su URI única.
5. **Persistencia Inmutable en TerminusDB (`ISO 15944-20/21`):** El payload JSON-LD se inyecta mediante las APIs de **DFRNT** en **TerminusDB**. Esto materializa el verdadero **OeDBTR**: una base de datos de grafos de conocimiento con bitemporalidad e inmutabilidad estricta.

---

## 6. Conclusión: El Triunfo de la Certeza Algorítmica

El trabajo de G. Ken Holman y William McCarthy demostró que las transacciones comerciales son dinámicas y deben gestionarse mediante máquinas de estado. La arquitectura **Accounting & Audit by Design (A&AD)** lleva esta premisa a su máxima expresión operativa al conectar la máquina de estados de **ISO/IEC 15944-21** con el rigor del módulo **SRCD de XBRL GL**, la metáfora del **Named Graph de Charles Hoffman** y la potencia de los **Grafos de Conocimiento en TerminusDB**.

El resultado es un ecosistema donde la contabilidad ya no es una autopsia pasiva de registros pasados, sino un **Grafo Contable-Ontológico Vivo e Incorruptible**, capaz de responder a auditorías en tiempo real bajo cualquier marco regulatorio del mundo.
