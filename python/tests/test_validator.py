#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from aegis_validator import validate_graph  # noqa: E402


def test_ok():
    ok, errs = validate_graph(
        {
            "schema": "aegis.artifact_graph.v0.1",
            "baseline_id": "bl-1",
            "artifacts": [{"id": "a1", "kind": "file", "digest": "abc"}],
        }
    )
    assert ok and not errs


def test_missing():
    ok, errs = validate_graph({"schema": "x"})
    assert not ok and errs


def _run_all() -> int:
    tests = [test_ok, test_missing]
    for fn in tests:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"{len(tests)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
