# ADR-001: Primary Representation

Status: Accepted (Draft Baseline)

## Decision
Forge adopts the Artifact Graph as its primary semantic representation.

## Rationale
The Artifact Graph provides a stable semantic representation independent of parser, syntax, backend, or implementation language. ASTs are parser-specific; the Artifact Graph is language-semantic and forms the basis for validation, transformation, proof generation, canonical representation, and conformance.
