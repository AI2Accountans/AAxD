---
title: Semantic Manifold
type: concept
layer: Reporting (MINI Framework)
---

# Semantic Manifold

## Definition
The **Semantic Manifold** is the logical mapping layer (the rules engine or ontology projection) that connects the granular, physical world (Economic Events, Resources, Agents) to the required standardized reporting abstractions (Standard Report Line Items). 

## The Holon Concept
Charles Hoffman describes the objective as creating the MINIMAL amount of information to NAVIGATE from EVENT >> Standard Report Line Item. The Semantic Manifold is that navigation pathway. It ensures that the ledger and the report are not two disconnected databases, but a single continuous graph. The Event Holon traverses the manifold to become a reported fact.

## Linkage to XBRL GL
- **Concept:** In the XBRL GL taxonomy, the manifold is realized by utilizing the `xbrlInfo` element to tag raw data, combined with formula linkbases or external rules engines that define the aggregation logic.
- **Mapping:** It serves as the crosswalk between the `cor` (Core) / `bus` (Business Concepts) modules of XBRL GL and the target reporting taxonomy (e.g., the MINI framework schemas).

## Linkage to Data Centric Accounting
In the "Momento 0" and "Momento 1" architectures, the Semantic Manifold is instantiated through a precise dual-step pipeline. The raw data is first passed through a standardization process into **XBRL GL** using MapForce mappings (e.g., `GS2XBRLGL2JSONLD_V1.mfd`). Following standardization, a **semantic transmutation** occurs, mapping the XBRL GL structures directly to **JSON-LD** using a predefined JSON-LD schema. This ensures the output is both compliant with accounting reporting standards (MINI framework) and inherently queryable as a semantic graph in Data Centric Accounting.
