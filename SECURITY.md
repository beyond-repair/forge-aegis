# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| v0.1 (vertical slice) | Yes |
| pre-v0.1 | No |

## Reporting a Vulnerability

Do **not** open a public issue for security-sensitive reports.

Contact the repository owner (`beyond-repair`) via private channel. Include:
- Affected component / path
- Reproduction steps (if safe)
- Impact assessment
- Suggested mitigation (optional)

## Design Invariants (non-negotiable)

1. **Offline contract**: Core pipeline and validator operate without network access. No outbound calls in measurement or verification paths.
2. **Deterministic integrity**: Same host tree + same policy → same `result_hash`. Hash construction is pure and reproducible.
3. **Fail-closed on mismatch**: Tamper or policy violation yields non-zero exit (code 2) and does not produce a valid anchor.
4. **No untrusted code execution**: The Python reference implementation measures files and digests; it does not execute host content.
5. **Policy as data**: Policies are JSON artifacts validated against the FLS schema surface; no dynamic code evaluation from policy.

## Dependency Policy

- Minimal surface: standard library + pure Python for the v0.1 reference pipeline.
- No third-party runtime dependencies required for core measurement/validation.
- CI runs unit tests and CLI smoke (PASS + FAIL paths) on every push/PR to main.

## Known Non-Goals

- This repository provides the Forge Language Specification (FLS) and a reference AEGIS pipeline; it is not a full production endpoint agent.
- Host isolation, privilege separation, and multi-tenant deployment hardening are out of scope for the v0.1 vertical slice.
- Cryptographic signing of baselines and remote attestation are planned beyond the current slice.

## Threat Model Summary

See `docs/THREAT_MODEL.md` for the documented threat model. Primary concern for the reference implementation is integrity of the measurement itself (correct digests, correct policy matching) under offline conditions.
