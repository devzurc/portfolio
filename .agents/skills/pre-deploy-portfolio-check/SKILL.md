---
name: pre-deploy-portfolio-check
description: Run the final static portfolio release gate for facts, accessibility, responsive behavior, SEO, performance regressions, and scope. Use before a commit or deployment.
---

# Pre-deploy portfolio check

## Inputs

Current diff, deployment target, and known change scope.

## Workflow

1. Inspect `git diff --check` and the changed files for unrelated scope or public-fact regressions.
2. Verify EN/PT parity, keyboard behavior, responsive layout at 390/768/1440, static SEO/crawl files, and critical assets.
3. Run relevant local checks and compare performance only when an equivalent baseline is available.
4. Have QA report pass/fail independently of the implementation owner.

## Output

Return release status, evidence, blockers, deferred risks, and a suggested Conventional Commit message. Do not commit or deploy without explicit instruction.
