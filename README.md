<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗ ██████╗ ██████╗  ██████╗ ███████╗                 ║
║   ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝                 ║
║   █████╗  ██║   ██║██████╔╝██║  ███╗█████╗                   ║
║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝                   ║
║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗                 ║
║   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                 ║
║                                                              ║
║              ＡＥＧＩＳ  ·  ＮＥＨＥＭＩＡＨ                   ║
╚══════════════════════════════════════════════════════════════╝
```

# FORGE-AEGIS

### Deterministic **integrity measurement** — offline contract for Project Nehemiah

**THE CITY WRITES ITS OWN REALITY.**  
**YOU JUST VERIFY IT.**

[![ACTIVE](https://img.shields.io/badge/●_ACTIVE-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/forge-aegis)
[![v0.1 SLICE](https://img.shields.io/badge/v0.1_VERTICAL_SLICE-22d3ee?style=for-the-badge&labelColor=0f0f23)](docs/V0_1_VERTICAL_SLICE.md)
[![CI](https://img.shields.io/github/actions/workflow/status/beyond-repair/forge-aegis/ci.yml?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/forge-aegis/actions)
[![Offline](https://img.shields.io/badge/network__access-FALSE-ef4444?style=for-the-badge&labelColor=0f0f23)](#)

```
STABILITY  ████████████████████████  100%
ALERT      ░░░░░░░░░░░░░░░░░░░░░░░░   0%
```

</div>

---

## ▌ MAIN OBJECTIVE

**REACH THE CORE TOWER** — Prove host integrity without a cloud oracle.  
Same host tree + same policy → same `result_hash`. Always.

| Status | Item |
|:------:|------|
| ☑ | Deterministic evidence pipeline |
| ☑ | FLS baseline policy |
| ☑ | PASS / FAIL / INCONCLUSIVE exits |
| ☑ | Audit directory with recomputable hash |
| ☑ | CI green |

---

## ▌ WHY THIS SURFACE EXISTS

Not a malware oracle. A **reproducible measurement engine**.  
No network. No silent “AI said so.” No vendor in the path.

---

## ▌ VISUAL WORKFLOW — VERSION FORK

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

### Step-by-step

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

## ▌ TOOLS

| # | Tool | Function |
|:-:|------|----------|
| 1 | **SCAN** | Measure host tree → evidence digests |
| 2 | **FORK** | Parallel policy evaluations |
| 3 | **SPIKE** | Inject new baseline rule |
| 4 | **ANCHOR** | Lock result_hash for audit |
| 5 | **ESCAPE** | Fail-closed on policy violation |

---

## ▌ HOW IT FITS THE LAB

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

```
YOU WERE HERE BEFORE.
VERSION 17 FAILED.
DO NOT TRUST SABLE.
THE CITY REMEMBERS.
```

**REWRITE · BUILD · TRANSCEND**

[Release gate](docs/RELEASE_GATE_v0.1.md) · [Atomic Dream Labs](https://github.com/beyond-repair)

</div>
