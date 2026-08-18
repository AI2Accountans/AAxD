"""
actus_pipeline.py
─────────────────────────────────────────────────────────────────────────────
Pipeline AAD: Google Sheets → Motor ACTUS → flujos_proyectados.json

Flujo:
  1. Lee los contratos desde la hoja de cálculo (CSV público de Google Sheets)
  2. Deduplica por actus_ContractID (cada contrato puede tener N asientos)
  3. Por cada contrato único, consulta el motor ACTUS en el Droplet
  4. Guarda los flujos proyectados (diarios) en Source/flujos_proyectados.json

Uso:
  python actus_pipeline.py

Requisitos:
  - Python 3.8+
  - Acceso a internet (para leer el CSV y llamar al motor ACTUS)
  - Motor ACTUS corriendo en http://165.245.137.44:8083
"""

import csv
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path

# ─── Configuración ─────────────────────────────────────────────────────────

CSV_URL = (
    "https://docs.google.com/spreadsheets/d/e/"
    "2PACX-1vT1Ve9XVb3kTQz40TcM7bR_Gj3AmDB4a9JVyiIAWnDDTsB0h96k3dUCO4pgEq0Ip2q9iriwweQpedAA"
    "/pub?gid=0&single=true&output=csv"
)

ACTUS_SERVER = "http://165.245.137.44:8083/events"

# Script está en Momento1/Script/ → Output va a Momento1/Source/
OUTPUT_DIR  = Path(__file__).parent.parent / "Source"
OUTPUT_FILE = OUTPUT_DIR / "flujos_proyectados.json"

# Proyección DIARIA
DAY_COUNT_CONVENTION = "30E360"
CYCLE_OF_INTEREST    = "P1DL1"   # D = Diario


# ─── Funciones auxiliares ───────────────────────────────────────────────────

def fetch_csv(url: str) -> list:
    """Descarga el CSV desde Google Sheets y lo parsea como lista de dicts."""
    print(f"[1/4] Leyendo contratos desde Google Sheets...")
    with urllib.request.urlopen(url) as resp:
        content = resp.read().decode("utf-8").splitlines()
    reader = csv.DictReader(content)
    rows = [row for row in reader]
    print(f"      {len(rows)} filas encontradas.")
    return rows


def deduplicate_contracts(rows: list) -> dict:
    """
    Agrupa las filas por actus_ContractID.
    Toma los parámetros ACTUS de la primera fila de cada grupo.
    """
    contracts = {}
    for row in rows:
        cid = row.get("actus_ContractID", "").strip()
        if not cid or cid in contracts:
            continue
        contracts[cid] = {
            "contractID":          cid,
            "contractType":        row.get("actus_ContractType", "PAM").strip(),
            "notionalPrincipal":   float(row.get("actus_NotionalPrincipal", 0)),
            "nominalInterestRate": float(row.get("actus_NominalInterestRate", 0)),
            "initialExchangeDate": row.get("actus_InitialExchangeDate", "").strip(),
            "maturityDate":        row.get("actus_MaturityDate", "").strip(),
            "currency":            row.get("currency", "COP").strip(),
            "agent":               row.get("rea_Agent", "").strip(),
        }
    print(f"      {len(contracts)} contratos únicos identificados.")
    return contracts


def next_day_str(date_str: str) -> str:
    """Día siguiente al desembolso — ancla del primer ciclo diario."""
    d = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    return d.strftime("%Y-%m-%dT00:00:00")


def to_datetime_str(date_str: str) -> str:
    """Convierte "YYYY-MM-DD" → "YYYY-MM-DDTHH:MM:SS"."""
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00")


def build_actus_payload(params: dict) -> dict:
    """Construye el payload JSON para el endpoint /events del motor ACTUS."""
    ied = params["initialExchangeDate"]
    return {
        "contract": {
            "contractType":                     params["contractType"],
            "contractID":                       params["contractID"],
            "contractRole":                     "RPA",
            "currency":                         params["currency"],
            "statusDate":                       to_datetime_str(ied),
            "notionalPrincipal":                params["notionalPrincipal"],
            "nominalInterestRate":              params["nominalInterestRate"],
            "dayCountConvention":               DAY_COUNT_CONVENTION,
            "maturityDate":                     to_datetime_str(params["maturityDate"]),
            "initialExchangeDate":              to_datetime_str(ied),
            "cycleAnchorDateOfInterestPayment": next_day_str(ied),
            "cycleOfInterestPayment":           CYCLE_OF_INTEREST,
        },
        "riskFactors": []
    }


def query_actus(payload: dict, contract_id: str) -> list:
    """Envía el payload al motor ACTUS y retorna la lista de eventos."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ACTUS_SERVER,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"      ⚠️  Error HTTP {e.code} para {contract_id}")
        return []
    except Exception as e:
        print(f"      ⚠️  Error de conexión para {contract_id}: {e}")
        return []


def enrich_events(events: list, contract_id: str, params: dict) -> list:
    """
    Agrega metadatos a cada evento:
    - event_id           : ID único (para JSON-LD / grafo TerminusDB)
    - actus_ContractID   : referencia al contrato padre
    - dayNumber          : número de día dentro del contrato (solo IP)
    - interestCumulative : interés causado acumulado hasta este evento
    - negotiableValue    : capital + interés acumulado (precio sucio del título)
    - isZeroDay          : True si el día no genera causación (día 31 en 30E360)
    """
    notional  = params["notionalPrincipal"]
    acumulado = 0.0
    dia_num   = 0
    enriched  = []

    for e in events:
        if e["type"] == "IP":
            dia_num  += 1
            acumulado = round(acumulado + e["payoff"], 4)

        date_str = (e["time"].replace(":", "")
                             .replace("-", "")
                             .replace("T", "")[:8])
        event_id = f"ACTUS_Event/{contract_id}-{e['type']}-{date_str}"

        entry = {
            **e,
            "payoff":             round(e["payoff"], 4),
            "event_id":           event_id,
            "actus_ContractID":   f"ACTUS_Contract/{contract_id}",
            "interestCumulative": round(acumulado, 2),
            "negotiableValue":    round(notional + acumulado, 2),
        }

        if e["type"] == "IP":
            entry["dayNumber"] = dia_num
            entry["isZeroDay"] = (round(e["payoff"], 4) == 0.0)

        enriched.append(entry)

    return enriched


# ─── Pipeline principal ─────────────────────────────────────────────────────

def main():
    print("\n" + "═" * 64)
    print("  Pipeline AAD: ACTUS Cash Flow Projector  [Proyección DIARIA]")
    print("═" * 64)

    rows      = fetch_csv(CSV_URL)
    contracts = deduplicate_contracts(rows)

    print(f"\n[2/4] Consultando motor ACTUS en {ACTUS_SERVER}...")
    results = []

    for cid, params in contracts.items():
        print(f"      → {cid} ({params['contractType']}, "
              f"${params['notionalPrincipal']:,.0f} {params['currency']}, "
              f"tasa {params['nominalInterestRate']*100:.1f}%)")

        payload   = build_actus_payload(params)
        events    = query_actus(payload, cid)
        events    = enrich_events(events, cid, params)

        ip_events = [e for e in events if e["type"] == "IP"]
        md_events = [e for e in events if e["type"] == "MD"]
        zero_days = [e for e in ip_events if e.get("isZeroDay")]
        total_ip  = round(sum(e["payoff"] for e in ip_events), 2)
        total_md  = round(sum(e["payoff"] for e in md_events), 2)

        print(f"        Días proyectados  : {len(ip_events)} "
              f"({len(zero_days)} días sin causación por conv. 30E360)")
        print(f"        Intereses totales : ${total_ip:>12,.2f} {params['currency']}")
        print(f"        Principal         : ${total_md:>12,.2f} {params['currency']}")
        print(f"        Flujo total       : ${total_ip + total_md:>12,.2f} {params['currency']}")
        print(f"        Tasa diaria       : ${params['notionalPrincipal'] * params['nominalInterestRate'] / 360:>10,.4f} {params['currency']}/día")

        results.append({
            "actus_ContractID":   f"ACTUS_Contract/{cid}",
            "actus_ContractType": params["contractType"],
            "agent":              params["agent"],
            "inputContract":      payload["contract"],
            "summary": {
                "totalInterest":     total_ip,
                "totalPrincipal":    total_md,
                "totalCashflow":     round(total_ip + total_md, 2),
                "currency":          params["currency"],
                "totalDays":         len(ip_events),
                "zeroCausationDays": len(zero_days),
                "dailyRate":         round(
                    params["notionalPrincipal"] * params["nominalInterestRate"] / 360, 4
                ),
            },
            "events": events,
        })

    print(f"\n[3/4] Construyendo archivo de salida...")
    output = {
        "pipeline":           "AAD - ACTUS Cash Flow Projector",
        "projectionMode":     "DAILY",
        "generatedAt":        datetime.now().isoformat(),
        "actusServer":        ACTUS_SERVER,
        "csvSource":          CSV_URL,
        "dayCountConvention": DAY_COUNT_CONVENTION,
        "cycleOfInterest":    CYCLE_OF_INTEREST,
        "contractCount":      len(results),
        "contracts":          results,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[4/4] Archivo guardado: {OUTPUT_FILE}")
    print("\n" + "─" * 64)
    print(f"  Contratos procesados   : {len(results)}")
    total_flujo = sum(r["summary"]["totalCashflow"] for r in results)
    print(f"  Flujo total proyectado : ${total_flujo:>14,.2f} COP")
    print("─" * 64 + "\n")


if __name__ == "__main__":
    main()
