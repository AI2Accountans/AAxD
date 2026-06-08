# Framework de Contabilidad y Auditoría por Diseño (Accounting & Audit by Design - A&AD)

Este repositorio contiene la especificación, arquitectura conceptual y el esquema ontológico para el framework de **Contabilidad y Auditoría por Diseño (A&AD)**. Nuestro enfoque busca transformar la contabilidad corporativa tradicional basada en registros relacionales planos en un modelo semántico descentralizado, inmutable y de alta fidelidad, alineando múltiples estándares internacionales en un Grafo de Conocimiento de negocio.

---

## 1. El Enfoque Conceptual (A&AD Matrix)

El framework A&AD organiza la completitud de la empresa mediante una matriz conceptual inspirada en la **Estructura del Zachman Framework**. Esta matriz cruza las dimensiones de negocio (**Aspectos**) con las capas tecnológicas de la Web Semántica (**Capas TBL**):

| Capa / Aspecto | Why (Motivación) | How (Proceso) | What (Dato) | Who (Agente) | Where (Red) | When (Tiempo) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Trust & UI** | Auditoría y Confianza | Workflows de Reporte | Inmutabilidad (Blockchain) | Socios y Firmas | Red de Distribución | Períodos Fiscales |
| **2. Ontology (OWL)** | Reglas Ontológicas | MapForce Transforms | Catálogos (XBRL GL/GRI) | Competencias (1edtech) | Nodos Servidores | Secuencias de Logs |
| **3. RDF (Graph)** | Integridad SHACL | Mapeo ETL JSON-LD | Modelos de Grafo | Identidades de Agentes | APIs GraphQL/WOQL | Enlaces Temporales |
| **4. XML & Namespaces** | Esquemas XSD | Ingestores Locales | Documentos UBL (Invoices) | Clientes de Nodos | Rutas de Almacenamiento | Fechas de Emisión |
| **5. URI / IRI** | Contexto e Idioma | Lógicas de Línea | Identificadores de Conceptos | Certificados y Badges | Direcciones IP | Marcas de Epoch |
| **6. Linked Data Assets** | Retorno Económico | Contenedores en Ejecución | Instancias en DDBB | Sesiones Activas | Tráfico de Red | Logs Operacionales |

*Para un desglose interactivo de esta matriz, visita nuestro [Enterprise Reference Atlas Visual](https://ai2accountans.github.io/Zachman_Framework_Model_Momento0/).*

---

## 2. Evolución del Método Kimball: Del Star Schema al Grafo Semántico

Tradicionalmente, el **Método Kimball** (modelado dimensional con tablas de Hechos y Dimensiones) ha sido el estándar dorado para la estructuración analítica de datos en Business Intelligence. Sin embargo, en la era de la auditoría continua y la automatización por Inteligencia Artificial, el enfoque tradicional presenta límites severos:
*   **Validación Posterior:** Las validaciones de calidad de datos en Kimball se realizan *a posteriori* en procesos ETL, permitiendo que datos inconsistentes entren al almacén transaccional.
*   **Pérdida de Linaje:** Se pierde la relación directa de procedencia entre los hechos resumidos y el documento legal de origen.

**A&AD evoluciona el enfoque de Kimball mediante las siguientes innovaciones:**
1.  **Validación en el Origen (SHACL Guardrails):** En lugar de auditorías retrospectivas, las reglas de negocio y consistencia (como la partida doble o de atribución de contratos) se codifican mediante **SHACL (Shapes Constraint Language)** en el motor de base de datos. Si una transacción no cuadra o carece de linaje, el comando de escritura es rechazado de inmediato.
2.  **Grafo de Procedencia Criptográfica (PROV-O + Blockchain):** Cada hecho financiero en el grafo (`gl-cor:entryDetail`) está enlazado inmutablemente con su documento físico originador (como la factura XML UBL) mediante la propiedad `prov:wasDerivedFrom`. Las transacciones críticas del negocio (como los aportes de socios en el Momento Cero) se anclan a Blockchain (Algorand) para asegurar verdad jurídica indiscutible.
3.  **Flexibilidad Semántica Multiestándar:** A diferencia de las dimensiones rígidas de un Star Schema, el grafo de A&AD puede mapear e integrar de forma nativa múltiples ontologías internacionales (ISO 21838 BFO, REA, Gist, FIBO, y ACTUS) en un único modelo de datos sin necesidad de rediseñar tablas físicas.

---

## 3. Prueba de Concepto (PoC): El "Momento 0" en DFRNT

La viabilidad práctica de esta arquitectura se demuestra en la prueba de concepto **"Momento 0"** (el estado génesis societario y financiero de la firma):
*   **Ingesta Flexible:** Documentos de facturación y escrituras en XML UBL son transformados mediante **Altova MapForce** a formato **JSON-LD** libre de dependencias de formato (resiliencia ante cambios de jurisdicción).
*   **Grafo Activo (DFRNT / TerminusDB):** Los datos se inyectan en TerminusDB, estructurados bajo el esquema unificado `ontology_zachman_sunder_bernerslee.json`.
*   **Downstream Export ("Cuerpo de Cumplimiento Pasivo"):** El grafo actúa como la única fuente de verdad (SSOT). Desde allí, mediante consultas WOQL/GraphQL, el sistema aplana el grafo para exportar y sincronizar diarios tradicionales con ERPs legados o sistemas fiscales. El ERP tradicional opera únicamente como un repositorio pasivo de cumplimiento, protegiendo la pureza del grafo operativo.

---

## 4. Estructura del Repositorio

*   `/Schema JsonLD`: Contiene la definición ontológica consolidada del framework ([ontology_zachman_sunder_bernerslee.json](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Schema%20JsonLD/ontology_zachman_sunder_bernerslee.json)).
*   `/Momento0`: Contiene las instancias de datos demostrativas en formato JSON-LD que representan la constitución de la firma y sus asientos iniciales.
*   `/Documentacion`: Documentos conceptuales y técnicos detallados del framework.
    *   [Especificación Completa de A&AD](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Framework/accounting_audit_by_design_specification.md) (Nueva guía técnica de implementación).
    *   [Semantic Data Pipeline and Ingestion Architecture](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/dfrnt_semantic_accounting_architecture.md).

---

## 5. Licencia y Confort Legal

Este framework es de código abierto y de libre adopción industrial. Todo el material ontológico, esquemas y conceptos contenidos en este repositorio se licencian bajo los términos de la **Licencia Apache 2.0** (ver el archivo `LICENSE` para los términos de uso y distribución). Esta licencia provee la confianza jurídica y el confort necesarios para que corporaciones y desarrolladores incorporen A&AD en sus infraestructuras empresariales comerciales sin regalías.
