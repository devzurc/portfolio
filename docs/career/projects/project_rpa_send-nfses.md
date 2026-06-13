---
repo: project_rpa_send-nfses
github_url: https://github.com/devzurc/project_rpa_send-nfses
visibility: public
status: client-work
period: unknown
employer: unknown
role: Python RPA for HeroBy client billing email operations
domains: [client-ops, billing-automation, rpa]
stack:
  - Python
  - Email automation
portfolio_worthy: false
cv_worthy: true
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/project_rpa_send-nfses.md
---

# project_rpa_send-nfses

> Curated as early client-ops/RPA automation evidence. Raw README: `readmes/project_rpa_send-nfses.md`

## One-liner

Python RPA for sending client billing emails with NFSe attachments for customers registered on the HeroBy platform.

## Problem

Billing operations needed a repeatable way to locate saved NFSe files and send the corresponding invoice attachments/descriptions to registered platform clients.

## What I built

- A Python RPA flow for billing email delivery.
- A convention for placing NFSe files in a local `nfse` folder so the system can locate and route attachments.
- Menu options for test/client billing email sends and a planned measurement email flow.

## Architecture

```text
nfse folder
  -> Python RPA menu
  -> match existing NFSe files to registered HeroBy clients
  -> send billing email with attachments and description
```

## Stack (verified)

Python, email automation

## Outcomes

- No quantified outcome is verified in the README.
- README states the measurement email flow was still in development, and the repo itself was marked in development.

## Evidence

- GitHub: https://github.com/devzurc/project_rpa_send-nfses
- README: `readmes/project_rpa_send-nfses.md`
- CV alignment: general invoice/report automation appears in the resume, but this repo does not independently verify employer or dates.

## Notes for AI / alignment

- Keep `portfolio_worthy: false`; useful as supporting evidence for early Python RPA/client operations.
- If surfaced on CV, describe cautiously as billing email automation, not as a completed end-to-end invoicing platform.
- Do not invent employer, period, client count, delivery volume, or impact metrics.
