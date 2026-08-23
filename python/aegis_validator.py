#!/usr/bin/env python3
"""
Minimal offline validator for AEGIS Artifact Graph JSON (forge-aegis v0.1).

No network. Validates required keys and types only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REQUIRED_ROOT = ("schema", "artifacts", "baseline_id")
REQUIRED_ARTIFACT = ("id", "kind", "digest")


def validate_graph(doc: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    for k in REQUIRED_ROOT:
        if k not in doc:
            errors.append(f"missing root field: {k}")
    arts = doc.get("artifacts")
    if not isinstance(arts, list):
        errors.append("artifacts must be a list")
        return False, errors
    for i, a in enumerate(arts):
        if not isinstance(a, dict):
            errors.append(f"artifacts[{i}] must be object")
            continue
        for k in REQUIRED_ARTIFACT:
            if k not in a:
                errors.append(f"artifacts[{i}] missing {k}")
        if "digest" in a and not isinstance(a["digest"], str):
            errors.append(f"artifacts[{i}].digest must be string")
    return len(errors) == 0, errors


def main(argv: List[str] | None = None) -> int:
    path = Path((argv or sys.argv)[1] if (argv or sys.argv)[1:] else "")
    if not path or not path.is_file():
        print("usage: aegis_validator.py <graph.json>", file=sys.stderr)
        return 2
    doc = json.loads(path.read_text(encoding="utf-8"))
    ok, errs = validate_graph(doc)
    print(json.dumps({"ok": ok, "errors": errs}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
