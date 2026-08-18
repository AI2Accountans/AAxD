xquery version "3.1";

(: 
  ===========================================================================
  PROYECTO: GSKM_FON - Enriquecimiento a CSV Directo
  ARCHIVO: merge_to_csv.xq
  DESCRIPCIÓN: Retorna directamente la salida en formato CSV.
               Ideal para ejecución desde consola de comandos (CLI)
               o integración con pipelines de datos.
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

let $csv-structure := 
  <csv>
    <record>
      <entry>Compañia</entry>
      <entry>Desc, compañia</entry>
      <entry>Auxiliar</entry>
      <entry>Cuenta 6</entry>
      <entry>Desc, auxiliar</entry>
      <entry>Saldo inicial</entry>
      <entry>Saldo final</entry>
      { for $t in 1 to 12 return <entry>Tag {$t}</entry> }
    </record>
    {
      for $row in $data-rows
      let $entries := $row/entry
      let $comp     := local:clean(string($entries[1]))
      let $desc-c   := local:clean(string($entries[2]))
      let $aux      := local:clean(string($entries[3]))
      let $desc-a   := local:clean(string($entries[4]))
      let $s-init   := local:clean(string($entries[5]))
      let $s-fin    := local:clean(string($entries[6]))
      let $cuenta-6 := substring($aux, 1, 6)
      let $tags     := map:get($tags-map, $cuenta-6)
      return
        <record>
          <entry>{$comp}</entry>
          <entry>{$desc-c}</entry>
          <entry>{$aux}</entry>
          <entry>{$cuenta-6}</entry>
          <entry>{$desc-a}</entry>
          <entry>{$s-init}</entry>
          <entry>{$s-fin}</entry>
          {
            for $t in 1 to 12
            let $val := if (exists($tags)) then $tags[$t] else ""
            return <entry>{$val}</entry>
          }
        </record>
    }
  </csv>

return csv:serialize($csv-structure, map { 'header': false(), 'separator': ',' })
