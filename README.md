<div align="center">

# forge-aegis

### Project Nehemiah · AEGIS integrity engine

**Measure · Prove · Decide** — offline host integrity without the malware guessing game

[![Status](https://img.shields.io/badge/status-ACTIVE-22c55e?style=for-the-badge)](https://github.com/beyond-repair/forge-aegis)
[![Slice](https://img.shields.io/badge/v0.1-vertical%20slice-0ea5e9?style=for-the-badge)](docs/V0_1_VERTICAL_SLICE.md)
[![CI](https://img.shields.io/github/actions/workflow/status/beyond-repair/forge-aegis/ci.yml?style=for-the-badge&label=CI)](https://github.com/beyond-repair/forge-aegis/actions)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](python/aegis_pipeline.py)

</div>

---

## Philosophy

Traditional tools ask: *“Is this malicious?”*  
**AEGIS asks:**

> What changed? · Can I prove it? · Is it authorized? · Does the baseline still hold?

---

## v0.1 vertical slice

```text
  Host tree
      │
      ▼
  Evidence (SHA-256 digests)
      │
      ▼
  FLS policy (baseline)
      │
      ▼
  Validator  →  PASS | FAIL | INCONCLUSIVE
      │
      ▼
  Audit record (deterministic result_hash)
```

**Invariant:** same host evidence + same policy → same `result_hash`.

```bash
python python/aegis_pipeline.py \
  --host ./my_host_tree \
  --policy examples/policy_example.json \
  --audit-dir ./aegis_audit
```

Exit codes: `0` PASS · `2` FAIL · `3` INCONCLUSIVE

---

## Tests & release gate

```bash
python python/tests/test_pipeline.py
python python/tests/test_validator.py
```

| Doc | Role |
|-----|------|
| [V0_1_VERTICAL_SLICE.md](docs/V0_1_VERTICAL_SLICE.md) | Contract |
| [RELEASE_GATE_v0.1.md](docs/RELEASE_GATE_v0.1.md) | Tag checklist |
| [THREAT_MODEL.md](docs/THREAT_MODEL.md) | Threat model |

**Operator tag:** `v0.1.0` when CI is green (implementation frozen until then).

---

## Boundaries (v0.1)

| Does | Does not |
|------|----------|
| Offline measurement & audit | Network fetch |
| Deterministic PASS/FAIL | Auto-remediation |
| Contract for Nehemiah | Live host agent (Nehemiah’s job) |

```text
forge-aegis  ──contract──►  AEGIS-Nehemiah (live collection)
```

---

<div align="center">

**Atomic Dream Labs** · [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

<sub>Integrity first. Spec docs under `docs/`, `rfc/`, `fls/` guide what comes next.</sub>

</div>
