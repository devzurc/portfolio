---
repo: cnpj-lakehouse
github_url: https://github.com/devzurc/cnpj-lakehouse
github_ref: devzurc/cnpj-lakehouse
visibility: public
status: learning
period: Sep 2026
employer: Personal / challenge
role: Data engineer — local-first lakehouse delivery
domains: [data-engineering, lakehouse, public-data]
stack: [Python, Prefect, dbt Core, DuckDB, Docker, uv]
portfolio_worthy: true
cv_worthy: false
verified_outcomes:
  - "January 2026 sample verified by aggregate counts in the README: 10,000 companies, 10,349 establishments, 4,057 partners. This is a deterministic sample, not the full CNPJ registry."
  - "Gold dashboard shows aggregates only (UF, CNAE, tax regime, capital, totals), not raw CNPJ rows."
  - "BigQuery appears only as a FinOps design document. No cloud project is provisioned. The README states there is no Spark or Dask."
links:
  demo:
  docs: https://github.com/devzurc/cnpj-lakehouse
renamed_from: franq-data-lakehouse-challenge
last_synced: 2026-10-05
source_readme: readmes/cnpj-lakehouse.md
---

# cnpj-lakehouse

> Public personal challenge. Formerly `franq-data-lakehouse-challenge` (GitHub rename). Site card approved 2026-10-05 as personal proof, not a client system and not a CV notable project.

## One-liner

Local-first GOV.BR CNPJ lakehouse: public mirror → Prefect ingest → Bronze/Silver/Gold on DuckDB, with dbt SCD2 snapshots and a Gold-only dashboard.

## Problem

Deliver a reproducible CNPJ analytics lakehouse without putting source extracts in Git, while keeping lineage, tests, and a read-only consumption layer.

## What I built (from public README)

- Prefect flow for monthly ingest from the public CNPJ mirror, with SHA-256 manifests and a deterministic 10,000-company sample.
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

Python · Prefect · dbt Core · DuckDB · Docker · uv.

Do not list Spark, RAG, or a provisioned GCP/BigQuery project. The auto-stub inferred those from README words that describe limits, not the running stack.

## Outcomes

- January 2026 sample, verified by aggregate counts in the README: 10,000 companies, 10,349 establishments, 4,057 partners.
- The runnable delivery is a sample. Annual 2026 backfill (`S12-01`) is still blocked.
- README records about 2h26 for one official sample month (download + ranking). Do not promote that duration as a production SLA.

## Public-safe scope note

Portfolio card: personal project, with the GitHub link and the 10,000-company sample limit. Keep it off CV Notable Projects. dbt, Prefect, and DuckDB belong in a labs skills line, not in the production stack.
