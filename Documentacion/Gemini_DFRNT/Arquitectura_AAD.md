# Manifiesto y Arquitectura: Accounting and Audit by Design (A&AD)
**Autor:** Richard Gabriel Gasca Buelvas  
**Versión de la Arquitectura:** 1.1 (Julio, 2026)  
**Entorno de Desarrollo:** Bogotá, Colombia  

---

## I. Principios Epistemológicos de la Contabilidad por Diseño

### 1. La Naturaleza Predictiva del Hecho Financiero
*   **Axioma Central:** La contabilidad es inherentemente *predictiva* y *cartográfica*, no conclusiva. 
*   **La Hipótesis del Negocio en Marcha (Going Concern):** Bajo los marcos internacionales (NIIF/IFRS), los estados financieros no son registros estáticos del pasado, sino previsiones de continuidad. Un activo o un pasivo representan la predicción de flujos de efectivo y comportamientos contractuales futuros.
*   **La Excepción de Liquidación:** La contabilidad solo se transforma en un sistema *conclusivo* cuando la entidad entra en un proceso de liquidación, momento en el cual la hipótesis de negocio en marcha desaparece y el tiempo del sistema se detiene, cambiando a una base estricta de Valor Neto de Realización.

### 2. El Derrumbe de las Ilusiones Tecnológicas
*   **La Ilusión de la Ontología (Nicolas Figay):** Los modelos estadísticos de Inteligencia Artificial (LLMs) no generan ontologías reales ni compromisos institucionales genuinos; producen representaciones candidatas plausibles pero propensas a la *alucinación por falsa coherencia*.
*   **El Techo Estructural de la Lógica Clásica:** Las ontologías formales tradicionales en el Mundo Abierto (OWL DL) sufren de un techo de tratabilidad computacional. Para mantener la decidibilidad, ocultan la incertidumbre mediante el *silencio*, omitiendo las complejas realidades de $n$-vías que gobiernan los negocios.
*   **El Error de "Plataformización" (Eric Cohen):** Tratar al contador como un "cliente" de software propietario cerrado (estilo las cajas negras corporativas de Intuit) destruye la gobernanza de la información. El framework A&AD defiende la *Soberanía Semántica del Auditor*, donde el profesional diseña y controla las leyes lógicas de sus datos mediante estándares abiertos (XBRL GL, JSON-LD, REA).

---

## II. El Sustento Científico: Modelos Universales Core

La validación cruzada entre restricciones de cumplimiento (Mundo Cerrado) y ontologías institucionales (Mundo Abierto) se resuelve matemáticamente adoptando la semántica del **Modelo Canónico Austero** (*Austere Canonical Model*) propuesta por la vanguardia científica de la *TU Wien* (Oudshoorn, Ortiz, Šimkus, 2026):

*   **Minimidad Local:** El sistema satisface los axiomas de la ontología introduciendo la menor cantidad posible de elementos sucesores anónimos en el grafo, garantizando que la estructura resultante sea un *Core* en el sentido estricto de bases de datos.
*   **Complejidad Computacional Bajo Control:** Aunque el problema combinatorio generalizado es EXPTIME-completo (debido al razonamiento sobre árboles infinitos), la reescritura de restricciones (*SHACL/SHACL*$\color{red}^*$ *rewriting*) aplicada al grafo local reduce la **Complejidad de Datos a PTIME-completo en entornos de producción**. Esto asegura un rendimiento óptimo al procesar volúmenes masivos de transacciones.

---

## III. Clasificación Ontológica Definitiva de Contratos (UFO)

Bajo la **Ontología Unificada de Fundamentos (UFO)** de Guizzardi, los contratos de la entidad no son registros planos; se elevan a la categoría de **Relatores (Relators)**, entidades que vinculan agentes, recursos y compromisos mutuos a lo largo del tiempo. Se clasifican rígidamente en el origen:

### 1. Contratos Financieros (Motor Algorítmico ACTUS)
*   **Naturaleza:** Intercambio de dinero en el tiempo gobernado por algoritmos de flujos de efectivo estrictos y variables financieras parametrizadas (tasas nominales, periodos de capitalización, plazos de vencimiento)[cite: 1].
*   **Instancia de Negocio:** El Certificado de Depósito a Término (CDT) o la Cuenta de Ahorro Programado (PMA) en Scotiabank Colpatria[cite: 1].
*   **Comportamiento:** En el momento de la firma (Momento 0), el contrato proyecta matemáticamente toda su vida útil en el grafo, definiendo de forma exacta los flujos futuros esperados y gestionando cláusulas restrictivas como prórrogas automáticas regulatorias[cite: 1].

### 2. Contratos Operativos (Motor de Dualidad REA)
*   **Naturaleza:** Intercambio asociado a la operación diaria de la entidad, vinculando dinero a cambio de recursos productivos, bienes o la prestación de servicios específicos[cite: 1].
*   **Instancia de Negocio:** Contrato de leasing de un camión operativo, infraestructura en la nube en DigitalOcean, o el contrato de mandato con Deceval (Anexo 1)[cite: 1].
*   **Comportamiento:** Su cumplimiento se evalúa de manera determinista comparando la dualidad económica de REA: el derecho de uso del recurso frente a la obligación de pago (hitos de entrega versus transacciones en efectivo)[cite: 1].

#### Caso de Uso: Dualidad Asimétrica del Leasing de un Camión
Un mismo hecho operativo (el uso y pago del camión) contiene dos interpretaciones lógicas que conviven bajo reglas impuestas por las **Políticas Contables de la Entidad** (Restricciones de Dominio Global):
*   **Capa IFRS (NIIF 16):** Un enfoque predictivo puro que exige calcular el valor presente de los cánones futuros, dando origen a un *Activo por Derecho de Uso* y un *Pasivo por Leasing* desde el Momento 0[cite: 1].
*   **Capa Fiscal (Estatuto Tributario):** Un enfoque tradicional que trata la transacción como un gasto por arrendamiento operativo deducible en el periodo.

---

## IV. Arquitectura del Pipeline A&AD (Versión 1.1)

El framework rechaza la contabilidad reactiva (esperar el extracto bancario de fin de mes para hacer registros). El contrato genera el futuro del sistema; el paso del tiempo solo verifica la verdad preestablecida.