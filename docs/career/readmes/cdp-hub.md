<!-- public-safe excerpt from the CDP platform README -->
# CDP Platform

CDP is a monorepo for automotive parts intelligence. It takes SKU requests from
chat, email, schedules, or spreadsheets; dispatches public-site pricing search
and internal stock lookup in parallel; then delivers structured results to
spreadsheet reporting plus chat/email notifications.

This career summary is sanitized for public sharing. Live workflow names,
webhook URLs, workflow IDs, cloud resource names, vault names, secret names, and
environment variable names are intentionally omitted.

## What It Does

- **Public pricing search:** FastAPI + Celery + Playwright searches supplier and
  marketplace sites with a 24h cache.
- **Internal stock lookup:** FastAPI + Redis Streams worker queries internal
  stock data and persists raw snapshots/results.
- **Workflow automation:** coordinates chat/email intake, schedules, progress
  polling, receiver handoff, and final notification.
- **Spreadsheet reporting:** detailed, historical, summary, and dashboard views
  keep found-price, no-price, not-found, blocked, timeout, and error outcomes distinct.

## Runtime Flow

```text
Chat / email / spreadsheet / schedule intake
  -> workflow automation router
      -> public pricing search service
          -> background workers -> result receiver
      -> internal stock lookup service
          -> queue worker -> result receiver
  -> spreadsheet reporting
  -> aggregate chat/email notification
```

Live workflow registry details and deployment-specific identifiers are excluded
from this public version.

## Repository Layout

| Path | Purpose |
|------|---------|
| [infra/](infra/) | Platform Azure Bicep and shared infrastructure modules |
| [scrapers/](scrapers/) | Scraper API, Celery worker, Playwright scrapers, cache |
| [muvstok-api/](muvstok-api/) | Internal stock lookup API, Redis worker, persistence |
| [n8n/](n8n/) | Workflow automation source, receiver helpers, SDK |
| [contracts/](contracts/) | Shared JSON Schema for jobs, callbacks, dispatch runs |
| [docs/](docs/) | Architecture, runbooks, setup docs, ADRs |

## Local Development

```bash
make setup
make migrate-scraper
make dev-scraper   # Scraper API on :8000
make dev-stokapi   # Internal stock lookup API on :8001
```

Configuration templates and full-stack Docker profiles are documented in the
private project runbooks; secret and environment variable names are not included
in this public career excerpt.

## Quality Gates

```bash
make lint
make test
make check-muvstok
make -C scrapers test lint
```

Run the narrow service checks for the code you touched. Contract changes must
update [contracts/](contracts/) and the owning service tests.

## Workflow Automation

Workflow source is maintained in the repository and synchronized through guarded
release commands. Live workflow IDs, webhook URLs, and deployment-specific
configuration names are intentionally omitted from this public summary.

## Reporting Contract

Found-price success is represented only when the result contract marks a valid
price. A detailed row is audit evidence, not success by itself. Seller,
location, and company fields are normalized before being written to reporting
outputs.

Details are tracked in the platform data-contract documentation.

## Key Docs

[Architecture](docs/ARCHITECTURE.md) ·
[Dual pipeline](docs/architecture/DUAL_PIPELINE.md) ·
[Contributing](docs/CONTRIBUTING.md)
