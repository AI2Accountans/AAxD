---
title: Stock-Flow
type: concept
layer: Foundation (REA / ISO 15944-4)
---

# Stock-Flow

## Definition
**Stock-Flow** defines the relationship between an Economic Event and an Economic Resource. It specifies whether the event represents an inflow (increase) or an outflow (decrease) of the resource. 

## The Holon Concept
The Stock-Flow is the directed edge connecting the Event Holon to the Resource node. In double-entry accounting, this is analogous to assigning a debit or credit to an account, but semantically, it simply describes the physical or logical movement of a resource.

## Linkage to XBRL GL
- **Concept:** Represents the combination of an `entryDetail`'s directional sign and its associated `measurable`.
- **Mapping:** Identified primarily through the `signOfAmount` field (or implicitly through positive/negative values depending on the specific GL module implementation) mapped against the resource described in the `measurable` structure.

## Linkage to Data Centric Accounting
Stock-Flow eliminates the need for predefined Chart of Accounts balances. The total stock of any resource is deterministically calculated by traversing all associated inflow and outflow edges over time.
