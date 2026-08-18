(:
  ===========================================================================
  Prueba de Fuego - BaseX XQuery
  Calcula el Saldo Inicial acumulado de la etiqueta 'Deudores' (SRCD)
  para una Entidad / Compañía específica (ej. 174, 178, 175, 176).
  ===========================================================================
:)
xquery version "3.1";

declare namespace gl-cor = "http://www.xbrl.org/int/gl/cor/2015-03-25";
declare namespace gl-bus = "http://www.xbrl.org/int/gl/bus/2015-03-25";
declare namespace gl-srcd = "http://www.xbrl.org/int/gl/srcd/2015-03-25";

(: Cambia este código de Entidad según desees consultar :)
declare variable $TARGET_ENTITY := "174";

let $doc := root()

(: Filtrar los detalles contables que corresponden a la Entidad y a la etiqueta Deudores :)
let $matchingDetails := 
  for $entry in $doc//gl-cor:accountingEntries
  let $detail := $entry/gl-cor:entryHeader/gl-cor:entryDetail
  let $idCode := data($detail/gl-cor:identifierReference/gl-cor:identifierCode)
  let $filters := $detail/gl-cor:xbrlInfo/gl-srcd:detailedContentFilter/data(.)
  where $idCode = $TARGET_ENTITY and any(contains(lower-case($), "deudores"))
  return $detail

let $debito := sum($matchingDetails[gl-cor:debitCreditCode = "D"]/xs:decimal(gl-cor:amount))
let $credito := sum($matchingDetails[gl-cor:debitCreditCode = "C"]/xs:decimal(gl-cor:amount))

return map {
  "entidadConsultada": $TARGET_ENTITY,
  "filtroEtiqueta": "Deudores",
  "totalRegistrosCoincidentes": count($matchingDetails),
  "sumaDebito": $debito,
  "sumaCredito": $credito,
  "saldoNeto": $debito - $credito,
  "desgloseCuentas": array {
    for $d in $matchingDetails
    return map {
      "cuentaPUC": data($d/gl-cor:account/gl-cor:accountMainID),
      "descripcion": normalize-space(data($d/gl-cor:account/gl-cor:accountMainDescription)),
      "monto": data($d/gl-cor:amount),
      "codigoDC": data($d/gl-cor:debitCreditCode),
      "filtrosSRCD": array { $d/gl-cor:xbrlInfo/gl-srcd:detailedContentFilter/data(.) }
    }
  }
}
