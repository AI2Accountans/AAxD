xquery version "3.1";

declare namespace file = "http://expath.org/ns/file";

declare variable $BASE-DIR  as xs:string := file:base-dir();
declare variable $JSON-PATH as xs:string := file:resolve-path("../Output/CSV2XBRLGL2JSONLD.json", $BASE-DIR);
declare variable $OUT-PATH  as xs:string := file:resolve-path("../../.gemini/antigravity-ide/brain/1fb67e31-86ac-46a0-a6e0-8a1cec01800d/scratch/inspect_jsonld.txt", $BASE-DIR);

let $json-text := file:read-text($JSON-PATH)
let $items := parse-json($json-text)?*
let $details := for $i in $items where string($i("@type")) = "EntryDetail" return $i

(: Sumas por clase 1, 2, 3, 4, 5, 6, 7, 8, 9 :)
let $c1 := sum(for $d in $details where starts-with(string($d("account")), "1") return xs:decimal($d("amount")))
let $c2 := sum(for $d in $details where starts-with(string($d("account")), "2") return xs:decimal($d("amount")))
let $c3 := sum(for $d in $details where starts-with(string($d("account")), "3") return xs:decimal($d("amount")))
let $c4 := sum(for $d in $details where starts-with(string($d("account")), "4") return xs:decimal($d("amount")))
let $c5 := sum(for $d in $details where starts-with(string($d("account")), "5") return xs:decimal($d("amount")))
let $c8 := sum(for $d in $details where starts-with(string($d("account")), "8") return xs:decimal($d("amount")))
let $c9 := sum(for $d in $details where starts-with(string($d("account")), "9") return xs:decimal($d("amount")))

(: Sumas por Tag 1 en gl-srcd:detailedContentFilter :)
let $assets := sum(for $d in $details
                   let $tags := $d("gl-srcd:detailedContentFilter")?*
                   where $tags[1] = "gsk:Assets"
                   return xs:decimal($d("amount")))

let $equity-liab := sum(for $d in $details
                         let $tags := $d("gl-srcd:detailedContentFilter")?*
                         where $tags[1] = "gsk:EquityAndLiabilities"
                         return xs:decimal($d("amount")))

let $res := concat(
  "Total EntryDetails: ", count($details), "&#10;",
  "=== POR CLASE CONTABLE (PUC) ===", "&#10;",
  "Clase 1 (Activos): ", format-number($c1, "#,##0.00"), "&#10;",
  "Clase 2 (Pasivos): ", format-number($c2, "#,##0.00"), "&#10;",
  "Clase 3 (Patrimonio): ", format-number($c3, "#,##0.00"), "&#10;",
  "Clase 4 (Ingresos): ", format-number($c4, "#,##0.00"), "&#10;",
  "Clase 5 (Gastos): ", format-number($c5, "#,##0.00"), "&#10;",
  "Clase 8 (Cuentas de Orden): ", format-number($c8, "#,##0.00"), "&#10;",
  "Clase 9 (Cuentas de Orden): ", format-number($c9, "#,##0.00"), "&#10;&#10;",
  "=== POR TAG 1 (SRCD) ===", "&#10;",
  "Tag1 Assets: ", format-number($assets, "#,##0.00"), "&#10;",
  "Tag1 EquityAndLiabilities: ", format-number($equity-liab, "#,##0.00")
)

return file:write-text($OUT-PATH, $res)
