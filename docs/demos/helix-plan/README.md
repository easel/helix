# helix-plan demo

The brief is written and aligned. The plan side of the alignment
skill decomposes the feature spec into bounded beads — each with
deterministic acceptance criteria and named evidence — that a
runtime can execute.

## Files

- `session.jsonl` — committed session record.
- `fixture/` — post-brief artifact set for a CSV-to-Parquet
  healthcare-claims pipeline:
  - `docs/helix/00-discover/product-vision.md`
  - `docs/helix/01-frame/prd.md` (R-1..R-5)
  - `docs/helix/01-frame/concerns.md` (go-std + security-owasp)
  - `docs/helix/01-frame/features/FEAT-001-csv-ingest.md` with
    US-INGEST-1..4

The session's four beads (header sniffer, row validator, Parquet
writer, CLI surface) trace directly to FEAT-001's user stories and
acceptance.

## Rebuild the cast

```
python3 scripts/demos/render_session.py docs/demos/helix-plan/session.jsonl
bash tests/validate-demos.sh
```

## Re-capture from a live agent

```
python3 scripts/demos/capture_session.py helix-plan \
    --prompt "Decompose FEAT-001 into bounded beads with deterministic acceptance criteria and named evidence." \
    --fixture docs/demos/helix-plan/fixture/
```
