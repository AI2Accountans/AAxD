# De GRC-XML a la Web Semántica: Evolución del Cumplimiento como Código (Compliance-as-Code)

La visión de la auditoría continua y el aseguramiento integrado ha sido un objetivo fundamental para organizaciones como el Open Compliance and Ethics Group (OCEG). En su documento fundamental sobre *GRC-XML* (Täbet et al., 2009), se propuso el uso de XBRL y su marco *Global Ledger* (XBRL GL) como el vehículo universal para recolectar evidencia transaccional y mapearla contra marcos de control como COSO y COBIT. 

Sin embargo, el ecosistema tecnológico actual permite llevar esta visión fundacional hacia un nuevo paradigma utilizando Tecnologías de Grafos de Conocimiento (Knowledge Graphs) y la Web Semántica.

## 1. XBRL GL como el "Payload" de Evidencia
La propuesta original de OCEG establece que para probar la efectividad de un control se requiere evidencia estandarizada. En nuestra arquitectura, XBRL GL (a través de sus constructos `EntryHeader` y `EntryDetail`) actúa precisamente como ese *payload*. Sin embargo, al transicionar de las tradicionales instancias XML hacia representaciones en **JSON-LD**, logramos que los asientos contables y eventos económicos se conviertan en Nodos conectados dentro de un Grafo de Conocimiento (ej. TerminusDB).

## 2. Formalización de COSO en Taxonomías Semánticas
Mientras que GRC-XML sugería traducir COSO a esquemas XML rígidos, la Web Semántica nos permite declarar el *GRC Capability Model* como una Ontología (Clases y Propiedades en el Grafo). Esto significa que un "Riesgo de Mercado" o una "Actividad de Control" dejan de ser texto en un PDF para convertirse en entidades vivas que pueden heredar propiedades y conectarse bidireccionalmente con la evidencia contable.

## 3. SHACL como Guardián Activo y "Shift Left"
La verdadera disrupción ocurre en el mecanismo de validación. En lugar de ejecutar reportes a posteriori sobre bases de datos relacionales, introducimos **SHACL (Shapes Constraint Language)**. 

SHACL funciona como el tester automatizado de la evidencia (XBRL GL). Al aplicar el principio de *Shift Left* (mover la validación lo más cerca posible del origen del dato), las formas SHACL evalúan la transacción financiera *antes* de que sea inyectada al Grafo. 

Más importante aún, SHACL permite anotaciones semánticas en sus reglas. Por ejemplo, una regla técnica que restringe la tasa de un contrato (PAM Contract) entre el 8% y el 11%, se anota explícitamente con metadatos que la vinculan a una Actividad de Control de COSO. Si el dato viola el límite, la transacción es rechazada en origen, mitigando el riesgo proactivamente y no reactivamente.

## 4. SPARQL como Motor de Trazabilidad de Auditoría
El eslabón final de esta cadena evolutiva es **SPARQL**. Dado que tanto la evidencia (XBRL GL), el marco de control (COSO) y los validadores (SHACL) conviven bajo el mismo paradigma RDF/Grafo, un auditor puede ejecutar una consulta SPARQL transversal para obtener la matriz de trazabilidad en tiempo real. 

SPARQL puede responder interrogantes como: *"Muestre todos los controles COSO actualmente vigilados por reglas SHACL y liste las instancias XBRL GL que requirieron excepciones aprobadas por el comité en el último trimestre"*.

## 5. Reconocimiento de la Industria: El Caso de la Cloud Security Alliance (CSA)
La transición hacia reportes estructurados de auditoría no es puramente académica, sino un mandato de los marcos más rigurosos de la industria. Un ejemplo de esto es la *Cloud Security Alliance (CSA)*. En su Matriz de Controles (CCM) y su Cuestionario de Evaluaciones de Consenso (CAIQ), específicamente en el dominio de Planeación de Auditoría (Control CO-01), la CSA exige formalmente a los proveedores en la nube: 

> *"¿Produce aserciones de auditoría utilizando un formato estructurado y aceptado por la industria (ej. Ontología CloudAudit, GRC XML, etc.)?"*

La inclusión explícita de GRC-XML y las ontologías semánticas como estándares aceptados por la CSA demuestra que la evolución propuesta en esta arquitectura (utilizar el Grafo y SHACL para generar aserciones de cumplimiento) alinea directamente el ecosistema transaccional con las exigencias de ciberseguridad y gobierno corporativo global.

## Conclusión
La arquitectura aquí propuesta no reinventa la rueda de los dominios contables o de riesgo, sino que toma la arquitectura fundacional de OCEG (GRC-XML + XBRL GL + COSO) y la validación de marcos globales como el de la CSA, y la eleva utilizando el stack tecnológico de la Web Semántica (JSON-LD, SHACL, SPARQL y Bases de Datos de Grafos). El resultado es la materialización del *Continuous Audit* y el *Compliance by Design*.
