---
repo: spacecom-iot-lakehouse
github_url:
visibility: private
status: client-work
period: 2023-04 - 2024-07
employer: Spacecom Monitoramento
role: Data Engineer - AWS S3 lakehouse, PySpark/Delta pipelines, Trino/BI enablement, LGPD/GDPR handling
domains: [iot, lakehouse, data-governance, analytics-engineering]
stack:
  - AWS S3
  - PySpark
  - Delta Lake
  - Parquet
  - Apache Airflow
  - Trino
  - Apache Superset
  - Qlik Sense
  - LGPD/GDPR data handling
portfolio_worthy: true
cv_worthy: true
verified_outcomes:
  - Supported IoT platform scale of 95K+ devices
  - Processed hundreds of millions of records per day
  - Delivered curated datasets to Apache Superset and Qlik Sense dashboards
  - Handled sensitive telemetry data under LGPD/GDPR requirements
links:
  demo:
  docs:
last_synced: 2026-06-12
source_evidence:
  - docs/resume/source/LucasCruz_CV_EN.txt
  - docs/resume/source/LucasCruz_CV_PT.txt
cv_alignment: Spacecom Monitoramento - Data Engineer
confidentiality: Sanitized from CV facts only; no internal schemas, customer names, credentials, endpoints, or proprietary implementation details.
---

# Spacecom IoT Lakehouse

> Sanitized professional project profile based only on CV-backed facts.

## One-liner

AWS S3 IoT lakehouse using Medallion Architecture, PySpark, Delta Lake, Parquet, Trino, Airflow, and BI delivery for high-volume telemetry analytics.

## Problem

Spacecom needed reliable analytics-ready data for a high-volume IoT platform while handling sensitive telemetry under LGPD/GDPR requirements.

## What I built

- Designed and maintained a Big Data Lakehouse on AWS S3.
- Organized data using Medallion Architecture: Bronze, Silver, and Gold layers.
- Built/maintained PySpark pipelines using Delta Lake and Parquet.
- Used Apache Airflow for orchestration.
- Used Trino for analytical access to curated data.
- Delivered datasets for Apache Superset and Qlik Sense dashboards.
- Supported privacy-aware handling of sensitive telemetry data under LGPD/GDPR requirements.

## Architecture

```text
IoT telemetry
  -> AWS S3 Bronze layer
  -> PySpark + Delta Lake / Parquet processing
  -> AWS S3 Silver and Gold layers
  -> Trino analytical access
  -> Apache Superset / Qlik Sense dashboards
```

## Stack (verified)

AWS S3 · PySpark · Delta Lake · Parquet · Apache Airflow · Trino · Apache Superset · Qlik Sense · LGPD/GDPR data handling

## Outcomes

- Supported IoT platform scale of 95K+ devices.
- Processed hundreds of millions of records per day.
- Delivered curated datasets to Superset and Qlik dashboards.
- Maintained LGPD/GDPR-aware handling for sensitive telemetry data.

## Evidence

- CV source: `docs/resume/source/LucasCruz_CV_EN.txt`
- CV source: `docs/resume/source/LucasCruz_CV_PT.txt`
- User-provided curation brief for this shard: use only CV facts for Spacecom profile.

## Notes for AI / alignment

- Strongest data/lakehouse CV proof point; keep `cv_worthy` and `portfolio_worthy` true.
- Do not add unverified metrics such as accuracy improvement unless separately approved.
- Keep customer-specific, judicial, schema, endpoint, access-control, and operational details out of public portfolio copy unless separately cleared.
