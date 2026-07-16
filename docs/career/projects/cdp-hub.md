---
repo: cdp-hub
github_url: https://github.com/tktechnologies/cdp-hub
mirror_url: https://github.com/devzurc/cdp-hub
visibility: private
status: active
period: Feb 2026 - Present
period_note: "TK Technologies contract extended to 6 months; expected completion in Aug 2026."
employer: TK Technologies
role: Platform engineer - monorepo architecture, dual-pipeline orchestration, Azure deployment, workflow automation
domains: [automotive-parts, gen-ai, iot-adjacent, procurement-intelligence]
stack:
  - Python
  - FastAPI
  - Celery
  - Playwright
  - Redis
  - PostgreSQL
  - n8n
  - Google Sheets API
  - Gmail
  - Telegram
  - Docker
  - Azure Container Apps
  - Azure Bicep
  - JSON Schema
portfolio_worthy: true
cv_worthy: true
verified_outcomes:
  - Dual-pipeline SKU intelligence across public pricing data and internal stock lookup per batch
  - Workflow automation for chat, email, schedules, progress polling, and spreadsheet reporting
  - Monorepo with contracts, infrastructure, scraping, internal API, and automation components
links:
  demo:
  docs: https://github.com/tktechnologies/cdp-hub
last_synced: 2026-06-13
source_readme: readmes/cdp-hub.md
related_projects: [muvstok-api]
cv_alignment: Automotive Market Price Intelligence Platform (TK Technologies)
public_safety: Live webhook URLs, workflow identifiers, cloud resource names, vault names, secret names, and environment variable names are omitted.
---

# CDP Platform (cdp-hub)

> **CDP** - automotive parts intelligence platform. Monorepo orchestrating public pricing search, internal stock lookup, workflow automation, and spreadsheet/chat delivery.

## One-liner

End-to-end platform that ingests SKU requests from chat, email, schedules, or spreadsheets; runs **parallel public pricing search and internal stock lookup**; and delivers structured pricing intelligence through automated reporting and notifications.

## Problem

Procurement teams need competitive automotive parts pricing across supplier sites and internal stock systems. Manual lookup is slow, error-prone, and difficult to audit consistently.

## What I built

- **Monorepo architecture** across scraping, internal stock lookup, workflow automation, contracts, and infrastructure.
- **Workflow automation** for chat/email intake, scheduled runs, progress polling, receiver handoff, and final notifications.
- **Dual pipeline dispatch** that runs public pricing search and internal stock lookup for the same SKU batch with shared run tracking.
- **Spreadsheet reporting** with detailed, historical, summary, and dashboard-style views while keeping outcome types distinct.
- **Azure deployment model** using containerized services, managed secrets, and infrastructure-as-code.
- **Contract-driven result handling** to keep pricing outcomes auditable across services.

## Architecture

```text
Chat / email / spreadsheet / schedule intake
  -> workflow automation router
      -> public pricing search service -> background workers -> result receiver
      -> internal stock lookup service -> queue workers -> result receiver
  -> spreadsheet reporting
  -> aggregate notifications
```

## Stack (verified)

Python · FastAPI · Celery · Playwright · Redis · PostgreSQL · n8n · Google Sheets · Telegram · Docker · Azure Container Apps · Bicep · JSON Schema contracts

## Outcomes

- Built and operated during the current TK Technologies engagement, Feb 2026 - Present; contract expected through Aug 2026.
- Parallel public price search and internal stock enrichment per SKU batch.
- Structured reporting contract distinguishes found-price, no-price, not-found, blocked, timeout, and error outcomes.

## Evidence

- Mirror (private): https://github.com/devzurc/cdp-hub
- Public org repo: https://github.com/tktechnologies/cdp-hub
- README: `readmes/cdp-hub.md`

## Notes for AI / alignment

- Strongest portfolio narrative for **Gen. AI Engineer + Data Engineer** work at TK Technologies.
- Surface the internal stock lookup service as a component of this platform, not as a duplicate standalone portfolio card.
- Public-safe summary only: live webhook URLs, workflow IDs, cloud resource names, vault names, secret names, and environment variable names are intentionally omitted.
