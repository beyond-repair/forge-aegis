# forge-aegis v0.1 Vertical Slice

**Status:** PRIMARY BUILD — implementation, not docs-only

## Invariant

> Given a defined host-state input and FLS policy, forge-aegis produces a **deterministic** validation result with machine-readable evidence and an auditable explanation.

## Pipeline

```text
Host directory
      ↓
collect_evidence()     → digests + evidence_hash
      ↓
load_policy()          → FLS JSON (aegis.fls.v0.1)
      ↓
validate_against_policy()
      ↓
ValidationResult       → PASS | FAIL | INCONCLUSIVE
      ↓
write_audit_record()   → audit_<hash>.json
```

## CLI

```bash
cd python
python aegis_pipeline.py --host /path/to/tree --policy ../examples/policy_example.json --audit-dir ./audit
```

Exit codes: `0` PASS · `2` FAIL · `3` INCONCLUSIVE

## Tests

```bash
python python/tests/test_pipeline.py
python python/tests/test_validator.py
```

## Explicitly out of scope for v0.1

- Network fetches
- Auto-remediation / rollback execution
- Kernel drivers / WMI live agents
- Integration with sovereign-clean-room (optional later one-way attestation only)

## Nehemiah integration surface

Consume `ValidationResult.to_dict()` and audit JSON; do not re-implement hashing rules.
