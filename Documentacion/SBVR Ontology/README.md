# Ontología OMG SBVR (Semantics of Business Vocabulary and Business Rules)

Este directorio contiene las especificaciones ontológicas formales del estándar **OMG SBVR 1.5** en formato **OWL 2 / RDF Turtle (`.ttl`)** y su documentación asociada para el framework **Accounting & Audit by Design (A&AD)**.

---

## 1. Contenido del Directorio

* 📄 **`sbvr_metamodel.ttl`**: Ontología formal en OWL 2 / Turtle (`http://www.omg.org/spec/SBVR/20190901/sbvr#`) que define el metamodelo de OMG SBVR:
  * **Conceptos:** `sbvr:NounConcept`, `sbvr:GeneralConcept`, `sbvr:FactType`, `sbvr:BinaryFactType`.
  * **Reglas de Negocio:** `sbvr:BusinessRule`, `sbvr:StructuralRule`, `sbvr:OperatingRule`.
  * **Modalidades Deónticas:** `sbvr:ObligationFormulation`, `sbvr:ProhibitionFormulation`, `sbvr:PermissibilityFormulation`.
  * **Cuantificadores:** `sbvr:UniversalQuantification`, `sbvr:ExistentialQuantification`, `sbvr:AtLeastNQuantification`.

---

## 2. Propósito e Integración con A&AD ($1 Shift-Left)

Esta ontología actúa como la **fuente de gobernanza normativa internacional** para A&AD:

1. **Expresión Formal de Reglas de Negocio:** Permite que los contadores y auditores definan reglas en lenguaje natural estructurado (ej. *"It is obligatory that every Invoice > $10,000 USD is associated with a signed NIIF 15 Contract"*).
2. **Compilación Directa a SHACL 1.2:** La estructura ontológica de `sbvr_metamodel.ttl` permite compilar automáticamente las reglas de negocio redactadas por contadores a restricciones **SHACL 1.2 / SPARQL / Datalog** para inyección inmutable en **TerminusDB vía DFRNT**.
3. **Conciliación con UBL y REA (ISO 15944-4):** Mapea los conceptos deónticos de SBVR con los nodos de datos de UBL y REA mediante equivalencias `owl:equivalentClass` sin duplicar tripletas en el grafo.
