---
repo: project_etl_emissaoCO2
github_url: https://github.com/devzurc/project_etl_emissaoCO2
visibility: public
status: learning
period: unknown
employer: Personal
role: Data engineering learner - Pandas/PyArrow ETL and Medallion layout
domains: [data-engineering, sustainability-data, learning-lab]
stack:
  - Python
  - Pandas
  - PyArrow
  - Parquet
  - Logging
  - Medallion Architecture
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/project_etl_emissaoCO2.md
---

# project_etl_emissaoCO2

> Curated as a **learning/lab project**. Raw README: `readmes/project_etl_emissaoCO2.md`

## One-liner

Learning ETL lab that transforms a CO2 emissions CSV into Bronze, Silver, and Gold Parquet outputs for analysis.

## Problem

Practice file-based ETL and medallion-style data organization using a public/sample CO2 emissions dataset.

## What I built

- Python pipeline that converts raw CSV data to Parquet.
- Bronze/Silver/Gold folder layout for raw, cleaned, and analysis-ready data.
- Pandas/PyArrow transformations for column normalization, type cleanup, and aggregate outputs.
- Logging for pipeline execution.

## Architecture

```text
CO2 emissions CSV
  -> Bronze Parquet
  -> Silver cleaned/standardized Parquet
  -> Gold analytical aggregates
  -> Notebook/BI-style analysis
```

## Stack (verified)

Python · Pandas · PyArrow · Parquet · Logging · Medallion Architecture

## Outcomes

- No employer, client, production deployment, or business impact is verified.
- Do not treat README scenario language about a company/team as evidence of client work.

## Evidence

- GitHub: https://github.com/devzurc/project_etl_emissaoCO2
- README: `readmes/project_etl_emissaoCO2.md`
- README verifies a CSV-to-Parquet ETL lab with Bronze/Silver/Gold folders and logging.

## Notes for AI / alignment

- `RAG` was removed from the verified stack because the README evidence does not support it.
- Keep `portfolio_worthy` and `cv_worthy` false unless owner provides original project context or stronger evidence.
