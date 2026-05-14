---
title: Demos
weight: 7
prev: /reference/glossary
aliases:
  - /docs/demos
---

# Demo Reels

Scripted terminal recordings of HELIX in action. New-user workflows should
prefer `helix input` to shape work and `ddx agent execute-loop` to drain the
execution-ready queue. The current demo recordings focus on the first-five-
minutes experience and may still show compatibility wrappers or direct
`ddx agent run` prompt capture inside the recording harness.

The shipped public demo inventory is `helix-quickstart`, `helix-concerns`,
`helix-evolve`, and `helix-experiment`. The repo also contains
`docs/demos/helix-interactive/` as experimental source material, but it is not
currently embedded here or recorded by the Pages workflow.

---

## Quickstart: Intake to Queue Drain

The complete HELIX onboarding experience: install, shape a request with
`helix input`, then let DDx drain execution-ready work. The current recording
still visualizes the phase-by-phase compatibility flow while the docs here
reflect the new default contract. The demo builds a Node.js temperature
converter from scratch, driven entirely by HELIX artifacts and the tracker.

{{< asciinema src="helix-quickstart" >}}

| Act | Phase | What Happens |
|-----|-------|-------------|
| 1 | Install | Install HELIX skills and CLI, verify ddx agent harness |
| 2 | Setup | Initialize git repo, tracker, and AGENTS.md |
| 3 | Input | `helix input` shapes the request into governed HELIX artifacts |
| 4 | Queue | `ddx agent execute-loop` drains the execution-ready queue |
| 5 | Build | The work follows HELIX's test-first Build discipline |
| 6 | Verify | Run tests, check acceptance criteria |
| 7 | Review | Review surfaces follow-on gaps or drift |

{{< tabs >}}

{{< tab name="Docker" >}}
```bash
docker build -t helix-demo docs/demos/helix-quickstart/
docker run --rm \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude \
  -v $(pwd):/helix:ro \
  -v $(pwd)/../ddx/ddx:/usr/local/bin/ddx:ro \
  -v $(pwd)/docs/demos/helix-quickstart/recordings:/recordings \
  helix-demo
```
{{< /tab >}}

{{< tab name="Local" >}}
```bash
cd /tmp
bash /path/to/helix/docs/demos/helix-quickstart/demo.sh
```

Requires: git, jq, node, npm, ddx, helix CLI.
{{< /tab >}}

{{< /tabs >}}

---

## Concerns: Preventing Technology Drift

Demonstrates how [concerns](/concerns/) keep agents on the declared technology stack. A Bun/TypeScript project declares `typescript-bun` as its concern. The agent builds with Bun-native tools, then a deliberate drift (vitest import) is introduced and caught by concern-aware review.

{{< asciinema src="helix-concerns" >}}

| Act | Phase | What Happens |
|-----|-------|-------------|
| 1 | Setup | Create Bun project with `typescript-bun` concern |
| 2 | Frame | Agent reads concerns, uses Bun-native requirements |
| 3 | Build | Agent implements with Bun.serve(), bun:test, Biome |
| 4 | Drift | Deliberate Node.js drift introduced (vitest import) |
| 5 | Review | Agent detects drift and files a tracker issue |

{{< tabs >}}

{{< tab name="Docker" >}}
```bash
docker build -t helix-concerns-demo docs/demos/helix-concerns/
docker run --rm \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude \
  -v $(pwd):/helix:ro \
  -v $(pwd)/../ddx/ddx:/usr/local/bin/ddx:ro \
  -v $(pwd)/docs/demos/helix-concerns/recordings:/recordings \
  helix-concerns-demo
```
{{< /tab >}}

{{< tab name="Local" >}}
```bash
cd /tmp
bash /path/to/helix/docs/demos/helix-concerns/demo.sh
```

Requires: git, jq, bun, ddx, helix CLI.
{{< /tab >}}

{{< /tabs >}}

---

## Evolve: Threading Requirements Through the Stack

Demonstrates how `helix evolve` propagates a new requirement through every layer of the artifact stack. Starting from a working temperature converter, a "Add Kelvin support" requirement is threaded through the PRD, feature spec, and technical design, then implemented via TDD.

{{< asciinema src="helix-evolve" >}}

| Act | Phase | What Happens |
|-----|-------|-------------|
| 1 | Setup | Working v1 project with existing artifacts and code |
| 2 | Evolve | Thread "Add Kelvin" through PRD, feature spec, design, tracker |
| 3 | Build | TDD: failing Kelvin tests (Red), then implementation (Green) |
| 4 | Verify | All tests pass, new CLI flags work |

{{< tabs >}}

{{< tab name="Docker" >}}
```bash
docker build -t helix-evolve-demo docs/demos/helix-evolve/
docker run --rm \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude \
  -v $(pwd):/helix:ro \
  -v $(pwd)/../ddx/ddx:/usr/local/bin/ddx:ro \
  -v $(pwd)/docs/demos/helix-evolve/recordings:/recordings \
  helix-evolve-demo
```
{{< /tab >}}

{{< tab name="Local" >}}
```bash
cd /tmp
bash /path/to/helix/docs/demos/helix-evolve/demo.sh
```

Requires: git, jq, node, npm, ddx, helix CLI.
{{< /tab >}}

{{< /tabs >}}

---

## Experiment: Metric-Driven Optimization

Demonstrates how `helix experiment` optimizes code through measured iteration. A deliberately slow string processing function is improved through hypothesis-driven changes, with correctness tests enforced at every step.

{{< asciinema src="helix-experiment" >}}

| Act | Phase | What Happens |
|-----|-------|-------------|
| 1 | Setup | Project with slow function, correctness tests, and benchmark |
| 2 | Iterate | Agent hypothesizes, edits, tests, benchmarks (iteration 1) |
| 3 | Iterate | Agent finds next bottleneck, optimizes further (iteration 2) |
| 4 | Results | Final benchmark shows improvement, all tests still passing |

{{< tabs >}}

{{< tab name="Docker" >}}
```bash
docker build -t helix-experiment-demo docs/demos/helix-experiment/
docker run --rm \
  -v ~/.claude.json:/root/.claude.json:ro \
  -v ~/.claude:/root/.claude \
  -v $(pwd):/helix:ro \
  -v $(pwd)/../ddx/ddx:/usr/local/bin/ddx:ro \
  -v $(pwd)/docs/demos/helix-experiment/recordings:/recordings \
  helix-experiment-demo
```
{{< /tab >}}

{{< tab name="Local" >}}
```bash
cd /tmp
bash /path/to/helix/docs/demos/helix-experiment/demo.sh
```

Requires: git, jq, node, npm, ddx, helix CLI.
{{< /tab >}}

{{< /tabs >}}
