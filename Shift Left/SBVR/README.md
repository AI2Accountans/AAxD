# Módulo SBVR (Semantics of Business Vocabulary and Business Rules)

Este directorio forma parte del pipeline **Shift Left ($1 Prevención)** dentro del framework **Accounting & Audit by Design (A&AD)**.

Se encuentra ubicado en la raíz del repositorio a la misma altura que `ISO 15944/`:

```
Shift Left /
├── ISO 15944 /                              <-- Ontología REA (ISO 15944-4)
├── SBVR /                                   <-- Vocabulario & Reglas Deónticas (OMG Standard)
│   ├── SBVR-XML-Schema.xsd                  <-- Esquema XSD Normativo OMG 1.5 (dtc/19-05-32)
│   ├── sbvr_metamodel.ttl                   <-- Ontología Metamodelo OMG SBVR en OWL 2 / Turtle
│   ├── sbvr_ubl_rea_reconciliation.jsonld   <-- Matriz Canónica de Conciliación (owl:equivalentClass)
│   ├── sbvr_fundamentos_arquitectura_aad.md <-- Documento Maestro: Fundamentos y Rol Deóntico
│   └── README.md
├── Ricordanze Plane /                       <-- Registro Primario de Eventos & Contratos (ACTUS)
└── ISO15944.sps                             <-- Plantilla de Captura (Altova StyleVision)
```

---

## 1. Documentos Clave

1. 📘 **[sbvr_fundamentos_arquitectura_aad.md](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Shift%20Left/SBVR/sbvr_fundamentos_arquitectura_aad.md):**  
   Explicación magistral sobre el problema raíz que resuelve SBVR (La Torre de Babel), los 2 cimientos (Vocabulario de Negocio y Reglas Deónticas/Aléticas), el ejemplo ejecutable NIC 24 a SHACL 1.2, y el rol de SBVR como Gobernador Deóntico Transversal para LLMs y Agentes de IA.
2. 📄 **[SBVR-XML-Schema.xsd](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Shift%20Left/SBVR/SBVR-XML-Schema.xsd):**  
   Esquema XSD normativo oficial de OMG SBVR 1.5 (`dtc/19-05-32`).
3. 📄 **[sbvr_metamodel.ttl](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Shift%20Left/SBVR/sbvr_metamodel.ttl):**  
   Ontología en OWL 2 / RDF Turtle del metamodelo OMG SBVR 1.5.
4. 📄 **[sbvr_ubl_rea_reconciliation.jsonld](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Shift%20Left/SBVR/sbvr_ubl_rea_reconciliation.jsonld):**  
   Matriz canónica que mapea `sbvr:NounConcept` = `rea:Agent` = `ubl:Party` mediante `owl:equivalentClass`.

---

## 2. Resumen de la Arquitectura A&AD

* **UBL:** Pone el contrato de intercambio comercial.
* **ISO 15944 (REA):** Pone la causalidad económica.
* **XBRL GL + SRCD:** Pone la estructura contable multidimensional.
* **SBVR:** Gobernador Deóntico Transversal (la mente formal que expresa las reglas claramente para humanos y compilables vía SHACL para la IA).
