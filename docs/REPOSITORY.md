# Repository Structure

This repository hosts the Forge Language Specification (FLS) and the AEGIS domain package for Project Nehemiah.

## Layout

```
.
├── README.md                 # Project overview (Nehemiah / AEGIS)
├── GOVERNANCE.md             # Change control and RFC process
├── CONTRIBUTING.md           # Contribution guidelines
├── EDITORIAL.md              # Document style and identifier policy
├── LICENSE                   # License (currently TBD)
├── fls/                      # Normative Forge Language Specifications
├── adr/                      # Architecture Decision Records
├── rfc/                      # Request for Comments (change proposals)
├── schemas/                  # Derived schemas (generated from FLS prose)
├── docs/                     # Educational material, tutorials, examples
│   └── examples/
└── .gitignore
```

## Branching Model (Recommended)

- `main` — Accepted baseline (currently FLS-0 Draft)
- `draft/*` — Work-in-progress FLS or RFC branches
- Tags — Used for formal FLS maturity releases

## Change Process

1. Open an RFC using the template in `rfc/RFC-TEMPLATE.md`.
2. Discussion and review.
3. Accepted RFCs are merged into the appropriate FLS documents.
4. Specification always takes precedence over any reference implementation.
