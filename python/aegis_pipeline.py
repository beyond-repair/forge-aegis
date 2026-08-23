#!/usr/bin/env python3
"""
forge-aegis v0.1 vertical slice (offline).

Host/Input → Evidence → FLS schema check → Policy → Structured result → Audit record

Invariant: same host snapshot + same policy ⇒ deterministic validation result.
No network. No auto-remediation.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SCHEMA_ID = "aegis.fls.v0.1"
RESULT_SCHEMA = "aegis.validation_result.v0.1"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def _digest(obj: Any) -> str:
    return hashlib.sha256(_canonical_json(obj).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Evidence collection
# ---------------------------------------------------------------------------


def collect_evidence(root: Path, *, relative_paths: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Hash files under root. If relative_paths given, only those; else all regular files.
    Returns evidence bundle with per-path digests.
    """
    root = Path(root).resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"host root not found: {root}")

    artifacts: List[Dict[str, Any]] = []
    if relative_paths:
        candidates = [root / p for p in relative_paths]
    else:
        candidates = [p for p in root.rglob("*") if p.is_file()]

    for path in sorted(candidates, key=lambda p: str(p.relative_to(root))):
        if not path.is_file():
            artifacts.append(
                {
                    "id": str(path.relative_to(root)),
                    "kind": "file",
                    "digest": None,
                    "present": False,
                }
            )
            continue
        rel = str(path.relative_to(root)).replace("\\", "/")
        artifacts.append(
            {
                "id": rel,
                "kind": "file",
                "digest": _sha256_file(path),
                "present": True,
                "size": path.stat().st_size,
            }
        )

    evidence = {
        "schema": "aegis.evidence.v0.1",
        "root": str(root),
        "artifacts": artifacts,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "network_access": False,
    }
    evidence["evidence_hash"] = _digest(
        {"artifacts": artifacts, "root": str(root)}
    )
    return evidence


# ---------------------------------------------------------------------------
# FLS / baseline schema
# ---------------------------------------------------------------------------


def load_policy(path: Path) -> Dict[str, Any]:
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    required = ("schema", "baseline_id", "artifacts")
    for k in required:
        if k not in doc:
            raise ValueError(f"policy missing field: {k}")
    if doc["schema"] != SCHEMA_ID and not str(doc["schema"]).startswith("aegis."):
        raise ValueError(f"unsupported schema: {doc['schema']}")
    if not isinstance(doc["artifacts"], list):
        raise ValueError("artifacts must be a list")
    return doc


# ---------------------------------------------------------------------------
# Validator + policy evaluation
# ---------------------------------------------------------------------------


@dataclass
class Finding:
    artifact_id: str
    code: str
    severity: str
    message: str


@dataclass
class ValidationResult:
    schema: str = RESULT_SCHEMA
    baseline_id: str = ""
    status: str = "FAIL"  # PASS | FAIL | INCONCLUSIVE
    findings: List[Dict[str, Any]] = field(default_factory=list)
    evidence_hash: str = ""
    policy_hash: str = ""
    result_hash: str = ""
    explanation: str = ""
    network_access: bool = False

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return d


def validate_against_policy(
    evidence: Dict[str, Any], policy: Dict[str, Any]
) -> ValidationResult:
    """
    Compare evidence digests to policy baseline digests.
    Deterministic for fixed inputs.
    """
    findings: List[Finding] = []
    by_id = {a["id"]: a for a in evidence.get("artifacts") or [] if isinstance(a, dict)}

    for expected in policy.get("artifacts") or []:
        aid = expected.get("id")
        if not aid:
            findings.append(
                Finding("", "MALFORMED_POLICY", "high", "artifact missing id")
            )
            continue
        want = expected.get("digest")
        got = by_id.get(aid)
        if got is None or not got.get("present", True):
            findings.append(
                Finding(aid, "MISSING", "high", f"expected artifact absent: {aid}")
            )
            continue
        if want and got.get("digest") != want:
            findings.append(
                Finding(
                    aid,
                    "DIGEST_MISMATCH",
                    "critical",
                    f"digest mismatch for {aid}: expected {want[:12]}… got {str(got.get('digest'))[:12]}…",
                )
            )

    # Unexpected files (optional strict mode)
    if policy.get("strict_inventory", False):
        allowed = {a.get("id") for a in policy.get("artifacts") or []}
        for aid, art in by_id.items():
            if art.get("present") and aid not in allowed:
                findings.append(
                    Finding(aid, "UNEXPECTED", "medium", f"unexpected file: {aid}")
                )

    if any(f.code == "MALFORMED_POLICY" for f in findings):
        status = "INCONCLUSIVE"
        explanation = "Policy malformed; cannot complete evaluation."
    elif findings:
        status = "FAIL"
        explanation = f"{len(findings)} integrity finding(s) against baseline {policy.get('baseline_id')}."
    else:
        status = "PASS"
        explanation = f"All policy artifacts match evidence for baseline {policy.get('baseline_id')}."

    result = ValidationResult(
        baseline_id=str(policy.get("baseline_id", "")),
        status=status,
        findings=[asdict(f) for f in findings],
        evidence_hash=str(evidence.get("evidence_hash", "")),
        policy_hash=_digest(policy),
        explanation=explanation,
    )
    result.result_hash = _digest(
        {
            "status": result.status,
            "baseline_id": result.baseline_id,
            "findings": result.findings,
            "evidence_hash": result.evidence_hash,
            "policy_hash": result.policy_hash,
        }
    )
    return result


# ---------------------------------------------------------------------------
# Audit record
# ---------------------------------------------------------------------------


def write_audit_record(
    result: ValidationResult,
    out_dir: Path,
    *,
    evidence: Optional[Dict[str, Any]] = None,
) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "schema": "aegis.audit_record.v0.1",
        "result": result.to_dict(),
        "evidence_hash": result.evidence_hash,
        "recorded_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "network_access": False,
    }
    if evidence is not None:
        record["evidence_root"] = evidence.get("root")
    name = f"audit_{result.result_hash[:16]}.json"
    path = out_dir / name
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# End-to-end pipeline
# ---------------------------------------------------------------------------


def run_pipeline(
    host_root: Path,
    policy_path: Path,
    audit_dir: Path,
    *,
    relative_paths: Optional[List[str]] = None,
) -> Tuple[ValidationResult, Path]:
    evidence = collect_evidence(host_root, relative_paths=relative_paths)
    policy = load_policy(policy_path)
    result = validate_against_policy(evidence, policy)
    audit_path = write_audit_record(result, audit_dir, evidence=evidence)
    return result, audit_path


def main(argv: Optional[List[str]] = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="forge-aegis v0.1 integrity pipeline (offline)")
    p.add_argument("--host", required=True, help="directory to measure")
    p.add_argument("--policy", required=True, help="FLS policy JSON")
    p.add_argument("--audit-dir", default="./aegis_audit", help="audit output directory")
    p.add_argument(
        "--only",
        action="append",
        default=None,
        help="relative path under host (repeatable); default: all files",
    )
    args = p.parse_args(argv)

    result, audit_path = run_pipeline(
        Path(args.host),
        Path(args.policy),
        Path(args.audit_dir),
        relative_paths=args.only,
    )
    print(json.dumps({"result": result.to_dict(), "audit": str(audit_path)}, indent=2))
    if result.status == "PASS":
        return 0
    if result.status == "INCONCLUSIVE":
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
