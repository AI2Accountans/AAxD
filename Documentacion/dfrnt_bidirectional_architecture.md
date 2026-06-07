# The Bidirectional Semantic Accounting Architecture ("Momento 0")

## 1. Introduction
This document outlines the architectural implementation of the "Momento 0" framework using DFRNT and TerminusDB. The objective is to evolve beyond traditional double-entry bookkeeping (Pacioli's model) by establishing a Semantic Enterprise Architecture. This architecture bridges the gap between structured financial reporting (XBRL GL), sustainability metrics (GRI), and the strict auditability requirements of the Artificial Intelligence era.

## 2. The Core Challenge: The "Seam Problem"
Modern financial ecosystems face a critical "seam problem": traditional relational ERPs and flat-file accounting systems obscure the decision-making loop. As AI begins to automate financial transactions, regulators and auditors require cryptographic and semantic proof of provenance. Traditional systems cannot provide observable, native audit trails for algorithmic decisions.

## 3. The Solution: A Bidirectional Semantic Hub
To solve this, we have designed a **Bidirectional Data Pipeline** that decouples storage, business logic, and semantic querying, placing DFRNT and TerminusDB at the core of the Enterprise Knowledge Graph.

### Phase 1: Ingestion and Extraction (The Edge)
- **Source Data & Portability:** Electronic invoices and standard business documents (supporting UBL/XML, JSON, CSV, or any other structured schema). **A key architectural feature of our MOSA approach is complete format independence. If a specific jurisdiction requires JSON, a custom XML layout, or any other format instead of UBL, the core of the semantic accounting stack remains completely untouched. Only the edge source schema is adjusted, leaving downstream models, databases, and validations fully intact.**
- **Processing:** Raw XML documents are ingested into native XML databases (BaseX) using XQuery, while JSON/JSON-LD or other native payloads are parsed directly, maintaining full context and structural integrity at the ingest boundary.

### Phase 2: Enrichment and Mapping (Altova MapForce)
- **Accounting Logic:** Business rules, tax calculations, and Chart of Accounts (PUC) assignments are visually mapped.
- **Semantic Translation:** Through **Altova MapForce**, the incoming raw data format (XML, JSON, or CSV) is mapped to the W3C-compliant **JSON-LD** graph format, using the XBRL Global Ledger (XBRL GL) schema as the underlying dictionary. This ensures that the core ledger is decoupled from localized invoicing syntax.

### Phase 3: The Semantic Graph (DFRNT / TerminusDB)
- **Immutable Storage:** The enriched JSON-LD is ingested into TerminusDB.
- **Data Products & Foreign References:** DFRNT is used to model the schema. Transactional data products link natively to Master Data products (e.g., FIBO for financial concepts, GRI for ESG/Sustainability reporting) using Foreign References.
- **Provenance:** Using the PROV-O ontology (`prov:wasDerivedFrom`), every node in the graph maintains an immutable, cryptographically verifiable link back to its original source document. This provides the ultimate "human/AI-in-the-loop" observability.

### Phase 4: The Bidirectional Export (Legacy Integration)
TerminusDB is not a data silo; it is a bidirectional engine. 
- **Reverse Engineering:** Using TerminusDB's native querying capabilities (WOQL/GraphQL), the complex semantic graph can be flattened on-demand.
- **The "Passive Compliance Vault":** The system can automatically generate and export flat CSV files containing exact debits and credits required by legacy ERPs or local tax authorities. The graph remains the Single Source of Truth (SSOT), while the ERP acts merely as a downstream compliance ledger.

## 4. Conclusion
By utilizing DFRNT as the central Semantic Data Hub, we achieve full legal compliance (aligning with UNCITRAL functional equivalence principles) while future-proofing enterprise accounting. This bidirectional architecture ensures that transactional data flows seamlessly from raw XML to a rich, queryable knowledge graph, and back to legacy flat-files when necessary.
