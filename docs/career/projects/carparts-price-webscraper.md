---
repo: carparts-price-webscraper
github_url:
github_ref:
visibility: private
status: archived
period: 2025 - 2026
period_note: "Superseded by cdp-hub monorepo; README evidence merged into CDP platform profile."
employer: TK Technologies
role: Pre-monorepo automotive parts scraping API (FastAPI, Playwright, PostgreSQL, n8n)
domains: [automotive-parts, scraping, private-client-automation]
stack:
  - Python
  - FastAPI
  - Playwright
  - PostgreSQL
  - Redis
  - n8n
  - Docker
  - Azure
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-17
source_readme: readmes/carparts-price-webscraper.md
related_projects: [cdp-hub, muvstok-api]
---

# carparts-price-webscraper

> **Archived** — early CDP scraping service superseded by `cdp-hub`. Do not surface as a separate public project.

## One-liner

Private FastAPI + Playwright scraping service for automotive parts price comparison, later consolidated into the CDP platform monorepo.

## Problem

Automotive pricing intelligence needed programmatic scraping, persistence, and n8n integration before the platform moved into the unified CDP monorepo.

## What I built

- FastAPI job orchestration with Playwright-based scrapers
- PostgreSQL persistence and n8n callback integration
- Azure deployment patterns later carried into CDP platform work

## Architecture

```text
n8n / client  ->  FastAPI  ->  scrapers  ->  PostgreSQL  ->  callback to n8n
```

## Stack (verified)

Python · FastAPI · Playwright · PostgreSQL · Redis · n8n · Docker · Azure

## Outcomes

- Evidence of early CDP scraping architecture; public narrative belongs under `cdp-hub` only

## Evidence

- GitHub: private repo (archived for career knowledge)
- README: `readmes/carparts-price-webscraper.md`
- Successor profile: `projects/cdp-hub.md`

## Notes for AI / alignment

- Keep `portfolio_worthy` and `cv_worthy` false
- Do not duplicate CDP bullets on CV or portfolio
- Product/client names from README must not appear on public surfaces
