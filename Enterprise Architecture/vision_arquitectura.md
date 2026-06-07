# Visión de la Arquitectura Empresarial Fundacional

**Fecha de consolidación:** Abril 2026
**Ecosistema:** TerminusDB (DFRNT), MapForce, XBRL GL, UBL.

## 1. El Fundamento Teórico (Sunder + Zachman)

El diseño arquitectónico de **Momento Cero** abandona las representaciones planas tradicionales (tablas SQL/CSV estáticas) para abrazar un modelo de base de datos de grafos orientado por documentos (JSON-LD) que respeta íntegramente dos grandes marcos conceptuales:

### La Lente de Zachman (Matriz Dimensional)
La empresa se modela en su nivel de máxima abstracción (Planner Level), garantizando que se respondan las interrogantes universales:
*   **QUIÉN (Who):** Los Agentes.
*   **QUÉ (What):** Los Recursos, activos y datos contables.
*   **DÓNDE (Where):** Las Ubicaciones / Nodos transaccionales.
*   **CUÁNDO (When):** Los Eventos de afectación a lo largo del tiempo.
*   **POR QUÉ y CÓMO (Why / How):** Los Contratos y las mecánicas operativas.

### La Lente de Shyam Sunder (Teoría de la Contabilidad y el Control)
Extraída directamente de su texto, la entidad se concibe intrínsecamente como un **"Nexo de Contratos"** entre individuos de interés (Stakeholders). Para evitar que este nexo se rompa, se requiere un mecanismo de **control** y **equilibrio**. La contabilidad asume su fin superior: proveer *"hechos fehacientes y compartidos para la resolución de conflictos"*. 

Esta fusión da a luz a nuestras **6 Clases Maestras** de TerminusDB:
1. `Agent` (Inversores, Clientes B2B, Gobierno, Empleados)
2. `Resource` (Flujos de efectivo, saldos contables)
3. `Contract` (Políticas de equilibrio y gobernanza)
4. `Event` (La materialización de un intercambio o corte)
5. `Location` 
6. `Entity` (El Nexo Supremo de Contratos)

---

## 2. Inyección Semántica: Alineación XBRL Global Ledger

El sistema es robusto y puede sostener financieramente a la entidad a partir de un **Balance de Apertura (Momento 0)**. Conservando la meta de ultra-simplicidad de este esquema, alineamos la taxonomía oficial **XBRL GL 2006** (`Trial_Balance_704171.xml`) sin necesidad de inflar el código:

*   **El Catálogo de Cuentas (`<gl-cor:account>`) $\to$ Se modela a través del Nodo `Resource`:**
    *   `accountMainID` (Ej. 1001)
    *   `accountMainDescription` (Ej. Banco / Efectivo Operativo)
    *   `accountPurposeCode`
*   **Los Saldos Iníciales (`<gl-cor:entryDetail>`) $\to$ Se modelan como un Nodo `Event`:**
    *   `amount` (El impacto financiero contable)
    *   `debitCreditCode` ('D' o 'C')
    *   `xbrlInclude`: Constante inyectada como `"beginning_balance"` para estampar que este salto temporal es el Momento Cero sin precedente histórico.
    *   `postingDate` (Fecha de corte)

---

## 3. Orquestación y Mapeo ETL con Altova MapForce

La superestructura abstracta se alinea con el mundo material de ingesta (Facturas en formato UBL y/o XMLs transaccionales) a través de una tubería con Altova MapForce.

Dado que MapForce opera estructurando validadores transaccionales ($schema JSON plano) y no ontologías relacionales RDF (JSON-LD de TerminusDB), la estrategia es una inyección mediante **ejemplos tipo Payload (`payload-ejemplo-mapforce.json`)**:

1. **Source:** MapForce lee un documento contable crudo (UBL/XBRL local).
2. **Target Schema:** MapForce infiere e inserta las ramificaciones JSON correctas basándose en el Payload de Ejemplo (creando los objetos `Agent`, `Resource`, `Event` dinámicamente).
3. **Mapeo Visual:** Trazamos visualmente el monto y la fecha hacia los atributos del Evento, y ligamos las partes afectadas.
4. **Exportación e Ingesta:** Al generar la salida, MapForce orquesta miles de pequeñas piezas unificadas en un archivo compatible sintácticamente con JSON-LD que TerminusDB consume de golpe, encendiendo el motor de grafos y dibujando de manera visible todos los vínculos monetarios al instante.
