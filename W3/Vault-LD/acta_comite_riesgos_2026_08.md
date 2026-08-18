---
@context: "https://dfrnt.io/context/v2.jsonld"
@type: "RiskCommitteeMinute"
@id: "urn:dfrnt:minute:risk-2026-08"
artifact_name: "Acta del Comité de Evaluación de Riesgos - Sesión Ordinaria N° 08-2026"
documentNumber: "ACTA-CER-2026-08"
documentDate: "2026-08-10"
engaged_agents:
  - "GistPerson/Socio_A"
  - "GistPerson/Auditor_Principal"
  - "GistPerson/Oficial_Cumplimiento"
nexus:
  - "SourceDocument/Notaria 25 - 2005"
isGovernedBy: "urn:dfrnt:rule:sbvr:const-01"
riskCategory: "operating-financial"
evaluationStatus: "approved_with_constraints"
---

# Acta del Comité de Evaluación de Riesgos y Control Interno (CER)
**Sesión Ordinaria N° 08-2026**

- **Entidad Evaluada:** [[FIBO_StockCorporation/SOCIEDAD_GENESIS_LTDA]] (NIT 900.123.456-7)
- **Documento Causal Origen:** [[SourceDocument/Notaria 25 - 2005]] (Escritura Pública de Constitución N° 2525 de la Notaría 25)
- **Fecha de Evaluación:** 10 de Agosto de 2026
- **Gobernador Deóntico Transversal:** [[urn:dfrnt:rule:sbvr:const-01]]

---

## 1. Asistentes y Verificación de Quórum

Se reúnen en la sala de juntas de la entidad y vía nodo seguro de gobernanza:
* **Dr. Fernando Morales** — [[GistPerson/Auditor_Principal]] *(Presidente del Comité)*
* **Dra. Elena Restrepo** — [[GistPerson/Oficial_Cumplimiento]] *(Secretaria Técnica)*
* **Don Ricardo Gasca** — [[GistPerson/Socio_A]] *(Representante de los Socios Fundadores)*

Se verifica el quórum reglamentario del 100% para deliberar y tomar decisiones vinculantes.

---

## 2. Orden del Día y Evaluación de Riesgo de Constitución

El Comité de Evaluación de Riesgos procede a analizar la estructura financiera y la suficiencia de capital del asiento de apertura (**Momento Cero**) derivado de la Escritura Pública de Constitución N° 2525.

### 2.1. Análisis del Riesgo de Impago de Capital (NIC 24 / Código de Comercio)
El Oficial de Cumplimiento expone que en la constitución de sociedades de responsabilidad limitada se presenta frecuentemente el riesgo de **"Capital Ficticio o No Liquido"**, mediante el cual se registran aportes de capital utilizando pagarés o cuentas por cobrar a socios ([[Account/311505]] vs [[Account/130505]]), violando la capacidad real de operación.

### 2.2. Aplicación de la Regla Deóntica SBVR (`const-01`)
En virtud de la regla deóntica SBVR [[urn:dfrnt:rule:sbvr:const-01]], registrada en el sistema de gobernanza bajo la modalidad de **Obligación (`obligation`)**:

> *"Es obligatorio el pago del 100% de los aportes de capital al momento de la constitución de la entidad."*

---

## 3. Conclusiones y Dictamen Vinculante del Comité

Tras revisar los registros transaccionales en el vehículo canónico XBRL GL y la proyección en el Libro Diario:

1. **Ratificación del Débito en Caja Real:** Se constata que el aporte total de \$10,000,000 COP fue efectivamente depositado al 100% en la cuenta de efectivo [[Account/110505]] (Caja General / Bancos) según comprobante de depósito, respaldando los créditos de capital de \$2,500,000 COP asignados a cada uno de los cuatro socios fundadores ([[GistPerson/Socio_A]], Socio B, Socio C y Socio D).
2. **Prohibición Estricta de Cuentas por Cobrar:** Se aprueba la restricción deóntica de **Prohibición (`prohibition`)** para la ingesta de cualquier registro de constitución que pretenda sustituir el efectivo en caja por cuentas por cobrar a socios ([[Account/130505]]).
3. **Inmunización Algorítmica SHACL 1.2:** Se solicita a la arquitectura de TI la activación del escudo SHACL 1.2 en [[TerminusDB]] para ejecutar un **Rollback Inmediato ($1 Shift-Left)** en el evento de que cualquier intento de carga viole esta condición.

---

## 4. Cierre y Firma Criptográfica

No habiendo más asuntos que tratar, se levanta la sesión a las 11:30 a.m. La presente acta queda anclada semánticamente al Grafo Bitemporal de Conocimiento mediante su URI determinista `urn:dfrnt:minute:risk-2026-08` con linaje W3C PROV-O.

```yaml
# Firma de Gobernanza Vault-LD
signature:
  signedBy: "urn:dfrnt:agent:auditor-principal"
  timestamp: "2026-08-10T11:30:00-05:00"
  integrityHash: "sha256:a8f9d3b1e7c5a2f4d6e8b0c2a4f6e8d1c3b5a7f9e1d3c5b7a9f0e2d4c6b8a1f3"
```
