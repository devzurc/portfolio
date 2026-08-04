<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/marketing-socialmedia-app on 2026-07-31 -->

# marketing-socialmedia-app (social media runtime)

Automations powered by [n8n]([REDACTED_URL]) for Instagram Direct and comments — **Nox** (TK Tech / Stok AI), with PostgreSQL `socialmedia.*` and **Redis** as the intended durable and shared runtime state backbone (logs, dedupe, sessions, tickets).

Current execution scope: Instagram-first. Schema supports TikTok/WhatsApp/LinkedIn (deferred).

**Greenfield contracts and navigation:** [.agent/SOURCE_OF_TRUTH.md](.agent/SOURCE_OF_TRUTH.md). Reference JSON under `services/n8n/workflows/` may still use legacy patterns until an accepted greenfield export set exists; acceptance is defined by SPECs + DDL + [`SPEC-WF-ARCH-001.md`](.agent/SPECIFICATIONS/SPEC-WF-ARCH-001.md) (no production-critical `staticData`).

## Repository layout

```
marketing-socialmedia-app/
├── .agent/              # SDD source of truth: specs, pipelines — start at SOURCE_OF_TRUTH.md
├── database/            # Schema, migrations, data model docs (Postgres + Redis)
├── infra/               # Azure IaC (Bicep), networking, operations runbooks
├── services/            # Containerized applications
│   ├── n8n/             # Orchestration workflows + Dockerfile + ACA manifest
│   └── dashboard/       # Frontend app + Dockerfile + ACA manifest
├── tests/               # Test contracts + fixtures
├── CHANGELOG.md
└── README.md
```

## Main components

| Area | Role | Notes |
|------|------|-------|
| [.agent/](.agent/) | Direction, specs, pipelines | [`SOURCE_OF_TRUTH.md`](.agent/SOURCE_OF_TRUTH.md); handoff [`HANDOFF_GREENFIELD_EXECUTION.md`](.agent/HANDOFF_GREENFIELD_EXECUTION.md); build order [`BUILD_PLAN_SPEC_BY_SPEC.md`](.agent/BUILD_PLAN_SPEC_BY_SPEC.md) |
| [services/n8n/](services/n8n/) | Reference exports (`00`–`05`) and deployment | Policy: [.agent/MAINTENANCE.md](.agent/MAINTENANCE.md); topology [`services/n8n/workflows/README.md`](services/n8n/workflows/README.md) |
| [database/](database/) | Schema `socialmedia.*`, migrations | [`database/docs/SOCIALMEDIA_DATA_MODEL.md`](database/docs/SOCIALMEDIA_DATA_MODEL.md), [`database/docs/REDIS_DESIGN.md`](database/docs/REDIS_DESIGN.md) |
| [services/dashboard/](services/dashboard/) | Vite + React UI scaffolding | Modules DEFERRED — [`services/dashboard/README.md`](services/dashboard/README.md) |
| [infra/](infra/) | Azure scripts, IaC, runbooks | Start at [`infra/docs/AZURE_ARCHITECTURE.md`](infra/docs/AZURE_ARCHITECTURE.md) |
| [tests/](tests/) | Payload fixtures + traceability | [`tests/README.md`](tests/README.md) |
| [archive/](archive/) | Legacy SQL and artifacts | Non-active code |

## Quickstart

### Local development

```bash
cd database && docker compose up -d
curl -X POST [REDACTED_URL] -H "Content-Type: application/json" -d @tests/payloads/dm-payloads/simple-greeting.json
```

### Apply DDL (only if needed)

On first `docker compose up`, greenfield DDL is applied automatically. If you reuse an old Postgres volume from before that init, run once:

```bash
psql -h localhost -p 5433 -U igwarehouse -d instagram_wh -f database/migrations/install_socialmedia_greenfield.sql
```

## Workflow exports and automation changes

Maintainers: follow [.agent/MAINTENANCE.md](.agent/MAINTENANCE.md) (export policy, changelog, data-model updates) and [`services/n8n/workflows/README.md`](services/n8n/workflows/README.md) for topology/import notes.