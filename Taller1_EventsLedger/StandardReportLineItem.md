---
title: Standard Report Line Item
type: concept
layer: Reporting (MINI Framework)
---

# Standard Report Line Item

## Definition
A **Standard Report Line Item** is a formalized disclosure concept defined within a specific financial reporting taxonomy (in this case, the MINI Reporting Framework). It represents an aggregated or calculated financial fact (e.g., "Cash and Cash Equivalents", "Cost of Goods Sold") required for regulatory or management reporting.

## The Holon Concept
The Line Item is the *output* view. It is not physically stored as a static balance in the Data Centric model. Instead, it is a dynamic aggregation derived from the underlying Business Event Holons. The Line Item exists at the very end of the semantic manifold.

## Linkage to XBRL GL
- **Concept:** This is the bridge between the XBRL GL instance (the ledger) and the XBRL FR (Financial Reporting) taxonomy. 
- **Mapping:** In XBRL GL, this is achieved using the `xbrlInfo` structure within an `entryDetail`. The `xbrlInfo` allows a specific granular entry to be tagged with the taxonomy element name (e.g., `<gl-cor:xbrlElement>CashAndCashEquivalents</gl-cor:xbrlElement>`) from the MINI framework.

## Linkage to Data Centric Accounting
Instead of a rigid Chart of Accounts, mapping occurs organically. The Semantic Graph allows traversing from the `Standard Report Line Item` node backward through the `Semantic Manifold` (the rules engine) directly to the `Economic Event` and its source document, ensuring 100% machine-readable traceability.
