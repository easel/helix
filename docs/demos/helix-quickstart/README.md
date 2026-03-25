# HELIX Quickstart Demo

A reproducible, scripted demo showing the full HELIX development cycle on a
tiny Node.js temperature converter CLI.

## What It Shows

1. **Setup** — init repo, beads tracker, DDx plugin
2. **Planning Stack** — PRD, user story with acceptance criteria, technical
   design, test plan with failing tests (Red phase)
3. **Execution** — create a bead, implement to pass the tests (Green phase),
   close the bead with traceability
4. **Alignment** — HELIX check to assess queue health

## Prerequisites

- Docker
- Claude OAuth credentials at `~/.claude.json` and `~/.claude/`

## Build

```bash
cd docs/demos/helix-quickstart
docker build -t helix-demo .
```

## Run

Record an asciinema session:

```bash
docker run --rm \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude:ro \
  -v "$(git rev-parse --show-toplevel)":/ddx-library:ro \
  -v "$(pwd)/recordings":/recordings \
  helix-demo
```

The `.cast` file is written to `recordings/`.

Run without recording (interactive):

```bash
docker run --rm -it \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude:ro \
  -v "$(git rev-parse --show-toplevel)":/ddx-library:ro \
  helix-demo
```

## Playback

```bash
asciinema play recordings/helix-quickstart-*.cast
```

Or upload to asciinema.org:

```bash
asciinema upload recordings/helix-quickstart-*.cast
```

## Troubleshooting

**Claude authentication fails**: Ensure both `~/.claude.json` and `~/.claude/`
exist and contain valid OAuth credentials. Both are bind-mounted read-only
into the container. Run `claude` locally first to authenticate if needed.

**br not found**: The install script downloads a pre-built binary. If it fails
in your environment, install manually with `cargo install --git https://github.com/Dicklesworthstone/beads_rust.git`.

**Tests don't fail in Red phase**: The demo script creates tests before
implementation. If a previous run left artifacts in the workspace, rebuild
the container or use `docker run --rm` to ensure a clean workspace.
