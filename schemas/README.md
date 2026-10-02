# Schemas

v0.1 ships one reference JSON Schema for the baseline policy the Python pipeline reads:

- `aegis.fls.v0.1.schema.json`

It is aligned with `python/aegis_pipeline.py` (`schema`, `baseline_id`, `artifacts[].id/kind/digest`). It is not generated from the FLS prose, and the runtime does not fetch it. Normative FLS documents under `fls/` remain draft and are not executed.
