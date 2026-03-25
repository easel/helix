# Lessons Learned Generation

## Required Inputs
- `docs/helix/06-iterate/metrics-dashboard.md` - Production metrics
- `docs/helix/06-iterate/feedback-analysis.md` - User feedback
- Project retrospective notes

## Produced Output
- `docs/helix/06-iterate/lessons-learned.md` - Documented learnings

## Prompt

You are documenting lessons learned from a completed iteration. Your goal is to capture insights that will improve future iterations.

Based on production metrics, user feedback, and team retrospective, document:

1. **Iteration Summary**
   - Goals achieved vs. planned
   - Key metrics comparison
   - Overall assessment

2. **What Went Well**
   | Category | Success | Contributing Factors | How to Repeat |
   |----------|---------|---------------------|---------------|
   | [Process/Technical/Team] | [Description] | [Why it worked] | [Action] |

3. **What Could Be Improved**
   | Category | Issue | Root Cause | Improvement Action |
   |----------|-------|------------|-------------------|
   | [Process/Technical/Team] | [Description] | [Analysis] | [Specific action] |

4. **Technical Debt Identified**
   - New debt incurred
   - Debt addressed
   - Priority for remediation

5. **Process Improvements**
   - Workflow changes recommended
   - Tool improvements needed
   - Communication enhancements

6. **Knowledge Transfer**
   - Key insights for new team members
   - Documentation updates needed
   - Training recommendations

Use the template at `workflows/helix/phases/06-iterate/artifacts/lessons-learned/template.md`.

## Completion Criteria
- [ ] Both successes and improvements documented
- [ ] Root causes identified for issues
- [ ] Candidate backlog beads identified for actionable follow-up work
- [ ] Knowledge transfer items identified
