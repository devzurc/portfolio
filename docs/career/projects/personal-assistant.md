---
repo: personal-assistant
github_url:
github_ref:
visibility: private
status: private-evidence
parked: true
parked_on: 2026-10-18
parked_reason: Private personal project; no public CV or portfolio copy until owner publication permission.
period: Oct 2026
employer: Personal
role: Full-stack engineer — local-first productivity workspace and daily sync pipeline
domains: [productivity, local-first, data-sync]
stack:
  - TypeScript
  - Next.js
  - SQLite
  - Node.js
  - Google Calendar API
  - Gmail API
  - Google Tasks API
  - Jira API
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-10-18
source_readme: readmes/personal-assistant.md
---

# personal-assistant

> **Parked 2026-10-18.** Private evidence only. Do not add to CV or `index.html` until the owner confirms publication permission.

## One-liner

Local-first personal productivity workspace unifying Google Calendar, Gmail, Google Tasks, and Jira with idempotent daily SQLite sync.

## Problem

Consolidate daily calendar events, unread emails, tasks, and Jira tickets into a fast local-first workspace without waiting on live API calls.

## What I built

- Next.js dashboard for daily/weekly/monthly schedule, inbox, tasks, Jira, projects, and leads views.
- Idempotent daily sync script (`npm run sync`) persisting raw payloads, normalized rows, and daily facts in SQLite (`data/assistant.db`).
- Cron-ready Linux/WSL execution wrapper and type-checked build pipeline.

## Architecture

```text
Google Calendar / Gmail / Google Tasks / Jira APIs
  --> idempotent daily sync script (cron)
  --> SQLite (raw payloads + normalized rows + daily facts)
  --> Next.js local-first web workspace
```

## Stack (verified)

TypeScript · Next.js · SQLite · Node.js · Google Calendar API · Gmail API · Google Tasks API · Jira API

## Outcomes

_Parked as private evidence; no public claims._

## Evidence

- Repository: private — sanitized evidence only
- README: `readmes/personal-assistant.md`

## Notes for AI / alignment

- [ ] Keep off public CV and portfolio unless owner approves public release
