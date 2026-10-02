# forge-aegis v0.1 Vertical Slice

**Status:** reference implementation for the offline integrity slice. Not a full host platform and not an FLS compiler.

## Invariant

> Given the same file bytes (relative paths) and the same FLS policy, forge-aegis produces the same `result_hash`.

The absolute directory path is recorded as `evidence_root` on the audit record and is **not** an input to `evidence_hash` or `result_hash`. Timestamps (`collected_at`, `recorded_at`) are also excluded from those hashes.

`evidence_hash` is SHA-256 over canonical JSON of the artifact list (`id`, `kind`, `digest`, `present`, `size`).

`result_hash` is SHA-256 over canonical JSON of `status`, `baseline_id`, `findings`, `evidence_hash`, and `policy_hash`.

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

Configuring a baseline is separate: `--emit-policy` writes a policy from a trusted directory and exits. It does not validate.

## CLI

```bash
python python/aegis_pipeline.py --host examples/demo_host --emit-policy ./baseline.json --baseline-id demo-001
python python/aegis_pipeline.py --host examples/demo_host --policy examples/policy_example.json --audit-dir ./aegis_audit
```

Exit codes: `0` PASS · `2` FAIL (or missing path) · `3` INCONCLUSIVE

## Tests

```bash
python python/tests/test_validator.py
python python/tests/test_pipeline.py
```

## Explicitly out of scope for v0.1

- Network fetches
- Auto-remediation / rollback execution
- Kernel drivers / WMI live agents
- Integration with sovereign-clean-room (optional later one-way attestation only)
- A Forge language implementation

## Nehemiah integration surface

Consume `ValidationResult.to_dict()` and audit JSON; do not re-implement hashing rules.
