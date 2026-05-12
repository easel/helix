---
name: helix-commit
description: Create a traceable commit, run the project gate, push, and update tracked work when applicable.
argument-hint: '[issue-id]'
---

# Commit: HELIX-Compliant Git Commit

Create a well-formatted commit with issue traceability, run the project's build
gate, push, and optionally update the work tracker.

## When to Use

- after implementing a tracked work item
- when you need a properly formatted commit message
- when an agent needs commit support
- when session completion requires local work to land remotely

## What It Does

1. **Inspect** staged changes.
2. **Format** the commit message:
   - First line: `<issue-id> <concise summary>` under 72 chars when an ID exists
   - Body: what changed and why, with governing artifact references
   - Trailer: verification commands run
3. **Pre-push gate**: run the project's required quality check before pushing.
4. **Commit and push**: create the commit, rebase on the remote branch, and push.
5. **Tracker update**: close or update the work item when an issue ID is provided.

## Commit Message Format

```text
hx-abc123 Short summary of the change

Longer description of what changed and why. Reference governing
artifacts when relevant (SD-001, TP-002, etc.).

Verification: cargo test -p changed-crate, cargo clippy
```

## Running with DDx

The current HELIX wrapper provides these commands:

```bash
helix commit hx-abc123      # commit, gate, push, close issue
helix commit                # commit and gate without tracker update
```

Typical project gates include:

```bash
lefthook run pre-commit
cargo check --workspace
npm test
```
