xquery version "3.1";

(: 
  ===========================================================================
  PROYECTO: GSKM_FON - Transformación XBRL GL (SRCD) a JSON-LD
  ARCHIVO: xbrlgl_to_jsonld.xq
  DESCRIPCIÓN: Lee el documento XBRL GL 'Output/Qx_SaldoInicialQxSiesa2XBRLGL.xml'
               y extrae los asientos contables junto con el enriquecimiento 
               del módulo SRCD (gl-srcd:detailedContentFilter) para generar
               la ontología en formato JSON-LD.
  ===========================================================================
:)

declare namespace xbrli   = "http://www.xbrl.org/2003/instance";
declare namespace gl-cor  = "http://www.xbrl.org/int/gl/cor/2015-03-25";
declare namespace gl-srcd = "http://www.xbrl.org/int/gl/srcd/2015-03-25";
declare namespace file    = "http://expath.org/ns/file";

(: -------------------------------------------------------------------------
   1. Configuración de Rutas de Entrada y Salida (Resueltas dinámicamente)
   ------------------------------------------------------------------------- :)
declare variable $BASE-DIR   as xs:string := file:base-dir();
declare variable $XML-PATH   as xs:string := file:resolve-path("../Output/Qx_SaldoInicialQxSiesa2XBRLGL.xml", $BASE-DIR);
declare variable $TARGET-LD  as xs:string := file:resolve-path("../Output/Qx_SaldoInicialQxSiesa2XBRLGL.jsonld", $BASE-DIR);

(: -------------------------------------------------------------------------
   2. Carga y Procesamiento del Documento XBRL GL
   ------------------------------------------------------------------------- :)
let $doc := doc($XML-PATH)

(: Extraer metadatos del Contexto XBRL :)
let $entity-id := string(($doc//xbrli:entity/xbrli:identifier)[1])
let $instant   := string(($doc//xbrli:period/xbrli:instant)[1])

(: Recorrer cada elemento gl-cor:entryDetail :)
let $entries := 
  for $entry at $idx in $doc//gl-cor:entryDetail
  let $account-id    := normalize-space(string($entry/gl-cor:account/gl-cor:accountMainID))
  let $account-desc  := normalize-space(string($entry/gl-cor:account/gl-cor:accountMainDescription))
  let $amount-str    := string($entry/gl-cor:amount)
  let $amount-num    := if ($amount-str castable as xs:decimal) then xs:decimal($amount-str) else 0.0
  let $debit-credit  := normalize-space(string($entry/gl-cor:debitCreditCode))
  let $posting-date  := normalize-space(string($entry/gl-cor:postingDate))
  let $ident-code    := normalize-space(string($entry/gl-cor:identifierReference/gl-cor:identifierCode))
  let $ident-desc    := normalize-space(string($entry/gl-cor:identifierReference/gl-cor:identifierDescription))
  
  (: -----------------------------------------------------------------------
     ENRIQUECIMIENTO SRCD: Extracción de etiquetas gl-srcd:detailedContentFilter
     ----------------------------------------------------------------------- :)
  let $srcd-tags := array {
    for $filter in $entry//gl-srcd:detailedContentFilter
    let $val := normalize-space(string($filter))
    where $val != ""
    return $val
  }

  return map {
    "@type": "EntryDetail",
    "@id": concat("EntryDetail/", $account-id, "_", $idx),
    "lineNumberCounter": $idx,
    "account": concat("Account/", $account-id),
    "accountMainID": $account-id,
    "accountMainDescription": $account-desc,
    "amount": $amount-num,
    "debitCreditCode": $debit-credit,
    "postingDate": $posting-date,
    "companyCode": $ident-code,
    "companyDescription": $ident-desc,
    
    (: Metadatos del Módulo SRCD transmitidos al JSON-LD :)
    "gl-srcd:detailedContentFilter": $srcd-tags,
    
    "prov:wasDerivedFrom": "xbrl_gl:entryDetail"
  }

(: -------------------------------------------------------------------------
   3. Estructuración del Documento JSON-LD con @context Ontológico
   ------------------------------------------------------------------------- :)
let $jsonld-document := array {
  map {
    "@context": map {
      "@vocab": "http://dfrnt.com/ontology/aad#",
      "gl-cor": "http://www.xbrl.org/int/gl/cor/2015-03-25#",
      "gl-srcd": "http://www.xbrl.org/int/gl/srcd/2015-03-25#",
      "gsk": "http://dfrnt.com/taxonomy/gsk#",
      "prov": "http://www.w3.org/ns/prov#",
      "fibo": "https://spec.edmcouncil.org/fibo/ontology/FBC/"
    },
    "entityIdentifier": $entity-id,
    "periodInstant": $instant,
    "totalEntries": count($entries),
    "entries": array { $entries }
  }
}

(: -------------------------------------------------------------------------
   4. Serialización JSON y Escritura en Disco
   ------------------------------------------------------------------------- :)
let $json-serialized := serialize($jsonld-document, map { 'method': 'json', 'indent': 'yes' })
let $write-status     := file:write-text($TARGET-LD, $json-serialized)

(: Retornar estado del proceso :)
return
  <resultado status="ÉXITO">
    <mensaje>Transformación XBRL GL (SRCD) -> JSON-LD completada con éxito.</mensaje>
    <total_asientos_procesados>{count($entries)}</total_asientos_procesados>
    <archivo_jsonld_generado>{$TARGET-LD}</archivo_jsonld_generado>
  </resultado>
