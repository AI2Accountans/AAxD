# Guión Técnico y Narrativo de Video: El Flujo A&AD
## *De la Escritura Pública al Grafo de Conocimiento Semántico*

---

## 🎬 Ficha Técnica del Video
* **Título**: De la Escritura Pública al Grafo Semántico: El Flujo Industrializado de Accounting and Audit by Design (A&AD).
* **Objetivo**: Explicar pedagógicamente el paradigma **Shift-Left** (Interacción 2 del 2026-08-06 con Charles Hoffman): mover la validación y gobernanza semántica con SBVR y REA al extremo izquierdo (origen legal / Holón Génesis en Momento 0), garantizando $1 en prevención y derivando determinísticamente la contabilidad en XBRL GL, JSON-LD, DataBooks y SHACL.
* **Principio Clave**: **Shift-Left ($1 Prevención)** — Capturar la verdad económica en el documento fuente legal en lugar de corregir errores de $10 en el ERP o colapsos de $100 en reportes finales.
* **Tono**: Profesional, disruptivo, técnico-contable y vanguardista.

---

## 📐 Estructura por Escenas (Flujo Shift-Left)

```mermaid
graph LR
    subgraph ShiftLeft["<b>EXTREMO IZQUIERDO: $1 PREVENCIÓN</b>"]
        E1["Escena 1: Escritura / UBL<br/><i>Holón Génesis (SBVR + REA)</i>"]
    end
    
    subgraph Downstream["<b>PROYECCIÓN CONTABLE Y AUDITORÍA</b>"]
        E2["Escena 2: XBRL GL<br/><i>Canónico / Bifurcación</i>"] --> E3["Escena 3: Transmutación<br/><i>XQuery ➔ JSON-LD</i>"]
        E3 --> E4["Escena 4: DataBook<br/><i>Holón Híbrido</i>"]
        E4 --> E5["Escena 5: SHACL<br/><i>Control Preventivo</i>"]
        E5 --> E6["Escena 6: Ricordanze<br/><i>Multicontrato NIIF/ESG</i>"]
    end

    E1 --> E2
```

---

### 🎥 Escena 1: El Origen - Reificación del Contrato de Constitución y Shift-Left (Momento 0)

* **Visual en Pantalla**: 
  * Imagen/PDF de la Escritura Pública de Constitución (`SOCIEDAD_LIMITADA.pdf`).
  * Resaltado dinámico de las cláusulas: Socios, Aportes de Capital ($10,000,000 COP) y Nombre de la entidad.
  * Captura de pantalla de la interfaz **XForms + IA Generativa** extrayendo los componentes **REA** (*Resource, Event, Agent*).
  * **Overlay de Shift-Left (Regla 1-10-100 de Hoffman)**: Gráfica animada mostrando la flecha desplazándose hacia el extremo izquierdo ($1 Prevención en el origen legal vs. $10 en ERP relacional vs. $100 en informe publicado).
* **Voz en Off / Locución**:
  > *"Todo proceso contable nace de una realidad jurídica. En la contabilidad tradicional, avanzamos a ciegas post-facto: una Escritura de Constitución se convierte en un PDF estático en un archivo y en números planos digitados manualmente en un ERP, acumulando riesgos de hasta $100 por errores no auditados.*
  > 
  > *Siguiendo el principio **Shift-Left** consolidado con Charles Hoffman (Interacción 2 del 6 de agosto de 2026), en **Accounting and Audit by Design (A&AD)** **avanzamos decididamente hacia el extremo izquierdo**. La Escritura de Constitución es nuestro **Holón Génesis** (Momento 0). Mediante una interfaz inteligente en XForms guiada por SBVR y apoyada por IA, reificamos el contrato en la fuente ($1 de prevención), extrayendo sus Recursos, Agentes y Compromisos antes de cualquier registro diario."*

---

### 🎥 Escena 2: El Canónico XBRL GL - La "Aduana" Universal y la Doble Bifurcación

* **Visual en Pantalla**:
  * Diagrama de flujo mostrando la exportación hacia la estructura XML de **XBRL Global Ledger (XBRL GL)**.
  * Animación de una bifurcación con dos caminos:
    * **Camino A (Lado Izquierdo)**: Flechas hacia bases de datos relacionales SQL (SAP, Siesa, PostgreSQL).
    * **Camino B (Lado Derecho)**: Flechas hacia el motor semántico XQuery 3.1.
* **Voz en Off / Locución**:
  > *"Aquí llegamos a un principio arquitectónico innegociable: **Todo Holón debe ser procesado primeramente en XBRL GL**. XBRL GL actúa como nuestra aduana de estandarización universal e independiente de plataforma. Preserva la fidelidad de los asientos, los participantes y las notas legales.*
  > 
  > *A partir de este punto canónico en XBRL GL se abre una **doble posibilidad**:
  > 1. **Para sistemas legacy**: Podemos alimentar directamente tablas relacionales SQL en ERPs tradicionales como Siesa o SAP sin perder la trazabilidad de origen.
  > 2. **Para el paradigma A&AD**: Transmutamos de forma limpia el XML hacia un Grafo de Conocimiento Semántico."*

---

### 🎥 Escena 3: La Transmutación a JSON-LD vía XQuery 3.1

* **Visual en Pantalla**:
  * Código XQuery 3.1 ejecutándose (`xbrlgl2jsonld.xq`).
  * Estructura del Payload JSON-LD resultante (`xbrlgl2jsonld.json`) destacando el `@context` y el `@graph`.
  * Grafos visuales mostrando la deduplicación de nodos: `AccountingEntry`, `Account`, `Entity` y `TaxonomyConcept`.
* **Voz en Off / Locución**:
  > *"Mediante un motor declarativo XQuery 3.1, transmutamos la instancia XBRL GL en un **Payload JSON-LD**. 
  > 
  > *En este paso no solo convertimos texto en código: reificamos y deduplicamos las entidades. Cada cuenta contable, cada socio fundador y cada concepto de reporte NIIF o fiscal adquiere una URI única e inmutable. Las transacciones dejan de ser registros aislados para convertirse en un grafo plano e interconectado de conocimiento."*

---

### 🎥 Escena 4: El DataBook - El Envoltorio Vivo para Humanos e Inteligencia Artificial

* **Visual en Pantalla**:
  * Apertura del archivo `output.databook.md`.
  * Desplazamiento visual: arriba se observa el texto legal legible en Markdown; abajo se despliega el bloque ` ```json-ld ` incrustado.
  * Demostración en Google Colab/Python ejecutando consultas SPARQL en memoria de forma offline.
* **Voz en Off / Locución**:
  > *"El Payload JSON-LD se incrusta junto con la narrativa del contrato en un **DataBook** (`.databook.md`), el envoltorio ideado por Kurt Cagle.
  > 
  > *El DataBook es un **Holón autocontenido con naturaleza dual**: el ser humano o el juez lee la narrativa en texto plano, mientras que los motores de grafo y los agentes de IA leen el JSON-LD incrustado. Esto permite ejecutar auditorías externas deterministas offline con SPARQL, sin necesidad de conectarse a la base de datos de origen y eliminando el riesgo de alucinaciones en la IA."*

---

### 🎥 Escena 5: Control Interno Preventivo con SHACL (Shapes Guard)

* **Visual en Pantalla**:
  * Código de reglas Turtle SHACL (`entry_shape.ttl` o `balance_shape.ttl`).
  * Simulación visual de un intento de ingreso de un asiento desbalanceado o con acciones embargadas $\rightarrow$ Icono de **RECHAZADO EN TIEMPO REAL**.
* **Voz en Off / Locución**:
  > *"¿Dónde está el control interno? Aquí entra **SHACL (Shapes Constraint Language)**. SHACL actúa como una puerta de guardia en el momento de la ingesta.
  > 
  > *En lugar de hacer auditorías forenses al final del mes en hojas de cálculo, SHACL evalúa el Grafo en tiempo real. Si un asiento está desbalanceado o si intenta venderse una acción que tiene un embargo judicial registrado, SHACL rechaza la transacción en la puerta de entrada. **En A&AD, todo se controla desde el principio.**"*

---

### 🎥 Escena 6: Evolución Multicontrato - El Ricordanze Moderno y Reportes NIIF / ESG

* **Visual en Pantalla**:
  * Animación de múltiples contratos ingresando al Grafo (Facturas UBL de agua en $m^3$, métricas XBRL UTR, acuerdos financieros ACTUS, medidas cautelares).
  * El Grafo en DFRNT / TerminusDB creciendo de forma inmutable (**Append-Only / PROV-O**).
  * Dashboard final mostrando la derivación en tiempo real del **Estado de Situación Financiera (NIIF)** y el **Reporte de Huella Hídrica / Sostenibilidad (ESG/GRI 303)**.
* **Voz en Off / Locución**:
  > *"A partir del Momento 0, la empresa vive y celebra múltiples contratos. Siguiendo la visión de Charles Hoffman, el Grafo de Conocimiento se convierte en el **Ricordanze Moderno**: un registro de memoria empresarial inmutable y bitemporal.
  > 
  > *Desde esta misma **Fuente Única de Verdad**, podemos consultar en tiempo real los Estados Financieros bajo NIIF y, simultáneamente, los reportes de sostenibilidad ESG con métricas físicas estandarizadas por el Registro UTR de XBRL International. 
  > 
  > *Esto es **Accounting and Audit by Design**: el fin del control reactivo y el inicio de la certeza algorítmica."*

---

## 📌 Consejos de Edición para el Video
1. **Tomas de Código**: Destacar con luces/zoom de cámara los bloques ` ```json-ld ` en el DataBook y el script `xbrlgl2jsonld.xq`.
2. **Diagramas**: Usar animaciones vectoriales limpias (estilo la interfaz de DFRNT y el Atlas de Zachman).
3. **Música de Fondo**: Estilo corporativo/tecnológico sobrio y moderno (estilo ciencia de datos/blockchain).

---

## 📚 Fundamentación Teórica: Interacción 2 (2026-08-06) con Charles Hoffman

> **Charlie Hoffman (2026-08-06):** *"Let me think about this in terms of an 'ideal' implementation... I feel you and I are closer than anyone else in terms of a common understanding."*

* **Avanzar hacia la Izquierda (Shift-Left)**: Significa reubicar el centro de gravedad de la auditoría y la arquitectura desde la Fila 6 (reportes contables / auditoría forense post-mortem) hasta el **extremo izquierdo** (el Documento Fuente / Holón Génesis / UBL + SBVR + REA en el Momento 0).
* **Impacto Económico**: 
  * **$1 Prevención**: Validación semántica e invariantes de negocio (SBVR + SHACL) aplicadas directamente al contrato/formulario de origen.
  * **$10 Remediación (Evitada)**: Se eliminan las conciliaciones manuales y asientos de ajuste por errores de digitación en ERPs relacionales.
  * **$100 Falla Total (Eliminada)**: Se erradica el riesgo de re-emisión de estados financieros, sanciones regulatorias y fraudes no detectados.

