---
title: Business Event Journal
type: concept
layer: Ledger & XBRL GL
---

# Business Event Journal

## Definition
The **Business Event Journal** is the physical and logical container that logs chronologically all Economic Events occurring within the enterprise. Unlike traditional general ledgers that store aggregated monetary balances, the Business Event Journal stores granular, immutable event records.

## The Holon Concept
The entire Journal acts as the macro-structure containing individual Event Holons. Because every event is self-describing and immutable (Data Centric), the Journal serves as the absolute "Single Source of Truth." Any report, from the Trial Balance to specific line items, is simply a semantic view generated dynamically from this Journal.

## Linkage to XBRL GL
- **Concept:** Represents the entire instance document or a continuous stream of `<xbrl>` GL instances.
- **Mapping:** Corresponds to the overarching `<gl-cor:accountingEntries>` structure that encapsulates all headers and details.

## Linkage to Data Centric Accounting
In a graph database implementation (TerminusDB / Momento 0), the Journal is not a table, but the continuous sub-graph of Event Nodes connected over time via PROV-O provenance links (`wasGeneratedBy`, `wasDerivedFrom`).
