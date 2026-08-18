# Traducción de la Taxonomía GRC-XML (OCEG) a Web Semántica (SHACL y SPARQL)

Al analizar la taxonomía original en XBRL (`risk.xsd` y `control.xsd`), encontramos que OCEG define un Riesgo con atributos clave como `likelihood` (Probabilidad), `impact` (Impacto), `inherentRiskScore`, y `mitigatingControls` (Controles Mitigantes). 

A continuación, se presenta cómo esta estructura rígida de XML de 2010 se transforma en una poderosa arquitectura de **Grafos de Conocimiento** para Auditoría Continua en 2026.

---

## 1. La Ontología GRC (El Grafo)
En lugar de un esquema `.xsd`, definimos las Clases en RDF (Turtle) para inyectarlas en TerminusDB. Note cómo los elementos exactos del esquema de OCEG se conservan semánticamente.

```turtle
@prefix grc: <http://www.oceg.org/ontology/grc#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Equivalente a <xsd:element name="risk" ...>
grc:Risk a rdfs:Class ;
    rdfs:label "Risk Event" ;
    rdfs:comment "A potential event that may impact the organization." .

grc:Control a rdfs:Class ;
    rdfs:label "Control Activity" ;
    rdfs:comment "A policy or procedure that mitigates a Risk." .

# Propiedades extraídas del risk.xsd de OCEG
grc:hasLikelihood a rdf:Property ; rdfs:range xsd:string . # High, Medium, Low
grc:hasImpact a rdf:Property ; rdfs:range xsd:string . # Grave, Serious, Minor
grc:mitigatesRisk a rdf:Property ; rdfs:domain grc:Control ; rdfs:range grc:Risk .
```

---

## 2. SHACL: El "Guardián" (Shift Left)
Aquí es donde ocurre la magia de la Auditoría Continua (Continuous Control Monitoring). Tomamos una actividad de control de OCEG y la convertimos en una regla **SHACL ejecutable**. 

Este SHACL evalúa, por ejemplo, que si entra un contrato financiero (CDT), su tasa no exceda los límites de control, y *etiqueta la violación con el riesgo exacto de la taxonomía OCEG*.

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix grc: <http://www.oceg.org/ontology/grc#> .
@prefix actus: <https://www.actusfrf.org/ontology/actus#> .

grc:CDT_InterestRateGuardian a sh:NodeShape ;
    sh:targetClass actus:PAMContract ; # Apunta a los datos transaccionales (XBRL GL / ACTUS)
    
    # === METADATOS DE TRAZABILIDAD OCEG ===
    grc:implementsControl grc:Control_011210_RateLimit ;
    grc:mitigatesRisk grc:Risk_MarketFluctuation ;
    
    sh:property [
        sh:path actus:nominalInterestRate ;
        sh:minInclusive 0.08 ;
        sh:maxInclusive 0.11 ;
        sh:message "Alerta de Auditoría Continua: La tasa excede el límite del 11%. Violación del Control OCEG 011210." ;
        sh:severity sh:Violation ;
    ] .
```
> **Nota de Arquitectura:** Cuando PySHACL evalúa el JSON-LD de un asiento contable contra esta forma, si la tasa es 15%, bloquea la transacción y retorna el mensaje exacto, logrando la prevención en tiempo real (Shift Left).

---

## 3. SPARQL: El Motor de Reporte de Auditoría
Si un auditor externo (como sugiere el modelo de Vasarhelyi) necesita comprobar que el entorno de control COSO está activo y automatizado en los sistemas, no necesita revisar manuales. Ejecuta esta consulta SPARQL directamente sobre el Grafo:

```sparql
PREFIX sh: <http://www.w3.org/ns/shacl#>
PREFIX grc: <http://www.oceg.org/ontology/grc#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?guardianSHACL ?controlAplicado ?riesgoMitigado ?reglaDeAuditoria
WHERE {
  # Buscar todas las formas SHACL que actúan como Guardianes
  ?guardianSHACL a sh:NodeShape ;
                 grc:implementsControl ?control ;
                 grc:mitigatesRisk ?riesgo ;
                 sh:property ?propiedad .
                 
  # Extraer la metadata del riesgo/control desde la ontología OCEG
  ?control rdfs:label ?controlAplicado .
  ?riesgo rdfs:label ?riesgoMitigado .
  
  # Extraer el mensaje de error de auditoría que se dispara
  ?propiedad sh:message ?reglaDeAuditoria .
}
```

### Resultado de la Consulta
| GuardianSHACL | ControlAplicado | RiesgoMitigado | ReglaDeAuditoria |
|--------------|----------------|----------------|-----------------|
| `grc:CDT_InterestRateGuardian` | Límite de Tasa de Interés | Fluctuación de Mercado | Alerta de Auditoría Continua: La tasa excede el límite... |

De esta manera, la taxonomía estática de OCEG cobra vida y se convierte en un sistema defensivo y auditable matemáticamente.
