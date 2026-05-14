# HELIX Demo Scenarios

The demos under `docs/demos/` are screencasts of the HELIX user experience as
described in `docs/helix/00-discover/product-vision.md` and
`docs/helix/01-frame/prd.md`. Each scenario is captured as a
**session record** (a committed transcript of a real Claude/Codex run) and
**rebuilt into an asciicast** at build time. Capture once → check the record
→ regenerate the visual artifact on every release.

## Source contract

The PRD's four-step Core Workflow Contract:

1. **Write the brief** — users create or update governing artifacts.
2. **Check alignment** — HELIX reviews the artifact graph for drift.
3. **Create the work plan** — aligned artifacts become bounded work.
4. **Run it in the factory** — a runtime executes; evidence updates the graph.

The product-vision UX scenario:

> A team wants to add OAuth login. They describe the intent to their agent.
> The agent invokes the HELIX alignment skill against existing governing
> artifacts. The skill produces an authority-ordered plan. The team reviews,
> approves, hands it to the runtime.

## Scenarios

| Slug | Title | What it shows | Primary skill |
|------|-------|---------------|---------------|
| adopt | Adopt HELIX in a new project | `ddx install helix` (or equivalent skill install), running `/helix` to discover capabilities, dropping templates into a fresh repo | install + `helix` umbrella |
| brief | Author the brief | Creating product-vision + PRD + feature spec from templates with the `helix` skill in frame mode | `/helix-frame` |
| align | Check alignment | Running the alignment skill against an existing artifact set, getting findings, getting an authority-ordered plan | `/helix-align` |
| plan | Create the work plan | Turning aligned artifacts into bounded implementation work — scoped beads with acceptance criteria and evidence expectations | `/helix-align` (planning mode) |
| evolve | Evolve a requirement | The OAuth-style scenario: a new requirement threads through PRD → feature spec → solution design → security architecture → tracker beads | `/helix-evolve` |
| concerns | Detect technology drift | Concerns declared in the brief catch local agent decisions that drift from project intent (Bun vs Node-style drift) | `/helix-align` with concerns scope |
| review | Fresh-eyes review | Reviewer agent inspects completed work against the artifacts that govern it; findings become tracker items | `/helix-review` |
| execute | Run in the factory | Handoff of a planned bead to DDx (or another runtime); evidence flows back and the artifact graph updates | runtime (DDx) — HELIX skill is offstage |

## Session record contract

Each demo lives at `docs/demos/helix-<slug>/` with:

- `session.jsonl` — line-per-event transcript of the real Claude/Codex run.
  Schema (see `scripts/demo_session_schema.json`):
  - `{"t": "narration", "text": "…"}` — voiceover line
  - `{"t": "user", "text": "…"}` — operator typed input
  - `{"t": "tool", "name": "Read", "args": {…}}` — tool invocation
  - `{"t": "assistant", "text": "…", "duration_ms": 1200}` — model output
  - `{"t": "fs", "op": "write", "path": "…", "content": "…"}` — files written
- `fixture/` — minimal repo state the demo runs against
- `assertions.yml` — claims about the recorded session that CI verifies
  (specific tool calls present, specific file outputs, etc.)
- `demo.sh` — thin rebuild wrapper that drives `scripts/rebuild_demo.sh`

## Build pipeline

```
session.jsonl  →  scripts/rebuild_demo.sh  →  *.cast (asciinema)
   ↑                       ↑
 captured once          run in CI / locally
```

`scripts/rebuild_demo.sh` replays `session.jsonl` through a terminal renderer
with deterministic timing controls (text pacing, narration delay, tool-call
animation) and emits an asciicast. The .cast files are also committed under
`website/static/demos/` so the microsite always has a fallback.

## Verification

`tests/validate-demos.sh` checks, for every demo:

1. `session.jsonl` parses against the schema
2. `assertions.yml` holds (named tool calls fired, expected files written,
   expected text produced)
3. `scripts/rebuild_demo.sh <slug>` produces a non-empty `.cast` that loads
   in asciinema's player
4. The rebuilt `.cast` matches the committed one within a tolerance, OR the
   commit message contains `DEMO_REBUILD: <slug>` to flag intentional refresh

## Capturing new sessions

```
scripts/capture_demo.sh helix-<slug>
```

Wraps a Claude/Codex session that:

1. Sets up the demo's `fixture/` directory
2. Drives the agent with the scenario's planned prompts
3. Captures every event into `session.jsonl`
4. Stops at the scenario's success criterion

The maintainer reviews the captured session and the diff to `assertions.yml`
before committing.
