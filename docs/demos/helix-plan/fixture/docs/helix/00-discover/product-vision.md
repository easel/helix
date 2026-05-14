# Product Vision

## Mission

A claims-ingest pipeline for a healthcare payer. CSV in, Parquet out,
with deterministic schema mapping and an audit trail that makes
disputes resolvable.

## Vision

Operations stops eyeballing spreadsheets. A single canonical claims
table backs every downstream report; payer files land in it via a
declarative pipeline whose specs travel with the data.

## North Star

Time-from-payer-file-arriving to claims-table-row drops from days to
under fifteen minutes, and the lineage from row back to source CSV is
one query away.
