#!/usr/bin/env python3
"""Offline tests for aegis_pipeline vertical slice."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from aegis_pipeline import (  # noqa: E402
    collect_evidence,
    load_policy,
    run_pipeline,
    validate_against_policy,
)


def _write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def test_pass_and_fail_and_deterministic():
    with tempfile.TemporaryDirectory() as td:
        host = Path(td) / "host"
        _write(host / "a.txt", "alpha")
        _write(host / "b.txt", "beta")

        evidence = collect_evidence(host)
        digests = {a["id"]: a["digest"] for a in evidence["artifacts"]}

        policy_path = Path(td) / "policy.json"
        policy = {
            "schema": "aegis.fls.v0.1",
            "baseline_id": "bl-test",
            "artifacts": [
                {"id": "a.txt", "kind": "file", "digest": digests["a.txt"]},
                {"id": "b.txt", "kind": "file", "digest": digests["b.txt"]},
            ],
        }
        policy_path.write_text(json.dumps(policy), encoding="utf-8")

        r1, audit1 = run_pipeline(host, policy_path, Path(td) / "audit")
        r2, _ = run_pipeline(host, policy_path, Path(td) / "audit2")
        assert r1.status == "PASS"
        assert r1.result_hash == r2.result_hash
        assert audit1.is_file()

        # Tamper
        _write(host / "a.txt", "TAMPERED")
        r3, _ = run_pipeline(host, policy_path, Path(td) / "audit3")
        assert r3.status == "FAIL"
        assert any(f["code"] == "DIGEST_MISMATCH" for f in r3.findings)


def test_missing_artifact():
    with tempfile.TemporaryDirectory() as td:
        host = Path(td) / "host"
        _write(host / "only.txt", "x")
        evidence = collect_evidence(host)
        policy = {
            "schema": "aegis.fls.v0.1",
            "baseline_id": "bl-miss",
            "artifacts": [
                {
                    "id": "gone.txt",
                    "kind": "file",
                    "digest": "0" * 64,
                }
            ],
        }
        result = validate_against_policy(evidence, policy)
        assert result.status == "FAIL"
        assert any(f["code"] == "MISSING" for f in result.findings)


if __name__ == "__main__":
    test_pass_and_fail_and_deterministic()
    test_missing_artifact()
    print("ok")
