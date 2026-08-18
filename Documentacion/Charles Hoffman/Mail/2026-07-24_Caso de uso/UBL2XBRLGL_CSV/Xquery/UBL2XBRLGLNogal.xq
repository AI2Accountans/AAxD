declare namespace ds="http://www.w3.org/2000/09/xmldsig#";
declare namespace cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2";
declare namespace cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2";
declare namespace ccts="urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2";
declare namespace ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2";
declare namespace xades="http://uri.etsi.org/01903/v1.3.2#";
declare namespace xades141="http://uri.etsi.org/01903/v1.4.1#";
declare namespace sts="dian:gov:co:facturaelectronica:Structures-2-1";
declare namespace inv="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2";
declare namespace n0="urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2";
declare namespace qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDataTypes-2";
declare namespace sac="urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2";
declare namespace sbc="urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2";
declare namespace udt="urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2";
declare namespace ccts-cct="urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2";

declare option output:omit-xml-declaration "yes";

file:write-text("C:\Users\IPHIX\Documents\Capacitacion XBRL\UBL2XBRLGL\Entregable\dataLuis.csv",

<csv>{
  let $db := db:get("GSKM")

    for $doc in $db//(inv:Invoice|cac:Attachment/cac:ExternalReference/cbc:Description/parse-xml(.)/*[self::*:Invoice])
  
 
  let $QRCode := string-join($doc/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions, ' | ')
  let $IssueDate := string-join($doc/cbc:IssueDate, ' | ')
  let $NumeroFactura := string-join($doc/cbc:ID, ' | ')
  let $ASP_PartyName := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name, ' | ')
  let $ASP_CityName := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName, ' | ')
  let $ASP_CountrySubentity := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity, ' | ')
  let $ASP_AdresseLine := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line, ' ')
  let $ASP_Country := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name, ' | ')
  let $ASP_NIT := string-join($doc/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID, ' | ')
  let $ACP_PartyName := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name, ' | ')
  let $ACP_AdresseLine := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line, ' ')
  let $ACP_CityName := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName, ' | ')
  let $ACP_CountrySubentity := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity, ' | ')
  let $ACP_Country := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name, ' | ')
  let $ACP_NIT := string-join($doc/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID, ' | ')
  let $BaseImpto := string-join($doc/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxInclusiveAmount, ' | ')
  let $ImptoIVA := string-join($doc/cac:TaxTotal/cbc:TaxAmount, ' | ')
  let $VrTotal := string-join($doc/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount, ' | ')
  for $InvoiceLine in $doc/cac:InvoiceLine
  let $Quantity := string-join($InvoiceLine/cbc:InvoicedQuantity, ' | ')
  let $PrecioTotal := string-join($InvoiceLine/cbc:LineExtensionAmount, ' | ')
  let $Codigo := string-join($InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID, ' | ')
  let $Description := string-join($InvoiceLine/cac:Item/cbc:Description, ' | ') 
  
  
  order by $ASP_NIT descending
  
  return
   
    <record>
      <entry name="QRCode">{
        if (contains($QRCode, "http"))
        then "http" || substring-after($QRCode, "http")
        else ()
      }</entry>
      <entry name="Fecha Factura">{data($IssueDate)}</entry>
      <entry name="Número Factura">{data($NumeroFactura)}</entry>
      <entry name="ASP_Proveedor">{data($ASP_PartyName)}</entry>    
      <entry name="ASP_Dirección">{normalize-space($ASP_AdresseLine)}</entry>
      <entry name="ASP_Ciudad">{normalize-space($ASP_CityName)}</entry>
      <entry name="ASP_Departamento">{normalize-space($ASP_CountrySubentity)}</entry>
      <entry name="ASP_País">{normalize-space($ASP_Country)}</entry>
      <entry name="ASP_NIT">{normalize-space($ASP_NIT)}</entry>
      <entry name="ACP_Cliente">{data($ACP_PartyName)}</entry>
      <entry name="ACP_Dirección">{data($ACP_AdresseLine)}</entry>
      <entry name="ACP_Ciudad">{normalize-space($ACP_CityName)}</entry>
      <entry name="ACP_Departamento">{normalize-space($ACP_CountrySubentity)}</entry>
      <entry name="ACP_País">{normalize-space($ACP_Country)}</entry>
      <entry name="ACP_NIT">{normalize-space($ACP_NIT)}</entry>
      <entry name="Base Impuesto">{normalize-space($BaseImpto)}</entry>  
      <entry name="Impuesto IVA">{normalize-space($ImptoIVA)}</entry>
      <entry name="Vr.Total">{normalize-space($VrTotal)}</entry>
      <entry name="Código">{normalize-space($Codigo)}</entry>
      <entry name="Descripción">{normalize-space($Description)}</entry>   
      <entry name="Cantidad_Ítems">{data($Quantity)}</entry>
      <entry name="Precio_Total">{data($PrecioTotal)}</entry>
    </record>
       
}</csv> 
  => csv:serialize(map {"header": true(), "format": "attributes","separator":"comma"})
)
