# forge-aegis

Offline reference pipeline for the Forge Language Specification (FLS) / AEGIS v0.1 vertical slice (Project Nehemiah).

Given a directory and a baseline policy, it hashes the files, compares digests, and writes an audit record. The same file bytes and the same policy produce the same `result_hash` on any path. It does not use the network, does not execute host files, and does not change the host.

This is **not** a full endpoint agent, a Forge language compiler, or a Nehemiah host. Documents under `fls/` are draft specification. The runnable product is the Python slice below.

## Requirements

- Python 3.10 or newer
- No third-party packages for running or testing

## Install

From a clone of this repository:

```bash
python -m pip install -e .
```

That installs the `forge-aegis` command. You can skip the install and call the module directly, as the examples below do.

## Configure

Baseline a directory you already trust. This writes policy JSON; it does not modify the directory.

```bash
python python/aegis_pipeline.py \
  --host examples/demo_host \
  --emit-policy ./baseline.json \
  --baseline-id demo-001
```

Add `--strict-inventory` if extra files should fail closed later. Artifact ids are paths relative to `--host`, with forward slashes.

`examples/policy_example.json` is a checked-in baseline for `examples/demo_host` (`strict_inventory: true`). The reference shape is also in `schemas/aegis.fls.v0.1.schema.json` (not fetched at runtime).

## Run

```bash
python python/aegis_pipeline.py \
  --host examples/demo_host \
  --policy examples/policy_example.json \
  --audit-dir ./aegis_audit
```

After install, the same flags work as `forge-aegis`.

Exit codes: `0` PASS, `2` FAIL or a missing host/policy path, `3` INCONCLUSIVE (malformed policy).

A passing run prints JSON with `result.status`, `result.result_hash`, and `audit` (a file `aegis_audit/audit_<hash>.json`). `evidence_hash` and `result_hash` ignore the absolute host path and the timestamps. The audit record still stores `evidence_root` so an operator can see where the measurement ran.

Repeat the command. `result_hash` does not change. To see a failure, copy the demo tree, edit a file, and point `--host` at the copy. Expect exit code 2 and a `DIGEST_MISMATCH` finding.

Limit measurement to named files with repeatable `--only RELATIVE/PATH`.

Check a graph document's required keys without measuring a tree:

```bash
python python/aegis_validator.py examples/policy_example.json
```

## Test

```bash
python python/tests/test_validator.py
python python/tests/test_pipeline.py
```

`test_validator.py` prints `2 passed`. `test_pipeline.py` prints `8 passed`. If pytest is installed, `pytest -q` collects the same tests (`pythonpath` is set in `pyproject.toml`).

## What v0.1 does not do

- Network fetches, remote attestation, or signed baselines
- Auto-remediation or rollback
- Kernel or live host agents
- Executing a Forge language
- Integration with sovereign-clean-room

See `docs/V0_1_VERTICAL_SLICE.md` and `docs/THREAT_MODEL.md`.
