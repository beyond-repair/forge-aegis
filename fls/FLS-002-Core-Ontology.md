# FLS-002: Core Ontology

Status: Draft Baseline
Version: FLS-0
Category: Technical Specification
Normative Level: Level A

## 1. Purpose
This document defines the normative Forge Core Ontology.

## 2. Normative Requirements

### FLS-002-ONT-001 (Artifact)
An Artifact is the fundamental semantic unit of Forge. Every value participating in Forge computation SHALL be represented as an Artifact.

### FLS-002-ONT-002 (Identity)
An Identity SHALL uniquely represent an immutable, persistent, logical reference to an Artifact.

### FLS-002-ONT-003 (Revision)
A Revision SHALL represent an immutable historical state of an Artifact. A Revision SHALL NOT alter the Identity of an Artifact.

### FLS-002-ONT-004 (Relationship)
A Relationship SHALL be a typed, directed association between two Artifacts. Its semantic meaning SHALL derive from its Kind and its source and target endpoints.

### FLS-002-ONT-005 (Property)
A Property SHALL be a deterministic, serializable semantic value. Properties SHALL NOT encode architectural relationships.

### FLS-002-ONT-006 (Locator)
A Locator SHALL identify a retrieval location for an Artifact or Revision. A Locator MAY become invalid without affecting the referenced Identity.

### FLS-002-ONT-007 (Annotation)
An Annotation SHALL be semantic-neutral metadata. Annotations SHALL NOT affect transformation results or proof obligations.

### FLS-002-ONT-008 (Kind)
A Kind SHALL classify the semantic role of an Artifact or Relationship. The Forge Core defines a minimal set of standard Kinds. Packages MAY define additional Kinds.

### FLS-002-ONT-900 (Ontology Stability)
The Forge Core Ontology is intentionally minimal. New ontology primitives SHALL NOT be introduced except through the Forge RFC process. New concepts SHOULD be expressed as Artifact Kinds.
