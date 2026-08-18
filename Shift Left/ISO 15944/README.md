# Shift Left — Estándar ISO/IEC 15944-4 & Ontología REA / Valueflows

Esta carpeta contiene los esquemas, guías de diseño, módulos RESTXQ y hojas de transformación XSLT que formalizan el enfoque **Shift Left** en la arquitectura **Accounting & Audit by Design (A&AD)**.

---

## 📂 Contenido del Directorio `Shift Left/ISO 15944/`

* **`valueflows_schema.xsd`**: Esquema W3C XML Definition (XSD) oficial de la ontología REA / Valueflows (ISO/IEC 15944-4), incluyendo soporte para partes relacionadas (NIC 24 / IAS 24).
* **`guia_diseno_stylevision_iso15944.md`**: Guía paso a paso para compilar formularios XForms y plantillas electrónicas `.sps` en Altova StyleVision.
* **`iso15944_ingest.xq`**: Módulo RESTXQ para BaseX que captura e ingiere los contratos XML en la fuente.
* **`valueflows_to_html.xslt`**: Hoja de estilo XSLT para transformar transacciones ISO 15944-4 en vistas web HTML5 interactivas y bilingües (`ES` | `EN`).
* **`valueflows_to_pdf.xslt`**: Hoja de estilo XSL-FO para generar reportes impresos en PDF con maquetación formal A4.
* **`Autentic2HTML.xq`** & **`Autentic2PDF.xq`**: Scripts XQuery auxiliares para transformar instancias XML guardadas.
* **`analisis_ontologia_valueflows_all_vf.md`**: Análisis detallado de los mapeos ontológicos de Valueflows.

---

## 🎯 Principio de Operación
El enfoque *Shift Left* desplaza la validación de reglas de negocio y semántica contable **al momento mismo del acuerdo comercial**, garantizando que ninguna transacción ingrese al sistema sin cumplir el esquema formal ISO/IEC 15944-4.
