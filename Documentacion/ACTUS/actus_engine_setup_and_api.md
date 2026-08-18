# ACTUS Engine: Despliegue y Descubrimiento de la API

**Fecha:** 2026-07-14  
**Contexto:** Proyecto "Accounting & Audit by Design" (AAD)  
**Objetivo:** Instalar el motor matemático ACTUS en el Droplet de DigitalOcean y lograr generar eventos financieros para contratos PAM (Principal at Maturity), equivalente al CDT colombiano.

---

## 1. Infraestructura

### Droplet DigitalOcean
- **IP:** `165.245.137.44`
- **OS:** Ubuntu 22.04 LTS
- **Acceso:** `ssh root@165.245.137.44`

### Servicios Docker en ejecución
| Contenedor | Puerto | Descripción |
|---|---|---|
| `actus-docker-networks-actus-server-rf20-1` | `8083` | Motor matemático ACTUS (actus-service v1.0.2) |
| `mongodb` | `27017` | Base de datos para persistencia |

### Archivos de orquestación
- Ubicación en el servidor: `~/actus-docker-networks/`
- Archivo principal: `quickstart-docker-actus-rf20.yml`

### Comandos de gestión
```bash
# Ver contenedores activos
docker ps

# Iniciar el stack
cd ~/actus-docker-networks
docker-compose -f quickstart-docker-actus-rf20.yml up -d

# Ver logs en tiempo real
docker logs actus-docker-networks-actus-server-rf20-1 --tail 50

# Ver errores específicos en logs
docker logs actus-docker-networks-actus-server-rf20-1 --tail 150 | grep "^[a-zA-Z]"
```

---

## 2. Arquitectura del Servicio

### Stack tecnológico (descubierto por ingeniería inversa)
- **Framework:** Spring Boot 3.x (Tomcat embebido, puerto 8083)
- **Librería matemática:** `actus-core v1.1.0` (JAR en `/app/actus-core/target/`)
- **JAR de la aplicación:** `/app/actus-service/build/libs/actus-service-1.0.2-SNAPSHOT.jar`
- **Build tool:** Gradle 8.4

### Endpoints disponibles
| Método | Endpoint | Descripción |
|---|---|---|
| `POST` | `/events` | Genera eventos para **un** contrato |
| `POST` | `/eventsBatch` | Genera eventos para **múltiples** contratos en lote |

> **Nota:** No hay endpoints de documentación (`/swagger-ui`, `/v3/api-docs`, etc.). La API fue descubierta completamente por ingeniería inversa del bytecode compilado.

---

## 3. La Receta Ganadora: JSON para el Endpoint `/events`

### Estructura del Request

```json
{
  "contract": {
    "contractType": "PAM",
    "contractID": "PAM-01",
    "contractRole": "RPA",
    "currency": "USD",
    "statusDate": "2026-01-01T00:00:00",
    "notionalPrincipal": 1000.0,
    "nominalInterestRate": 0.05,
    "dayCountConvention": "30E360",
    "maturityDate": "2027-01-01T00:00:00",
    "initialExchangeDate": "2026-01-01T00:00:00",
    "cycleAnchorDateOfInterestPayment": "2026-02-01T00:00:00",
    "cycleOfInterestPayment": "P1ML1"
  },
  "riskFactors": []
}
```

### Reglas Críticas del Formato

| Regla | ❌ Incorrecto | ✅ Correcto |
|---|---|---|
| Envoltura del contrato | `"terms"`, `"contractAttributes"`, plano | `"contract"` |
| Factores de riesgo | Omitir el campo | `"riskFactors": []` (lista vacía, obligatorio) |
| Valores numéricos | `"notionalPrincipal": "1000"` (string) | `"notionalPrincipal": 1000.0` (número) |
| Ciclos | `"P1M"` | `"P1ML1"` (formato ACTUS con convención fin de mes) |
| Calendario/Feriados | `"calendar": "NC"` (no existe en esta versión) | `"holidays": ["2026-12-25"]` o simplemente omitir |
| Nombres de campos | Acrónimos `cType`, `NT`, `IPNR` | Nombres largos: `contractType`, `notionalPrincipal` |
| Moneda | Omitir | `"currency": "USD"` (obligatorio) |

### Ejemplo con curl
```bash
curl -X POST "http://localhost:8083/events" \
  -H "Content-Type: application/json" \
  -d '{
    "contract": {
      "contractType": "PAM",
      "contractID": "CDT-001",
      "contractRole": "RPA",
      "currency": "COP",
      "statusDate": "2026-01-01T00:00:00",
      "notionalPrincipal": 1000000.0,
      "nominalInterestRate": 0.12,
      "dayCountConvention": "30E360",
      "maturityDate": "2027-01-01T00:00:00",
      "initialExchangeDate": "2026-01-01T00:00:00",
      "cycleAnchorDateOfInterestPayment": "2026-02-01T00:00:00",
      "cycleOfInterestPayment": "P1ML1"
    },
    "riskFactors": []
  }'
```

---

## 4. Output: Eventos Generados para PAM

La respuesta del motor para el contrato de ejemplo (CDT a 1 año, $1.000 USD, tasa 5% EA, pagos mensuales):

```json
[
  { "type": "IP", "time": "2026-02-01T00:00", "payoff": 4.1667, "currency": "USD", "nominalValue": 1000.0, "nominalRate": 0.05 },
  { "type": "IP", "time": "2026-03-01T00:00", "payoff": 4.1667, "currency": "USD", "nominalValue": 1000.0, "nominalRate": 0.05 },
  "... (10 pagos IP más, uno por mes) ...",
  { "type": "IP", "time": "2027-01-01T00:00", "payoff": 4.1667, "currency": "USD", "nominalValue": 1000.0, "nominalRate": 0.05 },
  { "type": "MD", "time": "2027-01-01T00:00", "payoff": 1000.0, "currency": "USD", "nominalValue": 0.0,    "nominalRate": 0.05 }
]
```

### Interpretación de los Tipos de Evento

| Tipo | Nombre completo | Descripción |
|---|---|---|
| `IED` | Initial Exchange Date | Desembolso inicial del capital |
| `IP` | Interest Payment | Pago periódico de intereses |
| `IPCI` | Interest Payment Capitalization | Capitalización de intereses |
| `PR` | Principal Repayment | Amortización parcial del principal |
| `MD` | Maturity Date | Devolución del principal al vencimiento |
| `RR` | Rate Reset | Reseteo de tasa de interés variable |
| `TD` | Termination Date | Cancelación anticipada |
| `FP` | Fee Payment | Pago de comisión |

> **Verificación matemática:** 12 × $4.1667 = **$50.00** intereses totales = 1000 × 5% × 1 año ✅

---

## 5. Referencia de Parámetros ACTUS para Contratos Simples

### Tipos de Contrato

| Tipo | Nombre | Equivalente Colombia |
|---|---|---|
| `PAM` | Principal at Maturity | CDT, Bono bullet |
| `LAM` | Linear Amortizer | Crédito con amortización lineal |
| `ANN` | Annuity | Crédito hipotecario (cuota fija) |
| `CLM` | Call Money | Cuenta de ahorros, depósito a la vista |
| `NAM` | Negative Amortizer | Crédito con capitalización de intereses |

### Roles de Contrato

| Código | Descripción | Perspectiva |
|---|---|---|
| `RPA` | Real Person Asset | Acreedor / Tenedor del activo (inversionista en CDT) |
| `RPL` | Real Person Liability | Deudor / Emisor del pasivo (banco emisor del CDT) |

### Convenciones de Día (`dayCountConvention`)

| Código | Descripción | Uso común |
|---|---|---|
| `30E360` | 30/360 Europeo | CDTs, bonos corporativos Colombia |
| `A365` | Actual/365 | Mercado de dinero |
| `A360` | Actual/360 | Operaciones interbancarias |
| `AA` | Actual/Actual | Deuda soberana |

### Formato de Ciclos

El formato es `P{n}{período}L{convención}`:

| Ciclo | Significado |
|---|---|
| `P1ML1` | Mensual |
| `P3ML1` | Trimestral |
| `P6ML1` | Semestral |
| `P1YL1` | Anual |

---

## 6. Script Python de Referencia

```python
import urllib.request
import json

def query_actus(contract_params, risk_factors=None, host="http://localhost:8083"):
    """
    Consulta el motor matemático ACTUS para generar eventos de un contrato.
    
    Args:
        contract_params (dict): Parámetros del contrato según estándar ACTUS v1.1.
        risk_factors (list): Factores de riesgo observados (default: []).
        host (str): URL base del servidor ACTUS.
    
    Returns:
        list: Lista de eventos financieros generados por el motor.
    """
    payload = {
        "contract": contract_params,
        "riskFactors": risk_factors or []
    }
    req = urllib.request.Request(
        f"{host}/events",
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))


if __name__ == "__main__":
    # CDT colombiano de ejemplo
    cdt = {
        "contractType": "PAM",
        "contractID": "CDT-001",
        "contractRole": "RPA",
        "currency": "COP",
        "statusDate": "2026-01-01T00:00:00",
        "notionalPrincipal": 10000000.0,
        "nominalInterestRate": 0.12,
        "dayCountConvention": "30E360",
        "maturityDate": "2027-01-01T00:00:00",
        "initialExchangeDate": "2026-01-01T00:00:00",
        "cycleAnchorDateOfInterestPayment": "2026-02-01T00:00:00",
        "cycleOfInterestPayment": "P1ML1"
    }
    
    eventos = query_actus(cdt, host="http://165.245.137.44:8083")
    print(f"Eventos generados: {len(eventos)}")
    for e in eventos:
        print(f"  [{e['type']}] {e['time']} → ${e['payoff']:>12,.4f} {e['currency']}")
```

---

## 7. Técnica de Ingeniería Inversa (cómo descubrimos la API)

Como el servidor no tiene documentación pública, la API fue descifrada descompilando el bytecode Java:

```bash
# 1. Copiar el JAR de la aplicación desde el contenedor
docker cp actus-docker-networks-actus-server-rf20-1:/app/actus-service/build/libs/actus-service-1.0.2-SNAPSHOT.jar ./app.jar

# 2. Descomprimir el JAR (es un ZIP)
unzip -q -o app.jar "BOOT-INF/classes/org/actus/webapp/*"

# 3. Descompilar con CFR usando eclipse-temurin (imagen correcta en Docker Hub)
docker run --rm -v $(pwd):/app -w /app eclipse-temurin:17-jdk sh -c "
  wget -qO cfr.jar https://github.com/leibnitz27/cfr/releases/download/0.152/cfr-0.152.jar
  java -jar cfr.jar app.jar org.actus.webapp.controllers.EventController
"

# 4. Copiar y descompilar actus-core para ver la lógica de parseo
docker cp actus-docker-networks-actus-server-rf20-1:/app/actus-core/target/actus-core-1.1.0.jar ./actus-core.jar
docker run --rm -v $(pwd):/app -w /app eclipse-temurin:17-jdk sh -c "
  wget -qO cfr.jar https://github.com/leibnitz27/cfr/releases/download/0.152/cfr-0.152.jar
  java -jar cfr.jar actus-core.jar org.actus.attributes.ContractModel
"
```

### Cronología de errores y soluciones

| Intento | Estructura enviada | Error | Causa raíz |
|---|---|---|---|
| 1 | `{"contractAttributes": {...}}` | `NPE: contractAttributes is null` | La llave es `"contract"`, no `"contractAttributes"` |
| 2 | `{...}` (plano) | `NPE: contractAttributes is null` | Sin la llave `"contract"`, el campo llega null al parser |
| 3 | `{"contract": {...}}` sin riskFactors | `NPE: json is null` en forEach | `"riskFactors"` es obligatorio (debe ser `[]` mínimo) |
| 4 | `{"contract": {...}, "riskFactors": []}` con strings | `AttributeConversionException` | `actus-core` hace cast a `Double`; strings fallan |
| **5 ✅** | `{"contract": {...numerics...}, "riskFactors": []}` con `currency` | **HTTP 200 OK** | JSON correcto con tipos numéricos y campo obligatorio |

---

## 8. Próximos Pasos: Integración con el Ejercicio CDT

### Pipeline previsto para Accounting & Audit by Design

```
CDT_JSONLD.jsonld
    ↓ Extracción de parámetros financieros
Parámetros ACTUS (PAM)
    ↓ POST http://165.245.137.44:8083/events
Eventos ACTUS [IP × n, MD]
    ↓ Mapeo semántico a XBRL GL
Entradas contables en formato GL (gl-cor:entryDetail)
    ↓ Ingesta a TerminusDB / DFRNT
Grafo de conocimiento auditado con trazabilidad algorítmica
```

### Campos del CDT real a mapear desde JSONLD

| Campo en JSONLD | Campo ACTUS | Tipo | Notas |
|---|---|---|---|
| Valor nominal | `notionalPrincipal` | `number` | Sin comillas |
| Tasa de interés | `nominalInterestRate` | `number` | Decimal (0.12 = 12%) |
| Fecha de expedición | `initialExchangeDate` | `string` ISO 8601 | `"YYYY-MM-DDTHH:MM:SS"` |
| Fecha de vencimiento | `maturityDate` | `string` ISO 8601 | |
| Fecha inicio análisis | `statusDate` | `string` ISO 8601 | Igual o anterior a `initialExchangeDate` |
| Periodicidad pago | `cycleOfInterestPayment` | `string` | `"P1ML1"`, `"P3ML1"`, etc. |
| Moneda | `currency` | `string` | `"COP"` para pesos colombianos |

---

*Documentado por: Antigravity AI + IPHIX*  
*Sesión de depuración: 2026-07-14*  
*Motor: actus-service v1.0.2 / actus-core v1.1.0*
