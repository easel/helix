# Project Concerns

## Active Concerns

- go-std (tech-stack)
- security-owasp (security)

## Area Labels

| Label | Applies to |
|-------|-----------|
| `all` | every bead |
| `ingest` | parser, validator, Parquet writer |
| `cli` | operator CLI |

## Project Overrides

### go-std

- **HTTP framework**: net/http (no Gin, no Echo).
- **Test framework**: `testing` + `testify/require` for assertions.
- **CSV reader**: encoding/csv from the standard library.
- **Parquet**: parquet-go (segmentio).
