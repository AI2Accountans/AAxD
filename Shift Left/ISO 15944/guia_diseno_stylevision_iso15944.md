# Guía Interactiva de Diseño de Formularios ISO 15944-4 en Altova StyleVision

## 📌 Objetivo
Diseñar una plantilla de formulario interactiva (`.sps`) en **Altova StyleVision Enterprise Edition** que mapee los campos del esquema **[valueflows_schema.xsd](valueflows_schema.xsd)**, generando una vista fluida de contrato inteligente e ingiriendo las instancias XML directamente en **BaseX** (`ubl2dfrnt`).

---

## 🛠️ Requisitos Previos
* **Altova StyleVision** instalado.
* BaseX corriendo localmente en el puerto `8984`.
* Módulo RESTXQ de ingesta ubicado en `C:\Program Files (x86)\BaseX\webapp\iso15944_ingest.xq`.

---

## 🚀 Pasos de Construcción en StyleVision

### 1. Inicialización del Proyecto
1. Abre **Altova StyleVision**.
2. Selecciona **File -> New -> New from XML Schema / DTD / XML**.
3. Selecciona el esquema: `Shift Left/ISO 15944/valueflows_schema.xsd`.
4. Asigna como archivo XML de prueba: `Ricordanze Plane/valueflows_sample_instance.xml`.
5. En el cuadro de diálogo de plantilla, selecciona **`Free-Flow Document`**.

### 2. Diseño del Encabezado (Header Banner)
1. Inserta una tabla de 1 fila x 2 columnas para el encabezado superior.
2. Aplica estilo de fondo azul oscuro (`#1E1B4B`) y texto blanco.
3. En la columna izquierda:
   * Arrastra `transactionId` como **Input Field**.
   * Arrastra `issueDate` como **Input Field** con formato fecha.
   * Arrastra `governingJurisdiction` como **Input Field**.

### 3. Sección del Acuerdo y Partes Relacionadas (NIC 24)
1. Arrastra `vf:agreement` al lienzo.
2. En `buyer` y `seller`:
   * Arrastra `vf:name` como **Input Field**.
   * Arrastra `vf:isRelatedParty` como **Check Box `[X]`**.
   * Arrastra `vf:relatedPartyType` como **Combo Box** desplegable con los valores de `RelatedPartyTypeEnum`.

### 4. Tabla Dinámica de Compromisos Económicos (REA Commitments)
1. Despliega `vf:commitments` y haz clic derecho en `vf:commitment`.
2. Selecciona **Insert Table -> Dynamic Table**.
3. Elige las 6 columnas principales para evitar saturar el ancho de página:
   - `id`
   - `action` (Combo Box de acciones REA)
   - `provider`
   - `receiver`
   - `resourceQuantity/value` + `resourceQuantity/unitSymbol`
   - `due`

### 5. Configuración del Botón de Envío Inmediato a BaseX (Shift Left)
1. En la barra de herramientas, inserta un **Button**.
2. Cambia la etiqueta del botón a: `Firmar & Ingerir Contrato en BaseX`.
3. En las propiedades de acción del botón, configura:
   * **Action:** `Submit XML`.
   * **Target URL:** `http://localhost:8984/iso15944/ingest`
   * **HTTP Method:** `POST`.
