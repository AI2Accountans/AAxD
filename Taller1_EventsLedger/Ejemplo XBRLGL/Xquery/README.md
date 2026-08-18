# Transformación XBRL GL a JSON-LD en BaseX

Este directorio contiene el script XQuery para transformar datos contables en formato **XBRL GL** cargados en **BaseX** a un grafo ontológico **JSON-LD** listo para ingesta en **DFRNT**, **TerminusDB** o herramientas de análisis de grafos.

## Archivos

- [`xbrlgl2jsonld.xq`](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Taller1_EventsLedger/Ejemplo%20XBRLGL/Xquery/xbrlgl2jsonld.xq): Script principal XQuery 3.1.

## Formas de Ejecución en BaseX

### 1. Desde BaseX GUI
1. Abre **BaseX GUI**.
2. Abre la base de datos donde cargaste la instancia XBRL GL (o abre el archivo [`xbrlgl2jsonld.xq`](file:///C:/Users/IPHIX/Documents/Projects/DFRNT/Taller1_EventsLedger/Ejemplo%20XBRLGL/Xquery/xbrlgl2jsonld.xq)).
3. En el editor de XQuery, asegura que la variable `$DB_NAME` coincida con el nombre de tu base de datos en BaseX:
   ```xquery
   declare variable $DB_NAME external := "XBRLGL2JSONLD";
   ```
4. Haz clic en **Ejecutar (Play / F5)**.
5. Guarda o exporta el resultado JSON generado.

### 2. Desde BaseX HTTP REST API
Puedes invocar la transformación enviando una solicitud HTTP POST o GET a BaseX:

```bash
curl -u admin:admin "http://localhost:8984/rest?query=@C:/Users/IPHIX/Documents/Projects/DFRNT/Taller1_EventsLedger/Ejemplo%20XBRLGL/Xquery/xbrlgl2jsonld.xq" -o output.jsonld
```

### 3. Desde BaseX CLI / PowerShell
```powershell
basex -bDB_NAME=XBRLGL2JSONLD "C:\Users\IPHIX\Documents\Projects\DFRNT\Taller1_EventsLedger\Ejemplo XBRLGL\Xquery\xbrlgl2jsonld.xq" > output.jsonld
```

## Estructura del JSON-LD Generado

El script produce una estructura cumpliendo el estándar W3C JSON-LD:

```json
{
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25/",
    "dfrnt": "http://dfrnt.com/schema/audit#",
    "AccountingEntry": "dfrnt:AccountingEntry",
    "amount": { "@id": "gl-cor:amount", "@type": "xsd:decimal" }
  },
  "@graph": [
    {
      "@type": "AccountingEntry",
      "@id": "urn:entry:1:111505003",
      "entriesType": "trialbalance",
      "accountMainID": "111505003",
      "accountMainDescription": "(FI) PICHINCHA Cta No. 410216321",
      "amount": "55919562.97",
      "debitCreditCode": "D",
      "identifierCode": "3",
      "identifierDescription": "FONDO DE INVERSION COLETIVA INTERES",
      "taxonomicFilters": ["gsk:Activo", "gsk:ActivoCorriente", "gsk:Efectivoyequivalesdeefectivo", "gsk:Bancosnacionales", "gsk:Disponible"]
    }
  ]
}
```
