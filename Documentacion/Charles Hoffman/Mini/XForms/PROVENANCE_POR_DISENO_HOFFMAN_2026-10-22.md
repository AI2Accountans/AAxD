# Análisis Estratégico: Procedencia por Diseño en el Stack DFRNT y W3C
**Fecha de Interacción:** 22 de Octubre de 2026  
**Contexto:** Interacción de Charles Hoffman sobre la implementación de Procedencia (*Provenance*) y el artículo de *The Inference Engineer*  
**Ubicación Original Solicitada:** `C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mini\XForms\`  
**Referencia Principal:** [Where Does Provenance Come From? (Kurt Cagle & Chloe Shannon)](https://inferenceengineer.substack.com/p/where-does-provenance-come-from)  
**Imagen Clave:** `1.png` (Los 7 Hábitos de la Procedencia)  

---

## 1. El Mensaje de Charles Hoffman

El 22 de Octubre de 2026, Charles Hoffman compartió el análisis de *The Inference Engineer*, validando explícitamente el enfoque arquitectónico de nuestro proyecto:

> *"This is an excellent article about provenance and events. It has a bunch of information to help make sure provenance is implemented correctly and **how to differentiate the DFRNT implementation (e.g. implemented provenance correctly) and those that really are not even thinking about provenance**. This is absolutely worth reading."*

### Diagnóstico de la Brecha en la Industria
La mayoría de los sistemas contables y ERPs tradicionales conciben la procedencia como un campo de texto cosmético (`source = "Factura 123"`) llenado a posteriori (*reporting feature*). Cuando un auditor o regulador formula la pregunta fundamental: **«¿De dónde provino esta cifra?»**, la respuesta rara vez reside en los datos; suele perderse en pipelines reescritos, memorias humanas o papeles de trabajo desvinculados.

En el marco **Accounting & Audit by Design (A&AD)**, la procedencia no es un accesorio: **es un requisito estructural de diseño desde el momento cero (*Provenance as a Design Requirement*)**.

---

## 2. Los 7 Hábitos de la Procedencia por Diseño aplicados al Stack

```
[ Evidencia Fuente (UBL / JPG / MD) ]
                 │
                 ▼ (Hábito 1: Registro instantáneo en el momento del acto)
    [ Evento de Ingesta en BaseX ] ── (Hábito 2: Bitemporalidad + Agente + Versión)
                 │
                 ▼ (Hábito 7: Aduana SHACL / Prolog: Rechazo en frontera si falta linaje)
    [ Curaduría XForms (HITL) ]
                 │
                 ▼ (Hábito 3 y 4: Reificación con IRIs explícitos RDF 1.2 / PROV-O)
    [ Mapeo MapForce JE2XBRLG2JSONLDV4 ]
                 │
                 ▼ (Hábito 6: Inmutabilidad tipo Git: Nunca sobrescribir, superseder)
    [ Grafo en TerminusDB / DFRNT ] ── (Hábito 5: Confianza como fluente evaluado)
```

### Hábito 1: Registrar un evento por cada paso que cree o mute una afirmación
* **Principio:** No registrar saldos estáticos huérfanos. Todo cambio nace en un hecho fáctico.
* **Implementación:** Al ingresar un documento (ej. `01-Check-Investment.jpg` o factura UBL en BaseX), se instancia un evento (`prov:Activity`) calculando de inmediato su hash criptográfico SHA-256 antes de cualquier transformación contable.

### Hábito 2: Bitemporalidad (dos relojes) + Actor + Versión del modelo
* **Principio:** Desacoplar el tiempo del suceso del tiempo del reporte.
* **Implementación:**
  1. **Valid Time (Tiempo Válido):** Fecha fáctica del contrato o comprobante (`2024-01-01`).
  2. **Transaction Time (Tiempo de Transacción):** Estampa de tiempo inmutable del commit en TerminusDB.
  3. **Actor y Versión:** Identidad del curador en XForms (`GistPerson/Curator`) y versión de la base de conocimiento en Prolog (`decreto_2650_prolog.pl` v1.0).

### Hábito 3: Enlazar afirmaciones a eventos por referencia con IRIs (W3C RDF 1.2)
* **Principio:** No pegar texto plano en campos de origen. Utilizar reificación y grafos con nombre donde cada afirmación tenga un identificador universal.
* **Implementación en Turtle 1.2:**
  ```turtle
  PREFIX ex:   <http://dfrnt.org/entity/>
  PREFIX prov: <http://www.w3.org/ns/prov#>

  ex:Mini_Lemonade ex:contributedCapital 5000.00 ~ex:claim-0001 {|
      prov:wasDerivedFrom ex:evidence-check-01 ;
      prov:wasAttributedTo ex:curator-charlie ;
      prov:wasGeneratedBy ex:prolog-dinamica-3105
  |} .
  ```
* **En MapForce (`JE2XBRLG2JSONLDV4.mfd`):** Eliminación total de colisiones mediante identificadores `@id` normalizados en cada `EntryDetail`.

### Hábito 4: El mensaje lleva su propia cadena de procedencia
* **Principio:** La carga de identificar el origen no recae en el receptor; viaja integrada en el mensaje.
* **Implementación:** La instancia JSON-LD emitida transporta punteros hacia `prov:wasDerivedFrom` y los hashes de los artefactos previos, permitiendo la trazabilidad bidireccional inmediata.

### Hábito 5: Fuentes registradas como entidades y confianza medida como un fluente (*Trust Score*)
* **Principio:** Las fuentes (OCR, ERPs, proveedores UBL) tienen niveles de confianza dinámicos que se evalúan y actualizan con la evidencia empírica.
* **Implementación:** El motor en LPS/Prolog modela la confiabilidad como un estado continuo (*fluent*). Si una fuente presenta descuadres recurrentes en la partida doble, el sistema eleva alertas de riesgo epistémico de forma preventiva.

### Hábito 6: Nunca sobrescribir; superseder (*Append-only Ledger*)
* **Por qué DFRNT / TerminusDB marca la diferencia:**  
  A diferencia de las bases de datos relacionales convencionales donde se ejecutan `UPDATE` destructivos, **TerminusDB opera sobre una arquitectura de grafo inmutable inspirada en Git**.
* Toda corrección contable no destruye el registro previo; crea un nuevo estado vinculado mediante `prov:wasRevisionOf` y declara la anterior mediante `prov:invalidatedAtTime`. La historia permanece viva, auditable y trazable en el tiempo (*time-travel queries*).

### Hábito 7: Rechazar datos en la frontera si carecen de evento o traza (*Fail Loudly*)
* **Principio:** La calidad de datos se defiende en la aduana de entrada, no corrigiendo errores aguas abajo.
* **Implementación:** Las restricciones **W3C SHACL** y los axiomas de partida doble en **Prolog** bloquean cualquier transacción que no provenga de un evento económico REA legítimo o cuyo balance contable sea dispar:
  $$\sum \text{Débitos} \neq \sum \text{Créditos} \implies \textbf{RECHAZO DETERMINISTA}$$

---

## 3. Integración en el Flujo Operativo (`flow.png`)

Esta interacción consolida los componentes ya existentes en nuestro repositorio:

1. **Entrada Heterogénea (Shift-Left):**  
   Facturas UBL (procesadas nativamente por XQuery en BaseX) y contratos/cheques no estructurados (PDF/JPG procesados vía OCR).
2. **Curaduría Humana (HITL):**  
   El formulario declarativo en **W3C XForms** (`curation_workbench.xhtml` / `index.xhtml`) alimentado con la pre-población del extractor y verificado por el auditor antes de iniciar cualquier mutación en el libro diario.
3. **Deducción de Dinámica Contable:**  
   El motor **SWI-Prolog** (`decreto_2650_prolog.pl` y el nuevo modelo para el **PCGE 2026 de Perú**) que deduce los débitos y créditos con justificación legal estricta.
4. **Presentación y Reportes:**  
   **Altova StyleVision** compila hojas de transformación XSLT sobre el esquema canónico [`BusinessEvent_XBRLGL_REA.xsd`](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Charles%20Hoffman/Mini/XForms/BusinessEvent_XBRLGL_REA.xsd), generando papeles de trabajo formales y reportes de auditoría de calidad editorial.
5. **Proyección Canónica al Grafo:**  
   Transformación vía Altova MapForce ([`JE2XBRLG2JSONLDV4.mfd`](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Charles%20Hoffman/Mini/Mapping/JE2XBRLG2JSONLDV4.mfd)) inyectando las 70 instancias normalizadas en **TerminusDB / DFRNT**, sellando la procedencia matemática y fáctica desde el balance financiero hasta el pixel o byte original.
