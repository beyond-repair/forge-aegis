# Threat Model — forge-aegis v0.1

## Assets

- Artifact Graph integrity (hashes, baseline IDs)
- Validation results used for host trust decisions

## Adversaries

1. Local malware altering files after measurement
2. Operator error (wrong baseline)
3. Supply-chain tampering of validator code

## Boundaries

- Validator is **offline**; no network fetch of schemas at runtime in v0.1
- Does **not** auto-remediate host state (AEGIS restore is separate, authorized)
- Does **not** depend on sovereign-clean-room

## Mitigations (v0.1)

- Explicit required fields for graph documents
- Deterministic JSON validation
- Versioned schema id string

## Out of scope (later)

- Remote attestation
- Kernel rootkits
- Side-channel resistance
