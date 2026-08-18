# Análisis Estratégico: Posición de COSO sobre IA Generativa

**Fecha de análisis:** 15 de julio de 2026
**Referencia:** Documento `GenerativeAI.pdf` (COSO - *Achieving Effective Internal Control Over GENERATIVE AI*)

Este documento analiza cómo la posición oficial de COSO valida directamente la necesidad de la arquitectura **Accounting & Audit by Design (A&AD)** y el **Semantic Ricordanze Plane (SRP)** en el entorno financiero.

---

## 1. El Problema Central Identificado por COSO
La posición de COSO se resume en una advertencia lapidaria sobre la naturaleza de los LLMs:
> *"GenAI is probabilistic, not deterministic. GenAI outputs are probabilistic and can be confidently wrong. Controls should treat outputs as claims requiring validation, rather than as facts..."* (Pág 8).

**El miedo de los auditores:**
COSO advierte a la industria que no se puede depender de la Inteligencia Artificial Generativa para tomar decisiones financieras, contables o regulatorias autoritativas porque **alucina y carece de determinismo**. Para mitigar esto, proponen controles exhaustivos, validaciones manuales (human-in-the-loop) y el uso de "algoritmos de referencia determinísticos" (Pág 14).

## 2. El Encuadre con la Arquitectura A&AD
El marco de COSO encuadra de manera perfecta y simbiótica con A&AD. Mientras que COSO provee un listado de controles paliativos para sistemas probabilísticos riesgosos, A&AD provee la solución estructural de raíz: **resolver el problema por diseño.**

### A. Solución a la Falta de Determinismo
*   **Requerimiento COSO:** Validar la IA probabilística con modelos determinísticos.
*   **Solución A&AD:** El *Semantic Ricordanze Plane (SRP)* utiliza el motor **ACTUS**. ACTUS no es probabilístico; es matemática pura y determinística. La proyección de flujos de caja y cálculos contractuales son una verdad inquebrantable, eliminando el riesgo de "alucinación" en el procesamiento principal.

### B. Solución a la Pérdida de Procedencia (Provenance)
*   **Requerimiento COSO:** Evitar la "Pérdida de Provenance" (Pág 23), que es el riesgo de no saber el origen de los datos al ingresarlos a los modelos, destruyendo la auditabilidad.
*   **Solución A&AD:** Al utilizar **TerminusDB**, se cuenta con un Grafo de Conocimiento *bitemporal*. La pérdida de procedencia es imposible por arquitectura, ya que cada transacción mantiene un rastro criptográfico del momento de creencia y el momento de ocurrencia.

### C. Reconciliación y Fragmentación
*   **Requerimiento COSO:** Controlar estrictamente la ingesta y transformación de datos para evitar que los errores silenciosos corrompan la integridad (*Silent corruption from mapping errors* - Pág 24).
*   **Solución A&AD:** La estandarización desde el "Momento Cero" mediante la semántica inmutable de **XBRL GL** elimina el concepto de "reconciliación a posteriori", que es la principal fuente de fragilidad en bases de datos relacionales (*Chance Products*).

## 3. El Rol Correcto de la IA (Auditoría Zero-Shot)
COSO pide segregar estrictamente la "asistencia" de la IA de la "toma de decisiones autoritativas" (Pág 13). 
En el stack A&AD, **la IA no calcula la contabilidad ni ejecuta las transacciones**. Todo el peso matemático y lógico descansa en el sustrato computacional determinístico (SRP + ACTUS + XBRL). 
La IA se despliega en la capa superior (como un *AI-Ready Glass Box*) exclusivamente para tareas de consulta, análisis de tendencias y **Auditoría Zero-Shot**, donde su razonamiento está enraizado (*grounded*) rígidamente en un grafo inmutable, evitando cualquier posibilidad de sobre-dependencia irresponsable.

---
**Conclusión Comercial / Académica:**
El reporte de COSO demuestra que intentar gobernar la Inteligencia Artificial Generativa sobre infraestructuras legacy (relacionales) es riesgoso e ineficiente. A&AD es el sustrato computacional necesario (Semantic Ricordanze Plane) que los reguladores y auditores globales exigen para operar de manera segura en la era algorítmica.
