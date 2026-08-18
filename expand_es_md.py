import re

# File Paths
es_md_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrativa_ES.md"
en_md_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Memoria\Momento_0_Narrative_EN.md"

# Let's load Spanish markdown
with open(es_md_path, 'r', encoding='utf-8') as f:
    es_content = f.read()

# 1. Update Genesis (Momento 0) in ES
target_genesis_es = """### ¿Qué es el "Momento 0" (Estado Génesis)?
El término **"Momento 0" (Génesis)** no es un concepto abstracto; define el **Estado de Nacimiento Legal, Societario y Financiero de la firma**. Es el nodo origen e inmutable del grafo contable, constituido por el Balance de Apertura auditado, la Escritura de Constitución oficial y la estructura accionaria inicial. A partir de este "Momento 0", cada transacción subsecuente se registra como una derivación determinista, inmutable y criptográficamente verificable del estado anterior, permitiendo reconstruir la historia de la empresa desde su primer segundo de vida con total certeza jurídica."""

replacement_genesis_es = """### ¿Qué es el "Momento 0" (Estado Génesis) y la Inmutabilidad de los Hechos Económicos?

Siguiendo la línea fundacional de **Shyam Sunder (Scheinman-Sonder)** en la teoría de la contabilidad y el control (la empresa como un nexo de contratos), el **Contrato de Constitución** o la escritura que da origen a la entidad representa el documento fundacional que se inyectará en el **Momento Cero (Estado Génesis)**. Tratándose de una empresa que ya se encuentra en marcha, el Génesis lo constituirá un **Balance de Apertura auditado**. 

Para garantizar una inmutabilidad y transparencia absoluta y legalmente vinculante, estos documentos iniciales (Escritura de Constitución y/o Balance de Apertura) se alojarán de forma descentralizada en **IPFS (InterPlanetary File System)**. Mediante el anclaje en una **red blockchain**, se sellará su inalterabilidad histórica, y el identificador criptográfico único (el **CID de IPFS**) quedará registrado de forma permanente dentro de la instancia JSON-LD génesis que se inyectará a **TerminusDB**.

En este punto fundacional, es crítico identificar con precisión a los accionistas y las entidades que aportan al capital social. El grafo semántico está diseñado con la capacidad de estructurar y rastrear estas relaciones de propiedad, permitiendo generar vistas dinámicas en tiempo real que den cuenta exacta de los propietarios y su participación en un momento determinado. Para asegurar la inmutabilidad y certeza jurídica de este registro de socios frente a cualquier auditoría o ente regulador, el estado de la tenencia accionaria se sella criptográficamente en la blockchain de **Algorand**."""

es_content = es_content.replace(target_genesis_es, replacement_genesis_es)

# 2. Update SHACL section in ES
target_shacl_es = """### SHACL: "Contabilidad y Auditoría por Diseño"
**SHACL (Shapes Constraint Language)** es la tecnología del W3C que nos permite implementar la **Auditoría por Diseño** directamente en el motor de base de datos, antes de generar cualquier reporte:
*   **¿Cómo funciona?** En lugar de validar los datos *después* de que se escribe el reporte financiero, los SHACL *Shapes* (formas de restricción) validan la estructura e integridad del grafo en tiempo real al momento de la ingesta.
*   **Reglas Contables Nativas:** Podemos definir SHACL Shapes para forzar lógicas contables irrompibles en el grafo:"""

replacement_shacl_es = """### SHACL: "Contabilidad y Auditoría por Diseño" (El Equivalente a las Linkbase de Fórmulas)

**SHACL (Shapes Constraint Language)** es la tecnología del W3C que nos permite implementar la **Auditoría por Diseño y el Control Interno** directamente en el motor de base de datos. En este stack contable semántico, **SHACL representa el equivalente tecnológico a las "Linkbase de Fórmulas" (Formula Linkbases) dentro del estándar XBRL tradicional**. 

*   **Control Interno por Diseño y Equivalencia a Linkbases:** Al igual que las fórmulas XBRL validan consistencias lógicas y matemáticas en los reportes financieros externos, los SHACL *Shapes* (formas de restricción) operan como el mecanismo definitivo de control interno en la base de datos de grafos de **TerminusDB**, imponiendo restricciones y condiciones al momento exacto en que un dato es inyectado. El motor rechaza de forma nativa cualquier transacción que no cumpla con estas reglas estructurales y de negocio desde el primer milisegundo de su existencia, garantizando el control interno de la entidad por diseño.
*   **Reglas Contables y de Control:** Podemos definir SHACL Shapes para forzar lógicas contables irrompibles en el grafo:"""

es_content = es_content.replace(target_shacl_es, replacement_shacl_es)

# 3. Update XBRL-GL Ontology in ES
target_ont_es = """*   **Ontología Transaccional Custom:** Ante la falta de un estándar oficial en la Web Semántica (confirmado por Eric Cohen), traducimos la taxonomía **XBRL GL (Global Ledger)** a un modelo semántico nativo en JSON-LD."""

replacement_ont_es = """*   **Ontología Transaccional Custom y Soporte de DFRNT:** Ante la falta de un estándar oficial en la Web Semántica para la contabilidad transaccional (confirmado por Eric Cohen), traducimos la taxonomía **XBRL GL (Global Ledger)** a un modelo semántico nativo en JSON-LD. **El diseño y refinamiento de esta ontología de XBRL-GL es un tema de alta especialización y complejidad técnica, por lo cual se requerirá una estrecha colaboración y soporte técnico por parte del equipo de DFRNT**. Utilizando la suscripción activa de DFRNT para la definición del producto, se estructurarán las características y constraints de esta ontología para garantizar que las instancias **JSON-LD** inyectadas en la base de datos de **TerminusDB** empaten y validen perfectamente con el esquema semántico empresarial."""

es_content = es_content.replace(target_ont_es, replacement_ont_es)

# 4. Update MapForce and add XForms / BaseX in ES
target_mapforce_es = """*   **Ingeniería de Ingesta con Altova MapForce (Flexibilidad de Jurisdicción y Formatos):** Se establece como pilar clave que mediante herramientas de mapeo, específicamente **Altova MapForce**, se generará el documento a partir de las diferentes fuentes a formato **JSON-LD** para que sea inyectado directamente en el grafo de conocimiento de **TerminusDB**. **Es crucial destacar la alta portabilidad y resiliencia de este enfoque: si una jurisdicción no maneja UBL para la facturación sino que usa JSON, XML personalizado o cualquier otro lenguaje, no se requiere realizar grandes cambios en el núcleo del stack contable. La arquitectura y sus reglas de validación permanecen intactas, siendo únicamente necesario ajustar la definición de la fuente origen en el mapeador visual de MapForce.** Esto desacopla el cumplimiento local de la base de datos semántica empresarial."""

replacement_mapforce_es = """*   **Doble Canal de Ingesta Semántica (Altova MapForce y W3C XForms):** 
    1. **Tubería Altova MapForce (Documentos Electrónicos):** Los contratos y documentos transaccionales se procesan (sean electrónicos o físicos). En el caso de documentos estructurados como facturas **UBL 2.1 (XML)**, se transforman directamente a **JSON-LD** utilizando un script visual de mapeo diseñado en **Altova MapForce**, donde se le inyecta la semántica contable requerida para su integración en el grafo. **Es crucial destacar la alta portabilidad de este enfoque: si una jurisdicción no maneja UBL sino que usa JSON u otros formatos, no se altera el núcleo del stack; solo se ajusta la definición de la fuente origen en MapForce.**
    2. **Tubería XForms y BaseX (Captura de Datos Interactiva):** Para la entrada manual y parametrizada de datos, el autor cuenta con experticia en el uso de **XForms** (el estándar de la W3C para formularios enriquecidos). Con esto, se capturan los datos de entrada directamente hacia una base de datos XML estructurada (**BaseX**) alojada en un servidor en la nube de **DigitalOcean**. Una vez almacenados en BaseX, los datos son extraídos, transformados en formato **JSON-LD** mediante scripts de automatización e inyectados de forma nativa a **TerminusDB** para poblar el grafo semántico empresarial."""

es_content = es_content.replace(target_mapforce_es, replacement_mapforce_es)

# 5. Add ESG, Sustainability (ISSB, GRI, EFRAG), Inventory, Entry Purposes (IFRS, Fiscal, local GAAP) and Auto-Reconciliation in ES
# Let's insert this under "Generación de Instancias de Reporte Financiero (XBRL FR) y Formatos Físicos"
target_reports_es = """        *   **PDF y Word (DOCX):** Renderizado estético y estructurado de alta fidelidad para revisiones editoriales de la junta directiva, firmas físicas, archivos y cumplimiento legal."""

replacement_reports_es = """        *   **PDF y Word (DOCX):** Renderizado estético y estructurado de alta fidelidad para revisiones editoriales de la junta directiva, firmas físicas, archivos y cumplimiento legal.
*   **Información No Financiera, ESG e Inventarios:**
    Los documentos electrónicos (como facturas UBL o contratos) contienen valiosa información no financiera que es crucial para operaciones y cumplimiento de reportes. El stack extrae estos datos directamente para alimentarlos al grafo:
    *   *Sostenibilidad y Clima:* Se extraen datos no financieros de impacto climático y sostenibilidad embebidos en contratos y facturas, alimentando el grafo para poblar taxonomías internacionales como las de **ISSB**, **GRI** y **EFRAG** (EFRAC).
    *   *Control de Inventarios:* Los detalles cuantitativos y de ítems físicos se extraen de los documentos origen e ingresan directamente al grafo contable, alimentando en tiempo real los sistemas de control de inventarios de la firma.
*   **Propósito de Asiento Contable Multi-Libro (XBRL GL Purposes) y Auto-Reconciliación:**
    De acuerdo con la taxonomía XBRL Global Ledger, el stack permite asociar explícitamente el **Propósito Contable** (`purpose`) a cada apunte, facilitando la contabilidad multi-libro y el reporte multijurisdiccional:
    *   *Fiscal / Tributario:* Registros enfocados en el cumplimiento de impuestos y normativas de la jurisdicción local.
    *   *IFRS / NIIF:* Enfocado en reportes financieros bajo estándares internacionales, el cual rige transacciones, documentos, eventos (riesgos) y condiciones (contratos) de la jurisdicción del autor. El stack está diseñado para dar alcance pleno a IFRS, pero mantiene la posibilidad de cubrir otros marcos conceptuales.
    *   *Juzgada / Local GAAP:* Registros para el cumplimiento de normativas locales e históricas específicas de la entidad.
    *   *Auto-Reconciliación:* Al residir la información en un grafo de relaciones continuas, el stack está en capacidad de **auto-reconciliar de forma nativa la información contable** dentro del grafo, cruzando de manera determinista los hechos de tesorería, inventarios y contratos sin necesidad de rutinas de conciliación externas."""

es_content = es_content.replace(target_reports_es, replacement_reports_es)

# 6. Update Episode 7 detail and add the 7-Episode Roadmap & Book concluding section in ES
target_ep7_es = """#### Episodio 7: The Zachman Semantic Fusion Unveiled
*   **Foco Contable:** La presentación de la matriz de fusión final. Demostrar cómo las taxonomías y modelos de reporte de **Charlie Hoffman** y la arquitectura operacional basada en REA y TerminusDB de **Richard Gasca** se fusionan en un único grid de completitud que representa el futuro de los sistemas empresariales en la era de la IA."""

replacement_ep7_es = """#### Episodio 7: The Zachman Semantic Fusion Unveiled
*   **Foco Contable:** La presentación de la matriz de fusión final. Demostrar cómo las taxonomías y modelos de reporte de **Charlie Hoffman** y la arquitectura operacional basada en REA y TerminusDB de **Richard Gasca** se fusionan en un único grid de completitud que representa el futuro de los sistemas empresariales en la era de la IA.

---

### Plan del Libro "Contabilidad Semántica" (Primera Edición)

El acuerdo colaborativo establecido con la entidad **DFRNT** plantea que una vez que se completen de manera exitosa los **7 episodios** de la serie de liderazgo intelectual, estos servirán como los hitos físicos y conceptuales estructurados de desarrollo. 

Este camino metodológico consolidará los fundamentos de lo que se convertirá en el libro fundacional de **"Contabilidad Semántica" (Semantic Accounting)**. Este libro no solo presentará la teoría formal del stack de forma internacional, sino que dará el paso definitivo para el lanzamiento y despliegue oficial de la **primera versión productiva** del software, marcando un hito en la transición global hacia sistemas de información empresarial autogobernados y lógicamente perfectos."""

es_content = es_content.replace(target_ep7_es, replacement_ep7_es)

# Save updated Spanish file
with open(es_md_path, 'w', encoding='utf-8') as f:
    f.write(es_content)
print("Spanish Markdown successfully updated!")
