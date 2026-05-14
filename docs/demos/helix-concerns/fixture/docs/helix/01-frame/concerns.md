# Project Concerns

## Active Concerns

- typescript-bun (tech-stack)

## Area Labels

| Label | Applies to |
|-------|-----------|
| `all` | every bead |
| `api` | HTTP server, endpoints, tests |

## Project Overrides

### typescript-bun

- **HTTP runtime**: raw `Bun.serve()` — no Express, no Fastify, no node `http`.
- **Test framework**: `bun:test` — do not use Vitest or Jest.
- **Linter/formatter**: Biome — do not use ESLint or Prettier.
- **Script runner**: `bun run` / `bun test` — not `npm` or `node`.
