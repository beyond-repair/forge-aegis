<div align="center">

# 🛡️ forge-aegis

### Deterministic **integrity measurement** — offline contract for Nehemiah

[![ACTIVE](https://img.shields.io/badge/●_ACTIVE-22c55e?style=for-the-badge)](https://github.com/beyond-repair/forge-aegis)
[![v0.1](https://img.shields.io/badge/v0.1_SLICE-0ea5e9?style=for-the-badge)](docs/V0_1_VERTICAL_SLICE.md)
[![CI](https://img.shields.io/github/actions/workflow/status/beyond-repair/forge-aegis/ci.yml?style=for-the-badge)](https://github.com/beyond-repair/forge-aegis/actions)

</div>

---

## Why it is unique

Not a malware oracle. A **reproducible measurement engine**: same host tree + same policy → same `result_hash`. No network. No silent “AI said so.”

---

## Visual workflow

```text
  ┌─────────────┐
  │ 1. HOST     │  files / tree you point at
  └──────┬──────┘
         ▼
  ┌─────────────┐
  │ 2. EVIDENCE │  digests (SHA-256) of selected paths
  └──────┬──────┘
         ▼
  ┌─────────────┐
  │ 3. POLICY   │  FLS baseline — what “good” means
  └──────┬──────┘
         ▼
  ┌─────────────┐
  │ 4. VALIDATE │  compare evidence ↔ baseline
  └──────┬──────┘
         ▼
  ┌─────────────────────────────────────┐
  │ 5. RESULT  PASS | FAIL | INCONCLUSIVE │
  │    + deterministic result_hash        │
  └──────┬──────────────────────────────┘
         ▼
  ┌─────────────┐
  │ 6. AUDIT    │  written record you can recompute later
  └─────────────┘
```

### Step-by-step — how & why

| Step | How | Why |
|-----:|-----|-----|
| **1** | Point at a local host directory | Reality input — not a cloud feed |
| **2** | Hash artifacts into evidence | Tamper-evident snapshot |
| **3** | Load policy JSON (baseline) | You define “known good” |
| **4** | Deterministic compare | Same inputs → same verdict |
| **5** | Exit 0 / 2 / 3 | Machine-readable, CI-friendly |
| **6** | Write audit dir | Provenance without a SaaS SIEM |

```bash
python python/aegis_pipeline.py \
  --host ./my_host_tree \
  --policy examples/policy_example.json \
  --audit-dir ./aegis_audit
```

---

## How it works with the lab

```text
forge-aegis  ══contract authority══►  AEGIS-Project-Nehemiah-
     │                                    (live collection)
     │
     └── offline CLI / CI only in v0.1

Clean-Room may attest workspace integrity separately (JKillnHide).
BlockSwarm does not depend on this path.
```

---

<div align="center">

[Release gate](docs/RELEASE_GATE_v0.1.md) · [Atomic Dream Labs](https://github.com/beyond-repair)

</div>
