# FLS-003: Graph Semantics

Status: Draft Baseline
Version: FLS-0
Category: Technical Specification
Normative Level: Level A

## 0. Applicability
Defines the semantic rules governing valid Forge Artifact Graphs.

## 1. Purpose
Defines graph meaning independent of implementation.

# Part I — Semantic Objects

## 2. Artifact Graph
A Forge Artifact Graph consists of Artifacts and Relationships.

## 3. Vertices
Vertices are identified by Artifact Identity and Revision.

## 4. Relationships
Relationships are typed directed associations between endpoint identities.

# Part II — Semantic Rules

## 5. Identity
Artifact Identity SHALL be unique within a graph.

## 6. Reachability
Relationships SHALL be navigable through endpoint identities.

## 7. Integrity
Every Relationship SHALL reference existing Artifacts.

## 8. Extension
Graph extensions SHALL preserve graph validity.

# Part III — Validity

## 9. Valid Graph
A graph is valid iff schema validity, referential integrity, lifecycle consistency, proof obligations, and identity consistency are satisfied.

## 10. Structural Equivalence
Two graphs are structurally equivalent iff there exists an identity-preserving bijection over Artifacts and Relationships preserving Kind, endpoint identities, and semantic properties.

### Normative Invariants

FLS-003-GRF-001: Every Relationship SHALL reference existing Artifacts.
FLS-003-GRF-002: Artifact Identity SHALL be unique within a graph.
FLS-003-GRF-003: Relationship Kind SHALL determine semantic interpretation.
FLS-003-GRF-004: The graph SHALL satisfy referential integrity.
FLS-003-GRF-005: The graph SHALL satisfy lifecycle consistency.
FLS-003-GRF-006: Graph validity SHALL be independent of serialization.
FLS-003-GRF-007: No semantic information SHALL be derived from traversal order.
FLS-003-GRF-008: Graph validity SHALL be monotonic with respect to Annotation addition or removal.

## 11. Informative Examples
Non-normative examples are provided separately.
