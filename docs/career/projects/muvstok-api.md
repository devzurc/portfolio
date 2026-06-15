---
repo: muvstok-api
github_url: https://github.com/tktechnologies/cdp-hub/tree/main/muvstok-api
mirror_url: https://github.com/tktechnologies/cdp-hub
visibility: public-safe summary
status: active
period: Feb 2026 - Present
period_note: "TK Technologies contract extended to 6 months; expected completion in Aug 2026."
employer: TK Technologies
role: Backend engineer - FastAPI job API, Redis Streams workers, PostgreSQL persistence, Azure container deployment
domains: [automotive-parts, api-design, data-ingestion]
stack:
  - Python 3.12
  - FastAPI
  - Pydantic v2
  - PostgreSQL
  - SQLAlchemy 2.x
  - Alembic
  - Redis Streams
  - Azure Container Apps
  - Managed cloud secrets
  - n8n
  - Docker
portfolio_worthy: false
cv_worthy: true
verified_outcomes:
  - Async job API with Redis Streams worker and PostgreSQL persistence
  - Integrated into the CDP dual pipeline through workflow automation and result receivers
  - Deployed as separate containerized API and worker services on Azure
links:
  demo:
  docs: https://github.com/tktechnologies/cdp-hub/tree/main/muvstok-api
last_synced: 2026-06-13
source_readme: readmes/muvstok-api.md
parent_monorepo: cdp-hub
related_projects: [cdp-hub]
public_safety: Live endpoint URLs, webhook paths, workflow identifiers, cloud resource names, vault names, secret names, and environment variable names are omitted.
---

# Internal Stock Lookup API (muvstok-api)

> Internal automotive stock SKU lookup service inside the CDP monorepo, built with async workers and workflow-automation callbacks.

## One-liner

FastAPI + Redis Streams + PostgreSQL component that accepts SKU batches, processes internal stock lookups, and returns normalized results to the CDP reporting pipeline.

## Problem

Internal stock data needed to be queried alongside public pricing data for the same SKU batch, with reliable async processing and auditable results.

## What I built

- Authenticated async job ingestion for SKU batches and callback configuration.
- Redis Streams consumer group with sequential SKU processing.
- PostgreSQL persistence with async SQLAlchemy and Alembic migrations.
- Workflow automation integration through a result receiver used by the CDP reporting pipeline.
- Azure deployment pattern for separate API and worker containers with managed secrets.

## Architecture

```text
CDP workflow automation
  -> authenticated stock lookup job submission
  -> Redis Streams queue -> stock lookup worker
  -> PostgreSQL persistence
  -> result callback -> reporting + notification pipeline
```

## Stack (verified)

Python 3.12 · FastAPI · Pydantic v2 · PostgreSQL · SQLAlchemy · Alembic · Redis Streams · Azure Container Apps · managed cloud secrets · n8n · Docker

## Outcomes

- Backend service for the internal-stock leg of the CDP dual pipeline.
- Job progress surfaced through status responses for workflow automation.
- Contract-driven callbacks shared through JSON Schema definitions.

## Evidence

- Path in monorepo: `muvstok-api/`
- README: `readmes/muvstok-api.md`
- Parent: `projects/cdp-hub.md`

## Notes for AI / alignment

- Not a standalone portfolio card; reference as a **component of CDP** on CV/portfolio.
- Mention under TK Technologies / automotive intelligence platform work.
- Public-safe summary only: exact routes, webhook paths, workflow IDs, cloud resource names, vault names, secret names, and environment variable names are intentionally omitted.
