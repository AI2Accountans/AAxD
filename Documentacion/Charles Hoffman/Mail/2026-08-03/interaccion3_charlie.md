# Interacción 3: Charlie Hoffman

**Fecha**: 3 de agosto de 2026  
**De**: Charles Hoffman  
**Para**: Richard Gasca  
**Archivo Origen**: `interaction3.txt`  

---

## Mensaje Original (Inglés)

```text
Richard;

I am trying to explain these two paradigms and the difference between them. Give me a couple of days and I will have something for you. What I would encourage you to do is to “prototype” both the legacy approach and the new approach. This allows three things: (1) an understanding of the legacy approach, (2) an understanding of the new approach, (3) the ability to explain the “gap” between the two.

It seems to me that two different “source” documents or document formats are possible. The first is the traditional “document” or PDF structured for presentation (i.e. not meaning). The second is a “graph” structured for meaning for which a presentation (i.e. document) can be generated from the graph.

How well do you think people “get” what we are trying to communicate? This seems so obvious to me.

Cheers,
```

---

## Traducción al Español

```text
Richard:

Estoy intentando explicar estos dos paradigmas y la diferencia entre ellos. Dame un par de días y tendré algo listo para ti. Lo que te animaría a hacer es “prototipar” tanto el enfoque heredado (legacy) como el nuevo enfoque. Esto permite tres cosas: (1) comprender el enfoque heredado, (2) comprender el nuevo enfoque, y (3) tener la capacidad de explicar la "brecha" (the gap) entre ambos.

Me parece que son posibles dos "documentos fuente" o formatos de documento diferentes. El primero es el "documento" tradicional o PDF estructurado para la presentación (es decir, no para el significado). El segundo es un "grafo" estructurado para el significado, a partir del cual se puede generar una presentación (es decir, un documento) desde el grafo.

¿Qué tan bien crees que la gente "entiende" lo que estamos tratando de comunicar? Esto me parece tan obvio.

Saludos,
```

---

## Notas de Trabajo e Implementación para Hoy

* **Objetivo de Ingeniería**: Implementar el prototipado dual exigido por Charlie.
* **Modelo REA (ISO 15944-4)**: Mapear la ontología REA a una interfaz de captura **XForms** en BaseX.
* **Desacoplamiento de Datos**: Desacoplar la captura del almacenamiento mediante **XBRL GL** y **JSON-LD (Valueflows / ISO 15944)**.
* **Operación Dual**:
  1. **Visualizaciones PDF (Legacy Mode)**: Generación al vuelo de PDFs de contratos/facturas tradicionales desde el Grafo utilizando Altova StyleVision / XSL-FO.
  2. **Operación en Grafo (New Approach Mode)**: Procesamiento granular, consultas SPARQL/GraphQL y reglas de validación SHACL en el grafo de conocimiento en vivo.
