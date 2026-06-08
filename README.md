# Framework de Contabilidad y Auditoría por Diseño (Accounting & Audit by Design)

Este repositorio contiene la arquitectura conceptual y el esquema ontológico para el framework de **Contabilidad y Auditoría por Diseño**. Nuestro enfoque busca transformar la contabilidad corporativa tradicional basada en registros relacionales planos en un modelo semántico descentralizado, inmutable y de alta fidelidad, alineando múltiples estándares internacionales.

---

## 1. El Enfoque Conceptual

La contabilidad moderna no debe ser una reconstrucción posterior a los hechos (*after-the-fact*), sino un proceso de **aseguramiento preventivo e inmediato en la fuente**.

Vinculamos cinco niveles conceptuales y estándares de industria dentro de un **Enterprise Reference Atlas (Stack "Momento 0")**:
1. **ISO/IEC 21838-2 (BFO - Basic Formal Ontology):** La raíz ontológica formal que define las entidades continuas (`BFO_Continuant` como agentes, recursos y acuerdos) y las entidades concurrentes (`BFO_Occurrent` como procesos y eventos contables).
2. **REA (Resource-Event-Agent):** Para modelar la semántica conceptual de las operaciones del negocio, superando la ceguera dimensional de la partida doble relacional.
3. **Semantic Arts Gist (14.1.0):** La ontología de alto nivel que sirve de puente conceptual. Redefine la cuenta contable (`gist:Account`) no como un simple código numérico, sino como un *acuerdo de negocio con saldo* (alineado con la visión de Shyam Sunder).
4. **FIBO (Financial Industry Business Ontology):** Introduce clases financieras avanzadas (`FIBO_IncorporationAgreement`, `FIBO_StockCorporation`, `FIBO_Shareholder`) para modelar con precisión los agentes y derechos de propiedad en el Momento Cero del negocio.
5. **ACTUS (Unified Financial Standards):** Modelado de contratos financieros algorítmicos (`ACTUS_Contract`) que permite proyectar flujos de caja y compromisos contractuales de manera determinista.

---

## 2. Automatización desde XBRL GL (Global Ledger)

Para llevar la teoría a la práctica en tiempo de ejecución, el framework utiliza **XBRL GL (Global Ledger)** como el estándar universal de intercambio para capturar los diarios contables y transaccionales directamente desde los sistemas de información fuente.

Para comprender a fondo cómo funciona la recopilación de datos y la automatización mediante XBRL GL, recomendamos la lectura de los siguientes recursos:
* **[Automating XBRL Data Collection and Processing (Altova Blog)](https://www.altova.com/blog/2012/05/new-case-study-automating-xbrl-data-collection-and-processing):** Un análisis detallado sobre cómo se automatizan los flujos de trabajo de auditoría e ingesta de datos a través de motores de mapeo y traducción XML.
* **[Automating XBRL Data (MACPA Case Study)](https://www.altova.com/documents/macpa_casestudy.pdf):** Un caso de estudio real realizado en conjunto con la Asociación de CPAs de Maryland (MACPA), ilustrando la consolidación y el flujo continuo de datos contables en firmas de auditoría usando XBRL GL.

---

## 3. Arquitectura del Grafo y Gobernanza Semántica

* **Gemelo Digital y TerminusDB/DFRNT:** Los datos transaccionales se ingestan en forma de grafos semánticos **JSON-LD**. TerminusDB actúa como la base de datos de grafos maestra, permitiendo consultas rápidas (GraphQL/WOQL) y control de versiones de datos con ramificación (tipo Git).
* **Validación en Tiempo Real (SHACL):** Las reglas de control interno y partida doble se codifican como restricciones **SHACL (Shapes Constraint Language)**. El motor opera bajo la asunción de mundo cerrado, rechazando de manera automática cualquier transacción sin linaje de datos (`prov:wasDerivedFrom`) o descuadrada.
* **Almacenamiento Descentralizado (IPFS):** Los soportes documentales originales (XMLs de facturación electrónica, PDFs de escrituras de constitución) se almacenan en un **Private IPFS Swarm** seguro, vinculando sus identificadores inmutables (CIDs) directamente a las entidades del grafo.

---

## 4. Protección de Propiedad Intelectual

Para salvaguardar los derechos comerciales y la propiedad intelectual del framework:
* Este repositorio público aloja las **definiciones ontológicas del esquema conceptual y de los datos de salida demostrativos**.
* Los componentes mecánicos y la lógica interna de traducción (scripts ETL de traducción de QNames XML, archivos de mapeo `.mfd` de Altova MapForce, y flujos de automatización de compilación) son **estrictamente confidenciales y están excluidos del control de versiones**.

---

## 5. Licencia

Este proyecto está bajo los términos de la licencia especificada en el archivo `LICENSE` de este repositorio.
