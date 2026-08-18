---
id: urn:uuid:dbk-escritura-constitucion-001
type: DataBook
title: "Escritura Pública de Constitución - Asignación de Capital"
version: 1.0.0
created: "2026-06-16"
provenance:
  source: "DFRNT MapForce Pipeline"
  method: "Automated Semantic Transmutation"
manifest:
  entrypoints:
    - block: dataset
  blocks:
    dataset:
      type: json-ld
      description: "XBRL GL / REA Semantic Graph (Inline)"
---

# Escritura Pública de Constitución

El siguiente documento detalla la asignación de capital inicial (Momento 0), unificando la narrativa legal con los holones semánticos inyectables en TerminusDB.

### Socio Fundador A
El accionista **Socio Fundador A** suscribe y paga un total de **2500 Cuotas** por un valor monetario de **$2500000 COP**, registrado en la cuenta **311505**.

```json-ld
{
  "@context": {
    "terminus": "terminusdb:///",
    "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#"
  },
  "@type": "gl-cor:EntryDetail",
  "gl-cor:amount": 2500000,
  "gl-cor:agent_identifier": {
    "@id": "terminusdb:///data/GistPerson/Socio_A"
  },
  "gl-cor:measurable": {
    "gl-cor:measurableQuantity": 2500,
    "gl-cor:measurableUnitOfMeasure": "Cuotas"
  }
}
```

### Socio Fundador B
El accionista **Socio Fundador B** suscribe y paga un total de **2500 Cuotas** por un valor monetario de **$2500000 COP**, registrado en la cuenta **311505**.

```json-ld
{
  "@context": {
    "terminus": "terminusdb:///",
    "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#"
  },
  "@type": "gl-cor:EntryDetail",
  "gl-cor:amount": 2500000,
  "gl-cor:agent_identifier": {
    "@id": "terminusdb:///data/GistPerson/Socio_B"
  },
  "gl-cor:measurable": {
    "gl-cor:measurableQuantity": 2500,
    "gl-cor:measurableUnitOfMeasure": "Cuotas"
  }
}
```

### Socio Fundador C
El accionista **Socio Fundador C** suscribe y paga un total de **2500 Cuotas** por un valor monetario de **$2500000 COP**, registrado en la cuenta **311505**.

```json-ld
{
  "@context": {
    "terminus": "terminusdb:///",
    "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#"
  },
  "@type": "gl-cor:EntryDetail",
  "gl-cor:amount": 2500000,
  "gl-cor:agent_identifier": {
    "@id": "terminusdb:///data/GistPerson/Socio_C"
  },
  "gl-cor:measurable": {
    "gl-cor:measurableQuantity": 2500,
    "gl-cor:measurableUnitOfMeasure": "Cuotas"
  }
}
```

### Socio Fundador D
El accionista **Socio Fundador D** suscribe y paga un total de **2500 Cuotas** por un valor monetario de **$2500000 COP**, registrado en la cuenta **311505**.

```json-ld
{
  "@context": {
    "terminus": "terminusdb:///",
    "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#"
  },
  "@type": "gl-cor:EntryDetail",
  "gl-cor:amount": 2500000,
  "gl-cor:agent_identifier": {
    "@id": "terminusdb:///data/GistPerson/Socio_D"
  },
  "gl-cor:measurable": {
    "gl-cor:measurableQuantity": 2500,
    "gl-cor:measurableUnitOfMeasure": "Cuotas"
  }
}
```
