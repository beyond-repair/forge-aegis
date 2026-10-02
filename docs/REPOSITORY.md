# Repository Structure

This repository hosts the Forge Language Specification (FLS) drafts and the AEGIS v0.1 reference pipeline for Project Nehemiah.

## Layout

```
.
├── README.md                 # Install, configure, run, test
├── pyproject.toml            # Zero-dependency package; console script forge-aegis
├── python/                   # Reference implementation (stdlib only)
│   ├── aegis_pipeline.py
│   ├── aegis_validator.py
│   └── tests/
├── examples/                 # demo_host + matching policy_example.json
├── schemas/                  # v0.1 reference JSON Schema (not fetched at runtime)
├── fls/                      # Draft Forge Language Specifications (not executable)
├── adr/                      # Architecture Decision Records
├── rfc/                      # Request for Comments (change proposals)
├── docs/                     # Slice contract, threat model, release gate
├── GOVERNANCE.md
├── CONTRIBUTING.md
├── EDITORIAL.md
├── SECURITY.md
└── LICENSE                   # License TBD
```

## Branching Model (Recommended)

- `main` — Accepted baseline (FLS-0 draft + v0.1 Python slice)
- `draft/*` — Work-in-progress FLS or RFC branches
- Tags — Used for formal FLS maturity releases

## Change Process

1. Open an RFC using the template in `rfc/RFC-TEMPLATE.md`.
2. Discussion and review.
3. Accepted RFCs are merged into the appropriate FLS documents.
4. Specification always takes precedence over any reference implementation.
