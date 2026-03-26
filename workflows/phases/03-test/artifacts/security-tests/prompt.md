# Security Tests Generation

## Required Inputs
- `docs/helix/01-frame/threat-model.md`
- `docs/helix/02-design/security-architecture.md`
- `docs/helix/01-frame/security-requirements.md`

## Produced Output
- `docs/helix/03-test/security-tests.md`
- security test implementations

Create concise, project-specific security tests that map threats and security requirements to executable checks. Include only relevant categories, a threat-to-test matrix, and any tooling or automation needed for this stack.

Keep the output concrete:
- cover the highest-risk threats first
- note expected failures, pass criteria, and required fixtures or setup
- include only applicable security controls and tools

Use template at `workflows/phases/03-test/artifacts/security-tests/template.md`.
