# Respuesta Específica a la Solicitud de Charles Hoffman: Procesamiento del Trial Balance XBRL GL (MINI)

**De**: Prof. Richard Gasca  
**Para**: Charles Hoffman (`carlos.hoffman@gmail.com` / `charles.hoffman@xbrl.org`)  
**Asunto**: `Re: Running your valid XBRL Global Ledger trial balance & MINI framework through our pipeline`  
**Fecha**: 13 de Agosto de 2026  

---

## 1. Versión en Inglés (Correo Electrónico Directo listo para Enviar)

Hi Charlie,

Thank you for your message and for raising this key question.

To answer you directly: **Yes, it is 100% possible, and the effort required is very low (straightforward).**

Here is why, from both an architectural and accounting perspective:

### 1. Framework-Agnostic Core Engine & Internal Reporting Benefits
You mentioned that you don't fully follow the reporting framework we used in our prototype (which was based on the Colombian Financial Regulator - SFC / IFRS for Paladin Realty). That is completely understandable! The SFC IFRS framework was simply our initial jurisdictional test case to prove we could handle complex real-world regulatory schemas.

Our underlying processing pipeline (BaseX XQuery engine + Altova MapForce + JSON-LD Knowledge Graph in DFRNT) is **completely reporting-framework agnostic**. It relies on **XBRL Global Ledger (XBRL GL)** standard structures (`gl-cor`, `gl-bus`, `gl-srcd`) as its universal data payload. 

As highlighted in the landmark IMA *Strategic Finance* article (*"Internal Reporting with XBRL Global Ledger"*), the true power of XBRL GL lies in its ability to standardize internal accounting data from source transactions all the way to management and regulatory reporting, maintaining an unbroken audit trail. Our DFRNT architecture puts this exact principle into practice by storing XBRL GL payloads as reified Knowledge Graphs.

### 2. How Your MINI XBRL GL Trial Balance Flows Through Our Process
Because your MINI trial balance is already formatted as valid XBRL GL, ingesting it into our pipeline requires zero structural re-engineering:

1. **Ingestion**: We load your valid XBRL GL trial balance XML directly into our BaseX database environment.
2. **Semantic Graph Transmutation**: Our XQuery/MapForce pipeline transmutes the XBRL GL nodes into a reified Linked Data Knowledge Graph (`CSV2XBRLGL2JSONLD.json`) ready for native storage in DFRNT (TerminusDB).
3. **Declarative Framework Projection**: Using your MINI reporting framework concepts (instead of our SFC/IFRS mapping rules), the XQuery transformation categorizes and aggregates the trial balance items directly into your MINI Balance Sheet and Income Statement—without needing an arbitrary Chart of Accounts or manual lead schedule.
4. **Dual Output Generation**:
   * **Human-Readable Projection**: An interactive HTML rendering of your MINI financial statements.
   * **Machine-Readable Projection**: A valid XBRL instance file formatted according to your MINI taxonomy/XSD entry point, ready for you to pass through your certified XBRL processor and Seattle Method validation rules.

### 3. Next Step: Let's Run It!

I would love to run your exact MINI trial balance through our pipeline right away. 

Could you please confirm or send me:
* The link to your exact **valid XBRL GL trial balance XML file** (e.g., from your `seattlemethod/prototypes` repository).
* Your **MINI reporting framework taxonomy / XSD entry point**.

Once you share those, I will run the transformation and send back both the generated XBRL instance and the HTML/JSON-LD rendering so you can verify the results from an accounting and semantic perspective.

Looking forward to taking this next step together!

Cheers,

**Richard Gasca**  
*Accounting & Audit by Design (A&AD) Research Group*  
DFRNT & GSKM Project  

---

## 2. Versión en Español (Para Revisión Interna y Registro)

Hola Charlie,

Muchas gracias por tu mensaje y por plantear esta pregunta clave.

Para responderte directamente: **Sí, es 100% posible y el esfuerzo requerido es muy bajo (directo y sencillo).**

A continuación explico el porqué, tanto desde la perspectiva arquitectónica como contable:

### 1. Motor Central Independiente del Marco de Información (Framework-Agnostic) y Beneficios de XBRL GL
Mencionaste que no estás familiarizado con el marco de información financiera que utilizamos en nuestro prototipo (el cual se basó en las normas de la Superintendencia Financiera de Colombia - SFC / NIIF para Paladin Realty). ¡Es completamente comprensible! El marco NIIF de la SFC fue simplemente nuestro caso de prueba jurisdiccional inicial para demostrar que podíamos manejar esquemas regulatorios reales y complejos.

Nuestra canalización de procesamiento subyacente (Motor BaseX XQuery + Altova MapForce + Grafo de Conocimiento JSON-LD en DFRNT) es **completamente agnóstica al marco de reporte**. Se apoya en las estructuras estándar de **XBRL Global Ledger (XBRL GL)** (`gl-cor`, `gl-bus`, `gl-srcd`) como su carga útil universal de datos.

Tal como lo destaca el artículo clave de IMA *Strategic Finance* (*"Internal Reporting with XBRL Global Ledger"*), el verdadero poder de XBRL GL radica en su capacidad para estandarizar la información contable interna desde las transacciones de origen hasta los reportes de gestión y regulatorios, manteniendo una pista de auditoría inquebrantable. Nuestra arquitectura en DFRNT pone en práctica este principio exacto al almacenar las cargas útiles XBRL GL como Grafos de Conocimiento reificados.

### 2. Cómo Fluye tu Trial Balance XBRL GL del Modelo MINI en Nuestro Proceso
Debido a que tu balance de prueba MINI ya está formateado como un XBRL GL válido, su ingesta en nuestra canalización requiere cero reingeniería estructural:

1. **Ingesta**: Cargamos directamente tu XML de balance de prueba en XBRL GL en nuestro entorno BaseX.
2. **Transmutación a Grafo Semántico**: Nuestra canalización XQuery/MapForce transmuta los nodos de XBRL GL a un Grafo de Conocimiento Linked Data reificado (`CSV2XBRLGL2JSONLD.json`), listo para su almacenamiento nativo en DFRNT (TerminusDB).
3. **Proyección Declarativa del Marco de Reporte**: Utilizando los conceptos de tu marco de reporte MINI (en lugar de nuestras reglas de mapeo SFC/NIIF), la transformación XQuery categoriza y agrega los elementos del balance de prueba directamente en tu Balance General y Estado de Resultados MINI, sin necesidad de un plan de cuentas arbitrario ni planillas de trabajo manuales (*lead schedules*).
4. **Generación de Salida Dual**:
   * **Proyección Interpretable por Humanos**: Renderizado HTML interactivo de tus estados financieros MINI.
   * **Proyección Interpretable por Máquinas**: Archivo de instancia XBRL válido estructurado conforme a la taxonomía / punto de entrada XSD de tu modelo MINI, listo para que lo pases por tu procesador XBRL certificado y reglas de validación del Método Seattle.

### 3. Próximo Paso: ¡Ejecutémoslo!

Me encantaría procesar tu balance de prueba MINI exacto a través de nuestra canalización de inmediato.

¿Podrías confirmarme o enviarme:
* El enlace a tu **archivo XML de balance de prueba XBRL GL válido** (por ejemplo, de tu repositorio `seattlemethod/prototypes`).
* La **taxonomía / punto de entrada XSD de tu marco de reporte MINI**?

Tan pronto como los compartas, ejecutaré la transformación y te enviaré de vuelta tanto la instancia XBRL generada como la renderización en HTML/JSON-LD para que puedas verificar los resultados desde la perspectiva contable y semántica.

¡Quedo a la espera de dar este siguiente paso juntos!

Un saludo,

**Richard Gasca**  
*Grupo de Investigación Accounting & Audit by Design (A&AD)*  
Proyecto DFRNT / GSKM  
