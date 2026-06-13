---
repo: project_dashboard_heroby
github_url: https://github.com/devzurc/project_dashboard_heroby
visibility: public
status: client-work
period: unknown
employer: unknown
role: Python automation and BI reporting workflow for HeroBy client dashboards
domains: [client-ops, bi, reporting-automation, iot-adjacent]
stack:
  - Python
  - AWS CLI
  - Boto3
  - Pandas
  - Psycopg2-binary
  - Openpyxl
  - XlsxWriter
  - python-dotenv
  - Excel
portfolio_worthy: false
cv_worthy: true
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/project_dashboard_heroby.md
---

# project_dashboard_heroby

> Curated as early BI/client-ops automation evidence. Raw README: `readmes/project_dashboard_heroby.md`

## One-liner

Python RPA/ETL workflow for extracting HeroBy platform data, preparing Excel dashboard files per company, and sending dashboards to clients by email.

## Problem

Client-facing dashboard reporting required data extraction, Excel dashboard preparation, validation against the web platform, and email distribution. The README documents a repeatable operating procedure rather than a polished product case study.

## What I built

- A Python menu flow to extract production data for a selected date range.
- Report folder outputs for dashboard workbooks, event data, and device data per client/company.
- Excel-based dashboard update steps using copied data, hidden event sheets, pivot tables, and charts.
- A test/send email flow for dashboard delivery to selected clients.

## Architecture

```text
AWS/platform data
  -> Python extraction menu
  -> reports/data and reports/devices Excel files
  -> per-company dashboard workbooks
  -> manual validation against web platform
  -> test email
  -> client dashboard email send
```

## Stack (verified)

Python, AWS CLI, Boto3, Pandas, Psycopg2-binary, Openpyxl, XlsxWriter, python-dotenv, Excel

## Outcomes

- No quantified outcome is verified in the README.
- Strong evidence of early-career BI/reporting automation for client operations, but avoid claiming production impact, employer, dates, or client counts from this repo alone.

## Evidence

- GitHub: https://github.com/devzurc/project_dashboard_heroby
- README: `readmes/project_dashboard_heroby.md`
- CV alignment: general BI/dashboard and automated reporting workflow experience appears in the resume, but this repo does not independently verify employer or dates.

## Notes for AI / alignment

- Keep `portfolio_worthy: false`; the repo is useful evidence, not a flagship portfolio card.
- Use as supporting CV evidence for Python + Excel BI automation and client dashboard operations.
- Do not invent employer, period, number of clients, or reduction metrics.
