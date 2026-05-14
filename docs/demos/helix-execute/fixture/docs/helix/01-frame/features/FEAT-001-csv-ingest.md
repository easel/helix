# FEAT-001 — CSV ingest

## Summary

Read a CSV file, map payer headers to canonical schema, validate each
row, emit valid rows as Parquet, quarantine malformed rows.

## User stories

- **US-INGEST-1** — operator-driven file ingest with a manifest of
  accepted/rejected counts.
- **US-INGEST-2** — data steward gets a quarantine file with the
  rejected row + the rule that failed.
- **US-INGEST-3** — new payer support via `schema-mapping.yaml`, no
  code change.

## Acceptance

Round-trip equivalence on a golden CSV; new payers added via YAML
alone pass round-trip in CI.
