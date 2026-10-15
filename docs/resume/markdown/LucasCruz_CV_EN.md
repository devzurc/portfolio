---
lang: en
title: Lucas Cruz — CV (English)
google_doc: https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit
pdf: ../pdf/LucasCruz_CV_EN.pdf
word: ../word/LucasCruz_CV_EN.docx
last_synced: 2026-09-22
last_updated: 2026-10-06
sync_source: markdown-built-pdf-pending-google-paste
---

# LUCAS CRUZ

**AI Engineer / Senior Data Engineer**

dev.lucascruz@gmail.com · linkedin.com/in/lucas-cruz · devzurc.github.io/portfolio

Curitiba, Paraná, Brazil

## Professional Summary

AI engineer and senior data engineer with ~5 years in data engineering, building on earlier data-analyst experience, working across frontend, full-stack, backend, and AI automation. At TK Technologies, designed and built an automotive-parts pricing and stock data platform (async Python, n8n, Azure) and built frontend and full-stack features for a multi-model generative-AI chat platform (React, TypeScript, Tailwind). Previously built Python/SQL pipelines, Airflow-orchestrated ETL, data warehouses, and AWS lakehouses (Medallion, Delta Lake, Trino) for IoT, fintech, and agribusiness, handling LGPD/GDPR-governed data. Personal projects include a multi-tenant CRM with AI draft replies (FastAPI, Next.js, PostgreSQL), a local-first lakehouse (Prefect, dbt Core, DuckDB), and production RAG with pgvector (in progress). English: IELTS B2 (2025), self-assessed near C1.

## Technical Skills

| Category | Skills |
|----------|--------|
| AI data & LLM apps | LLM integration (Claude, Google AI Studio), AI automation, AI coding agents, conversational data querying, n8n, prompt design, chatbots, Meta Cloud API |
| Data engineering | Python, SQL, Pandas, Apache Spark (PySpark), Airflow, ETL/ELT, dimensional modelling, Delta Lake, Parquet, Trino, REST API ingestion, JSON Schema contracts, webhooks, Playwright, web scraping |
| Frontend & full-stack | React 18, TypeScript, Vite, Tailwind CSS, Figma-to-UI, Next.js, NestJS, FastAPI |
| Cloud & delivery | AWS, Azure, GCP, OCI, Docker, Azure Container Apps, Azure App Service, Bicep, Celery, Redis Streams, n8n, Git, GitHub Actions CI/CD |
| Databases & BI | PostgreSQL, SQL Server, Oracle Autonomous Database, Power BI, Qlik Sense, Apache Superset |
| Governance | LGPD/GDPR, RBAC, data privacy |
| Labs (not client production) | dbt Core, Prefect, DuckDB, Snowflake, pgvector/RAG (in progress) |
| Languages | Portuguese (Native) · English (IELTS B2 (2025), self-assessed near C1) · Spanish (B1 – Intermediate) |

## Work Experience

### Gen AI Engineer (AI Data & Full-Stack Engineering) — TK Technologies | Curitiba, PR – Brazil (Hybrid) · Feb 2026 – Present · Contract

- Designed and built, nearly alone, an automotive-parts pricing and stock data platform that takes SKU requests from chat, email, schedules, and spreadsheets and runs web scraping and internal inventory lookups in parallel.
- Built async Python services (FastAPI, Celery, Redis Streams, Playwright) with caching, JSON Schema contracts, and webhook callbacks, orchestrated with n8n.
- Deployed separate dev and prod environments on Azure with Bicep IaC, containers, and GitHub Actions CI/CD, adding health checks, outage guardrails, quotas, and access control.
- Delivered automated spreadsheet reporting and dashboards with clear outcome statuses and Telegram/email notifications, using AI coding agents throughout.
- Built a full-stack web workspace for the automotive-parts pricing platform: a React + TypeScript + Vite + Tailwind frontend with chat-based SKU lookups, results tables and an executive analytics dashboard (KPIs, catalog, site coverage, SKU benchmarking), tested with Vitest.
- Designed the FastAPI/Postgres backend behind it: authentication, per-tenant data isolation, an append-only audit log, and a two-stage (raw-to-cleaned) data pipeline that turns scraper and inventory results into certified metrics.
- Built frontend and full-stack features for a multi-model generative-AI chat platform in React 18, TypeScript, Vite, and Tailwind CSS: ~17 Figma-designed screens and ~6 chat input features (image generation, deep research, artifacts, file attachments, audio input), with 12 merged PRs in ~4 weeks as implementer under tech-lead review.
- Delivered through Jira-tracked tasks, conventional commits, QA and visual regression evidence, and review-gated merges, with GitHub Actions CI/CD to Azure App Service.


### Career break · Oct 2024 – Oct 2025

- English exchange in London, UK (daily immersion, IELTS B2) and upskilling studies, incl. IBM Introduction to Data Engineering.

### Data Engineer — Spacecom Monitoramento | Curitiba, PR – Brazil (On-site) · Apr 2023 – Jul 2024

- Designed and maintained an enterprise Big Data Lakehouse on AWS S3 leveraging Medallion Architecture (Bronze/Silver/Gold) alongside Delta Lake, Parquet, PySpark, and Trino to support heavy analytics workloads.
- Supported a high-availability IoT platform scaling to 95,000+ devices, efficiently processing hundreds of millions of telemetry records per day.
- Managed electronic security tag (RFID/NFC) data for government court systems, ensuring strict LGPD/GDPR compliance through robust data privacy controls, access governance, and secure handling of sensitive judicial data.
- Orchestrated and optimised ETL pipelines with Apache Airflow, reducing failure rates by ~30%; utilised Docker on AWS EC2 to cut deployment issues by an additional ~25%.
- Remediated inconsistencies in pipeline steps to boost downstream analytics accuracy by ~40%, successfully delivering reliable datasets to Qlik Sense and Apache Superset dashboards.

### Data Engineer Consultant — wDiscover | Curitiba, PR – Brazil (Remote) · Jun 2022 – May 2024

- Delivered end-to-end data projects across the fintech, agribusiness, and operations sectors by integrating high-volume payment providers (PagSeguro, Stone, Cielo), John Deere IoT APIs, and REST APIs.
- Designed dimensional Data Warehouses on SQL Server and Oracle Autonomous Database; automated complex ETL workflows with Airflow on Docker/Oracle Cloud to reduce manual effort by ~35%.
- Built dynamic Power BI dashboards to track critical KPIs, financial metrics, and operational performance for diverse client domains.

### Data Analyst — Itaete Group | Curitiba, PR – Brazil (Hybrid) · Jun 2020 – Feb 2023

- Designed a SQL Server Data Warehouse and robust Python/SQL pipelines using Pandas to cleanse, transform, and enrich data from IoT devices, PostgreSQL, APIs, and CSV sources.
- Built Power BI dashboards and automated legacy Excel/VBA reporting workflows, slashing data processing time by ~50% and significantly reducing manual operational workloads.
- Developed internal systems for inventory management and financial automation, streamlining invoice generation and automated weekly report distribution.

## Notable Projects



### Omnichannel AI Platform (private) · NestJS, Next.js, PostgreSQL, LLMs, Meta & Google Ads APIs, Azure Container Apps, Docker · TK Technologies – Jun 2026 – Present

- Built a secure omnichannel CRM integrating WhatsApp, Instagram, Facebook, Telegram, and Email into a unified inbox with role-based access control (RBAC).
- Layered Meta/Google Ads performance data and LLMs (Claude/Google AI Studio) for auto-replies, outbound messaging assistance, and automated campaign analysis.

### Automotive Parts Price Search (private) · Python, FastAPI, Celery, Playwright, Redis, PostgreSQL, n8n, Azure, Bicep · TK Technologies – Feb 2026 – Present

- Built a car-parts price searcher across 10+ sites, with parallel public-price and internal-stock lookup, auditable reporting, and notifications from containerised Azure services.

### IoT Data Lakehouse on AWS – Medallion Architecture · AWS S3, Apache Spark, Delta Lake, Airflow, Trino, Apache Superset · Client Project – Feb 2024

- Designed a Bronze/Silver/Gold lakehouse on AWS S3 ingesting from APIs and databases. Virtualised the Gold layer with Trino and surfaced governed datasets through BI dashboards.

## Education

**Bachelor of Systems Analysis and Development** — Dom Bosco University, Curitiba, Brazil · Jun 2023

Majors: Information Systems · Business Analytics · Data Analysis · Database Systems · Software Engineering

## Licenses & Certifications

- **IELTS General** — IELTS B2 (band 5.5, Sep 2025)
- **AI for Writing and Communicating** — Google (Credential ID: HE8YE5IS7WVW) · Jul 2026
- **AI for Research and Insights** — Google (Credential ID: 4PZDF3XQOF55) · Jul 2026
- **AI for Brainstorming and Planning** — Google (Credential ID: 7SFW2HGOKIU5) · Jul 2026
- **AI Fundamentals** — Google (Credential ID: UKBGM0AZUIS2) · Jul 2026
- **Introduction to Data Engineering** — IBM · Jan 2025
- **Docker Essentials** — LINUXtips · Jun 2024
- **AWS Cloud Practitioner Essentials** — AWS (Coursera) · Apr 2024
- **AWS Discovery Day** — Ka Solution · Feb 2024
