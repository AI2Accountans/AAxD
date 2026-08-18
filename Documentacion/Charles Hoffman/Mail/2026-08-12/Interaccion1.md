# Análisis de Interacción: The Third Manifesto y los Organismos de Información Digital

**Fecha de Registro:** 2026-08-12  
**Origen / Remitente:** Charles Hoffman ("Charlie")  
**Referencia Principal:** *The Third Manifesto: Databases, Types, and the Relational Model* (C. J. Date & Hugh Darwen)  
**Documento adjunto:** [DTATRM.pdf](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Charles%20Hoffman/Mail/2026-08-12/DTATRM.pdf)

---

## 1. Contenido de la Mensajería (Interaccion1.txt)

> **The Third Manifesto: Databases, Types, and the Relational Model**
>
> This explains a lot. The Third Manifesto: Databases, Types, and the Relational Model. This was published by database pioneers C. J. Date and Hugh Darwen and is a seminal proposal for the future foundation of Database Management Systems (DBMSs). It points out **DESIGN DEFECTS in SQL**. SQL is not mathematically pure and that causes accidental complexity. It also causes problems with nesting and composition. In SQL the boundary between the logical and the physical are intermingled.
>
> It basically says that a database needs to follow the **RULES OF MATH**. It also has the notion of “relational closure”. **Relational closure** is the foundational mathematical property stating that the output of every relational operation is itself a relation. This explains how “chaining” (subqueries) really should work. **This is EXACTLY HOW DIGITAL INFORMATION ORGANISMS WORK!**
>
> It also explains how **TYPES** need to work and says strong formal typing is what relational databases need. Fundamentally, a type is a named set of values equipped with a set of valid operations. The primary purpose of a type system in a database is to ensure that operations are semantically meaningful before they are ever evaluated. These types need to be controlled by the **DOMAIN** (e.g. the people putting information into the database) and not the database administrators. Conflating **TYPES and RELATIONS** is one of the most common pitfalls in data modeling.

---

## 2. Recursos Visuales Adjuntos

### A. Eliminación de las Fallas de SQL (`1.png`)
![Eliminación de las Fallas de SQL](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Charles%20Hoffman/Mail/2026-08-12/1.png)

*Tutorial D* elimina explícitamente varios defectos notorios del estándar SQL:
1. **No Duplicate Tuples:** Todas las relaciones son conjuntos matemáticos verdaderos (`sets`); las filas duplicadas no existen.
2. **No NULL Values:** La información faltante o desconocida debe manejarse usando relaciones o tipos explícitos, evitando la lógica trivalente de SQL.
3. **No Ordered Columns:** Los atributos dentro de una tupla/relación se referencian únicamente por su nombre, nunca por su posición ordinal.
4. **No Implicit Conversions:** El tipado fuerte y estricto requiere conversiones explícitas entre tipos.

### B. Clausura Relacional (`2.png`)
![Clausura Relacional](file:///c:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/Charles%20Hoffman/Mail/2026-08-12/2.png)

* **Relational Closure:** Toda operación relacional en *Tutorial D* toma una o más relaciones como entrada y produce una relación como salida. Esto permite la anidación y composición arbitraria de expresiones sin efectos secundarios inesperados.

---

## 3. Análisis Técnico Avanzado y Relevancia para DFRNT y XBRL

### A. Fallas de SQL vs. Pureza Matemática
SQL tradicional permite duplicados (multiconjuntos) y utiliza valores `NULL` que introducen la lógica trivalente (`TRUE`, `FALSE`, `UNKNOWN`), lo que corrompe la consistencia en agregaciones y razonamientos lógicos. La arquitectura planteada por Date y Darwen exige adherencia estricta a la teoría de conjuntos y la lógica de primer orden.

### B. Clausura Relacional y Organismos de Información Digital
En los **Organismos de Información Digital** (*Digital Information Organisms*), cada transformación o consulta sobre un reporte contable o grafo financiero debe preservar la validez del modelo. La clausura relacional asegura que el resultado de transformar un conjunto de hechos o nodos sea a su vez un organismo de información válido y computable, garantizando la composabilidad ilimitada.

### C. Tipos Gobernados por el Dominio vs. Relaciones
* **Tipo (Type):** Dominio semántico con operaciones válidas asociadas (ej. `MonetaryAmount`, `Period`, `AccountCode`). Asegura la validez semántica previa a la ejecución.
* **Control del Dominio:** La especificación de los tipos debe estar en manos de los expertos contables/financieros (creadores del conocimiento), no de los administradores del motor de base de datos (DBAs).
* **Trampa Común:** Confundir un *Tipo* (valor con comportamiento) con una *Relación* (colección de tuplas). En DFRNT, ontologías como OWL/SHACL definen los tipos de dominio, mientras que el grafo relacional conecta las instancias.

---

## 4. Matriz Comparativa

| Concepto del Manifiesto | SQL Tradicional | DFRNT / Grafos Semánticos / XBRL |
| :--- | :--- | :--- |
| **Tipado por Dominio** | Tipos genéricos de BD (`VARCHAR`, `DECIMAL`). | Taxonomías y Ontologías de dominio (XBRL/OWL/SHACL). |
| **Clausura Relacional** | Tablas temporales ad-hoc, vistas frágiles. | Grafo derivado donde la entrada y salida son modelos ontológicos válidos. |
| **Manejo de Ausencia** | Valores `NULL` ambiguos. | Ausencia de afirmación o representación tipada explícita. |
| **Composabilidad** | Consultas frágiles dependientes del orden. | Pipelines funcionales declarativos y encadenamiento sin efectos secundarios. |

---

## 5. Conclusión
El *Third Manifesto* sienta las bases teóricas de por qué las bases de datos relacionales tradicionales (SQL) son insuficientes para la contabilidad computacional sin una capa de abstracción rigurosa. La metodología **DFRNT**, al alinearse con la clausura relacional y el tipado gobernado por el dominio, permite materializar verdaderos **Organismos de Información Digital** capaces de ser auditados, compuestos y validados de forma totalmente automatizada.
