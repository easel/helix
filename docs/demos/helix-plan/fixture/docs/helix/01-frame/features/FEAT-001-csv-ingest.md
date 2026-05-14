# FEAT-001 — CSV ingest

## Summary

Read a CSV file, map payer headers to canonical schema, validate each
row, emit valid rows as Parquet partitioned by `(payer_id, ingest_date)`,
quarantine malformed rows.

## User stories

- **US-INGEST-1** — As an operator I point the CLI at a payer CSV and
  receive a Parquet partition and a manifest of accepted/rejected
  counts so I know the file landed.
- **US-INGEST-2** — As a data steward I get a `quarantine/<file>.csv`
  for every rejected row with the original line and the rule that
  failed, so I can fix payer-side issues.
- **US-INGEST-3** — As a developer I add a new payer by writing a
  `schema-mapping.yaml` — no code change — so onboarding is config.
- **US-INGEST-4** — As an oncall I see a single throughput counter and
  a single rejection-rate counter so I know the pipeline's healthy.

## Acceptance

- Round-trip equivalence on a golden CSV: every accepted row, written
  to Parquet and read back, equals the input modulo type widening.
- New payers added via `schema-mapping.yaml` alone pass the round-trip
  test in CI.
- Quarantine file format documented and stable across runs.

## Out of scope

OAuth, sessions, JWTs — see PRD non-goals.
