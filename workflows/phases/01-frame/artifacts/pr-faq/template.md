---
dun:
  id: helix.pr-faq
---
# PR-FAQ: [PRODUCT NAME]

<!--
This artifact has two halves: a launch-day press release (~350 words) and an
internal FAQ. Write it as if the product ships tomorrow. The press release is
customer-facing; the FAQ is internal and confronts the hard questions. If you
can't write a credible PR-FAQ, the team doesn't yet understand the problem.
-->

## Press Release

**FOR IMMEDIATE RELEASE — [CITY, COUNTRY] — [LAUNCH DATE]**

### Headline

[ONE-LINE VALUE PROPOSITION IN PLAIN ENGLISH. NO JARGON, NO ADJECTIVES LIKE "REVOLUTIONARY" OR "WORLD-CLASS". STATE WHAT THE PRODUCT DOES AND FOR WHOM.]

### Subhead

[ONE SENTENCE EXPANDING THE HEADLINE: WHO IT IS FOR, WHAT IT DOES, WHY IT MATTERS, WHEN IT IS AVAILABLE.]

### Summary

<!-- The lede. What is being announced, the customer outcome, and why now. 2-4 sentences. -->

[COMPANY NAME] today announced [PRODUCT NAME], [SHORT DESCRIPTION]. [PRODUCT NAME] helps [SPECIFIC CUSTOMER SEGMENT] [ACHIEVE SPECIFIC OUTCOME] by [HOW IT WORKS, ONE PHRASE]. It is available [WHERE/WHEN] starting [DATE].

### The Problem

<!-- Name the customer pain in their words. Not "users struggle" — "a 12-person bookkeeping firm spends 6 hours a week reconciling deposits by hand." -->

[CONCRETE PROBLEM, IN THE CUSTOMER'S TERMS, WITH A NUMBER OR FAILURE MODE THAT MAKES IT REAL.]

### The Solution

<!-- How the product solves the problem. Stay at the customer's level — what they do, not how the system is implemented. -->

[ONE PARAGRAPH DESCRIBING THE EXPERIENCE OF USING THE PRODUCT TO SOLVE THE PROBLEM ABOVE.]

### Quote from [LEADER NAME, TITLE]

> "[ONE PARAGRAPH IN THE COMPANY'S VOICE EXPLAINING WHY WE BUILT THIS. NAMES THE CUSTOMER, THE PROBLEM, AND THE COMMITMENT. NOT A SLOGAN.]"

### How It Works

<!-- 3-5 short steps from the customer's perspective. -->

1. [STEP ONE]
2. [STEP TWO]
3. [STEP THREE]

### Customer Quote

> "[ONE PARAGRAPH FROM THE IMAGINED CUSTOMER. IN THEIR VOICE. ABOUT THE OUTCOME THEY GOT, NOT THE FEATURES THEY USED. NAMES A SPECIFIC NUMBER, TIME SAVED, OR PROBLEM AVOIDED.]"
>
> — [CUSTOMER NAME, ROLE, COMPANY OR CONTEXT]

### Availability

[WHERE TO GET IT, WHAT IT COSTS, WHAT PLATFORMS, WHAT REGIONS, WHEN, HOW TO SIGN UP.]

---

## FAQ

<!--
Two halves. External FAQs are what a customer, journalist, or analyst would
ask. Internal FAQs are what an exec, engineer, lawyer, or finance partner
would ask in a review meeting. The internal FAQs should be the hardest
questions you can think of — not soft-balls.
-->

### External FAQs

#### How much does it cost?

[SPECIFIC PRICING. IF FREE, EXPLAIN HOW THE BUSINESS MODEL WORKS. IF NOT YET DECIDED, SAY SO AND NAME THE DECISION OWNER.]

#### How is this different from [EXISTING ALTERNATIVE]?

[NAME THE INCUMBENT OR ADJACENT PRODUCT. DESCRIBE THE SPECIFIC DIFFERENCE — WHO BENEFITS FROM THE DIFFERENCE AND WHEN.]

#### Who is this NOT for?

<!-- Forces honest scoping. -->

[SEGMENT OR USE CASE THAT IS BETTER SERVED BY AN ALTERNATIVE.]

#### What's not in v1?

[EXPLICIT LIST OF FEATURES OR USE CASES DELIBERATELY DEFERRED. EACH WITH A REASON.]

#### What platforms / regions / integrations are supported at launch?

[SPECIFIC LIST.]

#### When can I get it?

[DATE OR PHASED ROLLOUT.]

### Internal FAQs

<!--
Each question below should make at least one stakeholder uncomfortable to
answer. If they don't, the FAQ is too soft.
-->

#### What is the unit economics story? Is this profitable per customer?

[GROSS MARGIN ESTIMATE. ASSUMPTIONS. WHAT BREAKS THE MODEL.]

#### What is the riskiest technical assumption?

[NAME ONE SPECIFIC FEASIBILITY RISK. WHAT WOULD WE NEED TO BUILD OR PROVE TO DE-RISK IT.]

#### What experiments must run before we commit?

[LIST OF NAMED EXPERIMENTS WITH OWNERS AND DEADLINES. IF NONE — JUSTIFY WHY.]

#### What is the smallest viable launch?

[THE MINIMUM SHAPE OF V1 THAT VALIDATES THE THESIS.]

#### Who else has to ship something for this to work?

[EXTERNAL TEAMS, VENDORS, REGULATORY APPROVALS, OR CUSTOMERS. WHAT'S THE COMMITMENT STATUS.]

#### What regulatory or legal exposure does this create?

[LICENSING, DATA PROTECTION, FINANCIAL REGULATION, INDUSTRY-SPECIFIC RULES. NAME THE JURISDICTION.]

#### How does this scale? What breaks at 10x and 100x usage?

[SPECIFIC BOTTLENECKS. WHAT WE'D HAVE TO REBUILD.]

#### What are we choosing not to do, and why?

[EXPLICIT NON-GOALS WITH RATIONALE. PAIRS WITH THE PRD'S NON-GOALS SECTION.]

#### What would cause us to abandon this project?

<!-- Kill criteria. Concrete, observable. -->

[SPECIFIC SIGNAL — A METRIC TARGET MISSED, A COMPETITOR LAUNCH, A REGULATORY CHANGE — THAT WOULD MAKE US STOP.]

#### What does success look like 12 months after launch?

[QUANTITATIVE TARGETS THAT INFORM THE PRD'S SUCCESS METRICS.]

## Review Checklist

Use this checklist when reviewing a PR-FAQ artifact:

- [ ] Press release names a specific customer segment, not "users" or "teams"
- [ ] Press release reads as a real wire-service story — no marketing fluff
- [ ] Press release stays under ~350 words
- [ ] The Problem section uses the customer's words and names a specific failure mode with a number
- [ ] The Solution section describes the customer experience, not the implementation
- [ ] Customer quote describes an outcome the customer got, not features they used
- [ ] Availability names specific dates, prices, platforms, and regions
- [ ] External FAQ explicitly compares to existing alternatives
- [ ] External FAQ names who this is NOT for
- [ ] A FAQ explicitly lists what is out of scope for v1
- [ ] Internal FAQ surfaces at least one credible feasibility or technical risk
- [ ] Internal FAQ confronts unit economics or pricing plausibility
- [ ] Internal FAQ states explicit kill criteria
- [ ] Internal FAQ names experiments or validation steps required before commit
- [ ] No `[TBD]`, `[TODO]`, or `[NEEDS CLARIFICATION]` markers remain
- [ ] PR-FAQ is consistent with the governing Product Vision
