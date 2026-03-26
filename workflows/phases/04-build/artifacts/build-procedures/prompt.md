# Build Procedures Generation

## Required Inputs
- `docs/helix/04-build/implementation-plan.md`
- project build configuration

## Produced Output
- `docs/helix/04-build/build-procedures.md`

Document only the build steps needed to execute this project’s TDD loop: environment setup, project commands, test execution, quality checks, and CI hooks if they matter. Keep it specific to this stack and omit generic developer advice.

Use template at `workflows/phases/04-build/artifacts/build-procedures/template.md`.
