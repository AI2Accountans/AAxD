Subject: Re: Bypassing manual mappings with native semantics

Dear Charles,

To answer your question directly: **ABSOLUTELY TRUE.** 

You have perfectly identified the exact "self-induced" pain the industry suffers from. Because the industry relies on non-semantic physical formats (like flat PDFs), we are forced to build massive, error-prone manual mapping infrastructures. However, if the Source Document is natively semantic—such as the Inline XBRL invoice you shared, or an electronic invoice standard like UBL (Universal Business Language)—the need for human intervention or traditional accounting "mapping" vanishes entirely. The document *is* the event.

We are in complete agreement that if the document natively follows a structured HEADER (Who, When, What) and DETAIL (Line items, Amounts, Taxes) pattern, it should feed directly into the business event journal. It should be 100% "figure outable" by the machine, bypassing any mappings.

To prove your point empirically, **I have attached a ZIP file (`UBL2XBRLGL_CSV.zip`)** that demonstrates this exact workflow in action. 

Here is what the attached flow shows:
1. We took a standard electronic invoice in UBL format. 
2. Because it possesses native semantics, we transported it directly into an XBRL GL instance (`UBL2XBRLGL.mfd`), bypassing manual mapping.
3. Crucially, in the middle of this pipeline, we injected the necessary accounting semantics into the XBRL GL instance. 
4. This semantic enrichment allows us to flawlessly remap that XBRL GL instance into our JSON-LD Knowledge Graph.

When that instance enters the Knowledge Graph, the original invoice becomes the `SourceDocument` node, and the transaction is automatically assimilated into the Business Event Ledger. 

Please note that this specific mapping (UBL to JSON-LD via XBRL GL) is currently a standalone "Lego piece" in our lab. Moving forward, our goal is to integrate this piece seamlessly into the end-to-end continuous audit flow. Additionally, by leveraging XQuery against these native XML source documents, we have the capability to extract the most granular line-item data possible across all global jurisdictions that mandate the UBL standard.

Your example of the Inline XBRL invoice aligns perfectly with this vision. If one wants to do this right, there is indeed no technical impediment—only a historical reluctance to adopt standard semantics at the source.

I look forward to hearing your thoughts.

Best regards,

[Tu Nombre / AI2Accountans]
