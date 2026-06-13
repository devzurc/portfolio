<!-- public-safe excerpt from the CDP monorepo internal stock lookup service -->
# Internal Stock Lookup API

SKU ingestion and internal stock lookup service: FastAPI, PostgreSQL, Redis
Streams workers, and Azure Container Apps. Part of the CDP monorepo.

This career summary is sanitized for public sharing. Live endpoint URLs, webhook
paths, workflow IDs, cloud resource names, vault names, secret names, and
environment variable names are intentionally omitted.

## What it does

- Accepts authenticated SKU batch jobs with callback configuration.
- Queues jobs via Redis Streams for background processing.
- Workers fetch SKU data sequentially and persist results to PostgreSQL.
- Sends completion callbacks to the CDP reporting and notification pipeline.

## Production architecture (CDP dual pipeline)

Production dispatch is part of the CDP dual pipeline rather than a standalone
sender workflow. The platform automation submits internal stock lookup jobs
alongside public pricing searches for the same SKU batch:

```text
Chat / email / schedule intake
  -> internal stock lookup job submission
  -> Redis Streams queue -> stock lookup worker
  -> PostgreSQL
  -> result callback
  -> spreadsheet reporting + notifications
```

In parallel, the workflow automation dispatches the public pricing search
service for the same SKU batch. See
[../docs/architecture/DUAL_PIPELINE.md](../docs/architecture/DUAL_PIPELINE.md).

## Stack

| Layer | Technology |
|-------|-----------|
| API | Python 3.12, FastAPI, Pydantic v2 |
| Database | PostgreSQL (async SQLAlchemy 2.x, Alembic) |
| Queue | Redis Streams with consumer groups |
| Workers | `app.workers.redis_worker` (sequential SKU processing) |
| Hosting | Azure Container Apps for separate API and worker services |
| Secrets | Managed cloud secret store; identifiers omitted |
| Workflow receiver | Result receiver in the CDP automation platform; identifier omitted |

## Quick start

```bash
docker compose -f docker/docker-compose.yml up --build

uv run ruff check .
uv run mypy .
bash scripts/check_specs.sh
```

## Project structure

```text
app/                    # FastAPI application
├── api/                # Routes and dependencies
├── clients/            # Redis, stock lookup, cloud secrets, callback
├── workers/            # Redis Streams consumer
├── services/           # Job, queue, callback orchestration
└── db/                 # Models + Alembic migrations

n8n/                    # Workflow automation code, SDK, and operations docs

specs/                  # Planning specs
```

## API capabilities

| Capability | Auth | Purpose |
|------------|------|---------|
| Health check | none | Service readiness |
| Batch submission | required | Submit SKU lookup job |
| Job status | required | Inspect processing status and progress |

Exact routes, authentication header names, and live base URLs are omitted from
this public version.

## Deployment

The API and worker are deployed as separate containerized services through the
repository deployment scripts. Live app names, vault names, workflow IDs, and
webhook URLs are intentionally omitted.

## AI agents

Service-specific engineering notes and agent workspaces exist in the private
project context; this public summary keeps only recruiter-relevant architecture
and delivery evidence.
