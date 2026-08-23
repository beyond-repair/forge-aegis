<div align="center">

# 🛡️ forge-aegis

## Stop asking “is it malware?”
## Start asking **“what changed — and can I prove it?”**

[![ACTIVE](https://img.shields.io/badge/●_ACTIVE-22c55e?style=for-the-badge)](https://github.com/beyond-repair/forge-aegis)
[![v0.1](https://img.shields.io/badge/v0.1_SLICE-LIVE-0ea5e9?style=for-the-badge)](docs/V0_1_VERTICAL_SLICE.md)
[![CI](https://img.shields.io/github/actions/workflow/status/beyond-repair/forge-aegis/ci.yml?style=for-the-badge)](https://github.com/beyond-repair/forge-aegis/actions)

**Deterministic. Offline. Auditable.**  
Host state in → evidence → policy → **PASS / FAIL / INCONCLUSIVE** → hash-stable audit out.

</div>

---

## The pitch

Antivirus theater is a guessing game.  
**forge-aegis** is a **measurement engine**:

1. Hash what matters on disk  
2. Compare to a baseline policy you control  
3. Emit a result you can recompute tomorrow  

Same inputs → **same `result_hash`**. That's the product.

```bash
python python/aegis_pipeline.py \
  --host ./my_host_tree \
  --policy examples/policy_example.json \
  --audit-dir ./aegis_audit
```

```text
Host → Evidence → FLS policy → Validator → Audit record
```

---

## Built for Nehemiah — not instead of it

```text
forge-aegis     = contract authority (this repo)
AEGIS-Nehemiah  = live host collection (consumes the contract)
```

No network in the pipeline. No auto-wipe fantasy in v0.1.  
Just a vertical slice you can **trust enough to integrate against**.

---

<div align="center">

### ⭐ Integrity without theater. Star it if you're done with black boxes.

[Atomic Dream Labs](https://github.com/beyond-repair) · [Release gate](docs/RELEASE_GATE_v0.1.md)

</div>
