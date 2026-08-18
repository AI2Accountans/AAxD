---
title: Entry Header
type: concept
layer: Ledger & XBRL GL
---

# Entry Header

## Definition
The **Entry Header** contains the metadata for a specific Economic Event within the Journal. It binds together the overall context of the transaction, such as the date, the author, the source system, and the overall rationale, rather than the specific financial impacts.

## The Holon Concept
If the Economic Event is the conceptual Holon, the Entry Header is its concrete data structure representation in the physical ledger. It acts as the "envelope" for the granular stock-flows (Entry Details).

## Linkage to XBRL GL
- **Concept:** Maps exactly to the `<gl-cor:entryHeader>` element.
- **Components:** Contains fields like `enteredBy`, `enteredDate`, `sourceJournalID`, and `qualifierEntry`.
- **Purpose:** It provides the audit trail and provenance at the event level.

## Linkage to Data Centric Accounting
In the graph, the Entry Header metadata is stored as properties directly on the Economic Event node. This ensures that every resulting stock-flow and line item derivation inherits this strict provenance.
