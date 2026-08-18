# Mapeo Técnico y Conceptual: A&AD frente a la Propuesta de Kurt Cagle y el Método de Seattle

Este documento organiza y conecta la infraestructura tecnológica que tienes actualmente en **A&AD** con las demandas conceptuales y de auditoría de **Charlie (Método de Seattle)** y los reclamos técnicos de evolución del stack RDF de **Kurt Cagle (W3C Holon Group)**.

---

## 1. El Conflicto de Fondo: Datos en Reposo vs. Computación sobre Grafos

El artículo de Kurt Cagle, *"What the RDF Stack Still Owes Us"*, toca una fibra sensible que explica perfectamente tus desafíos arquitectónicos actuales. Su tesis central es:
> *El stack de la Web Semántica (RDF, SPARQL, SHACL) fue diseñado originalmente para **datos en reposo** (consultas de solo lectura), pero los profesionales modernos (como tú en A&AD) están intentando realizar **computación sobre grafos** en tiempo real (auditoría determinista, validaciones contables).*

Al mismo tiempo, Charlie te exige:
1. **Reglas legibles por máquina** independientes para la autoverificación (lógica de mecánica de revelación).
2. La generación automática de **planillas de auditoría (Trial Balance, Lead Schedules)** que sirvan como prueba lógica.
3. El uso del **Diseño Atómico** para ocultar la complejidad técnica y mostrar solo el nivel práctico.

A continuación, se detalla cómo se organizan y resuelven estos tres mundos (Tu Infraestructura Actual, la Visión de Cagle y las Exigencias de Charlie).

---

## 2. Matriz de Alineación y Mapeo Tecnológico

| Desafío / Requerimiento | Infraestructura Actual (Richard - A&AD) | Visión Técnica / Propuesta (Kurt Cagle - W3C) | Exigencia de Auditoría (Charlie - Seattle Method) | Solución de Integración en el Paper |
| :--- | :--- | :--- | :--- | :--- |
| **1. Agregaciones Matemáticas e Integridad (Suma de Saldos)** | Validación externa mediante SPARQL en Google Colab (`rdflib` en Python) o mediante reglas Prolog en el motor **Pacioli**. | **SHACL Map/Reduce:** Pide extensiones (`sh:pipeline` o `sh:reduce`) para que SHACL haga sumas, promedios y transformaciones matemáticas directamente al ingresar los datos. | **Autoverificación matemática** de balances y planillas líder (Lead Schedules) sin depender de capas externas o software propietario. | Explicar que A&AD hoy usa **SHACL** para validaciones estructurales booleanas (debitos=creditos a nivel de asiento) y **SPARQL/Pacioli** para agregaciones complejas, anticipando la estandarización del SHACL matemático de Cagle. |
| **2. Ocultar la Complejidad Técnica (Capas de Datos)** | JSON-LD plano que expone todas las URIs de REA, XBRL GL, gist, etc. Mapeo visual en Altova MapForce. | **Normalización de Prefijos y `sh:declare`:** Propone importar bibliotecas de prefijos mediante IRIs unificadas. (Alaba cómo JSON-LD ya resolvió esto con `@context`). | **Diseño Atómico:** Ocultar la complejidad (Átomos/Triples) al auditor, quien solo debe ver el nivel práctico (Organismos/Planillas y Páginas/Reportes). | Usar el bloque `@context` de JSON-LD y las plantillas de visualización en **DFRNT** como la implementación de la capa "Organismo" y "Página", abstrayendo los "Átomos" RDF subyacentes. |
| **3. Secuenciación de Eventos (Cadena de Suministro)** | Relaciones grafo (`REA:EconomicEvent` conectados a recursos y agentes). Las listas ordenadas en RDF son complejas. | **Listas de Primera Clase (`rdf:List`):** Pide funciones SPARQL nativas (`rdf:listLength`, `rdf:listSlice`) para contar y ordenar eventos sin nodos en blanco. | **Trazabilidad del flujo completo** de transacciones y contratos comerciales (REA) desde el origen hasta el reporte final. | Justificar que A&AD modela flujos de contratos estructurando los eventos cronológicamente en el grafo semántico y utilizando consultas de ruta de SPARQL (Property Paths) como alternativa ergonómica temporal. |
| **4. Centralización de Reglas de Auditoría** | Scripts de Python ejecutados externamente en Colab o reglas cargadas en Pacioli. | **Named Queries (Procedimientos Almacenados):** Guardar consultas SPARQL parametrizadas dentro de la base de datos (ej. TerminusDB) para llamarlas como funciones. | **Reglas de negocio y de revelación** legibles por máquina guardadas en el mismo contenedor (DIO) que los datos financieros. | Presentar el **DataBook** (Markdown + JSON-LD) como el contenedor (**DIO**) donde el dato y las reglas de validación (SHACL/SPARQL) coexisten físicamente, logrando la autoverificación. |
| **5. Transformación y Extracción de Datos** | Uso de **XQuery** (expresiones FLWOR) en Altova XMLSpy/MapForce para extraer datos de facturas XML (UBL) e inyectarlos al grafo. | **"XQuery para Grafos":** Cagle elogia la ergonomía de XQuery para navegar XML y pide crear un lenguaje de consulta y transformación homólogo para RDF. | **Evolución y gestión del cambio:** Mapear los documentos antiguos y convertirlos a "primero el grafo" para luego volver a generar reportes legibles. | Resaltar que tu elección de **XQuery** para el análisis XML es la herramienta más madura hoy, validada por la visión de Cagle, y que MapForce actúa como el motor de transformación entre el "disfraz" del documento (XML/UBL) y el grafo (JSON-LD). |

---

## 3. Implicaciones Estratégicas para tu Proyecto y el Paper

Esta organización te da un argumento académico sumamente poderoso. Te permite estructurar el artículo de la siguiente manera:

1. **La "Deuda" de la Web Semántica:** Puedes citar el post de Cagle & Shannon (2026) en la **Sección 2.3** para fundamentar que, si bien el stack RDF tradicional está limitado para operaciones de computación activa (como agregaciones de saldos en tiempo real), **A&AD resuelve esta limitación hoy mediante una arquitectura híbrida**:
   * Usas **Altova MapForce/XMLSpy** como motor de transmutación de documentos ("disfraces" XML/CSV) a grafos semánticos puros.
   * Usas **XQuery** en la primera milla (validando la postura de Cagle de que XQuery es el estándar de oro en ergonomía de transformación).
   * Usas **SHACL** en TerminusDB/DFRNT para asegurar la integridad topológica del grafo (la estructura formal de REA y XBRL GL).
   * Usas **SPARQL parametrizado (vía Python/Colab)** y el razonador **Pacioli (vía Prolog)** para ejecutar las "reglas de negocio y de mecánica de revelación" que Charlie exige para autoverificar el Trial Balance y las Lead Schedules.

2. **La Defensa del "Shift-Left" bajo Six Sigma:**
   * La validación debe ocurrir en la ingesta (Momento 0). Al combinar las reglas de negocio legibles por máquina con la verificación en tiempo real, A&AD implementa la **Regla 1-10-100**:
     * **Prevención ($1):** Reglas SHACL y MapForce al ingresar el dato (Data Contracts).
     * **Remediación ($10):** Corrección interna mediante el Trial Balance generado por SPARQL.
     * **Falla ($100):** Evitar que datos inconsistentes salgan al exterior, eliminando la necesidad de auditorías forenses posteriores.

3. **El DataBook como el DIO:**
   * El DataBook (Markdown + JSON-LD) no es solo un reporte bonito; es la implementación física de un **Organismo de Información Digital (DIO)** que encapsula los datos (Atoms/Molecules), las reglas de validación (SHACL) y la visualización humana (Pages), cumpliendo con la Metodología de Diseño Atómico de Charlie.
