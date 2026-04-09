# Security Architecture

`security-architecture` is restored as the canonical design-phase artifact for
trust boundaries, controls, and design-level security decisions.

## Decision

This artifact is restored rather than retired. Security requirements and the
threat model define the problem, but they do not replace the architectural
control surface that shapes implementation and testing.

## Why It Exists

- Security requirements say what must be protected.
- The threat model identifies what can go wrong.
- Security architecture decides how the system will prevent, detect, and
  recover from those threats.

## Canonical Inputs

- `docs/helix/01-frame/security-requirements.md`
- `docs/helix/01-frame/threat-model.md`
- `docs/helix/02-design/architecture.md`

## Minimum Prompt Bar

- Start from security requirements and the threat model.
- Define trust boundaries and control points.
- Map threats to controls and controls to tests.
- Make identity, access, data protection, logging, and monitoring decisions
  explicit.
- Stay at the design level and do not drift into implementation code.

## Minimum Template Bar

- scope and decision summary
- trust boundaries
- control mapping
- identity and access
- data protection
- logging and monitoring
- residual risk
- test hooks or verification notes

## Canonical Replacement Status

`security-architecture` is not replaced by `architecture` or `threat-model`.
Those artifacts are upstream inputs. The security architecture remains the
place where the design-level security decisions are made concrete.
