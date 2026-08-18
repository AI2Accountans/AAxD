xquery version "3.1";

declare namespace file = "http://expath.org/ns/file";

declare variable $BASE-DIR as xs:string := file:base-dir();
declare variable $JSON-PATH as xs:string := file:resolve-path("../Output/CSV2XBRLGL2JSONLD.json", $BASE-DIR);
declare variable $OUT-PATH as xs:string := file:resolve-path("../../.gemini/antigravity-ide/brain/1fb67e31-86ac-46a0-a6e0-8a1cec01800d/scratch/sum_result.txt", $BASE-DIR);

let $json-text := file:read-text($JSON-PATH)
let $items := parse-json($json-text)

(: Filtro 1: Estricto pedido por el usuario (293, 2026-07-31, gsk:Assets) :)
let $matching-exact := for $item in $items?*
                       where string($item?agent_identifier) = '293'
                         and string($item?postingDate) = '2026-07-31'
                         and (some $tag in $item?`gl-srcd:detailedContentFilter`?* satisfies $tag = 'gsk:Assets')
                       return xs:decimal($item?amount)

let $sum-exact := sum($matching-exact)

(: Filtro 2: Compañía en el dataset actual (agent_identifier = '3') :)
let $matching-comp3 := for $item in $items?*
                       where string($item?agent_identifier) = '3'
                         and (some $tag in $item?`gl-srcd:detailedContentFilter`?* satisfies $tag = 'gsk:Assets')
                       return xs:decimal($item?amount)

let $sum-comp3 := sum($matching-comp3)

let $res := concat(
  "Total registros en JSON: ", count($items?*), "&#10;",
  "=== RESULTADO SOLICITADO (agent_identifier='293', postingDate='2026-07-31', tag='gsk:Assets') ===", "&#10;",
  "Coincidencias encontradas: ", count($matching-exact), "&#10;",
  "Suma Total (amount): $", format-number($sum-exact, "#,##0.00"), "&#10;&#10;",
  "=== DATASET ACTUAL EN GSKM_FON (agent_identifier='3', tag='gsk:Assets') ===", "&#10;",
  "Coincidencias encontradas: ", count($matching-comp3), "&#10;",
  "Suma Total (amount): $", format-number($sum-comp3, "#,##0.00")
)

return file:write-text($OUT-PATH, $res)
