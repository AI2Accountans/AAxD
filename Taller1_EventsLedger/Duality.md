---
title: Duality
type: concept
layer: Foundation (REA / ISO 15944-4)
---

# Duality

## Definition
**Duality** is the fundamental REA concept that replaces the double-entry bookkeeping rule of "Debits = Credits". It defines the causal relationship between two Economic Events. Most economic activities involve an exchange: an organization gives up a resource (decrement event) to acquire a different resource (increment event). 

## The Holon Concept
While each Economic Event is its own Holon, the Duality acts as the binding edge (the "Manifold" connection) that logically groups them into a complete business transaction (e.g., A Cash Disbursement event is causally linked via Duality to an Inventory Receipt event).

## Linkage to XBRL GL
- **Concept:** XBRL GL handles duality intrinsically through the `entryDetail` repetitions and the overarching `documentInfo` that links multiple entry lines. 
- **Mapping:** The duality relationship is represented when multiple `entryDetail` structures (representing different flows) are bound under a single `entryHeader` that corresponds to the overarching business event.

## Linkage to Data Centric Accounting
In semantic graphs (like TerminusDB), Duality is an explicitly defined edge connecting two Event nodes. This ensures that the rational economic rationale ("Why did we lose cash? Because we gained inventory") is permanently preserved as machine-readable logic.
