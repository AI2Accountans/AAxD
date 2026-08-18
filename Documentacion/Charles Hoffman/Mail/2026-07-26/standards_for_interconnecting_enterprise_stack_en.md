# Standards for Interconnecting the Enterprise Stack

> **Source:** Charles Hoffman (Digital Financial Reporting Blog)  
> **URL:** https://digitalfinancialreporting.blogspot.com/2026/07/standards-for-interconnecting.html  
> **Published:** July 26, 2026 · **Last updated:** July 26, 2026 (09:22 PST)  
> **Elaborated with:** Microsoft Copilot + Google Gemini  

---

## 🎯 Central Question

Charlie's starting point is a question he has been trying to answer:

> *What is the relationship between UBL, REA (ISO/IEC), ACTUS, FASB/IFRS Taxonomies, SBVR, BPMN, and XBRL?*  
> *How are all these standards related to each other?*

His answer: **they are not competitors — they are layers of a single semantic supply chain for business meaning.**

---

## 🗺️ The Big Picture: A Continuous Semantic Chain

These standards form a **layered continuum of financial and business information**, spanning:

```
GOVERNANCE → WORKFLOW → TRANSACTION EXECUTION → COMPLIANCE REPORTING → ANALYSIS
```

Rather than competing, they **operate at different levels of abstraction** across the economic lifecycle.

> *"All of these standards and frameworks form a single semantic supply chain for business meaning; from the moment a business event occurs, through operational processing, into accounting recognition, and finally into regulated financial compliance reporting."*

Charlie identifies **three broad groups** (though he acknowledges better groupings may exist):

| Group | Function |
|---|---|
| **Conceptual & Semantic Foundation** | Defining meaning, concepts, and rules |
| **Operational Processing** | Describing action, execution, payload |
| **Accounting, Reporting & Analysis** | Transacting, recording, aggregating, reporting |

---

## 🧠 LAYER 1: The Conceptual, Semantic and Logical Foundation

### SBVR — Semantics of Business Vocabulary and Business Rules

- **Standard:** OMG (Object Management Group)
- **Standard URL:** https://www.omg.org/spec/SBVR/1.5/About-SBVR/
- **Role:** Provides **formal grounding** for the entire stack.
- **Function:** Provides a formal, language-independent way to define business terms and rules.

**What SBVR can describe:**

- The meaning of UBL document elements
- ISO accounting and economic concepts
- REA economic constructs
- XBRL Global Ledger contents
- XBRL Digital Financial Reporting contents
- ACTUS contract types
- Compliance reporting and analysis concepts

> *"SBVR is effectively the glue that ensures all layers share a consistent vocabulary and rule base; it supports the other standards/frameworks."*

**Relation to Seattle Method concepts:**

- [Conceptualization](https://seattlemethod.blogspot.com/2025/09/conceptualization.html)
- [Governance](https://seattlemethod.blogspot.com/2026/01/governance.html)
- [Epistemic Risk](https://seattlemethod.blogspot.com/2026/01/epistemic-risk.html)

---

### BPMN — Business Process Model and Notation

- **Standard:** OMG
- **Standard URL:** https://www.omg.org/bpmn/
- **Role:** Represents business workflows through which *business event* information travels.
- **Complementary to SBVR:** BPMN relates to **temporal and workflow dynamics** — the *when* and *how* information flows, while SBVR defines the *what it means*.

---

## ⚙️ LAYER 2: The Operational Workflow and Document Layer

### UBL — Universal Business Language

- **Standard:** ISO/IEC (Standard: https://www.iso.org/standard/66370.html)
- **Role:** The **natively semantic source document**.
- **Documents produced:** Orders, invoices, dispatch advices, etc.

**What UBL provides:**

- Describes real-world commercial interactions
- Carries granular facts about **"who did what, when, and why"**
- Forms the raw material for business events and financial transactions
- **Preserves meaning** as the event moves through operational steps

**Relation to Seattle Method concepts:**

- [Traceability/Trackability](https://seattlemethod.blogspot.com/2025/12/traceability.html)
- [Provenance](https://seattlemethod.blogspot.com/2026/02/provenance.html)

---

### ACTUS — Algorithmic Contract Types Unified Standards

- **Status:** On path to become ISO/IEC standard
- **URL:** https://www.actusfrf.org/
- **Role:** Specialized role for **financial contracts** (a type of business contract).
- **Difference from UBL:** Instead of static documents like invoices, ACTUS models the **deterministic state machine** of financial contracts.

**What ACTUS models:**

- Loans, derivatives, bonds
- Discrete future cash-flow events based on contractual terms and market triggers
- The financial institution is one side of the contract; the enterprise seeking financing is the other

**Unique capability:** ACTUS enables a **projection of the financial contract algorithm** — allowing **business events to be forecast far into the future**.

---

## 📊 LAYER 3: The Accounting & Aggregation Layer

### REA — Resources, Events, Agents (via ISO/IEC Accounting and Economic Ontology)

- **Standard:** ISO/IEC (Standard: https://www.iso.org/standard/67199.html)
- **Wikipedia:** https://en.wikipedia.org/wiki/Resources,_Events,_Agents
- **Role:** **Semantic interpretation** of UBL documents as economic events.
- **Function:** Provides the ontological framework that gives accounting meaning to operational documents.

**In the semantic pipeline:**

```
UBL captures the document → REA interprets it as an economic event
```

---

### XBRL GL — XBRL Global Ledger

- **Standard URL:** https://www.xbrl.org/the-standard/what/global-ledger/
- **Role:** The **universal audit trail** and internal reporting standard.
- **Function:** Acts as the immutable bridge between operations and reports.

**What XBRL GL ingests:**

- Transactional events from UBL invoices
- ACTUS cash flows
- ERP systems

**What it provides:**

- Transaction/journal-level representation
- **Full structural provenance** linking back to the originating operational event
- The foundation for mapping to compliance reports

> *"XBRL GL acts as the universal audit trail and internal reporting standard."*

---

### XBRL (Financial Reporting) + FASB US GAAP / IFRS Taxonomies

- **URLs:**
  - FASB US GAAP: https://www.fasb.org/projects/fasb-taxonomies
  - IFRS Taxonomy: https://www.ifrs.org/issued-standards/ifrs-taxonomy/#annual-taxonomies
  - What is XBRL: https://www.xbrl.org/the-standard/what/what-is-xbrl/
- **Role:** The top of the reporting pipeline — **external regulatory compliance reporting**.

**The complete flow:**

```
UBL Documents
    → XBRL GL journal entries
        → Aggregation per US GAAP / IFRS
            → Mapping to official XBRL Taxonomies
                → External financial statements and regulatory filings
```

**What the taxonomies report:** The "state" and "changes in state" of an economic entity, organized per the standard reporting framework expressed through the reporting taxonomy.

---

## 🔗 The Complete Semantic Pipeline: "One Semantic Pipeline"

The central conclusion of the post:

```
UBL              → Captures the documents
REA              → Interprets them as economic events
ACTUS            → Models the contractual behavior of financial instruments
US GAAP / IFRS   → Reports the aggregated results
SBVR             → Defines the shared vocabulary and rules
BPMN             → Orchestrates the processes that generate and consume all of the above
```

> *"Together, they form a coherent, end-to-end semantic architecture for representing business activity; from operational transactions to regulated financial compliance reporting and analysis of information; **without losing meaning along the way**."*

---

## 🪝 The Copper Plumbing Metaphor

Charlie uses a metaphor from the film *Moonstruck* (Cosmo Castorini, a plumber):

> *"... Then there is copper. It costs money. It costs money. Because it saves money."*

Applied to accounting system architecture:

> *"When I build my accounting information systems, I use the equivalent of copper 'plumbing'. The initial investment to do it right is higher; but things work better, the quality is higher, and things last significantly longer."*

But the argument has moved beyond the benefits of a well-functioning accounting system:

> *"The real value is the opportunity to maximize the benefit and utility of artificial intelligence."*

---

## ⚠️ The Sins of Self-Inflicted Complexity

Charlie concludes with a list of problems that are **self-inflicted** (and therefore avoidable):

| Problem | Characterization | Reference |
|---|---|---|
| Accidental complexity | Self-inflicted | — |
| Kludge | Self-inflicted | https://digitalfinancialreporting.blogspot.com/2025/10/no-kludge.html |
| Physical fragmentation | Self-inflicted | https://digitalfinancialreporting.blogspot.com/2026/06/fragmentation-and-defensible-compliance.html |
| Semantic fragmentation | Self-inflicted | https://digitalfinancialreporting.blogspot.com/2026/06/fragmentation-and-defensible-compliance.html |
| The "hairball" | Self-inflicted | https://digitalfinancialreporting.blogspot.com/2024/03/creeping-normality-integration-hairball.html |

> *"And, if your current accounting information is a hairball [...] and then you go through a transformation and things are not much better on the other end; the only thing you will have achieved is waste your hard earned money."*

---

## 🗂️ Complete Taxonomy of Standards Mentioned

| Standard | Body | Status | Layer | Role in the Pipeline |
|---|---|---|---|---|
| **SBVR** | OMG | Ratified (v1.5) | Conceptual | Vocabulary and rules — the glue |
| **BPMN** | OMG | Ratified | Conceptual | Workflow orchestration |
| **UBL** | ISO/IEC | Ratified (66370) | Operational | Natively semantic source documents |
| **REA** | ISO/IEC | Ratified (67199) | Semantic | Economic events ontology |
| **ACTUS** | ACTUS FRF | On path to ISO | Operational | Deterministic financial contracts |
| **XBRL GL** | XBRL International | Ratified | Accounting | Universal ledger / audit trail |
| **XBRL (Financial Reporting)** | XBRL International | Ratified | Reporting | External compliance reporting |
| **FASB US GAAP Taxonomy** | FASB | Current | Reporting | US GAAP framework for XBRL |
| **IFRS Taxonomy** | IFRS Foundation | Current | Reporting | IFRS framework for XBRL |

---

## 🔗 Additional Resources Referenced

### Seattle Method Blog Posts

- [Accounting & Audit by Design (A&AD) Framework](https://seattlemethod.blogspot.com/2026/07/accounting-audit-by-design-framework.html)
- [Knowledge as a Product](https://seattlemethod.blogspot.com/2026/07/knowledge-as-product.html)
- [The Accounting Manifold](https://seattlemethod.blogspot.com/2026/07/the-accounting-manifold.html)
- [Ledger](https://seattlemethod.blogspot.com/2026/06/ledger.html)
- [Theory of the Financial Reporting Framework](https://seattlemethod.blogspot.com/2026/06/theory-of-financial-reporting-framework.html)
- [Metatheory](https://seattlemethod.blogspot.com/2026/06/metatheory.html)
- [My Garden](https://seattlemethod.blogspot.com/2026/06/my-garden.html) *(fenced boundary)*
- [Professional Oriented Knowledge Framework](https://seattlemethod.blogspot.com/2026/05/professional-oriented-knowledge.html)
- [Digital Information Organism](https://seattlemethod.blogspot.com/2026/05/digital-information-organism.html)

### Digital Financial Reporting Blog Posts

- [Modern Version of Ricordanze](https://digitalfinancialreporting.blogspot.com/2026/07/modern-version-of-ricordanze.html)
- [Work System](https://digitalfinancialreporting.blogspot.com/2026/07/work-system.html)
- [Platforms and Ecosystems](https://digitalfinancialreporting.blogspot.com/2026/07/platforms-and-ecosystems.html)
- [Agentic AI](https://digitalfinancialreporting.blogspot.com/2026/07/agentic-ai.html)
- [Modeling Against the Stream](https://digitalfinancialreporting.blogspot.com/2026/06/modeling-against-the-stream.html)
- [Universal Business Language](https://digitalfinancialreporting.blogspot.com/2026/07/universal-business-language.html)

### Academic and Standards Resources

- [Using Natural Language and SBVR to Author Unambiguous Business Governance Documents](https://www.businesssemantics.com/UsingNaturalLanguageAndSBVRToAuthorUnambiguousBusinessGovernanceDocuments\(DonaldChapinAndJohn%20Hall\).pdf) — Donald Chapin & John Hall
- [The Semantics of Business Vocabulary and Business Rules: An Automatic Generation From Textual Statements](https://ieeexplore.ieee.org/document/9398685) — IEEE Xplore
- [Business Rules Community](https://www.brcommunity.com/authors.php?id=rosr)
- [SBVR: Ten Years and Still Ahead of Its Time!](https://www.brcommunity.com/articles.php?id=b933)

---

## 💡 Notes for the DFRNT / AI2Accountans Project

### Alignment with the pipeline already built

The `UBL → XBRL GL → JSON-LD` pipeline demonstrated in `UBL2XBRLGL_CSV.zip` maps directly onto the architecture Charlie describes:

```
UBL  (Operational Layer)
  → XBRL GL  (Accounting Layer — "immutable bridge")
    → JSON-LD / Knowledge Graph  (semantic projection = XBRL OIM)
```

### The missing layer: where is the accounting semantics?

Joey asked: *"Where do you anchor the accounting semantics?"* — Charlie answers implicitly here: it is **REA (ISO/IEC 67199)** that interprets UBL documents as economic events. The accounting semantics (which accounts, debit/credit treatment, accrual timing) come from REA, not from UBL itself.

### SBVR as the bridge between the two tribes

The role of SBVR as the "glue" of all layers connects directly to the image from the July 26 mail:

> *"The vision of SBVR has always been to enable the people who manage and run an organization to be able to express their business policies, business rules, and other governance documentation unambiguously using the same natural language and vocabulary they use every day to communicate with each other — in a standards-based, machine-readable format that has an interpretation in formal logic."*

SBVR is the formal bridge between:
- 👔 **Business People** → define rules in natural language
- 🛠️ **Technical People** → implement those rules in formal systems

---

*Document extracted and structured: July 26, 2026*
