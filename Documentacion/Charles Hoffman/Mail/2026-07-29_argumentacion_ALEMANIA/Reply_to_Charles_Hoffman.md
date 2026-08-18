# Email Reply to Charles Hoffman

**To**: Charles Hoffman <Charles.Hoffman@xbrl.org>  
**Subject**: Re: Proof of Concept: XBRL GL as a Semantic Bridge to DFRNT / TerminusDB Knowledge Graphs  
**Date**: 2026-07-29  

---

Hi Charlie,

Thank you for this sharp and spot-on observation. 

I completely agree with your thesis: an audit is ultimately an audit of the financial statements, and a GL ingestion pipeline is only truly proven when it can generate a provably correct set of primary financial statements (Balance Sheet, Income Statement, Cash Flow, and Equity Changes) according to a target financial reporting framework.

To clarify our current capabilities and target direction:

1. **Existing Working Pipeline (XML / XSLT)**: 
   With our current XBRL GL XML instance and custom XSLT stylesheets (in our `sps` directory), we **already generate complete, formatted financial statement reports** (such as the delivered balance sheet and income statement reports in our `Entregable` folder).

2. **Target Objective with TerminusDB / DFRNT**:
   The core purpose of transmuting XBRL GL into JSON-LD and ingesting it into TerminusDB is to **project that exact same target financial report structure natively out of the Knowledge Graph**—using WOQL graph queries, SHACL constraints, and semantic rules—rather than relying on static file-based XSLT stylesheets.

*(Note: We have updated the shared `.zip` archive to include the XSLT stylesheet currently used and the target financial statement result achieved with it, so you can inspect both the intermediate XSLT pipeline and the rendered output.)*

Your reference to Dave McComb's *Data-Centric Accounting* and the work of Joey French and Dudley Gould is spot-on. We strongly believe that the graph database layer—rather than proprietary ERP code or legacy XSLT scripts—is where business event discovery and provable financial statement projection should take place.

Would you be open to sharing some of the financial statement verification rules or event discovery criteria you’ve developed? We would love to test them as part of our TerminusDB/DFRNT graph projection validation to demonstrate provably correct financial statements directly out of the graph.

Cheers,

Richard  
DFRNT Accounting & Audit Project Team  
