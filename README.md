# forge-aegis (Project Nehemiah / AEGIS)

**Status:** ACTIVE — Security line · **v0.1 vertical slice implemented**  
**Governance:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

Offline integrity measurement: measure host files → compare to FLS baseline → deterministic result → audit record.

## v0.1 pipeline

```text
Host/Input → Evidence → FLS Policy → Validator → Structured Result → Audit
```

```bash
python python/aegis_pipeline.py \
  --host ./my_host_tree \
  --policy examples/policy_example.json \
  --audit-dir ./aegis_audit
```

See [docs/V0_1_VERTICAL_SLICE.md](docs/V0_1_VERTICAL_SLICE.md).

## Tests

```bash
python python/tests/test_pipeline.py
python python/tests/test_validator.py
```

## Philosophy

Not “is this malware?” — **what changed, can I prove it, is it authorized, does baseline hold?**

## Boundaries

- No network in the pipeline
- No auto-restore in v0.1
- Spec docs under `docs/`, `rfc/`, `fls/` remain normative for future expansion

## License

See LICENSE.
