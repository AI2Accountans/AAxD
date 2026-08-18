---
title: Entry Detail
type: concept
layer: Ledger & XBRL GL
---

# Entry Detail

## Definition
The **Entry Detail** captures the specific atomic impacts of an Economic Event. While traditional accounting calls these "Debits" and "Credits" affecting nominal accounts, in a semantic model, they represent the distinct Stock-Flows (inflows and outflows) acting upon specific Economic Resources.

## The Holon Concept
Entry Details are the internal components of the Event Holon. A single Holon (Event) will typically contain two or more Entry Details (to satisfy the Duality of an exchange), ensuring the physical transaction balances.

## Linkage to XBRL GL
- **Concept:** Maps directly to the `<gl-cor:entryDetail>` element, which is nested inside the `<gl-cor:entryHeader>`.
- **Components:** Contains the `account` structure (if mapped to a legacy Chart of Accounts), the `amount` and `signOfAmount` (Stock-Flow direction), and importantly, the `identifierReference` (Agent) and `measurable` (Resource) that the detail applies to.

## Linkage to Data Centric Accounting
Entry Details are the edges in the semantic graph. They are the traversable links that allow a query to start from an Agent (e.g., "Show me all interactions with Customer X") and sum the Entry Details to find the current state of a Resource.
