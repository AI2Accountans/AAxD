(:
  ===========================================================================
  Prueba de Fuego 2 - Verificación del Total del Activo (Saldo Final)
  para las Entidades 178 y 186
  ===========================================================================
:)
xquery version "3.1";

declare namespace gl-cor = "http://www.xbrl.org/int/gl/cor/2015-03-25";
declare namespace gl-bus = "http://www.xbrl.org/int/gl/bus/2015-03-25";
declare namespace gl-srcd = "http://www.xbrl.org/int/gl/srcd/2015-03-25";

declare option output:method "json";
declare option output:indent "yes";

let $doc := root()

let $targetEntities := ("178", "186")

let $resultados := array {
  for $ent in $targetEntities
  
  let $activoDetails := 
    for $entry in $doc//gl-cor:accountingEntries
    let $detail := $entry/gl-cor:entryHeader/gl-cor:entryDetail
    let $idCode := data($detail/gl-cor:identifierReference/gl-cor:identifierCode)
    let $filters := $detail/gl-cor:xbrlInfo/gl-srcd:detailedContentFilter/data(.)
    where $idCode = $ent and any(contains(lower-case($), "activo"))
    return $detail

  let $totalDebito := sum($activoDetails[gl-cor:debitCreditCode = "D"]/xs:decimal(gl-cor:amount))
  let $totalCredito := sum($activoDetails[gl-cor:debitCreditCode = "C"]/xs:decimal(gl-cor:amount))
  let $saldoNeto := $totalDebito - $totalCredito
  
  let $nombreEntidad := (
    data($activoDetails[1]/gl-cor:identifierReference/gl-cor:identifierDescription),
    concat("Entidad ", $ent)
  )[1]

  return map {
    "codigoEntidad": $ent,
    "nombreEntidad": $nombreEntidad,
    "totalCuentasActivo": count($activoDetails),
    "sumaTotalActivo": string($saldoNeto),
    "desgloseCuentas": array {
      for $d in $activoDetails
      let $accID := data($d/gl-cor:account/gl-cor:accountMainID)
      let $accDesc := normalize-space(data($d/gl-cor:account/gl-cor:accountMainDescription))
      let $amt := data($d/gl-cor:amount)
      order by $accID
      return map {
        "cuenta": $accID,
        "descripcion": $accDesc,
        "montoSaldoFinal": $amt
      }
    }
  }
}

return map {
  "prueba": "Verificación Total del Activo (Saldo Final)",
  "entidadesEvaluadas": $resultados
}
