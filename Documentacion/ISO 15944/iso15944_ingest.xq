(:
  Módulo RESTXQ para BaseX (Servidor de Escritorio Local: http://localhost:8984/iso15944/ingest)
  Recepción e Ingesta de Contratos ISO/IEC 15944-4 (REA / Valueflows XML) provenientes de Altova StyleVision.
:)
module namespace api = 'http://dfrnt.org/api/iso15944';

declare 
  %rest:path('/iso15944/ingest')
  %rest:POST("{$body}")
  %rest:consumes("application/xml", "text/xml")
  %rest:produces("application/xml")
function api:ingest-iso15944($body as node()) {
  let $db-name := "ubl2dfrnt"
  let $timestamp := replace(string(current-dateTime()), ":", "-")
  let $tx-id := data($body//*:transactionId)
  let $doc-id := concat("iso15944_", if ($tx-id != "") then $tx-id else $timestamp, ".xml")
  
  return (
    (: 1. Guardar documento XML en la base de datos BaseX :)
    db:add($db-name, $body, concat("contracts/", $doc-id)),
    
    (: 2. Retornar confirmación XML al formulario XForms de StyleVision :)
    <response status="200" success="true">
      <message>Contrato ISO 15944 capturado exitosamente en la fuente (Shift Left)</message>
      <documentId>{$doc-id}</documentId>
      <transactionId>{$tx-id}</transactionId>
      <timestamp>{string(current-dateTime())}</timestamp>
    </response>
  )
};
