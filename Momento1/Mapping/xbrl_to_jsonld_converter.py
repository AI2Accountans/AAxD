import csv
import json
import os
import uuid

csv_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento1\CDT_Santander.csv"
output_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento1\Output\CDT_JSONLD.jsonld"

print(f"Leyendo fuente inmutable: {csv_path}")

instances = []
accounts_added = set()
contracts_added = set()

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        # 1. Agregar Cuenta Contable (si no existe)
        acc_id = f"Account/{row['accountNumber']}"
        if acc_id not in accounts_added:
            instances.append({
                "@type": "Account",
                "@id": acc_id,
                "accountMainID": row['accountNumber'],
                "accountMainDescription": row['accountName'],
                "mainAccountType": "Asset" if row['sign'] == 'D' else "Liability",
                "artifact_name": "CDT Mapping Momento 1"
            })
            accounts_added.add(acc_id)
            
        # 2. Agregar Contrato ACTUS (si no existe)
        contract_id = f"ACTUS_Contract/{row['actus_ContractID']}"
        if contract_id not in contracts_added:
            instances.append({
                "@type": "ACTUS_Contract",
                "@id": contract_id,
                "actus_ContractType": row['actus_ContractType'],
                "actus_NotionalPrincipal": float(row['actus_NotionalPrincipal']),
                "actus_NominalInterestRate": float(row['actus_NominalInterestRate']),
                "actus_InitialExchangeDate": row['actus_InitialExchangeDate'],
                "actus_MaturityDate": row['actus_MaturityDate']
            })
            contracts_added.add(contract_id)
            
        # 3. Agregar el Evento Económico (EntryDetail)
        entry_id = f"EntryDetail/{row['entryNumber']}-{idx+1}"
        instances.append({
            "@type": "EntryDetail",
            "@id": entry_id,
            "artifact_name": "CDT Mapping Momento 1",
            "lineNumberCounter": idx + 1,
            "account": acc_id,
            "amount": float(row['amount']),
            "debitCreditCode": row['sign'],
            "postingDate": row['enteredDate'],
            "agent_identifier": row['rea_Agent'],
            "measurable": {
                "measurableCode": row['actus_ContractID'],
                "measurableID": contract_id,
                "measurableDescription": row['actus_MaturityDate'],
                "measurableQuantity": float(row['actus_NotionalPrincipal']),
                "measurableUnitOfMeasure": row['currency'],
                "measurableCostPerUnit": float(row['actus_NominalInterestRate'])
            }
        })

# Guardar el Grafo JSON-LD
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(instances, f, indent=4)

print(f"Grafo de Riesgos ACTUS generado exitosamente en: {output_path}")
print(f"Total de nodos generados: {len(instances)}")
