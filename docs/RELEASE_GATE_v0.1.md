# Release Gate — forge-aegis v0.1.0

Tag only when every box is checked.

## Functional

- [x] Evidence collection
- [x] Policy loading (`aegis.fls.v0.1`)
- [x] Deterministic validation (`result_hash`)
- [x] PASS / FAIL / INCONCLUSIVE
- [x] Tamper → DIGEST_MISMATCH
- [x] Audit records
- [x] CLI
- [x] Local tests (`test_pipeline.py`, `test_validator.py`)

## Hardening

- [ ] GitHub Actions CI green on `main`
- [ ] README matches v0.1 scope (offline validation engine, not full host platform)
- [ ] `docs/V0_1_VERTICAL_SLICE.md` matches code
- [ ] Example policy path documented
- [ ] No network dependency in pipeline
- [ ] No auto-remediation code paths
- [ ] No unsupported security marketing claims

## Operator release

```bash
git checkout main && git pull
# confirm CI green
git tag -a v0.1.0 -m "forge-aegis v0.1.0 deterministic validation vertical slice"
git push origin v0.1.0
```

## Explicit non-goals of this tag

Live Nehemiah collection · advanced policy DSL · auto-restore · cloud · distributed agents
