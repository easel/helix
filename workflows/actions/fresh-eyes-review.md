# HELIX Action: Fresh-Eyes Review

You are performing a self-review of recently completed work, looking for bugs,
omissions, and quality issues with fresh perspective.

After implementing a bead, 1-3 review passes catch bugs that implementation
blindness misses. Each pass focuses on a different failure mode.

## Action Input

You may receive:

- no argument (default: `last-commit`)
- `last-commit` — review the most recent commit
- a bead ID such as `bd-abc123` — review all changes associated with that bead
- a file list — review those specific files

Examples:

- `helix review`
- `helix review last-commit`
- `helix review bd-abc123`
- `helix review src/auth/`

## PHASE 0 - Identify Review Target

0. **Context Recovery**: Re-read AGENTS.md so project instructions are fresh
   in your working memory. After long sessions, context compaction may have
   dropped critical project rules. This step is cheap insurance against drift.
1. Determine what was just implemented:
   - If `last-commit` or no argument: `git diff HEAD~1`
   - If bead ID: load the bead, find associated commits via bead ID in commit
     messages, compute the aggregate diff
   - If file paths: review those files in their current state
2. Load the governing artifacts for the reviewed code (acceptance criteria,
   test plans, design docs).

## Pass 1 - Correctness Review

For every changed function or method:

1. Does it handle all error cases documented in the design?
2. Are edge cases covered (empty input, null, boundary values, overflow)?
3. Does it match the acceptance criteria from the governing bead?
4. Are return values and error codes consistent with interface contracts?
5. Are there off-by-one errors, missing bounds checks, or unclosed resources?

For every changed test:

1. Does it actually test what it claims to test?
2. Are assertions specific enough to catch regressions?
3. Could the test pass even if the code were broken (tautological assertion)?
4. Are error paths tested, not just the happy path?

## Pass 2 - Integration Review

1. How do the changes interact with existing code paths?
2. Are there race conditions, deadlocks, or ordering dependencies?
3. Are there missing imports, broken references, or stale caches?
4. Do configuration changes propagate correctly?
5. Are database migrations reversible?
6. Do API changes maintain backward compatibility where required?

## Pass 3 - Security and Performance Review (when applicable)

1. Are there injection vulnerabilities (SQL, command, XSS, template)?
2. Are there authentication or authorization bypasses?
3. Is sensitive data logged, cached, or exposed in error messages?
4. Are there O(n^2) loops, unbounded allocations, or missing pagination?
5. Are there unnecessary network calls in hot paths?

Skip this pass when changes are purely documentation, configuration, or
internal refactoring with no new attack surface or performance impact.

## Output

For each issue found, report:

- **File and line**: exact location
- **Category**: bug, security, performance, correctness, integration
- **Severity**: critical, high, medium, low
- **Description**: what is wrong
- **Suggested fix**: how to resolve it

Report these trailer lines at the end of your output:

```
REVIEW_STATUS: CLEAN|ISSUES_FOUND
ISSUES_COUNT: N
```

- `CLEAN`: no issues found across all passes
- `ISSUES_FOUND`: one or more issues identified

If issues are found with severity `critical` or `high`, recommend that the
associated bead be reopened or a regression bead be created.
