# Modulo SBVR (Semantics of Business Vocabulary and Business Rules)

Este directorio forma parte del pipeline **Shift Left ($1 Prevención)** dentro del framework **Accounting & Audit by Design (A&AD)**.

Se encuentra ubicado en la raíz del repositorio a la misma altura que `ISO 15944/`:

```
Shift Left /
├── ISO 15944 /                      <-- Ontología REA (ISO 15944-4)
├── SBVR /                           <-- Vocabulario & Reglas Deónticas (OMG Standard)
│   ├── SBVR-XML-Schema.xsd          <-- Esquema XSD Normativo OMG 1.5 (dtc/19-05-32)
│   ├── sbvr_metamodel.ttl           <-- Ontología Metamodelo OMG SBVR en OWL 2 / Turtle
│   ├── sbvr_ubl_rea_reconciliation.jsonld <-- Matriz Canónica de Conciliación (owl:equivalentClass)
│   └── README.md
├── Ricordanze Plane /               <-- Registro Primario de Eventos & Contratos (ACTUS)
└── ISO15944.sps                     <-- Plantilla de Captura (Altova StyleVision)
```

---

## 1. Propósito e Integración

1. **Separación de Incumbencias (*Separation of Concerns*):**
   * **UBL y REA (ISO 15944-4)** proveen la estructura de datos y los verbos/nodos económicos.
   * **SBVR** provee exclusivamente la **Lógica de Reglas de Negocio y Deóntica** (*Obligatorio, Prohibido, Permitido*).
2. **Matriz de Conciliación Semántica (`sbvr_ubl_rea_reconciliation.jsonld`):**
   * Elimina la duplicación de tripletas en el grafo de **TerminusDB**. Mapea `sbvr:NounConcept` = `rea:Agent` = `ubl:Party` hacia un nodo canónico unificado `urn:dfrnt:agent:...`.
3. **Inmunidad en Tiempo Real ($1 Shift-Left):**
   * Las reglas SBVR escritas en español/inglés estructurado se compilan a **SHACL 1.2 / Datalog Rules** para ser ejecutadas en la ingesta por el motor **DFRNT**.
