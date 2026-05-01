---
title: Phases
weight: 1
prev: /reference/glossary
next: /artifacts
aliases:
  - /docs/glossary/phases
---

HELIX structures software delivery into seven phases. Each phase has input
gates that validate the previous phase's outputs before allowing
progression, and each phase produces a specific set of
[artifacts](/artifacts/) that govern the work that follows.

## Phase 0: Discover

**Optional.** Validate the opportunity before committing to Frame.

| | |
|---|---|
| **Purpose** | Research the market, users, and technical feasibility |
| **Location** | `docs/helix/00-discover/` |
| **Key artifacts** | [Product Vision](/artifacts/product-vision/), [Business Case](/artifacts/business-case/), [Competitive Analysis](/artifacts/competitive-analysis/), [Opportunity Canvas](/artifacts/opportunity-canvas/) |
| **Output** | A validated opportunity worth pursuing |

## Phase 1: Frame

Define the problem, establish requirements, and scope the work.

| | |
|---|---|
| **Purpose** | Turn a validated opportunity into actionable requirements |
| **Location** | `docs/helix/01-frame/` |
| **Key artifacts** | [PRD](/artifacts/prd/), [Feature Specifications](/artifacts/feature-specification/), [User Stories](/artifacts/user-stories/), [Principles](/artifacts/principles/), [Stakeholder Map](/artifacts/stakeholder-map/), [Risk Register](/artifacts/risk-register/) |
| **Command** | `helix frame` |
| **Output** | Requirements clear enough to design against |

Frame also selects the project's active [cross-cutting
concerns](/concerns/) and establishes
[design principles](/artifacts/principles/) that govern downstream
judgment calls.

## Phase 2: Design

Architect the solution approach.

| | |
|---|---|
| **Purpose** | Make technology and architecture decisions before writing code |
| **Location** | `docs/helix/02-design/` |
| **Key artifacts** | [Architecture](/artifacts/architecture/), [ADR](/artifacts/adr/), [Solution Design](/artifacts/solution-design/), [Technical Design](/artifacts/technical-design/), [Contract](/artifacts/contract/), [Data Design](/artifacts/data-design/), [Tech Spike](/artifacts/tech-spike/) |
| **Command** | `helix design [scope]` |
| **Output** | Design contracts that tests can verify |

Solution designs are feature-level. Technical designs are story-level slices
that inherit from a solution design.

## Phase 3: Test

Write failing tests that define system behavior. This is the **Red** phase
of TDD.

| | |
|---|---|
| **Purpose** | Turn requirements and designs into executable specifications |
| **Location** | `docs/helix/03-test/`, `tests/` |
| **Key artifacts** | [Test Plan](/artifacts/test-plan/), [Story Test Plan](/artifacts/story-test-plan/), [Test Procedures](/artifacts/test-procedures/), [Test Suites](/artifacts/test-suites/), [Security Tests](/artifacts/security-tests/) |
| **Output** | Failing tests that define what "done" means |

Tests are the contract between design and implementation. Code must satisfy
tests, not the other way around.

## Phase 4: Build

Implement code to make tests pass. This is the **Green** phase of TDD.

| | |
|---|---|
| **Purpose** | Write the minimum code needed to satisfy the tests |
| **Location** | `docs/helix/04-build/`, source code |
| **Key artifacts** | [Implementation Plan](/artifacts/implementation-plan/) |
| **Command** | `helix build [issue-id]` |
| **Output** | Passing tests, committed code, closed tracker issues |

Build cannot start until tests are written and failing. Implementation is
complete when all tests pass.

## Phase 5: Deploy

Release to production with monitoring.

| | |
|---|---|
| **Purpose** | Safely deliver the built software to users |
| **Location** | `docs/helix/05-deploy/` |
| **Key artifacts** | [Deployment Checklist](/artifacts/deployment-checklist/), [Monitoring Setup](/artifacts/monitoring-setup/), [Runbook](/artifacts/runbook/), [Release Notes](/artifacts/release-notes/) |
| **Output** | Production rollout with observability, operator guidance, and release communication |

Deploy cannot start until all tests pass (Green phase complete).

## Phase 6: Iterate

Learn and improve for the next cycle.

| | |
|---|---|
| **Purpose** | Review what was built, capture learnings, plan the next cycle |
| **Location** | `docs/helix/06-iterate/` |
| **Key artifacts** | [Improvement Backlog](/artifacts/improvement-backlog/), [Metric Definition](/artifacts/metric-definition/), [Metrics Dashboard](/artifacts/metrics-dashboard/), [Security Metrics](/artifacts/security-metrics/) |
| **Commands** | `helix align`, `helix review`, `helix experiment` |
| **Output** | Actionable follow-up work feeding back into Frame |

Iterate closes the loop. Alignment reviews and experiments produce tracker
issues that drive the next cycle.
