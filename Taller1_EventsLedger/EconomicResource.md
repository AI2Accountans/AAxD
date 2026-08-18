---
title: Economic Resource
type: concept
layer: Foundation (REA / ISO 15944-4)
---

# Economic Resource

## Definition
An **Economic Resource** is an item of value that is either owned or controlled by an Economic Agent. Resources are the objects that are exchanged or transformed during an Economic Event. Examples include cash, inventory, equipment, or services.

## The Holon Concept
Within the Business Events Ledger, the Economic Resource is a primary node. It is independent of the events that affect it, existing as a distinct entity with its own properties (e.g., current value, quantity).

## Linkage to XBRL GL
- **Concept:** Maps directly to the `measurable` structure within an XBRL GL entry.
- **Identifier:** Captured using elements like `measurableID` (e.g., SKU, Asset ID) and `measurableName`.
- **Valuation:** Represented by `amount` and `quantity` fields inside the measurable section, representing the physical or monetary shift triggered by the event.

## Linkage to Data Centric Accounting
Instead of being represented as mere balances in T-accounts, Economic Resources are explicitly tracked. The current state (balance) of any resource is derived programmatically by aggregating all related Stock-Flows (inflows and outflows) connected to it via Economic Events.
