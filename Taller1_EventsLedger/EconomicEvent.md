---
title: Economic Event
type: concept
layer: Foundation (REA / ISO 15944-4)
---

# Economic Event

## Definition
An **Economic Event** is a business transaction or occurrence that either increases (inflow) or decreases (outflow) the quantity or value of an **Economic Resource**. In the context of Data Centric Accounting, an Economic Event represents the real-world action (e.g., a sale, a purchase, a cash receipt) that gives rise to the financial impact.

## The Holon Concept
As proposed in the "Momento 0" semantic architecture, an Economic Event is instantiated as a single, fully encapsulated **Holon**. 
- It is **ONE ENTRY** representing the overarching reality of what happened.
- It is the root node from which all related accounting entries (debits and credits) and stock-flows traverse.

## Linkage to XBRL GL
- **Concept:** Maps broadly to the overarching structure of an XBRL GL document.
- **Identifier:** `documentInfo` / `documentType` (e.g., Invoice, Order, Receipt) specifies the *type* of Economic Event.
- **Timestamp:** The date and time the event occurred, mapped to the GL Header's temporal fields.

## Linkage to Data Centric Accounting
In a Data Centric approach, the Economic Event is the nexus point. By avoiding relational silos, the Economic Event connects directly to the Agents who participated in it and the Resources it affected, allowing continuous audit trails and multidimensional analysis without pre-aggregated ledgers.
