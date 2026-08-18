(:
  ===========================================================================
  Script de Verificación Contable en BaseX
  Calcula y valida el Saldo Inicial acumulado de Cuentas por Cobrar
  para la Entidad 433 (FIC DIVERSIFICADO CONSERVADOR).
  ===========================================================================
:)
xquery version "3.1";

declare namespace gl-cor = "http://www.xbrl.org/int/gl/cor/2015-03-25";
declare namespace gl-bus = "http://www.xbrl.org/int/gl/bus/2015-03-25";
declare namespace gl-srcd = "http://www.xbrl.org/int/gl/srcd/2015-03-25";

declare option output:method "json";
declare option output:indent "yes";

(: Lee el documento XML activo en la base de datos de BaseX :)
let $doc := root()

(: 1. Filtrar los detalles que pertenecen a la Entidad 433 y a Cuentas por Cobrar / Deudores :)
let $matchingDetails := 
  for $entry in $doc//gl-cor:accountingEntries
  let $detail := $entry/gl-cor:entryHeader/gl-cor:entryDetail
  let $idCode := data($detail/gl-cor:identifierReference/gl-cor:identifierCode)
  let $filters := $detail/gl-cor:xbrlInfo/gl-srcd:detailedContentFilter/data(.)
  where $idCode = "433" and any(contains(lower-case($), "cuentasporcobrar") or contains(lower-case($), "deudores"))
  return $detail

(: 2. Calcular las sumas débito y crédito :)
let $totalDebito := sum($matchingDetails[gl-cor:debitCreditCode = "D"]/xs:decimal(gl-cor:amount))
let $totalCredito := sum($matchingDetails[gl-cor:debitCreditCode = "C"]/xs:decimal(gl-cor:amount))
let $saldoNeto := $totalDebito - $totalCredito

(: 3. Desglose detallado por cuenta auxiliar :)
let $desglose := array {
  for $d in $matchingDetails
  let $accID := data($d/gl-cor:account/gl-cor:accountMainID)
  let $accDesc := normalize-space(data($d/gl-cor:account/gl-cor:accountMainDescription))
  let $amt := xs:decimal($d/gl-cor:amount)
  let $dc := data($d/gl-cor:debitCreditCode)
  order by $accID
  return map {
    "cuentaPUC": $accID,
    "descripcionAuxiliar": $accDesc,
    "monto": string($amt),
    "debitCredit": $dc
  }
}

return map {
  "entidad": "433",
  "nombreEntidad": "FIC DIVERSIFICADO CONSERVADOR",
  "categoriaConsultada": "Cuentas por cobrar / Deudores",
  "totalRegistrosCoincidentes": count($matchingDetails),
  "sumaDebito": string($totalDebito),
  "sumaCredito": string($totalCredito),
  "saldoNetoCalculadoXML": string($saldoNeto),
  "saldoEsperadoExcel": "363462294.90",
  "diferenciaInyectadaMapForce": string($saldoNeto - 363462294.90),
  "desgloseCuentas": $desglose
}
