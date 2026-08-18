# Glosario Esencial de A&AD
*Términos clave explicados para no-tecnólogos.*

Para entender el futuro de la contabilidad y la auditoría, debemos hablar el mismo idioma. Este glosario traduce conceptos técnicos avanzados en definiciones prácticas.

---

### ACTUS (Algorithmic Contract Types Unified Standards)
**En simple:** La calculadora matemática para predecir contratos financieros hacia el futuro.  
**En detalle:** Estándar internacional (en camino a ISO/IEC) que modela contratos financieros (como préstamos, bonos y derivados) como máquinas de estado deterministas. En lugar de tratar un contrato como un documento estático en PDF, ACTUS calcula algorítmicamente todos los eventos de flujo de efectivo futuros condicionados a tasas y reglas de mercado.

### Algoritmo de Proyección Estándar (Global Projection Algorithm)
**En simple:** La "lente" o regla computacional que transforma los datos contables puros de la empresa en un informe financiero o fiscal específico sin duplicar la base de datos.  
**En detalle:** Concepto formulado en el reporte financiero digital por Charles Hoffman. En lugar de duplicar información o mantener sistemas paralelos para impuestos (TAX) y NIIF/IFRS, toda la realidad económica (fuentes, eventos, contratos) reside en una sola base de datos de grafos (TerminusDB). Un Algoritmo de Proyección es una regla determinista (basada en el módulo SRCD de XBRL GL y `accountingPurposeCode`) que "proyecta" un *Named Graph* con la visión contable requerida de manera instantánea e inalterable.

### Bitemporalidad (Bitemporality)
**En simple:** Una máquina del tiempo para los datos.  
**En detalle:** Una base de datos bitemporal guarda dos tipos de tiempo para cada transacción: *cuándo ocurrió el evento en el mundo real* y *cuándo quedó registrado en el sistema*. Esto permite a los auditores saber exactamente "qué sabía la empresa y en qué momento preciso lo supo", eliminando la posibilidad de alterar la historia.

### BPMN (Business Process Model and Notation)
**En simple:** El mapa del flujo de trabajo y del tiempo en la empresa.  
**En detalle:** Estándar de la OMG que representa los procesos de negocio y workflows por los que viaja la información. Mientras SBVR define qué significan los conceptos, BPMN orquesta la dimensión temporal: *cuándo* y *cómo* se ejecutan las actividades que generan los eventos de negocio.

### Certeza Algorítmica (Algorithmic Certainty)
**En simple:** Verdad matemática, no opinión humana.  
**En detalle:** El estado en el que la confianza en un reporte financiero no proviene de la revisión humana o de "muestras", sino de reglas matemáticas inflexibles integradas en la propia base de datos (ver *Mundo Cerrado*).

### DFRNT
**En simple:** La interfaz visual para construir y administrar Gemelos Digitales Semánticos.  
**En detalle:** Una plataforma de datos enfocada en modelar conocimiento (grafos) de forma visual. Permite gestionar reglas de negocio complejas sin ser un ingeniero de software, sirviendo de puente entre la mente del arquitecto empresarial y la base de datos (TerminusDB).

### Evento (Event)
**En simple:** Cualquier suceso que altere la realidad económica o el riesgo futuro de la empresa.  
**En detalle:** Va más allá de un "asiento de diario" tradicional. Un Evento es la piedra angular del *Libro de Eventos de Negocio*. Firmar un nuevo contrato es un evento; pagar una cuota es un evento transaccional; y el cambio de una tasa de inflación o riesgo identificado que afecta la viabilidad financiera también es un evento. En A&AD, todo se captura como un nodo de Evento inmutable antes de convertirse en contabilidad.

### Gemelo Digital Semántico (Semantic Digital Twin)
**En simple:** Una réplica virtual y viva de la empresa.  
**En detalle:** No es solo una copia en 3D o un panel de control (*dashboard*). Es un modelo de datos interconectado que representa todos los activos, reglas, contratos y transacciones de una organización, permitiendo que la inteligencia artificial "comprenda" a la empresa.

### Holón
**En simple:** Un bloque de construcción que es un todo y una parte a la vez.  
**En detalle:** En A&AD, un "Holón Inmutable" (como el *Momento Cero*) es un bloque de datos que tiene sentido por sí mismo, pero que también sirve como el cimiento sobre el cual se construyen los reportes futuros de toda la organización.

### JSON-LD (Linked Data)
**En simple:** Un archivo de texto que se comporta como un organismo vivo y conectado.  
**En detalle:** A diferencia de un archivo JSON tradicional (que almacena datos planos y aislados que la máquina no comprende), JSON-LD inyecta identidad matemática y semántica a través de tres propiedades especiales (`@id`, `@type`, `@context`). Esto convierte un simple texto en un "nodo" inteligente que el motor de grafos (como TerminusDB) puede fusionar, clasificar e interconectar automáticamente con el resto del universo de conocimiento de la empresa.

### Payload Estándar W3C (W3C JSON-LD Payload)
**En simple:** El pasaporte biométrico internacional de los datos contables.  
**En detalle:** Es la carga útil de información (*payload*) estructurada en formato W3C JSON-LD que se transmite entre APIs, webhooks y redes de eventos contables (*Event Ledgers*). A diferencia de un JSON tradicional (que es un mensaje "mudo" que requiere parsers a la medida), un Payload Estándar W3C es auto-descriptivo (*Self-Describing*): incluye su propio diccionario semántico (`@context`), preserva la precisión matemática estricta (`xsd:decimal`) y puede ser ingerido e interpretado de forma instantánea por cualquier motor de grafos o agente de Inteligencia Artificial en el mundo sin necesidad de escribir código parser adicional.


### Momento Cero (Moment 0)
**En simple:** El Big Bang de la confianza.  
**En detalle:** Es el balance de apertura inicial de la empresa, estructurado en un formato universal (XBRL GL) y sellado criptográficamente por un auditor. Es el punto de partida inalterable; cualquier transacción futura se calcula a partir de este punto con precisión absoluta.

### Named Graph (Grafo Nombrado)
**En simple:** Un "sobre" o contenedor semántico con su propia etiqueta digital que agrupa un conjunto de datos contables o contractuales.  
**En detalle:** Concepto de la arquitectura del Web Semántico (RDF Quads) popularizado en el reporte financiero digital por Charles Hoffman como la metáfora de "un informe o un contrato". En lugar de tener afirmaciones o datos contables flotando sueltos en una tabla, un Named Graph asigna un identificador único (IRI) a un grupo completo de triplas. Esto permite adjuntar metadatos al contenedor entero (quién lo firmó, sello de tiempo, procedencia), gestionar controles de acceso granulares y almacenar múltiples visiones contables (NIIF vs. TAX) dentro de la misma base de datos sin colisión de nombres.

### Mundo Cerrado (Closed World Assumption - CWA)
**En simple:** "Si no está registrado, no pasó."  
**En detalle:** Un principio lógico usado en TerminusDB. En un sistema de mundo cerrado, si una transacción no cumple estrictamente con las reglas o carece de información, el sistema la rechaza inmediatamente. Esto impide la creación de estados financieros inconsistentes, matando el concepto del "asiento de ajuste".

### One Semantic Pipeline (Pipeline Semántico Unificado)
**En simple:** La tubería continua donde los datos viajan desde la operación hasta el reporte financiero sin perder su significado en el camino.  
**En detalle:** Arquitectura semántica integrada donde cada estándar actúa en una capa específica: SBVR y BPMN definen vocabulario y workflow; UBL captura el documento fuente; ACTUS proyecta contratos; REA interpreta la dimensión económica; XBRL GL preserva la trazabilidad inmutable; y las Taxonomías XBRL (US GAAP/IFRS) generan el reporte externo.

### QOWL (GraphQL over OWL)
**En simple:** Un traductor para interrogar a tu base de datos.  
**En detalle:** Un lenguaje de consulta que permite a los humanos (y a la IA) hacer preguntas complejas a un Gemelo Digital, obteniendo respuestas precisas.

### REA (Resources, Events, Agents / ISO 67199)
**En simple:** La anatomía y semántica contable de un negocio.  
**En detalle:** Modelo ontológico contable (estandarizado bajo ISO/IEC 67199) que transforma documentos comerciales (como una factura UBL) en eventos económicos con significado contable real (determinando qué cuenta, el débito/crédito y el momento de acumulación/causación), relacionando Recursos, Eventos y Agentes.

### Reificación (Reification)
**En simple:** Convertir una idea o relación abstracta en un "objeto" real y auditable que la máquina puede procesar.  
**En detalle:** En la Web Semántica y en A&AD, reificar significa tomar algo abstracto (como la relación contractual entre dos empresas, una estimación actuarial o un evento de riesgo) y transformarlo en un Nodo de datos explícito (como tu `ACTUS_Contract` en JSON-LD) con sus propios atributos (identidad, fecha de creación, agente responsable). Esto permite que la IA audite la existencia y evolución del concepto mismo, no solo sus consecuencias numéricas en un balance.

### SBVR (Semantics of Business Vocabulary and Business Rules)
**En simple:** El diccionario y reglamento formal que hace de puente entre los líderes del negocio y los programadores.  
**En detalle:** Estándar formal de la OMG que permite expresar reglas de negocio y gobernanza en lenguaje natural, pero con una interpretación estricta en lógica formal interpretable por máquinas. En A&AD, SBVR actúa como el "pegamento semántico" que une los vocabularios de UBL, REA, ACTUS y XBRL.

### Semantic Ricordance Plane
**En simple:** El registro maestro de la realidad económica y el futuro de la empresa.  
**En detalle:** Un concepto que moderniza el "Memorial" (*Ricordanze*) de Luca Pacioli mediante la tecnología actual. Representa un plano de datos (Data Plane) donde todas las transacciones, eventos y condiciones que afectan a la entidad —tal como lo propone Charles Hoffman en su visión del "libro de eventos"— se modelan semánticamente de manera estandarizada. Este plano dota al sistema de la capacidad de razonar y "recordar" la totalidad de la operativa y los riesgos del negocio, mucho antes de ser procesado por la contabilidad tradicional de doble partida.

### SHACL
**En simple:** El guardia de seguridad de los datos.  
**En detalle:** Un lenguaje informático utilizado para validar que la información entrante cumpla con las reglas del negocio (ej. "Toda factura debe tener un NIT válido") antes de entrar al Gemelo Digital.

### TerminusDB
**En simple:** La bóveda incorruptible.  
**En detalle:** Una base de datos diseñada para manejar Grafos de Conocimiento (Knowledge Graphs) de manera inmutable (como Git) y bitemporal. Es el motor técnico que hace posible la Auditoría por Diseño.

### Taxonomías XBRL (US GAAP / IFRS)
**En simple:** El diccionario oficial regulatorio para presentar estados financieros al mercado.  
**En detalle:** Marcos estandarizados (desarrollados por FASB e IFRS Foundation) expresados en XBRL que estructuran los balances y estados de resultados finales. Reciben los datos agregados provenientes de diarios XBRL GL y permiten a reguladores, inversionistas y la IA consumir reportes financieros estructurados sin ambigüedades.

### UBL (Universal Business Language / ISO 66370)
**En simple:** El formato nativo e inteligente para documentos comerciales del mundo real.  
**En detalle:** Estándar ISO/IEC (66370) que estructura documentos como facturas, órdenes de compra y guías de despacho. Representa el principio de *Shift Left*: el documento digital ES la fuente de verdad y el evento operacional con semántica intrínseca ("quién hizo qué, cuándo y por qué").

### Vault-LD
**En simple:** El formato de memoria para los Agentes de IA.  
**En detalle:** Un patrón arquitectónico que inserta *Linked Data* (YAML-LD) dentro del encabezado (*frontmatter*) de un archivo de texto Markdown. Permite que documentos legibles por humanos se conviertan en nodos semánticos (holones) conectados a un Grafo de Conocimiento global. Esto resuelve el problema de escalabilidad en la memoria de los agentes de Inteligencia Artificial sin depender de bases de datos centralizadas.

### XBRL GL (Global Ledger)
**En simple:** El esperanto de la contabilidad transaccional.  
**En detalle:** Estándar de XBRL International que sirve como el rastro de auditoría universal e inmutable. Actúa como puente entre los documentos operacionales (UBL), contratos (ACTUS) y el diario contable interno, manteniendo la proveniencia estructural de cada asiento hacia el evento original.

### YAML-LD
**En simple:** Un puente semántico fácil de leer.  
**En detalle:** Un estándar (en proceso de adopción por la W3C) que transforma el formato YAML en *Linked Data*. Funciona igual que JSON-LD en la web, pero es mucho más amigable para que humanos y Agentes de IA lo lean y escriban directamente en sus archivos locales, permitiendo que simples notas se conecten a un contexto global compartido.

### Zero-Shot Auditing
**En simple:** Auditoría en piloto automático, sin entrenamiento previo.  
**En detalle:** La capacidad de un Agente de Inteligencia Artificial para auditar el 100% de las transacciones de una empresa analizando las reglas y los datos directamente, sin necesidad de que un humano le enseñe casos específicos.
