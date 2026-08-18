xquery version "3.1";

(: 
  ===========================================================================
  PROYECTO: GSKM_FON - Enriquecimiento de Datos Contables
  ARCHIVO: merge_data.xq
  DESCRIPCIÓN: Enriquece la información del archivo 'Data - Hoja 1.csv'
               asociando las etiquetas contables del archivo 'Tags.csv'
               mediante la coincidencia de los primeros 6 dígitos de 
               la columna 'Auxiliar' (9 dígitos) con la columna 'Cuenta' (6 dígitos).
  ===========================================================================
:)

declare namespace csv  = "http://basex.org/modules/csv";
declare namespace file = "http://expath.org/ns/file";

(: -------------------------------------------------------------------------
   1. Configuración de Rutas de Entrada y Salida (Resueltas dinámicamente)
   ------------------------------------------------------------------------- :)
declare variable $BASE-DIR    as xs:string := file:base-dir();
declare variable $SOURCE-PATH as xs:string := file:resolve-path("../Source/Data - Hoja 1.csv", $BASE-DIR);
declare variable $TAGS-PATH   as xs:string := file:resolve-path("../Tags/Tags.csv", $BASE-DIR);
declare variable $TARGET-CSV  as xs:string := file:resolve-path("../Target/Data_Enriquecida.csv", $BASE-DIR);
declare variable $TARGET-XML  as xs:string := file:resolve-path("../Target/Data_Enriquecida.xml", $BASE-DIR);

(: -------------------------------------------------------------------------
   2. Función Auxiliar para Limpieza de Cadenas
   ------------------------------------------------------------------------- :)
declare function local:clean($val as xs:string?) as xs:string {
  let $trimmed := normalize-space($val)
  return replace(replace($trimmed, '^"', ''), '"$', '')
};

(: -------------------------------------------------------------------------
   3. Lectura de 'Tags.csv' e Indexación por Código de Cuenta (6 dígitos)
   ------------------------------------------------------------------------- :)
let $tags-doc := csv:doc($TAGS-PATH, map { 'header': false(), 'separator': ',' })
let $tags-map := map:merge(
  for $rec in $tags-doc//record
  let $entries := $rec/entry
  let $cuenta  := local:clean(string($entries[1]))
  (: Filtrar filas válidas con código de cuenta a 6 dígitos :)
  where string-length($cuenta) = 6 and matches($cuenta, '^\d{6}$')
  return map {
    $cuenta: for $idx in 2 to 13 
             return local:clean(string($entries[$idx]))
  }
)

(: -------------------------------------------------------------------------
   4. Lectura de 'Data - Hoja 1.csv' y Proceso de Enriquecimiento
   ------------------------------------------------------------------------- :)
let $source-doc := csv:doc($SOURCE-PATH, map { 'header': false(), 'separator': ',' })
let $all-rows   := $source-doc//record
let $data-rows  := tail($all-rows)

let $enriched-nodes := 
  for $row in $data-rows
  let $entries := $row/entry
  let $compania      := local:clean(string($entries[1]))
  let $desc-compania := local:clean(string($entries[2]))
  let $auxiliar      := local:clean(string($entries[3]))
  let $desc-auxiliar := local:clean(string($entries[4]))
  let $saldo-inicial := local:clean(string($entries[5]))
  let $saldo-final   := local:clean(string($entries[6]))
  
  (: Extraer los primeros 6 dígitos de la columna Auxiliar (9 dígitos) :)
  let $cuenta-6 := substring($auxiliar, 1, 6)
  
  (: Buscar en el mapa de Tags :)
  let $matched-tags := map:get($tags-map, $cuenta-6)
  
  return
    <registro>
      <compania>{$compania}</compania>
      <desc_compania>{$desc-compania}</desc_compania>
      <auxiliar>{$auxiliar}</auxiliar>
      <cuenta_6>{$cuenta-6}</cuenta_6>
      <desc_auxiliar>{$desc-auxiliar}</desc_auxiliar>
      <saldo_inicial>{$saldo-inicial}</saldo_inicial>
      <saldo_final>{$saldo-final}</saldo_final>
      <tags>
        {
          for $t in 1 to 12
          let $tag-val := if (exists($matched-tags)) then $matched-tags[$t] else ""
          return element { concat("tag_", $t) } { $tag-val }
        }
      </tags>
    </registro>

(: -------------------------------------------------------------------------
   5. Construcción del Formato XML Final
   ------------------------------------------------------------------------- :)
let $xml-result := 
  <reporte_enriquecido total_registros="{count($enriched-nodes)}">
    {$enriched-nodes}
  </reporte_enriquecido>

(: -------------------------------------------------------------------------
   6. Construcción del Formato CSV Final
   ------------------------------------------------------------------------- :)
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
      <entry>Tag 1</entry>
      <entry>Tag 2</entry>
      <entry>Tag 3</entry>
      <entry>Tag 4</entry>
      <entry>Tag 5</entry>
      <entry>Tag 6</entry>
      <entry>Tag 7</entry>
      <entry>Tag 8</entry>
      <entry>Tag 9</entry>
      <entry>Tag 10</entry>
      <entry>Tag 11</entry>
      <entry>Tag 12</entry>
    </record>
    {
      for $r in $enriched-nodes
      return
        <record>
          <entry>{$r/compania/text()}</entry>
          <entry>{$r/desc_compania/text()}</entry>
          <entry>{$r/auxiliar/text()}</entry>
          <entry>{$r/cuenta_6/text()}</entry>
          <entry>{$r/desc_auxiliar/text()}</entry>
          <entry>{$r/saldo_inicial/text()}</entry>
          <entry>{$r/saldo_final/text()}</entry>
          <entry>{$r/tags/tag_1/text()}</entry>
          <entry>{$r/tags/tag_2/text()}</entry>
          <entry>{$r/tags/tag_3/text()}</entry>
          <entry>{$r/tags/tag_4/text()}</entry>
          <entry>{$r/tags/tag_5/text()}</entry>
          <entry>{$r/tags/tag_6/text()}</entry>
          <entry>{$r/tags/tag_7/text()}</entry>
          <entry>{$r/tags/tag_8/text()}</entry>
          <entry>{$r/tags/tag_9/text()}</entry>
          <entry>{$r/tags/tag_10/text()}</entry>
          <entry>{$r/tags/tag_11/text()}</entry>
          <entry>{$r/tags/tag_12/text()}</entry>
        </record>
    }
  </csv>

let $csv-serialized := csv:serialize($csv-structure, map { 'header': false(), 'separator': ',' })

(: -------------------------------------------------------------------------
   7. Escritura de Resultados en Disco (Target)
   ------------------------------------------------------------------------- :)
let $write-xml := file:write-text($TARGET-XML, serialize($xml-result, map { 'indent': 'yes' }))
let $write-csv := file:write-text($TARGET-CSV, $csv-serialized)

(: Retornar resumen del proceso :)
return
  <resultado status="ÉXITO">
    <mensaje>Proceso de enriquecimiento completado correctamente.</mensaje>
    <total_registros_procesados>{count($enriched-nodes)}</total_registros_procesados>
    <cuentas_tags_indexadas>{map:size($tags-map)}</cuentas_tags_indexadas>
    <archivo_xml_generado>{$TARGET-XML}</archivo_xml_generado>
    <archivo_csv_generado>{$TARGET-CSV}</archivo_csv_generado>
  </resultado>
