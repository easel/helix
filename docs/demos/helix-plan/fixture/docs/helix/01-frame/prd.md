---
ddx:
  id: claims-ingest.prd
---
# Product Requirements Document

## Summary

CSV-to-Parquet ingest for healthcare claims. Files arrive in a payer
inbox; the pipeline parses, validates, deduplicates, and emits a row
per claim into the canonical Parquet table.

## Requirements

### P0

**R-1: CSV header sniffing.** The pipeline reads the first row of an
incoming CSV and maps payer-specific headers to canonical claim
columns using a per-payer `schema-mapping.yaml`. Unknown payers fail
the file with a diagnostic.

**R-2: Row-level validation.** Each row is checked against the
canonical schema (types, required fields, value domains). Malformed
rows are quarantined, not silently dropped.

**R-3: Parquet emission.** Validated rows are written to a partitioned
Parquet dataset; the partition key is `(payer_id, ingest_date)`.

**R-4: Operator CLI.** A small CLI runs the pipeline on a file, or on
a directory of files, with `--schema <path>` and `--output <path>`
flags.

### P1

**R-5: Throughput.** The pipeline processes ≥10k rows/sec on a single
worker on commodity hardware.

## Out of scope

- Live streaming ingest.
- Cross-payer deduplication (single-file dedup is in scope).
