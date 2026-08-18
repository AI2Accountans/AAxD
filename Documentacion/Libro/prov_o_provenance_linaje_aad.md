# El Modelo W3C PROV-O (Provenance) en la Arquitectura Accounting & Audit by Design (A&AD)

**Autor:** Richard Gasca (`co.auditoria@pm.me`)  
**Estándar Normativo:** W3C PROV-O (Provenance Ontology / `http://www.w3.org/ns/prov#`)  
**Ubicación:** `Documentacion/Libro/prov_o_provenance_linaje_aad.md`

---

## 1. ¿Qué es W3C PROV-O y por qué es Vital en Auditoría?

El estándar del W3C **PROV-O (Provenance Ontology)** define la estructura matemática para registrar el **linaje, la cadena de custodia y la procedencia ininterrumpida de los datos**.

En contabilidad y auditoría tradicional, cuando un número aparece en un reporte financiero, es casi imposible rastrear mecánicamente qué software lo transformó, qué usuario lo ingresó originalmente y de qué contrato proviene.

En el framework **Accounting & Audit by Design (A&AD)**, **PROV-O opera como el tejido transversal de trazabilidad**, conectando cada nodo del Grafo de Conocimiento con su origen legal indiscutible.

---

## 2. Los 3 Pilares Fundamentales de W3C PROV-O

PROV-O se estructura sobre una triada conceptual muy simple y poderosa:

```mermaid
graph TD
    subgraph W3C_PROVO_Triad["Triada del Estándar W3C PROV-O"]
        Entity["prov:Entity (Entidad)<br/>Artefactos o Datos<br/>(XML BaseX, PDF, XBRL GL, JSON-LD, Grafo)"]
        Activity["prov:Activity (Actividad)<br/>Procesos o Transformaciones<br/>(FormSubmission, MapForceTransmutation, TerminusDBCommit)"]
        Agent["prov:Agent (Agente)<br/>Responsables del Proceso<br/>(Socio, Auditor, Engine MapForce, DFRNT Engine)"]
    end

    Agent -->|prov:wasAssociatedWith| Activity
    Activity -->|prov:generated| Entity
    Entity -->|prov:wasDerivedFrom| Entity
```

---

## 3. ¿En qué lugar EXACTO entra Provenance dentro de tu Stack A&AD?

**PROV-O amarra las 3 capas del pipeline de extremo a extremo:**

```mermaid
graph TD
    subgraph 1_ShiftLeft_Origen["1. Captura en Origen (Shift-Left)"]
        Act_XForms["prov:Activity: FormSubmission_XForms"]
        Ent_XML["prov:Entity: XML_Acta_BaseX"]
        Ag_Auditor["prov:Agent: GistPerson/Auditor_Principal"]
        Ag_Auditor -->|prov:wasAssociatedWith| Act_XForms
        Act_XForms -->|prov:generated| Ent_XML
    end

    subgraph 2_Transmutacion_MapForce["2. Transmutación Canónica (XBRL GL)"]
        Act_MapForce["prov:Activity: MapForce_Transmutation"]
        Ent_JSONLD["prov:Entity: JSONLD_V2_Payload"]
        Ag_MapForce["prov:Agent: Altova_MapForce_Engine"]
        Ent_JSONLD -->|prov:wasDerivedFrom| Ent_XML
        Ag_MapForce -->|prov:wasAssociatedWith| Act_MapForce
        Act_MapForce -->|prov:generated| Ent_JSONLD
    end

    subgraph 3_Inmunizacion_TerminusDB["3. Ingesta & Grafo Inmutable (TerminusDB)"]
        Act_Commit["prov:Activity: TerminusDB_Commit_Ingestion"]
        Ent_Graph["prov:Entity: TerminusDB_Knowledge_Graph"]
        Ag_DFRNT["prov:Agent: DFRNT_TerminusDB_Engine"]
        Ent_Graph -->|prov:wasDerivedFrom| Ent_JSONLD
        Ag_DFRNT -->|prov:wasAssociatedWith| Act_Commit
        Act_Commit -->|prov:generated| Ent_Graph
    end
```

---

## 4. Respuestas Forenses Inmediatas que PROV-O otorga al Auditor

Mediante la inclusión de las propiedades **W3C PROV-O** en tu JSON-LD V2 (`nexus`, `wasDerivedFrom`, `wasAttributedTo`), el auditor puede realizar consultas SPARQL/WOQL instantáneas:

1. **Prueba de Origen (`prov:wasDerivedFrom`):**  
   Demuestra que el asiento en el Libro Diario (`EntryDetail`) proviene del payload JSON-LD de MapForce, que a su vez se derivó del XML original guardado en BaseX desde el formulario XForms.
   $$\text{TerminusDB Graph} \xrightarrow{\text{wasDerivedFrom}} \text{JSON-LD V2} \xrightarrow{\text{wasDerivedFrom}} \text{XBRL GL} \xrightarrow{\text{wasDerivedFrom}} \text{XML BaseX (XForms)}$$

2. **Prueba de Responsabilidad (`prov:wasAttributedTo` / `prov:wasAssociatedWith`):**  
   Identifica qué agente humano (`GistPerson/Auditor_Principal`) o agente informático (`Engine/MapForce`) ejecutó cada transformación.

3. **Prueba de Integridad Temporal (`prov:startedAtTime` / `prov:endedAtTime`):**  
   Diferencia el tiempo en el que ocurrió el hecho en el mundo real (*Valid Time*) del tiempo en que el dato ingresó criptográficamente a la base de datos (*Transaction Time*), haciendo imposible la alteración retroactiva de la contabilidad.
