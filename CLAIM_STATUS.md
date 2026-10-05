# Claim status

**Sweep:** 221 (2026-10-04)
**Classification:** ACTIVE
**Claim level:** software / RUNNABLE SKETCH
**Pre-head:** `590ba108c93a2de04ed8f2390f68cf6353645b1c`

## Allowed claims

- Offline Python reference pipeline hashes a directory, compares digests to an FLS v0.1 baseline policy, and writes an audit record.
- Same file bytes and same policy produce the same `result_hash` independent of absolute host path (covered by `python/tests/test_pipeline.py`).
- Exit codes: `0` PASS, `2` FAIL or missing host/policy path, `3` INCONCLUSIVE (malformed policy).
- Documents under `fls/` are draft specification. Normative changes require an RFC.

## Not claimed

- Complete Nehemiah host integrity product
- Kernel agent, remote attestation, or auto-remediation
- Forge language compiler or execution of a Forge language
- Cryptographic signing of baselines
- Integration with `sovereign-clean-room`
- Validation of Coherence Drive, thrust, or any physical claim

## Evidence this sweep

- Local: `python3 python/tests/test_validator.py` (2 passed); `python3 python/tests/test_pipeline.py` (8 passed).
- Remote CI: workflow `forge-aegis CI` run 37065566958 success on pre-head `590ba108`. Post-push run 37257747973 success on `8083425d` (job test 111598348161; unit tests and CLI PASS/FAIL smokes success). Observed Sweep-222. Not a claim elevation.
- Dependabot open alerts: 0 at selection time.
- Releases API: empty. Tags API: empty. No tag created this sweep.

## Operator residuals

- `pyproject.toml` license text is `License TBD`. Not assigned here.
- Code scanning API was 404 on prior sweeps. Enabling it is operator-only.
- Non-default branches remain: `finish/forge-aegis-v0.1-runnable`, `repair/docs-python3-venv`, `repair/v0.1-installable-slice`. Not deleted.
