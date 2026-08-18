xquery version "3.1";

(: 
  ===========================================================================
  PROYECTO: GSKM_FON - Enriquecimiento a XML Nativo
  ARCHIVO: merge_to_xml.xq
  DESCRIPCIÓN: Retorna los datos enriquecidos en formato XML estructurado.
               Ideal para consultas XPath/XQuery adicionales o para
               almacenar como documento nativo en bases de datos BaseX.
  ===========================================================================
:)

declare namespace csv  = "http://basex.org/modules/csv";
declare namespace file = "http://expath.org/ns/file";

declare variable $BASE-DIR    as xs:string := file:base-dir();
declare variable $SOURCE-PATH as xs:string := file:resolve-path("../Source/Data - Hoja 1.csv", $BASE-DIR);
declare variable $TAGS-PATH   as xs:string := file:resolve-path("../Tags/Tags.csv", $BASE-DIR);

declare function local:clean($val as xs:string?) as xs:string {
  let $trimmed := normalize-space($val)
  return replace(replace($trimmed, '^"', ''), '"$', '')
};

let $tags-doc := csv:doc($TAGS-PATH, map { 'header': false(), 'separator': ',' })
let $tags-map := map:merge(
  for $rec in $tags-doc//record
  let $entries := $rec/entry
  let $cuenta  := local:clean(string($entries[1]))
  where string-length($cuenta) = 6 and matches($cuenta, '^\d{6}$')
  return map {
    $cuenta: for $idx in 2 to 13 return local:clean(string($entries[$idx]))
  }
)

let $source-doc := csv:doc($SOURCE-PATH, map { 'header': false(), 'separator': ',' })
let $all-rows   := $source-doc//record
let $data-rows  := tail($all-rows)

return
  <reporte_enriquecido total_registros="{count($data-rows)}">
    {
      for $row in $data-rows
      let $entries := $row/entry
      let $aux      := local:clean(string($entries[3]))
      let $cuenta-6 := substring($aux, 1, 6)
      let $tags     := map:get($tags-map, $cuenta-6)
      return
        <registro>
          <compania>{local:clean(string($entries[1]))}</compania>
          <desc_compania>{local:clean(string($entries[2]))}</desc_compania>
          <auxiliar>{$aux}</auxiliar>
          <cuenta_6>{$cuenta-6}</cuenta_6>
          <desc_auxiliar>{local:clean(string($entries[4]))}</desc_auxiliar>
          <saldo_inicial>{local:clean(string($entries[5]))}</saldo_inicial>
          <saldo_final>{local:clean(string($entries[6]))}</saldo_final>
          <tags>
            {
              for $t in 1 to 12
              let $val := if (exists($tags)) then $tags[$t] else ""
              return element { concat("tag_", $t) } { $val }
            }
          </tags>
        </registro>
    }
  </reporte_enriquecido>
