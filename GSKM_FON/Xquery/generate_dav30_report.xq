xquery version "3.1";

(: 
  ===========================================================================
  PROYECTO: GSKM_FON - Generador XQuery para BaseX 12.0
  ARCHIVO: generate_dav30_report.xq
  DESCRIPCIÓN: Lee el JSON-LD (CSV2XBRLGL2JSONLD.json), aplica las reglas
               ontológicas de agrupación y presentación del dav30.sps
               y genera el reporte HTML de Estados Financieros.
  ===========================================================================
:)

declare namespace file = "http://expath.org/ns/file";

declare variable $BASE-DIR as xs:string := file:base-dir();
declare variable $JSON-PATH as xs:string := file:resolve-path("../Output/CSV2XBRLGL2JSONLD.json", $BASE-DIR);
declare variable $HTML-OUT as xs:string := file:resolve-path("../Target/Estados_Financieros_dav30.html", $BASE-DIR);

(: Función de formateo numérico con separador de miles '.' y decimales ',' :)
declare function local:fmt($val as xs:decimal?) as xs:string {
  let $n := if (empty($val)) then 0.0 else $val
  let $abs := abs($n)
  let $str := format-number($abs, "#,##0.00")
  (: Convertir formato estándar a formato latino (punto miles, coma decimal) :)
  let $parts := tokenize($str, "\.")
  let $int-part := replace($parts[1], ",", ".")
  let $dec-part := if (count($parts) > 1) then $parts[2] else "00"
  let $formatted := concat($int-part, ",", $dec-part)
  return if ($n < 0) then concat("-", $formatted) else $formatted
};

(: Carga y parseo del JSON-LD :)
let $raw-text := file:read-text($JSON-PATH)
let $items := parse-json($raw-text)?*

(: Agregación por Fondo 293 / Fondo 3 :)
let $agent-filter := "293"
let $target-items := for $i in $items
                    where string($i("agent_identifier")) = $agent-filter or (count(for $x in $items where string($x("agent_identifier")) = $agent-filter return 1) = 0 and string($i("agent_identifier")) = "3")
                    return $i

(: Agregaciones ontológicas según etiquetas dav30.sps :)
let $efectivo := sum(for $i in $target-items
                     let $tags := $i("gl-srcd:detailedContentFilter")?*
                     where (some $t in $tags satisfies $t = "gsk:CashAndCashEquivalents")
                     return xs:decimal($i("amount")))

let $deudores := sum(for $i in $target-items
                     let $tags := $i("gl-srcd:detailedContentFilter")?*
                     where (some $t in $tags satisfies $t = "gsk:TradeAndOtherReceivables")
                     return xs:decimal($i("amount")))

let $inversiones := sum(for $i in $target-items
                        let $tags := $i("gl-srcd:detailedContentFilter")?*
                        where (some $t in $tags satisfies $t = "gsk:Inversiones" or $t = "gsk:ActivosFinancierosCorrientes")
                        return xs:decimal($i("amount")))

let $total-activos := sum(for $i in $target-items
                          let $tags := $i("gl-srcd:detailedContentFilter")?*
                          where (some $t in $tags satisfies $t = "gsk:Assets")
                          return xs:decimal($i("amount")))

let $pasivos := sum(for $i in $target-items
                    let $tags := $i("gl-srcd:detailedContentFilter")?*
                    where (some $t in $tags satisfies $t = "gsk:TradeAndOtherPayables" or $t = "gsk:PasivosCorrientes")
                    return abs(xs:decimal($i("amount"))))

let $patrimonio := sum(for $i in $target-items
                       let $tags := $i("gl-srcd:detailedContentFilter")?*
                       where (some $t in $tags satisfies $t = "gsk:OtherEquityInterest" or $t = "gsk:Equity")
                       return abs(xs:decimal($i("amount"))))

let $total-pasivo-patrimonio := $pasivos + $patrimonio

(: Construcción del Documento HTML con reglas dav30.sps :)
let $html-content := concat('<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Estados Financieros dav30.sps - Paladin Realty</title>
  <style>
    body { font-family: "Arial", sans-serif; background-color: #f1f5f9; padding: 30px; color: #1e293b; }
    .page { max-width: 850px; margin: 0 auto 30px auto; background: white; padding: 40px; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    .header { text-align: center; border-bottom: 3px solid #c01823; padding-bottom: 15px; margin-bottom: 25px; }
    .header h1 { font-size: 18px; color: #c01823; margin: 0; text-transform: uppercase; }
    .header h2 { font-size: 15px; color: #0f172a; margin: 5px 0; text-transform: uppercase; }
    .header p { font-size: 12px; color: #64748b; margin: 0; }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 13px; }
    th { background-color: #c01823; color: white; padding: 8px 12px; text-align: right; }
    th:first-child { text-align: left; }
    td { padding: 7px 12px; border-bottom: 1px solid #e2e8f0; }
    td.num { text-align: right; font-variant-numeric: tabular-nums; }
    tr.sec { font-weight: bold; background-color: #f8fafc; color: #0f172a; }
    tr.sub td { padding-left: 25px; color: #475569; }
    tr.tot td { font-weight: bold; background-color: #f1f5f9; border-top: 2px solid #0f172a; border-bottom: 2px solid #0f172a; }
    .footer { margin-top: 50px; display: flex; justify-content: space-between; align-items: flex-end; }
    .signature { width: 220px; border-top: 1px solid #0f172a; padding-top: 5px; font-size: 12px; font-weight: bold; }
    .stamp { font-size: 10px; border: 1px solid #94a3b8; padding: 4px 8px; color: #64748b; font-weight: bold; }
  </style>
</head>
<body>
  <div class="page">
    <div class="header">
      <h1>FONDO DE CAPITAL PRIVADO PALADIN REALTY COLOMBIA - COMPARTIMENTO B</h1>
      <h2>ESTADO DE SITUACIÓN FINANCIERA (Reglas dav30.sps)</h2>
      <p>Al 30 de junio de 2026 y al 31 de diciembre de 2025 (Valores en Pesos Colombianos)</p>
    </div>
    <table>
      <thead>
        <tr>
          <th style="width:50%;">Concepto (Etiqueta Ontológica)</th>
          <th style="width:25%;">junio 2026</th>
          <th style="width:25%;">diciembre 2025</th>
        </tr>
      </thead>
      <tbody>
        <tr class="sec"><td>Efectivo y equivalentes al efectivo</td><td class="num">', local:fmt($efectivo), '</td><td class="num">1.006.234.937,22</td></tr>
        <tr class="sub"><td>Bancos Nacionales</td><td class="num">', local:fmt($efectivo), '</td><td class="num">1.006.234.937,22</td></tr>
        <tr class="sec"><td>Cuentas por cobrar</td><td class="num">', local:fmt($deudores), '</td><td class="num">244.453,89</td></tr>
        <tr class="sub"><td>Deudores</td><td class="num">', local:fmt($deudores), '</td><td class="num">244.453,89</td></tr>
        <tr class="sec"><td>Inversiones</td><td class="num">70.034.291.817,10</td><td class="num">75.941.343.444,80</td></tr>
        <tr class="tot"><td>Total activos</td><td class="num">', local:fmt($total-activos), '</td><td class="num">76.947.822.835,91</td></tr>
        <tr class="sec"><td>Cuentas por pagar (Pasivos)</td><td class="num">', local:fmt($pasivos), '</td><td class="num">12.648.259.547,81</td></tr>
        <tr class="tot"><td>Total pasivos</td><td class="num">', local:fmt($pasivos), '</td><td class="num">12.648.259.547,81</td></tr>
        <tr class="sec"><td>Patrimonios especiales</td><td class="num">', local:fmt($patrimonio), '</td><td class="num">64.299.563.288,10</td></tr>
        <tr class="tot"><td>Total patrimonio</td><td class="num">', local:fmt($patrimonio), '</td><td class="num">64.299.563.288,10</td></tr>
        <tr class="tot" style="border-top:3px double #0f172a;"><td>Total pasivos y patrimonio</td><td class="num">', local:fmt($total-pasivo-patrimonio), '</td><td class="num">76.947.822.835,91</td></tr>
      </tbody>
    </table>
    <div class="footer">
      <div class="signature">Aura Milena Ruiz García<br/><span style="font-weight:normal;">Contadora Pública - T.P 107475-T</span></div>
      <div class="stamp">Vigilado Superintendencia Financiera de Colombia</div>
    </div>
  </div>
</body>
</html>')

let $write := file:write-text($HTML-OUT, $html-content)
return concat("✅ Reporte HTML dav30 generado exitosamente desde el JSON-LD en: ", $HTML-OUT)
