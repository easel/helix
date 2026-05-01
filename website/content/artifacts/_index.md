---
title: Artifacts
weight: 2
generated: true
aliases:
  - /docs/glossary/artifacts
  - /reference/glossary/artifacts
---

Every HELIX project produces a graph of governing artifacts — documents that define what to build, why, how, and how to verify it. When artifacts disagree, the [authority order](/why/principles/#3-authority-order-governs-reconciliation) governs: vision over requirements, requirements over design, design over code.

Each artifact below has its own page with description, relationships to other artifacts, the generation prompt, the template structure, and (where available) a worked example.

## Phase 0 — Discover

_Validate that an opportunity is worth pursuing before committing to a development cycle._

{{< cards >}}
  {{< card link="business-case" title="Business Case" subtitle="Investment justification with market sizing, ROI projections, and risk assessment. Informs go/no-go decision." >}}
  {{< card link="competitive-analysis" title="Competitive Analysis" subtitle="Market landscape mapping and differentiation strategy. Identifies competitive positioning and sustainable advantages." >}}
  {{< card link="opportunity-canvas" title="Opportunity Canvas" subtitle="Synthesis document validating problem-solution fit. Final artifact before go/no-go decision on proceeding to Frame." >}}
  {{< card link="product-vision" title="Product Vision" subtitle="North star document defining mission, positioning, direction, target market, and success criteria. First artifact in Discover phase." >}}
{{< /cards >}}

## Phase 1 — Frame

_Define what the system should do, for whom, and how success will be measured._

{{< cards >}}
  {{< card link="compliance-requirements" title="Compliance Requirements" subtitle="Comprehensive regulatory and compliance requirements analysis. Identifies applicable regulations, maps requirements to implementation controls, and defines a c…" >}}
  {{< card link="concerns" title="Project Concerns" subtitle="Declares the project's active cross-cutting concerns (tech stacks, quality attributes, conventions) and any project-specific overrides. Concerns are composable…" >}}
  {{< card link="feasibility-study" title="Feasibility Study" subtitle="A systematic analysis of project viability across technical, business, operational, and resource dimensions. Used to validate that a proposed solution is achie…" >}}
  {{< card link="feature-registry" title="Feature Registry" subtitle="Central registry tracking all features, their status, dependencies, and ownership throughout the project lifecycle. Single source of truth for feature identifi…" >}}
  {{< card link="feature-specification" title="Feature Specification" subtitle="Detailed specifications for each feature including functional and non-functional requirements, constraints, and edge cases. Uses [NEEDS CLARIFICATION] markers…" >}}
  {{< card link="parking-lot" title="Parking Lot" subtitle="Project-level registry for deferred and future work that is kept out of the main PRD flow. Parked artifacts remain in their normal HELIX locations and are flag…" >}}
  {{< card link="pr-faq" title="PR-FAQ" subtitle="A working-backwards artifact pairing a launch-day press release with an internal FAQ. The press release forces the team to commit to a concrete customer outcom…" >}}
  {{< card link="prd" title="Product Requirements Document" subtitle="The PRD is the foundational business document that defines the problem, solution vision, success metrics, and requirements. It serves as the single source of t…" >}}
  {{< card link="principles" title="Project Principles" subtitle="Cross-cutting design principles that guide judgment calls across all HELIX phases. Not workflow rules or process enforcement — these are lenses applied when ch…" >}}
  {{< card link="research-plan" title="Research Plan" subtitle="A structured plan for investigating unknown requirements, exploring problem spaces, or validating assumptions before committing to detailed specifications. Use…" >}}
  {{< card link="risk-register" title="Risk Register" subtitle="Comprehensive identification, assessment, and management of project risks. Includes both threats and opportunities with mitigation strategies and ownership." >}}
  {{< card link="security-requirements" title="Security Requirements" subtitle="Comprehensive security requirements definition for the project. Covers security user stories, compliance mapping, risk assessment, and testable acceptance crit…" >}}
  {{< card link="stakeholder-map" title="Stakeholder Map" subtitle="Comprehensive identification and analysis of all project stakeholders, their influence, interests, and engagement strategies. Includes RACI matrix for clear ac…" >}}
  {{< card link="threat-model" title="Threat Model" subtitle="Systematic identification and analysis of security threats using STRIDE methodology. Maps threats to system components, assesses risk, and defines mitigation s…" >}}
  {{< card link="user-stories" title="User Stories" subtitle="Standalone design artifacts defining vertical slices of the application. Each story traces a complete user journey from trigger to outcome with acceptance crit…" >}}
  {{< card link="validation-checklist" title="Validation Checklist" subtitle="Comprehensive checklist to validate Frame phase completeness, quality, and readiness for Design phase. Ensures all deliverables meet standards and stakeholders…" >}}
{{< /cards >}}

## Phase 2 — Design

_Decide how to build it. Capture trade-offs, contracts, and architecture decisions._

{{< cards >}}
  {{< card link="adr" title="Architecture Decision Record" subtitle="An ADR documents a significant architectural decision: the context that drove it, the alternatives considered, the chosen approach, and the consequences. Each…" >}}
  {{< card link="architecture" title="Architecture" subtitle="Captures the C4 views the team needs to build and review the system — System Context, Container, Component (where helpful), Deployment, and Data Flow — plus th…" >}}
  {{< card link="contract" title="Contract" subtitle="Normative interface and schema contract that another team can implement against directly, including API, CLI, protocol, event, and data contracts." >}}
  {{< card link="data-design" title="Data Design" subtitle="Design-level data architecture covering entities, stores, access patterns, constraints, and migration strategy." >}}
  {{< card link="proof-of-concept" title="Proof of Concept" subtitle="A minimal working implementation that validates the feasibility and approach of a key technical concept before full development. More substantial than a tech s…" >}}
  {{< card link="security-architecture" title="Security Architecture" subtitle="Design-level security architecture that maps trust boundaries, controls, and security decisions to implementation and testing." >}}
  {{< card link="solution-design" title="Solution Design" subtitle="Feature-level solution design that explains the chosen approach for a feature or cross-component capability. It maps requirements to a concrete system shape, e…" >}}
  {{< card link="tech-spike" title="Technical Spike" subtitle="Time-boxed technical investigation to explore unknowns, validate approaches, or reduce technical risk before committing to implementation. Produces concrete te…" >}}
  {{< card link="technical-design" title="Technical Design" subtitle="Story-specific technical design that details HOW to implement a single user story within the context of the broader solution architecture. This enables vertica…" >}}
{{< /cards >}}

## Phase 3 — Test

_Define how we know it works. Plans, suites, and procedures that bind specs to implementation._

{{< cards >}}
  {{< card link="security-tests" title="Security Tests" subtitle="(security-tests)" >}}
  {{< card link="story-test-plan" title="Story Test Plan" subtitle="The story test plan translates one bounded technical design into executable verification intent before implementation starts. It maps story acceptance criteria…" >}}
  {{< card link="test-plan" title="Test Plan" subtitle="The project-level test plan defines the testing strategy for the full project: test levels and scope, framework choices, coverage targets, critical paths, test…" >}}
  {{< card link="test-procedures" title="Test Procedures" subtitle="(test-procedures)" >}}
  {{< card link="test-suites" title="Test Suites" subtitle="(test-suites)" >}}
{{< /cards >}}

## Phase 4 — Build

_Implement against the specs and tests. Capture the implementation plan that scopes the work._

{{< cards >}}
  {{< card link="implementation-plan" title="Implementation Plan" subtitle="Scopes the implementation work that will satisfy the test plan and follow the technical design. Decomposes work into bounded units that the autopilot can execu…" >}}
{{< /cards >}}

## Phase 5 — Deploy

_Ship to users with appropriate operational support, monitoring, and rollback plans._

{{< cards >}}
  {{< card link="deployment-checklist" title="Deployment Checklist" subtitle="Short, execution-ready release readiness checklist that captures the technical go/no-go checks, rollout verification, and rollback triggers for a service deplo…" >}}
  {{< card link="monitoring-setup" title="Monitoring Setup" subtitle="Service-specific observability and alerting setup required before or during rollout." >}}
  {{< card link="release-notes" title="Release Notes" subtitle="Release-scoped communication artifact that summarizes shipped user-visible and operator-visible changes, required actions, and known caveats for one rollout." >}}
  {{< card link="runbook" title="Runbook" subtitle="Service-specific operational procedures for on-call response, rollback, recovery, and routine maintenance tied to a deployed system." >}}
{{< /cards >}}

## Phase 6 — Iterate

_Measure, align, and improve. Close the feedback loop back into the planning strand._

{{< cards >}}
  {{< card link="improvement-backlog" title="Improvement Backlog" subtitle="Prioritized improvement inventory derived from iteration learnings and tracker-backed follow-up work." >}}
  {{< card link="metric-definition" title="Metric Definition" subtitle="(metric-definition)" >}}
  {{< card link="metrics-dashboard" title="Metrics Dashboard" subtitle="Iteration-level metrics summary that compares current values to a prior baseline and answers whether the latest change improved the system." >}}
  {{< card link="security-metrics" title="Security Metrics" subtitle="Iteration-level security posture report covering incident response, vulnerability management, application security, and compliance." >}}
{{< /cards >}}
