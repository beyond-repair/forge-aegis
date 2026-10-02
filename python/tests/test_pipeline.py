#!/usr/bin/env python3
"""Offline tests for aegis_pipeline vertical slice."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT))

from aegis_pipeline import (  # noqa: E402
    collect_evidence,
    load_policy,
    main,
    policy_from_host,
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
        record = json.loads(audit1.read_text(encoding="utf-8"))
        assert record["result"]["result_hash"] == r1.result_hash
        assert record["network_access"] is False

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


def test_result_hash_ignores_absolute_path():
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        contents = {"a.txt": "alpha\n", "sub/b.txt": "beta\n"}
        hosts = []
        for name in ("tree-one", "nested/tree-two"):
            host = td / name
            for rel, text in contents.items():
                _write(host / rel, text)
            hosts.append(host)
        policy_doc = policy_from_host(hosts[0], baseline_id="path-indep")
        policy_path = td / "policy.json"
        policy_path.write_text(json.dumps(policy_doc), encoding="utf-8")
        r1, _ = run_pipeline(hosts[0], policy_path, td / "a1")
        r2, _ = run_pipeline(hosts[1], policy_path, td / "a2")
        assert r1.status == "PASS" and r2.status == "PASS"
        assert r1.evidence_hash == r2.evidence_hash
        assert r1.result_hash == r2.result_hash
        assert str(hosts[0].resolve()) != str(hosts[1].resolve())


def test_strict_inventory_unexpected():
    with tempfile.TemporaryDirectory() as td:
        host = Path(td) / "host"
        _write(host / "a.txt", "alpha")
        _write(host / "extra.txt", "nope")
        evidence = collect_evidence(host)
        digest = next(a["digest"] for a in evidence["artifacts"] if a["id"] == "a.txt")
        policy = {
            "schema": "aegis.fls.v0.1",
            "baseline_id": "strict",
            "strict_inventory": True,
            "artifacts": [{"id": "a.txt", "kind": "file", "digest": digest}],
        }
        result = validate_against_policy(evidence, policy)
        assert result.status == "FAIL"
        assert any(f["code"] == "UNEXPECTED" and f["artifact_id"] == "extra.txt" for f in result.findings)


def test_malformed_policy_inconclusive():
    with tempfile.TemporaryDirectory() as td:
        host = Path(td) / "host"
        _write(host / "a.txt", "alpha")
        evidence = collect_evidence(host)
        policy = {
            "schema": "aegis.fls.v0.1",
            "baseline_id": "bad",
            "artifacts": [{"kind": "file", "digest": "abc"}],
        }
        result = validate_against_policy(evidence, policy)
        assert result.status == "INCONCLUSIVE"
        assert result.result_hash


def test_emit_policy_round_trip():
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        host = td / "host"
        _write(host / "config/app.conf", "name=demo\n")
        out = td / "baseline.json"
        code = main(
            [
                "--host",
                str(host),
                "--emit-policy",
                str(out),
                "--baseline-id",
                "round",
                "--strict-inventory",
            ]
        )
        assert code == 0
        doc = load_policy(out)
        assert doc["baseline_id"] == "round"
        assert doc["strict_inventory"] is True
        assert doc["artifacts"][0]["id"] == "config/app.conf"
        result, _ = run_pipeline(host, out, td / "audit")
        assert result.status == "PASS"


def test_checked_in_demo_host_passes():
    with tempfile.TemporaryDirectory() as td:
        result, audit = run_pipeline(
            REPO / "examples" / "demo_host",
            REPO / "examples" / "policy_example.json",
            Path(td) / "audit",
        )
        assert result.status == "PASS", result.explanation
        assert audit.is_file()


def test_cli_exit_codes():
    script = ROOT / "aegis_pipeline.py"
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        host = td / "host"
        _write(host / "a.txt", "alpha")
        policy = td / "policy.json"
        code = main(
            ["--host", str(host), "--emit-policy", str(policy), "--baseline-id", "cli"]
        )
        assert code == 0
        proc = subprocess.run(
            [sys.executable, str(script), "--host", str(host), "--policy", str(policy), "--audit-dir", str(td / "audit")],
            capture_output=True,
            text=True,
            check=False,
        )
        assert proc.returncode == 0, proc.stderr
        _write(host / "a.txt", "tampered")
        proc = subprocess.run(
            [sys.executable, str(script), "--host", str(host), "--policy", str(policy), "--audit-dir", str(td / "audit2")],
            capture_output=True,
            text=True,
            check=False,
        )
        assert proc.returncode == 2, proc.stdout
        missing = main(["--host", str(td / "missing"), "--policy", str(policy)])
        assert missing == 2
        bad = td / "bad.json"
        bad.write_text("{", encoding="utf-8")
        assert main(["--host", str(host), "--policy", str(bad)]) == 3


def _run_all() -> int:
    tests = [
        test_pass_and_fail_and_deterministic,
        test_missing_artifact,
        test_result_hash_ignores_absolute_path,
        test_strict_inventory_unexpected,
        test_malformed_policy_inconclusive,
        test_emit_policy_round_trip,
        test_checked_in_demo_host_passes,
        test_cli_exit_codes,
    ]
    for fn in tests:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"{len(tests)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
