---
repo: marketing-socialmedia-app
github_url: https://github.com/devzurc/marketing-socialmedia-app
github_ref: devzurc/marketing-socialmedia-app
visibility: private
status: active
period: 2025 - ongoing
period_note: "TK Technologies social-media runtime; Instagram-first scope with PostgreSQL socialmedia schema and Redis state layer."
employer: TK Technologies
role: Social media automation platform - n8n workflows, PostgreSQL schema, Redis, Azure infra
domains: [social-media, marketing-automation, gen-ai-adjacent, private-client-automation]
stack:
  - n8n
  - PostgreSQL
  - PL/pgSQL
  - Redis
  - Docker
  - Azure
  - Python
portfolio_worthy: false
cv_worthy: false
verified_outcomes:
  - Greenfield socialmedia schema with migrations and Redis design docs
  - Instagram-first n8n workflow exports with spec-driven maintenance
links:
  demo:
  docs:
last_synced: 2026-06-17
source_readme: readmes/marketing-socialmedia-app.md
related_projects: [n8n-instagram-assistant]
repo_access: "Private/sanitized; no public repository link."
---

# marketing-socialmedia-app

> Private TK Technologies social-media runtime — Instagram-first n8n automations with PostgreSQL `socialmedia.*` and Redis-backed state.

## One-liner

Monorepo for social-media workflow automation, database schema, Azure infrastructure, and dashboard scaffolding for Instagram Direct and comment handling.

## Problem

Social operations needed durable workflow automation, shared runtime state, and a maintainable data model beyond one-off n8n exports.

## What I built

- PostgreSQL `socialmedia.*` schema with migrations and Redis design
- n8n workflow exports and Azure Container Apps deployment scaffolding
- Spec-driven maintenance under `.agent/` source-of-truth docs
- Test fixtures and traceability for webhook payloads

## Architecture

```text
Instagram events  ->  n8n workflows  ->  PostgreSQL socialmedia.* + Redis state
```

## Stack (verified)

n8n · PostgreSQL · PL/pgSQL · Redis · Docker · Azure · Python

## Outcomes

- Supporting evidence for social automation work; public narrative stays under sanitized automation bullets, not product names
- Closely related to `n8n-instagram-assistant` workflow exports

## Evidence

- Repository: private client/internal repo, not linked in public portfolio
- Sanitized README: `readmes/marketing-socialmedia-app.md`

## Notes for AI / alignment

- Keep off portfolio and CV unless owner adds a compact social-platform line
- Public copy must not expose product/client names, webhook URLs, or workflow IDs
- Use `n8n-instagram-assistant` for workflow-specific evidence
