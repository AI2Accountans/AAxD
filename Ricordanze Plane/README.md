# Semantic Ricordanze Plane — Instancias & Proyecciones Derivadas

Esta carpeta representa el **Semantic Ricordanze Plane (SRP)** dentro del marco **Accounting & Audit by Design (A&AD)** y la arquitectura DFRNT.

Inspirado en la visión de Charlie Hoffman ([Modern Version of Ricordanze](https://digitalfinancialreporting.blogspot.com/2026/07/modern-version-of-ricordanze.html)), el *Ricordanze Plane* almacena las **"gotas de lluvia congeladas" (Frozen Raindrops)**: los eventos económicos y contratos atómicos capturados en su origen con significado semántico inmutable.

---

## 📂 Contenido del Directorio `Ricordanze Plane/`

* **`valueflows_sample_instance.xml`**: Instancia XML atómica del contrato/transacción ISO/IEC 15944-4 (`BusinessTransaction`), capturando agentes, compromisos REA, reciprocidad *Give & Take* y partes relacionadas (NIC 24).
* **`contrato_iso15944.html`**: Vista proyectada interactiva bilingüe (`ES` | `EN`) en HTML5 generada dinámicamente desde el plano.
* **`contrato_iso15944.fo`**: Documento maquetado en XSL-FO proyectado para la generación de reportes impresos en PDF.

---

## 🏛️ Principio de Arquitectura
1. **El Grafo / XML es la Fuente de Verdad:** Almacena el significado del negocio antes de cualquier asiento contable o agregación ex-post.
2. **Las Vistas son Proyecciones Derivadas:** El HTML5 y el PDF no son archivos primarios estáticos; son vistas visuales proyectadas desde el *Semantic Ricordanze Plane*.
