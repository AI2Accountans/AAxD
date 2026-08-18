# La Teoría de la Contabilidad y el Control: Pilar Fundamental de A&AD

## *De Sorter e Ijiri a la Ontología REA y el Control Interno Autónomo en DFRNT*

---

## 1. El Fundamento Teórico: Los Tres Gigantes de la Contabilidad

El framework **Accounting & Audit by Design (A&AD)** no es una simple pila de tecnologías modernas; es la realización computacional de la **Teoría de la Contabilidad y el Control** desarrollada por los más grandes teóricos de la disciplina:

```
         GEORGE H. SORTER (1969)                     YUJI IJIRI (1975)                      WILLIAM E. MCCARTHY (1982)
       "An Events Approach"                     "Theory of Accounting Measurement"               "The REA Accounting Model"
                  │                                         │                                            │
                  ▼                                         ▼                                            ▼
   Captura del Evento Granular sin           Contabilidad de Responsabilidad                 Modelado Semántico en Grafos
  Agregaciones Prematuras (Data-as-Context)      (Accountability, Fuerza Probatoria)            Recursos - Eventos - Agentes (ISO 15944-4)
                  │                                         │                                            │
                  └─────────────────────────────────────────┼────────────────────────────────────────────┘
                                                            │
                                                            ▼
                                           ARQUITECTURA A&AD EN TERMINUSDB / DFRNT
```

### A. George H. Sorter (1969) — *An Events Approach to Basic Accounting Theory*
* **La Crítica de Sorter:** La contabilidad tradicional basada en "valores superagregados" (Value-Weighted Approach) destruye la información y el contexto del hecho de negocio al sintetizar miles de transacciones en un solo número contable.
* **La Solución A&AD:** El modelo **Data-as-Context**. A&AD captura el **evento económico crudo** en su nivel más granular (vía XForms, BaseX e ISO 21378 ADCS). La agregación (Trial Balance, estados financieros) ocurre bajo demanda sobre el Grafo de Conocimiento, permitiendo múltiples vistas sin perder la trazabilidad.

### B. Yuji Ijiri (1975) — *Theory of Accounting Measurement & Accountability*
* **La Filosofía de Ijiri:** La función primordial de la contabilidad no es solo "predecir la toma de decisiones", sino la **rendición de cuentas (*Accountability*)** y la fuerza probatoria de los contratos.
* **La Solución A&AD:** La inmutabilidad del grafo en **TerminusDB** (con versionado bitemporal tipo Git) y el anclaje de compromisos futuros (**ACTUS / ISO 15944-4**) garantizan la inviolabilidad probatoria de los acuerdos entre Agentes.

### C. William E. McCarthy (1982) — *Ontología REA (ISO 15944-4)*
* **El Avance de McCarthy:** Liberar a la contabilidad de las ataduras de los libros de papel del siglo XV (Pacioli) y estructurar los eventos económicos en términos de **Recursos (Resources), Eventos (Events) y Agentes (Agents)**.
* **La Solución A&AD:** REA es el núcleo ontológico de A&AD. Permite que la contabilidad financiera y la contabilidad de sostenibilidad (ESG) convivan en el mismo Grafo de Conocimiento sin duplicidades.

---

## 2. La Transformación del Control Interno: De COSO Reactivo a *Control by Design*

La **Teoría del Control** tradicional (marcos como **COSO ICIF**, **COBIT** u **OCEG GRC**) ha operado históricamente de forma reactiva: inspectores humanos revisando muestras meses después de ocurridas las transacciones.

**A&AD invierte el control interno hacia el paradigma *Control by Design* (Control Incorporado por Diseño):**

| Componente COSO ICIF | Control Tradicional (Reactivo) | Control by Design en A&AD (Autónomo) |
| :--- | :--- | :--- |
| **1. Ambiente de Control** | Políticas escritas en documentos PDF y manuales de procedimiento. | Gobernanza de nivel superior bajo **ISO 21838 (BFO)** e **ISO 15944-4 (REA)** fijada en código. |
| **2. Evaluación de Riesgos** | Matrices de riesgo en Excel actualizadas anualmente. | Reglas **SHACL 1.2** que detectan violaciones de dualidad y anomalías físicas/ESG en tiempo real. |
| **3. Actividades de Control** | Revisiones y firmas manuales ex-post por supervisores. | **Data Contracts (DPROD)** y validaciones sintáctico-semánticas en la ingesta ($1 Prevención / Shift-Left). |
| **4. Información & Comunicación** | Reportes estáticos mensuales distribuibles por correo electrónico. | Endpoints **WOQL/GraphQL** en DFRNT y papeles de trabajo vivos en **Vault-LD (.md con YAML-LD)**. |
| **5. Monitoreo Continuo** | Auditorías internas o externas periódicas por muestreo. | **Agentes IA de Auditoría** inspeccionando el 100% de las transacciones 24/7 sobre Mundo Cerrado (CWA). |

---

## 3. La Partida Triple y el Momentum Contable en A&AD

Ijiri propuso el concepto de **Partida Triple (Momentum Accounting)** para medir no solo el *Stock* (Activo/Pasivo) y el *Flujo* (Ingreso/Gasto), sino la **Aceleración/Impulso** (*Force/Momentum*) de los eventos de negocio.

En la arquitectura **A&AD**:
1. **Primer Elemento (Stock / Recursos):** Representado por los nodos `rea:EconomicResource` en TerminusDB.
2. **Segundo Elemento (Flujo / Eventos):** Representado por los nodos `rea:EconomicEvent` y asientos `XBRL GL`.
3. **Tercer Elemento (Impulso / Compromisos Futuros):** Representado por los contratos `ACTUS` y compromisos `rea:Commitment`.

Gracias al grafo de conocimiento en **TerminusDB**, A&AD calcula automáticamente la trayectoria de salud financiera y operativa de la organización en tiempo real.

---

## 4. Conclusión: El Triángulo de Certeza de A&AD

El framework A&AD logra su certeza algorítmica uniendo tres pilares científicos:

$$\text{Arquitectura Empresarial de Zachman} + \text{Pila Semántica TBL (SHACL 1.2 / RDF)} + \text{Teoría de Contabilidad y Control (Sorter/Ijiri/REA)}$$

Este pilar teórico es el que garantiza que el sistema no sea una simple "herramienta tecnológica", sino **el nuevo sustrato científico de la contabilidad y la auditoría del siglo XXI**.
