---
title: Economic Agent
type: concept
layer: Foundation (REA / ISO 15944-4)
---

# Economic Agent

## Definition
An **Economic Agent** is an individual, organization, or system that participates in an Economic Event. Agents are typically classified as internal (e.g., employees, departments) or external (e.g., customers, vendors). They have the power to control or exchange Economic Resources.

## The Holon Concept
Agents are foundational nodes in the ledger. Every Economic Event must involve at least one (often two) participating Agents. This explicit linkage answers the "Who" of every transaction in a multi-dimensional way that double-entry bookkeeping obscures.

## Linkage to XBRL GL
- **Concept:** Maps to the `identifierReference` structure in XBRL GL.
- **Classification:** Differentiated via `identifierType` (e.g., `v` for vendor, `c` for customer, `e` for employee).
- **Details:** Contains fields like `identifierCode`, `identifierName`, and `identifierRole`.

## Linkage to Data Centric Accounting
In a timeless REA system, Agents are abstracted from traditional accounts (like "Accounts Receivable"). A debt is simply a conceptual relationship inferred from an incomplete exchange between two Agents, enabling continuous auditing of counterparty risk and relationship provenance.
