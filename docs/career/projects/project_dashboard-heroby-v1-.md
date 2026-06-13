---
repo: project_dashboard-heroby-v1-
github_url: https://github.com/devzurc/project_dashboard-heroby-v1-
visibility: public
status: archived
period: unknown
employer: unknown
role: Old Python automation workflow for HeroBy dashboard reporting
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
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/project_dashboard-heroby-v1-.md
---

# project_dashboard-heroby-v1-

> Archived old version. Raw README: `readmes/project_dashboard-heroby-v1-.md`

## One-liner

Old version of the HeroBy dashboard automation workflow for extracting platform data, updating Excel dashboards, and sending client emails.

## Problem

The README describes the same client dashboard operations pattern as the later HeroBy dashboard repo: extract incident/device data, prepare company dashboard workbooks, validate the numbers, and send dashboard emails.

## What I built

- Installation and operation flow for the original auto-dashboard repo.
- Python-driven extraction for a selected production date range.
- Excel workbook preparation steps for per-company dashboards, event data, and device data.
- Test-first dashboard email delivery workflow.

## Architecture

```text
Production platform data
  -> Python extraction menu
  -> reports/dashboard, reports/data, reports/devices
  -> manual Excel dashboard refresh
  -> validation against platform
  -> test/client email send
```

## Stack (verified)

Python, AWS CLI, Boto3, Pandas, Psycopg2-binary, Openpyxl, XlsxWriter, python-dotenv, Excel

## Outcomes

- No quantified outcome is verified in the README.
- README explicitly labels this as an "old version", so treat it as archived historical evidence rather than an active project.

## Evidence

- GitHub: https://github.com/devzurc/project_dashboard-heroby-v1-
- README: `readmes/project_dashboard-heroby-v1-.md`

## Notes for AI / alignment

- Superseded by `project_dashboard_heroby`; do not list as a standalone CV or portfolio project.
- Useful only as provenance for early BI/client-ops automation.
- Do not invent employer, period, metrics, or current production status.
