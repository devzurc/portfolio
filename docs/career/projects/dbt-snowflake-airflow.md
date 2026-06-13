---
repo: dbt-snowflake-airflow
github_url: https://github.com/devzurc/dbt-snowflake-airflow
visibility: public
status: learning
period: unknown
employer: Personal
role: Data engineering learner - reproduced a dbt + Snowflake + Airflow tutorial workflow
domains: [data-engineering, analytics-engineering, learning-lab]
stack:
  - Python
  - SQL
  - Apache Airflow
  - dbt
  - Snowflake
  - Docker
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/dbt-snowflake-airflow.md
---

# dbt-snowflake-airflow

> Curated as a **learning/tutorial project**. Raw README: `readmes/dbt-snowflake-airflow.md`

## One-liner

Learning lab that connects dbt to Snowflake and orchestrates dbt work from Apache Airflow running in Docker.

## Problem

Practice the mechanics of an analytics engineering workflow: configure Snowflake access, load seed data with dbt, containerize dbt, and trigger it from Airflow.

## What I built

- Followed a Snowflake/Airflow/dbt guide to assemble a local tutorial repository.
- Configured Docker Compose for Airflow.
- Documented dbt setup against Snowflake, including profile configuration, `dbt debug`, and `dbt seed`.
- Built a Docker image for running dbt commands and documented Airflow DAG execution.

## Architecture

```text
CSV seed data
  -> dbt seed / dbt project
  -> Snowflake tables/views
  -> dbt container
  -> Airflow DAG orchestration
```

## Stack (verified)

Python · SQL · Apache Airflow · dbt · Snowflake · Docker

## Outcomes

- No employer, client, production deployment, or business impact is verified.
- Do not present this as professional delivery; use only as evidence of hands-on learning with dbt, Snowflake, and Airflow.

## Evidence

- GitHub: https://github.com/devzurc/dbt-snowflake-airflow
- README: `readmes/dbt-snowflake-airflow.md`
- README states the project is based on an external Snowflake guide for data engineering with Apache Airflow, Snowflake, and dbt.

## Notes for AI / alignment

- Keep `portfolio_worthy` and `cv_worthy` false unless owner adds evidence that this became original or production work.
- Do not infer Kafka usage from references; the README evidence verifies Airflow, dbt, Snowflake, Docker, Python, and SQL only.
