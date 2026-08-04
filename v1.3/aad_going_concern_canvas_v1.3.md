# A&AD Going Concern Onboarding Canvas — Versión 1.3

*Metodología de Implementación para Entidades en Marcha (SMEs & Firmas Tier 2)*  
*Con Captura Upstream (Shift Left ISO 15944), Base de Datos NoSQL y Proyección Dual al Plano Ricordanze*

---

## 1. El Nuevo "Momento 0" (Génesis Operacional)
Para una entidad en marcha, el universo semántico comienza con una foto inmutable de su estado actual, no con su escritura de constitución original.

*   **Balance de Apertura (Opening Balance Sheet):** El saldo inicial estructurado (XBRL GL). Este es el *holón* fundacional del nuevo Gemelo Digital. Todos los eventos futuros se calculan matemáticamente a partir de este punto.

---

## 2. Contexto Semántico y Legal + Shift Left (ISO 15944 & ACTUS)
Un saldo en el balance no significa nada sin los derechos, obligaciones y reglas que lo sustentan.

*   **Contratos Activos (ACTUS Framework):** Digitalización y extracción de todos los contratos vigentes (financieros con ACTUS y operacionales encuadrados en ISO 15944-4 / REA).
    *   **Captura Upstream (Shift Left XForms):** Formularios **XForms** (compilados vía Altova StyleVision) permiten la captura limpia de intenciones y transacciones en la fuente encuadradas en ISO 15944 REA.
    *   **Base de Datos NoSQL (Instancia XML):** Los formularios envían la instancia XML vía HTTP POST a la **Base de Datos NoSQL**, que encuadra y alimenta la caja de *Contratos Activos*.
    *   **Proyección al Plano Ricordanze:** Desde la Base de Datos NoSQL se proyectan vistas **HTML5 / PDF** hacia el *Semantic Ricordanze Plane* para conservación inmutable exigida por el sistema legado.
*   **Políticas Contables:** Las reglas de juego (US GAAP, IFRS, políticas internas) codificadas como restricciones formales en la ontología para gobernar el comportamiento del grafo.

---

## 3. Anclaje de Confianza (Assurance Anchor)
El "Shift-Left" requiere que la información que entra al sistema ya esté validada.

*   **Reporte del Auditor (Auditor's Report):** El dictamen del auditor independiente sobre el Balance de Apertura. Este documento firma criptográficamente la validez del Momento 0, estableciendo la confianza base sin necesidad de revisar la historia anterior al ERP legado.

---

## 4. Hidratación Histórica (El Puente)
Una vez establecido y validado el Momento 0, se debe conectar con el presente.

*   **Asientos Contables del Sistema Legado (Legacy Journal Entries):** Extracción de los asientos de diario desde la fecha de apertura hasta el día actual. Estos se transmutan mediante Altova MapForce de su formato tabular (CSV/SQL) a **JSON-LD (Eventos REA)**.
*   *Nota técnica:* Esta ingesta masiva se somete a validación **SHACL** instantánea al entrar al grafo.

---

## 5. El Estado Destino (El Grafo Operativo)
El resultado final de la implementación.

*   **TerminusDB / DFRNT Instanciado:** La base de datos de grafo inmutable, hidratada con el Momento 0, el contexto legal, y la historia reciente.
*   **Capacidad QOWL:** La información financiera ahora puede ser consultada multidimensionalmente usando GraphQL sobre OWL, permitiendo reportes simultáneos (NIIF, Fiscal, ESG) y auditorías por agentes de IA (**Zero-shot Audit**).

---

### Diagrama de Flujo de Implementación (Pipeline v1.3)

```mermaid
graph TD
    %% Shift Left Flow: XForms -> NoSQL DB -> Contratos Activos
    B1[Captura Upstream XForms<br>ISO 15944 REA] -->|HTTP POST XML| B2[Base de Datos NoSQL<br>Instancia XML]
    B2 -->|Encuadra Captura| B[Contratos Activos<br>ACTUS Framework]
    
    %% Plano Ricordanze (Proyección Documental)
    B2 -->|Proyección Documental| B3[Plano Ricordanze<br>HTML5 / PDF Legado]
    
    %% Nodos de Origen (Génesis / Momento 0)
    A[Balance de Apertura] -->|XBRL GL| E
    B -->|Metadata Financiera y Operacional| E
    C[Políticas Contables] -->|Ontología / SKOS| E
    D[Reporte del Auditor] -->|Firma de Confianza| E
    
    %% Nodo Central: El Momento 0
    E((Establecimiento del<br>Nuevo Momento 0))
    
    %% Ingesta Histórica Legada
    F[Sistemas ERP Legados] -->|Asientos de Diario CSV| G[Altova MapForce<br>Transmutación Semántica]
    G -->|Eventos de Negocio REA<br>JSON-LD| H{Validación SHACL}
    
    %% Flujo al Grafo
    E --> H
    H -->|Aprobado| I[(TerminusDB / DFRNT<br>Semantic Knowledge Graph)]
    
    %% Salidas
    I -->|QOWL Queries| J[Reportes Multidimensionales<br>NIIF / Fiscal / ESG]
    I -->|Zero-shot Audit| K[Agentes Autónomos IA]
    
    %% Estilos
    classDef genesis fill:#0d9488,stroke:#0f766e,stroke-width:2px,color:white;
    classDef process_legacy fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:white;
    classDef process_aad fill:#10b981,stroke:#047857,stroke-width:2px,color:white;
    classDef database fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:white;
    classDef output fill:#7c3aed,stroke:#5b21b6,stroke-width:2px,color:white;
    classDef shiftleft fill:#0ea5e9,stroke:#0284c7,stroke-width:2px,color:white;
    classDef ricordanze fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:white;
    
    class A,B,C,D,E genesis;
    class F,G process_legacy;
    class H process_aad;
    class I database;
    class J,K output;
    class B1 shiftleft;
    class B2 process_legacy;
    class B3 ricordanze;
```
