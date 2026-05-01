# PR-FAQ: Tally Reconcile

## Press Release

**FOR IMMEDIATE RELEASE — AUSTIN, TEXAS — MARCH 4, 2027**

### Headline

Tally launches Reconcile, an invoicing tool that matches every customer payment to its invoice automatically, for US small businesses with up to 50 customers.

### Subhead

Reconcile connects to a small business's bank account and its invoicing software, then closes the books each morning by matching deposits to invoices without human intervention. It is available today in the United States for $29 per month.

### Summary

Tally Software, Inc. today announced Tally Reconcile, an invoicing add-on that eliminates manual bank reconciliation for service-based small businesses. Reconcile reads bank deposits via Plaid, matches each one to an open invoice, posts the match back to QuickBooks Online, FreshBooks, or Wave, and flags exceptions for human review. The product is available today across the United States starting at $29 per month for businesses with up to 50 active customers.

### The Problem

Owners of small bookkeeping, consulting, and home-services firms typically spend four to eight hours each week reconciling deposits — opening their bank app in one tab, their invoicing tool in another, and manually marking invoices paid one at a time. When a customer pays two invoices in a single ACH, or pays a round number that doesn't match any single invoice, reconciliation stalls and accounts receivable drifts out of date. Most owners we talked to said it is the single task they most consistently put off.

### The Solution

Reconcile watches the business's bank account and the open invoices in its accounting software. When a deposit lands, Reconcile matches it to one or more invoices using payor name, amount, and timing, and posts the payment back automatically. Owners review a one-screen exception list each morning — typically two to four items — and approve or correct them with one click. The first reconciliation each morning is done before the owner finishes their coffee.

### Quote from Priya Shah, CEO, Tally Software

> "We built Reconcile because every small-business owner we interviewed told us bank reconciliation was a tax on their week — a task that mattered but that nobody enjoyed and nobody wanted to hire for. Reconcile pays for itself the first month for any firm doing more than five invoices a week, and it gives owners back the hours they were spending on something a computer should have been doing."

### How It Works

1. Connect your bank account through Plaid and your invoicing software through OAuth.
2. Reconcile imports the last 90 days and proposes matches for any open invoices.
3. Each morning, deposits from the prior day are matched and posted automatically.
4. Anything ambiguous lands on a one-screen exception list for one-click resolution.

### Customer Quote

> "I was spending Saturday mornings on reconciliation. Three weeks in with Reconcile, I have an empty exception list by 8:30 a.m. on a Tuesday and I have not opened my bank app on a weekend since. The first month it caught two invoices my old process had missed, which more than paid for the year."
>
> — Marcus Chen, owner, Chen & Associates Bookkeeping (12-person firm, Reno, Nevada)

### Availability

Tally Reconcile is available today at tally.com/reconcile in all 50 US states. Pricing is $29 per month for up to 50 active customers, $79 per month for up to 250. A 30-day free trial is available; a credit card is required to start. Integrations at launch: QuickBooks Online, FreshBooks, Wave, and Square Invoices. Stripe and PayPal payouts are supported as deposit sources in addition to direct bank ACH.

---

## FAQ

### External FAQs

#### How is this different from QuickBooks' built-in bank-feed matching?

QuickBooks' bank feed shows you a deposit and asks you to confirm a match. Reconcile makes the match automatically using payor name, invoice timing, and partial-payment heuristics, and only asks for human review on the small minority that are ambiguous. In our beta, QuickBooks bank feeds matched 41% of deposits without intervention; Reconcile matches 86%.

#### Who is Reconcile NOT for?

Reconcile is not for businesses that primarily take card payments at point of sale (a Square reader at a coffee shop), since those flows already reconcile cleanly inside Square. It's also not for firms with more than ~250 active customers — those firms typically have a bookkeeper on staff and need workflow controls Reconcile does not yet provide.

#### What's not in v1?

Multi-currency, foreign bank accounts, payments-on-account (where a customer prepays without a specific invoice), and class/department coding are deferred to v1.1. Direct support for Xero is planned for Q3 2027.

#### What if Reconcile makes a wrong match?

Every automatic match is reversible from the exception list for 14 days. Reconcile also requires confirmation when the matching confidence is below 95% or when the deposit amount is more than $5,000.

#### What data do you store?

Reconcile stores invoice metadata and deposit metadata. We do not store full bank credentials — those live with Plaid. We do not sell or share customer data.

### Internal FAQs

#### What are the unit economics?

At $29/month, gross margin is approximately 71% after Plaid ($3.50/customer/month at our negotiated rate), accounting-software API costs ($1.20), and infrastructure ($3.50). Customer acquisition cost target is under $90; we payback in month four. The model breaks if Plaid raises rates more than 40% or if the matching engine requires more than one human-reviewed exception per 20 transactions on average.

#### What is the riskiest technical assumption?

That the matching engine reaches 86% auto-match rate across the long tail of customer naming conventions. In beta with 14 firms, we saw 86% on the median firm but 62% on the worst-case firm (a contractor whose customers consistently used personal-account names that did not match invoice billing names). We need to ship a payor-aliasing UI to bring the floor up; that's tracked as a P0 in the PRD.

#### What experiments must run before we commit to a public launch?

(1) Closed beta with 50 firms across at least three verticals, target 80% auto-match floor — owner: ML team, due Feb 1, 2027. (2) Plaid rate negotiation with executed contract — owner: BD, due Jan 15, 2027. (3) Legal review of state-level money-transmitter exposure — owner: General Counsel, due Feb 15, 2027.

#### What is the smallest viable launch?

QuickBooks Online + Plaid + auto-match + exception review, US-only, English-only, no payments-on-account. Everything else is post-launch.

#### Who else has to ship something for this to work?

Plaid (rate contract — in negotiation), Intuit (we use their published API; no special partnership needed but their rate-limit policy could change), and our own platform team (need a new event bus for daily deposit ingestion — committed, on track for Jan 2027).

#### What regulatory or legal exposure does this create?

Reconcile does not move money — it only reads deposit data and posts ledger entries — so we believe we avoid money-transmitter licensing in all 50 states. General Counsel is confirming this state-by-state and the analysis is the gating item for the public-launch decision. We do hold financial transaction data, so SOC 2 Type I is in flight (target audit close: April 2027) and we will need a privacy notice that calls out Plaid's role explicitly.

#### How does this scale?

Today's architecture handles ~10,000 daily deposit events comfortably. At 100,000/day (roughly 30,000 paying customers), the matching service's database becomes the bottleneck and we'd need to shard by tenant. We have a design but have not built it. At 1M/day, we'd need to rebuild the deposit ingest pipeline as a streaming system — that's a 6-month project we have not started.

#### What are we choosing NOT to do?

We are choosing not to become a payments processor. We are choosing not to support enterprise customers (>250 active customers) in v1. We are choosing not to build our own accounting ledger — we integrate with existing tools rather than replacing them. Each of these is a deliberate scope cut, not an oversight.

#### What would cause us to abandon Reconcile?

(1) If the auto-match floor cannot exceed 75% on the worst-case firm even with payor aliasing, the value prop collapses and we kill it. (2) If Plaid rates rise to a point where gross margin drops below 50%, we cannot make the unit economics work at $29 and we kill it rather than reprice. (3) If state-level money-transmitter analysis comes back requiring licensure in more than 5 states, the compliance cost exceeds the addressable market over a 3-year horizon and we kill it.

#### What does success look like 12 months post-launch?

5,000 paying customers, $1.5M ARR, 86%+ median auto-match rate sustained, NPS above 40, and a signed Xero integration partnership. These targets seed the PRD's Success Metrics section.
