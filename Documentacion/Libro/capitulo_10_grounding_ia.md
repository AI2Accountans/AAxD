# Capítulo 10: Auditoría Zero-Shot y el Verdadero Grounding

El estado del arte de la Inteligencia Artificial reconoce un hecho ineludible: para lograr agentes autónomos reales, se necesita *Grounding* (Anclaje). Sin embargo, el mercado corporativo actual comete el grave error de creer que el "Grounding" significa simplemente vectorizar un lote de archivos PDF y hacer que la IA busque fragmentos de texto dentro de ellos (una técnica conocida como RAG o Generación Aumentada por Recuperación).

El RAG no es suficiente para la auditoría ni para las finanzas. Vectorizar un contrato en PDF no le enseña a la máquina cómo calcular una tasa de interés compuesta, ni previene que la IA invente números (alucine) cuando se le somete a preguntas complejas de liquidez.

Como magistralmente explica el arquitecto de software Kurt Cagle, el verdadero *Grounding* es un problema de **gestión de estados**. Para que una IA agéntica sea coherente, persistente y autónoma a lo largo del tiempo sin sufrir degradación de memoria, requiere cuatro tipos de anclajes estructurales. La arquitectura de *Accounting and Audit by Design* (A&AD) provee exactamente estos cuatro anclajes, no a través de texto, sino de matemáticas y grafos.

Esta integración de anclajes estructurales es lo que hace posible el salto hacia la **Auditoría Zero-Shot**. El concepto original de "Zero-Shot Learning" en inteligencia artificial, formalizado por Palatucci et al. (2009), se basó en el uso de "Semantic Output Codes" (Códigos de Salida Semánticos). Este enfoque demostró que un modelo no necesita adivinar ni requerir ejemplos previos de entrenamiento si las clases están definidas por una base de conocimiento semántica estricta. Al llevar este principio a las finanzas corporativas, las ontologías de la Web Semántica (XBRL GL, SKOS) actúan exactamente como estos *Semantic Output Codes*.

## 1. Denotative Grounding (Anclaje de Tipo y Definición)
El anclaje denotativo establece los criterios estrictos de membresía a una clase. Define qué características tiene un elemento y qué restricciones aplican. Si esto falla, el sistema sufre de *Semantic Drift* (desviación semántica), donde los conceptos pierden su significado original a medida que la IA opera.

**La Solución A&AD:** 
Este nivel está gobernado por el Diccionario del estándar **ACTUS** y las taxonomías de **XBRL GL**. A través de motores de transformación como Altova MapForce, los datos crudos se obligan a encajar en moldes rígidos y estandarizados globalmente. Un contrato *Principal At Maturity* (PAM) tiene propiedades explícitas y restrictivas. No hay espacio para que la IA "interprete" qué significa la tasa de interés; el tipo está blindado criptográficamente por diseño.

## 2. Instantive Grounding (Anclaje de Identidad)
Este nivel identifica individuos únicos y mantiene esa diferenciación a lo largo del tiempo. Los Modelos de Lenguaje Grandes (LLMs) son inherentemente deficientes aquí porque su memoria de contexto es una cola de mensajes (un flujo continuo), no un registro persistente. Si una conversación se alarga, la IA olvida las identidades y sufre *Attribute Drift* (mutación de atributos).

**La Solución A&AD:**
Se resuelve mediante **JSON-LD** y los identificadores únicos (`@id`) persistidos en bases de datos de grafos como **TerminusDB**. Al transmutar una transacción a un grafo semántico, cada contrato, cada cliente y cada asiento contable recibe una URI (Uniform Resource Identifier) única e inmutable. El agente de IA no tiene que esforzarse en recordar la identidad en su ventana de corto plazo; simplemente consulta el nodo persistente del grafo, garantizando que los atributos jamás muten por error del modelo.

## 3. Temporal Grounding (Anclaje de Procedencia)
El anclaje temporal registra la línea de tiempo inmutable: cuándo cambió algo, qué actor lo causó y qué afectó aguas abajo. Cagle establece una premisa lapidaria: *"Un LLM no hace aritmética ni contabilidad intrínsecamente; ese trabajo debe delegarse a procesos mejor equipados, y el modelo necesita saber qué concluyeron esos procesos y cuándo"*. Si este anclaje falla, hay *Provenance Loss* (pérdida de trazabilidad).

**La Solución A&AD:**
Esta es la justificación absoluta del uso de microservicios matemáticos aislados (como el motor `actus-webapp`) y la Bóveda Semántica. No le permitimos a la IA realizar matemáticas financieras complejas; se la delegamos al ejecutable determinístico de ACTUS. El resultado (los flujos de caja proyectados) se sella en el grafo de conocimiento utilizando las ontologías de la W3C (**PROV-O**). Esto registra el `prov:generatedAtTime` (cuándo) y el `prov:wasAttributedTo` (quién), asegurando el linaje forense de cada dato.

## 4. Spatial Grounding (Anclaje de Contención)
El anclaje espacial significa entender dónde está algo respecto a otra cosa mediante estructuras anidadas de contenedores o fronteras lógicas. La contención protege el estado interno de la corrupción mientras el sistema procesa interacciones externas. Sin fronteras claras, los datos terminan disolviéndose en el caos.

**La Solución A&AD:**
Esto se materializa en el concepto de **Holón** y las ramas aisladas (branches tipo Git) en **TerminusDB**. Al tratar cada contrato algorítmico como una entidad soberana y autocontenida (un Holón Semántico), impedimos que los datos se corrompan entre sí. Además, los entornos de simulación financiera pueden ejecutarse en ramas separadas que actúan como contenedores lógicos (*sandboxes*), donde la IA puede interactuar, proyectar futuros y estresar escenarios de riesgo sin alterar jamás la base de datos inmutable de producción.

## Conclusión: El Nacimiento de la Auditoría Zero-Shot

Cuando una arquitectura de sistemas integra los cuatro pilares (Tipo, Identidad, Procedencia y Contención), el comportamiento de la IA se transforma. Ya no dependemos de *prompts* elaborados ni de rezar para que el modelo no "adivine" o alucine. Hemos creado una infraestructura donde la máquina puede auditar el 100% de las transacciones financieras en tiempo real y con cero contexto externo preentrenado (*Auditoría Zero-Shot*), porque el contexto ya vive —inmutable, semántico y matemático— dentro del grafo de conocimiento.
