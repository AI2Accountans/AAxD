# Capítulo 12: Shift Left en Acción — De la Ontología ISO/IEC 15944-4 a la Ingesta Inmutable en BaseX

## De la Teoría Ontológica al Formulario Interactivo y la Captura en la Fuente

---

*"El error contable no es un fallo de cálculo en el balance final; es una falla de diseño semántico cometida en el momento mismo en que dos agentes acuerdan intercambiar valor."*

---

## 1. La Filosofía *Shift Left*: Mover la Certeza al Momento Cero

Durante décadas, la contabilidad tradicional ha operado bajo un esquema reactivo y forense: los eventos económicos ocurren en el mundo real, los agentes emiten documentos en papel o PDFs desestructurados, y meses después, un equipo de contadores intenta reconstruir la historia financiera etiquetando datos y registrando asientos de ajuste para corregir la ambigüedad.

La arquitectura **Accounting & Audit by Design (A&AD)** invierte radicalmente esta dinámica mediante el principio **Shift Left** (desplazamiento a la izquierda). En ingeniería de software, *Shift Left* significa mover las pruebas de calidad y seguridad al punto más temprano posible del ciclo de desarrollo. En A&AD, *Shift Left* significa mover la validación contable, la semántica del negocio y las restricciones contractuales **al instante mismo de la captura del dato**, antes de que exista el primer libro auxiliar o la primera factura.

Para lograr esto, A&AD no inventa un lenguaje propietario; adopta la norma internacional **ISO/IEC 15944-4** (Ontología de Contabilidad y Economía basada en el modelo **REA: Resources, Events, Agents**) y el vocabulario **Valueflows**.

En este capítulo documentaremos paso a paso el ejercicio práctico de implementación end-to-end: desde la definición del esquema formal XSD, pasando por la creación de una interfaz visual interactiva en **Altova StyleVision**, la ingesta en tiempo real en la base de datos XML **BaseX**, hasta la maquetación automática de reportes legales en **PDF via XSL-FO**.

---

## 2. Componente 1: La Formalización del Esquema XSD (`valueflows_schema.xsd`)

La primera etapa de la arquitectura consiste en traducir los axiomas ontológicos expresados en OWL/TTL a un esquema **XML Schema (XSD)** riguroso que sirva como contrato de interfaz para la captura de datos.

El esquema **`valueflows_schema.xsd`** formaliza la estructura bajo el namespace `https://w3id.org/valueflows/ont/vf#` e introduce conceptos fundamentales:

```
                          ┌──────────────────────────┐
                          │    BusinessTransaction   │
                          └────────────┬─────────────┘
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            ▼                          ▼                          ▼
    ┌───────────────┐          ┌───────────────┐          ┌───────────────┐
    │   agreement   │          │  commitments  │          │ reciprocities │
    │  (Contrato)   │          │ (Planificación)│          │ (Dualidad REA)│
    └───────────────┘          └───────────────┘          └───────────────┘
```

### A. Verbos Semánticos Restringidos (`vf:ActionEnum`)
A diferencia de los textos libres en las bases de datos relacionales, las acciones económicas se restringen estrictamente a los verbos ontológicos REA:

```xml
<xs:simpleType name="ActionEnum">
  <xs:restriction base="xs:string">
    <xs:enumeration value="deliver-service"/>
    <xs:enumeration value="pay"/>
    <xs:enumeration value="transfer"/>
    <xs:enumeration value="produce"/>
    <xs:enumeration value="consume"/>
    <xs:enumeration value="use"/>
    <xs:enumeration value="work"/>
  </xs:restriction>
</xs:simpleType>
```

### B. Separación entre Planificación y Observación
A&AD distingue explícitamente entre la **capa de planificación (*Commitments*)** y la **capa de observación (*EconomicEvents*)**:
* **`vf:CommitmentType`**: Captura la promesa futura de intercambio (monto, fecha límite, emisor, receptor). Esto permite a la contabilidad predecir flujos de caja y obligaciones futuras con absoluta certeza.
* **`vf:EconomicEventType`**: Captura la ejecución real en el mundo físico y se vincula mediante la propiedad `vf:fulfills` al compromiso que satisface.

### C. La Dualidad REA (*Give & Take / Reciprocity*)
En ISO/IEC 15944-4, todo intercambio económico exige reciprocidad (un compromiso de entrega de valor vincula inexorablemente un compromiso de contraprestación):

```xml
<xs:complexType name="ReciprocityType">
  <xs:sequence>
    <xs:element name="id" type="xs:string"/>
    <xs:element name="incrementCommitmentRef" type="xs:string"/>
    <xs:element name="decrementCommitmentRef" type="xs:string"/>
    <xs:element name="note" type="xs:string" minOccurs="0"/>
  </xs:sequence>
</xs:complexType>
```

---

## 3. Componente 2: La Interfaz Visual Interactiva en Altova StyleVision

Los esquemas XML y las ontologías RDF son poderosos para los motores de código, pero incomprensibles para los usuarios de negocio, contadores y abogados comerciales. Para cerrar la brecha del *Triángulo del Significado*, A&AD utiliza **Altova StyleVision** para compilar la ontología en una interfaz gráfica interactiva (**Authentic eForm / XForms**).

```
   Esquema XSD               Working XML                  Formulario SPS
(valueflows_schema.xsd) + (valueflows_sample_instance.xml) ➔ (Altova StyleVision)
                                                                 │
                                                                 ▼
                                                         Authentic eForm
                                                    (Interfaz de Usuario)
```

### Lecciones de Maquetación del Lienzo (*Free-Flow Layout*)
Durante el ejercicio práctico se establecieron principios clave de diseño UI/UX para auditoría:

1. **Selección de Modo *Free-Flow*:** El diseño fluido permite que las tablas dinámicas de compromisos crezcan y se adapten a diferentes resoluciones de pantalla sin romper la estructura.
2. **Tablas Dinámicas de Compromisos (`vf:commitments`):** En lugar de incluir masivamente todas las propiedades del esquema en una vista horizontal saturada (que causaría superposición de texto en PDF), la interfaz selecciona las 6 columnas fundamentales:
   * `ID Compromiso`
   * `Acción REA` (`deliver-service`, `pay`, etc.)
   * `Proveedor` (Emisor)
   * `Receptor` (Destinatario)
   * `Cantidad / Monto`
   * `Fecha de Vencimiento`
3. **Controles de Formulario Dinámicos (`Edit Field` / `Combo Box` / `DatePicker`):** Permiten a los usuarios agregar filas interactivamente mediante botones `[+]` y `[-]`, seleccionando verbos ontológicos de listas desplegables cerradas.

---

## 4. Componente 3: La Ingesta Inmutable en BaseX vía RESTXQ

Una vez que el usuario diligencia la transacción comercial en el formulario visual de Altova StyleVision, presiona el botón de envío. El formulario serializa la instancia XML validada y la transmite mediante `HTTP POST` hacia el servidor **BaseX**.

### El Módulo RESTXQ (`iso15944_ingest.xq`)
En el servidor local (o en el nodo de auditoría en la nube), el módulo RESTXQ recibe la carga útil XML y la persiste directamente en la base de datos nativa `ubl2dfrnt`:

```xquery
(:
  Módulo RESTXQ para BaseX: Recepción e Ingesta de Contratos ISO/IEC 15944-4
:)
module namespace api = 'http://dfrnt.org/api/iso15944';

declare 
  %rest:path('/iso15944/ingest')
  %rest:POST("{$body}")
  %rest:consumes("application/xml", "text/xml")
  %rest:produces("application/xml")
function api:ingest-iso15944($body as node()) {
  let $db-name := "ubl2dfrnt"
  let $timestamp := replace(string(current-dateTime()), ":", "-")
  let $tx-id := data($body//*:transactionId)
  let $doc-id := concat("iso15944_", if ($tx-id != "") then $tx-id else $timestamp, ".xml")
  
  return (
    (: Persistencia inmutable en la colección de contratos :)
    db:add($db-name, $body, concat("contracts/", $doc-id)),
    
    (: Acuse de recibo estructurado para XForms :)
    <response status="200" success="true">
      <message>Contrato ISO 15944 capturado exitosamente en la fuente (Shift Left)</message>
      <documentId>{$doc-id}</documentId>
      <transactionId>{$tx-id}</transactionId>
      <timestamp>{string(current-dateTime())}</timestamp>
    </response>
  )
};
```

### Beneficio del Almacenamiento Nativo XML en BaseX
Al almacenar el documento completo en BaseX:
* El contrato queda disponible para consultas XQuery instantáneas.
* Se preserva la totalidad del árbol de decisiones comerciales.
* Los algoritmos de DFRNT pueden proyectar el documento XML hacia un **Grafo de Conocimiento JSON-LD / RDF** para ejecutar razonamiento agéntico y validaciones de reglas de negocio en tiempo real.

---

## 5. Componente 4: Maquetación y Generación de Reportes Legales PDF (XSL-FO)

Un sistema de información moderno debe ofrecer una **doble cara de la verdad**:
1. **La cara para las máquinas:** Grafo JSON-LD / XML semántico consumable por agentes de IA y bases de datos inmutables.
2. **La cara para los humanos:** Documento impreso en PDF legalmente presentado con firma electrónica y tipografía clara.

Para lograr la cara humana sin perder sincronía con la base de datos, A&AD utiliza hojas de estilo **XSL-FO** (`valueflows_to_pdf.xslt`).

### Transformación XQuery a XSL-FO
En BaseX se ejecuta la transformación del documento XML almacenado contra la plantilla maquetada:

```xquery
let $xml := doc('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/valueflows_sample_instance.xml')
let $xslt := doc('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/valueflows_to_pdf.xslt')
let $fo := xslt:transform($xml, $xslt)
return file:write('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/contrato_iso15944.fo', $fo)
```

El resultado es un documento maquetado impecable en A4 que distribuye los bloques de información:
* **Cabecera de Jurisdicción y Transacción** (Bandas de contraste en `#1E3A8A`).
* **Tarjetas de Agentes Involucrados** (Comprador vs Vendedor).
* **Tabla de Compromisos Financieros** (Espaciados de celdas y alineación numérica).
* **Bloque de Reciprocidad REA** (Vínculos *Give & Take* destacados en azul `#EFF6FF`).

---

## 6. Conclusión: La Certeza Algorítmica como Realidad Práctica

El ejercicio práctico desarrollado en este capítulo demuestra que la contabilidad por diseño no es un concepto teórico abstracto. Es una arquitectura técnica ejecutable compuesta por herramientas estándares de la industria (XSD, Altova StyleVision, BaseX, XSL-FO, JSON-LD).

Al aplicar **Shift Left**:
1. Eliminamos el error humano en la codificación de transacciones.
2. Capturamos los compromisos económicos antes de que se conviertan en facturas o cuentas por pagar.
3. Alimentamos simultáneamente a los auditores humanos (con documentos PDF impecables) y a los agentes de Inteligencia Artificial (con grafos de conocimiento inmutables).

En el siguiente capítulo analizaremos cómo esta masa de datos estructurados se conecta de forma agéntica con el regulador sin necesidad de intermediarios ni auditorías posteriores.
