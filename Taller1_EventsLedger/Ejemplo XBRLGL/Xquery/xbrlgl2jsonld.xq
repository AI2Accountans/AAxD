(:
  ===========================================================================
  Script XQuery 3.1 para BaseX 12
  Transmuta instancias XBRL GL a un Grafo de Conocimiento JSON-LD Completo
  reificando Nodos de Cuenta, Entidad, Asientos y Taxonomías SRCD.
  ===========================================================================
:)
xquery version "3.1";

declare namespace gl-cor = "http://www.xbrl.org/int/gl/cor/2015-03-25";
declare namespace gl-bus = "http://www.xbrl.org/int/gl/bus/2015-03-25";
declare namespace gl-srcd = "http://www.xbrl.org/int/gl/srcd/2015-03-25";
declare namespace xbrli   = "http://www.xbrl.org/2003/instance";

(: Opción de salida para que BaseX serialice directamente en formato JSON :)
declare option output:method "json";
declare option output:indent "yes";

(: Obtiene el documento activo de la base de datos abierta en BaseX :)
let $doc := root()

(: Definición del contexto ontológico JSON-LD con prefijos e identificadores de aristas :)
let $context := map {
  "xsd": "http://www.w3.org/2001/XMLSchema#",
  "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
  "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25/",
  "gl-bus": "http://www.xbrl.org/int/gl/bus/2015-03-25/",
  "gl-srcd": "http://www.xbrl.org/int/gl/srcd/2015-03-25/",
  "dfrnt": "http://dfrnt.com/schema/audit#",
  "AccountingEntry": "dfrnt:AccountingEntry",
  "Account": "dfrnt:Account",
  "Entity": "dfrnt:Entity",
  "TaxonomyConcept": "dfrnt:TaxonomyConcept",
  "hasAccount": map { "@id": "dfrnt:hasAccount", "@type": "@id" },
  "hasEntity": map { "@id": "dfrnt:hasEntity", "@type": "@id" },
  "classifiedUnder": map { "@id": "dfrnt:classifiedUnder", "@type": "@id", "@container": "@set" },
  "accountMainID": "gl-cor:accountMainID",
  "accountMainDescription": "gl-cor:accountMainDescription",
  "amount": map { "@id": "gl-cor:amount", "@type": "xsd:decimal" },
  "debitCreditCode": "gl-cor:debitCreditCode",
  "contextRef": "gl-cor:contextRef",
  "identifierCode": "gl-bus:identifierCode",
  "identifierDescription": "gl-bus:identifierDescription",
  "entriesType": "gl-cor:entriesType",
  "postingDate": "gl-cor:postingDate",
  "conceptCode": "gl-srcd:detailedContentFilter"
}

(: 1. Generar Nodos de Conceptos Taxonómicos SRCD Deduplicados :)
let $taxonomyNodes := array {
  for $tag in distinct-values($doc//gl-srcd:detailedContentFilter/data(.)[string-length(.) > 0])
  let $cleanTag := normalize-space($tag)
  return map {
    "@type": "TaxonomyConcept",
    "@id": concat("urn:taxonomy:", encode-for-uri($cleanTag)),
    "conceptCode": $cleanTag,
    "rdfs:label": $cleanTag
  }
}

(: 2. Generar Nodos de Cuentas Contables Deduplicadas :)
let $accountNodes := array {
  for $acc in $doc//gl-cor:account
  let $accID := data($acc/gl-cor:accountMainID)
  let $accDesc := data($acc/gl-cor:accountMainDescription)
  group by $accID
  where string-length($accID) > 0
  return map {
    "@type": "Account",
    "@id": concat("urn:account:", $accID),
    "accountMainID": $accID,
    "accountMainDescription": normalize-space($accDesc[1])
  }
}

(: 3. Generar Nodos de Entidades/Fondos Deduplicados :)
let $entityNodes := array {
  for $ref in $doc//gl-cor:identifierReference
  let $idCode := data($ref/gl-cor:identifierCode)
  let $idDesc := data($ref/gl-cor:identifierDescription)
  group by $idCode
  where string-length($idCode) > 0
  return map {
    "@type": "Entity",
    "@id": concat("urn:entity:", $idCode),
    "identifierCode": $idCode,
    "identifierDescription": normalize-space($idDesc[1])
  }
}

(: 4. Generar Nodos de Asientos Contables con Aristas de Enlace (Iteración atómica por cada movimiento) :)
let $entryNodes := array {
  for $detail at $pos in $doc//gl-cor:entryDetail
  let $accID := data($detail/gl-cor:account/gl-cor:accountMainID)
  let $amt := data($detail/gl-cor:amount)
  let $dc := data($detail/gl-cor:debitCreditCode)
  let $ctx := data($detail/gl-cor:amount/@contextRef)
  
  (: Extraer información de periodo desde el contexto XBRL :)
  let $ctxNode := $doc//xbrli:context[@id = $ctx]
  let $instantDate := data($ctxNode//xbrli:instant)
  let $startDate := data($ctxNode//xbrli:startDate)
  let $endDate := data($ctxNode//xbrli:endDate)
  let $periodDate := (
    if ($instantDate != "") then $instantDate
    else if ($startDate != "" and $endDate != "") then concat($startDate, "/", $endDate)
    else data($detail/gl-cor:postingDate),
    "2025-07-31"
  )[1]

  let $idCode := data($detail/gl-cor:identifierReference/gl-cor:identifierCode)
  let $entryType := (
    data($detail/ancestor::gl-cor:entryHeader/gl-cor:entryType),
    data($detail/ancestor::gl-cor:accountingEntries/gl-cor:documentInfo/gl-cor:entriesType),
    "trialbalance"
  )[1]
  
  (: Aristas hacia los Conceptos Taxonómicos SRCD :)
  let $srcdTags := $detail/gl-cor:xbrlInfo/gl-srcd:detailedContentFilter/data(.)[string-length(.) > 0]
  let $taxonomyRefs := array {
    for $tag in $srcdTags
    return concat("urn:taxonomy:", encode-for-uri(normalize-space($tag)))
  }
  
  where $accID != ""
  return map {
    "@type": "AccountingEntry",
    "@id": concat("urn:entry:", $pos, ":", $accID),
    "entriesType": $entryType,
    "contextRef": if ($ctx) then $ctx else "ctx1",
    "hasAccount": concat("urn:account:", $accID),
    "hasEntity": if ($idCode) then concat("urn:entity:", $idCode) else (),
    "amount": string($amt),
    "debitCreditCode": $dc,
    "postingDate": $periodDate,
    "classifiedUnder": $taxonomyRefs
  }
}

return map {
  "@context": $context,
  "@graph": array:join(($taxonomyNodes, $accountNodes, $entityNodes, $entryNodes))
}


