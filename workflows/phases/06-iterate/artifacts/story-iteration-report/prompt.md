# Story Iteration Report Generation Prompt

Create a post-deployment iteration report that captures learnings, outcomes, and follow-up work for a single user story after it has been deployed and observed in production.

## Storage Location

Store the iteration report at: `docs/helix/06-iterate/IR-XXX-[story-name].md`

## Purpose

The iteration report ensures:
- Post-deployment outcomes are captured against acceptance criteria
- What worked and what did not is documented for future reference
- Issues encountered are recorded with resolutions
- Follow-up work is emitted as backlog beads, not buried in prose
- Canonical artifact updates are identified when specs drift from reality

## Key Requirements

### 1. Story Reference

Link the report to:
- The originating user story (US-XXX)
- Related deployment beads
- The observation period (start and end dates)

### 2. Outcome Summary

Provide:
- Overall status: Success, Partial Success, or Issues
- One-sentence key takeaway

### 3. Acceptance Criteria Review

For each acceptance criterion from the user story:
- State the target and actual outcome
- Mark as Pass, Partial, or Fail
- Note any deviations and their impact

### 4. Metrics and Evidence

For each relevant metric:
- Baseline value before deployment
- Target value from the story
- Actual observed value
- Notes on measurement methodology

### 5. Learnings

Document:
- What worked well (patterns to repeat)
- What did not work (patterns to avoid)
- Surprising observations

### 6. Issues and Resolutions

For each issue encountered:
- Describe the issue and its impact
- Document the resolution applied
- Flag whether follow-up is needed

### 7. Derived Backlog Beads

Actionable follow-up work MUST be emitted as beads, not embedded as free-form tasks:
- Create beads for improvements, bugs, tech debt, process changes, or research
- Include bead ID, type, title, priority, and rationale

### 8. Canonical Updates

Identify any governing artifacts that need updating because the deployed reality differs from what the specs describe.

## Quality Checklist

Before the iteration report is complete:
- [ ] All acceptance criteria are reviewed with actual outcomes
- [ ] Supporting evidence is linked
- [ ] Follow-up work is captured as beads, not prose
- [ ] Required canonical updates are identified
- [ ] Report is concise and actionable
