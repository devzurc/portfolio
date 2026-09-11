---
repo: franq-data-lakehouse-challenge
github_url: https://github.com/devzurc/franq-data-lakehouse-challenge
github_ref: devzurc/franq-data-lakehouse-challenge
visibility: public
status: learning
period: Sep 2026
employer: Personal / challenge
role: Data engineer — local-first lakehouse delivery
domains: [data-engineering, lakehouse, public-data]
stack: [Python, Prefect, dbt Core, DuckDB, Docker, uv]
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs: https://github.com/devzurc/franq-data-lakehouse-challenge
last_synced: 2026-09-11
source_readme: readmes/franq-data-lakehouse-challenge.md
---

# franq-data-lakehouse-challenge

> Public challenge repo. Evidence for lakehouse/orchestration skills only. Not a CV notable project or portfolio card until the owner promotes it.

## One-liner

Local-first GOV.BR CNPJ lakehouse: public mirror → Prefect ingest → Bronze/Silver/Gold on DuckDB, with dbt SCD2 snapshots and a Gold-only dashboard.

## Problem

Deliver a reproducible CNPJ analytics lakehouse without putting source extracts in Git, while keeping lineage, tests, and a read-only consumption layer.

## What I built (from public README)

- Prefect flow for monthly ingest from the public CNPJ mirror, with SHA-256 manifests and sample sizing.
- Medallion layers on DuckDB: append-only Bronze, dbt Silver hygiene/joins, SCD2 capital-social snapshot, Gold dimensions + fact.
- Docker Compose stack (Prefect UI + Gold dashboard). Dashboard shows UF/CNAE aggregates only — not CNPJ rows.
- Verify path (`./scripts/docker.sh verify`) for counts without printing raw lines.

## Architecture

```text
Public CNPJ mirror
  --> Prefect ingest + manifests
  --> Bronze (immutable)
  --> dbt Silver
  --> dbt snapshot SCD2
  --> Gold (dimensions + fact)
  --> read-only dashboard
```

## Stack (verified)

Python · Prefect · dbt Core · DuckDB · Docker · uv. README states there is no Spark/Dask and no GCP provision in the repo.

## Outcomes

None published as metrics. Do not invent runtime, row counts, or challenge scores.

## Public-safe scope note

Keep off the CV and portfolio until the owner confirms it should be a notable project. Useful interview evidence for lakehouse + orchestration while the Senior AI platform capstones are still planned.
