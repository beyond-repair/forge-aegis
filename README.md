# Project Nehemiah: AEGIS

> **Repository Status**: Initialized as specification-first repository (FLS-0 Draft Baseline).  
> See [docs/REPOSITORY.md](docs/REPOSITORY.md) for layout, branching model, and change process.  
> Normative changes require an approved RFC (see `rfc/RFC-TEMPLATE.md` and GOVERNANCE.md).

## Overview

**Project Nehemiah** is a high-assurance integrity ecosystem designed to move beyond traditional reactive malware detection. By shifting the paradigm from *detecting malice* to *measuring integrity*, the platform provides a mathematically verifiable, evidence-backed framework for endpoint state management.

The system is powered by **Forge**, a domain-agnostic engineering platform, and implemented through **AEGIS** (*Adaptive Endpoint Guardian & Integrity System*), a specialized domain package that defines the ontology of a trusted computing environment.

---

## The Architecture

Nehemiah operates as an integrated state machine anchored by the **Graph**—the canonical data model for all system components and their relationships.

### The Foundational Subsystems

1. **Truth**: The raw acquisition layer; measures reality.
2. **Graph**: The canonical data model; represents reality as a verifiable state.
3. **Watchman**: Observes changes and anomalies against the established baseline.
4. **Wisdom**: Correlates observations to identify patterns and systemic context.
5. **Discernment**: Explains findings; provides evidence-based attribution.
6. **Memory**: Preserves state; maintains historical provenance and audit trails.
7. **Restoration**: Repairs state; executes minimal, evidence-backed rollbacks.
8. **Stewardship**: Schedules policy enforcement and lifecycle management.

---

## Forge: The Engineering Platform

**Forge** serves as the meta-engineering framework, providing the tools to define, verify, and generate the system. It is strictly decoupled from platform-specific internals (drivers, registries, etc.), focusing instead on:

* **Specifications**: Formal schemas for system artifacts.
* **Verification**: Proving conformance between actual state and defined baseline.
* **Generation**: Automated deployment of verifiable integrity policies.
* **Transformations**: Managing state changes within the Graph.

---

## AEGIS: The Domain Implementation

**AEGIS** is the first implementation of the Forge ontology. It specializes generic artifacts into domain-specific nodes and edges, including:

* **Hardware/Firmware**: `FirmwareArtifact`, `DriverArtifact`
* **System/Registry**: `RegistryArtifact`, `ServiceArtifact`, `ProcessArtifact`
* **Policy/Evidence**: `PolicyArtifact`, `ACLArtifact`, `IncidentArtifact`, `RollbackArtifact`

---

## Philosophy: Integrity-First

Traditional security asks: *"Is this malicious?"*
**Nehemiah asks:**

* *What changed?*
* *Can I prove the change?*
* *Is it authorized?*
* *Does it preserve the trusted baseline?*

If a change cannot be justified or proven against the trusted baseline, the system treats it as an integrity violation, enabling precise restoration to the last known good state.

---

## Implementation Status

* **Forge Platform**: Core ontology and meta-framework finalized.
* **AEGIS Ontology**: Defining domain-specific artifacts for endpoint integrity.
* **Subsystem Integration**: Currently aligning the eight foundational pillars with the Graph-based canonical model.

---

*This project is built on the principle of sovereign, verifiable system integrity. Architecture developed by William Brian Ware.*
