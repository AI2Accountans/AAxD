let $xml := doc('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/valueflows_sample_instance.xml')
let $xslt := doc('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/valueflows_to_pdf.xslt')
let $fo := xslt:transform($xml, $xslt)
return file:write('C:/Users/IPHIX/Documents/Projects/DFRNT/Documentacion/ISO 15944/ontologias/contrato_iso15944.fo', $fo)
