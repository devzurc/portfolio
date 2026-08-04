<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/my-finance on 2026-07-31 -->

# Personal Finance OS

[![CI]([REDACTED_URL])]([REDACTED_URL])

Privacy-first personal finance platform. Ingest Nubank bank statements, normalize and enrich transactions, store them in PostgreSQL, and explore your money through an interactive web dashboard, Power BI, or a legacy offline HTML report.

**Repository:** [github.com/devzurc/my-finance]([REDACTED_URL]) (private)

---

## What we built

A **modular monolith** (Python 3.12 + React) maintained as production-grade software:

| Layer | What it does |
|-------|----------------|
| **Ingestion** | Nubank CSV → parse → clean → categorize → Postgres (idempotent by file hash + transaction ID) |
| **Web platform** | FastAPI API + React SPA: KPIs, Recharts, filters, transaction search, CSV upload, SSE live refresh |
| **Multi-user** | Invite-only auth, JWT httpOnly cookies, row-level data isolation per user |
| **Admin** | User management, audit log, RBAC at `/admin` |
| **Data management** | List/delete uploads, wipe all data for re-testing |
| **CLI** | `finance ingest`, `report`, `user create`, emergency operations |
| **Analytics** | SQL views for Power BI; legacy static HTML dashboard |

### Milestones shipped (M1–M5)

- **M1** — Nubank pipeline, CLI, analytics views
- **M2** — Web dashboard (FastAPI + React + Recharts + SSE)
- **M3** — Multi-user auth, Cloudflare Tunnel sharing
- **M4** — Admin panel, security audit trail, password policy
- **M5** — Global filters, paginated transaction explorer, upload batch delete

See [docs/ROADMAP.md](docs/ROADMAP.md) for vision, backlog, and deferred scope.

---

## Goals

1. **Own your data** — local Postgres; no mandatory cloud; financial CSVs stay in gitignored `data/`
2. **Understand spending** — categories, merchants, cashflow, rules-based insights
3. **Share safely** — invite-only users, audit logs, tunnel-based HTTPS (no router port forwarding)
4. **Evolve toward an AI-native CFO** — LLM layer stubbed; rules-first categorization today

---

## Quick start

### Prerequisites

- Python 3.12+, [uv]([REDACTED_URL])
- Node.js 20+
- Docker (PostgreSQL 16)

```bash
make install
cp .env.example .env
make dev          # Postgres + migrations
make ingest-all   # place NU_*.csv files in data/ first
```

### Run the web platform

```bash
make migrate
make web          # [REDACTED_URL]
```

Bootstrap admin is created by migration (see `.env.example` for `BOOTSTRAP_ADMIN_*`). **Change the default password immediately** — credentials are not shown on the login screen.

```bash
finance user create --email [REDACTED_EMAIL] --name "You" --password "..."
```

### Share with someone on another network

```bash
# Terminal 1
make web

# Terminal 2
make tunnel
```

Set `ALLOWED_ORIGINS` to your `*.trycloudflare.com` URL and `COOKIE_SECURE=true` in `.env`, then restart `make web`. Full workflow: [docs/deployment/cloudflare-tunnel.md](docs/deployment/cloudflare-tunnel.md) and [.ai/prompts/go-online.md](.ai/prompts/go-online.md).

---

## Development

```bash
make lint typecheck test     # backend
cd frontend && npm test      # frontend
make web-dev                 # API reload + use Vite proxy on :5173
make stop                    # free ports 8000 and 8765
```

**Logging:** `LOG_FORMAT=json`, optional `LOG_FILE=logs/app.log`, `X-Request-ID` on every response. See [ADR-0010](docs/adr/0010-structured-logging-and-request-correlation.md).

---

## Architecture

```
CLI (Typer) ──┐
Web (FastAPI) ├──► Application services ──► Ingestion pipeline ──► PostgreSQL
React SPA ◄───┘         │                                              │
  ▲ SSE                 Analytics / Insights                           ▼
  └─────────────────────────────────────────────────── SQL views → Power BI
```

Details: [docs/architecture/overview.md](docs/architecture/overview.md)

---

## CI/CD & production path

**Today:** GitHub Actions runs lint, typecheck, pytest, and frontend tests on every push to `main`.

**Future:** Docker image → VPS → named Cloudflare Tunnel or reverse proxy + DNS.

Plan: [docs/deployment/production-cicd.md](docs/deployment/production-cicd.md)

---

## Documentation index

| Topic | Path |
|-------|------|
| Roadmap & backlog | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Data model | [docs/data-model/entities.md](docs/data-model/entities.md) |
| Cloudflare quick share | [docs/deployment/cloudflare-tunnel.md](docs/deployment/cloudflare-tunnel.md) |
| Production / CI/CD | [docs/deployment/production-cicd.md](docs/deployment/production-cicd.md) |
| Specs | [docs/specs/](docs/specs/) |
| ADRs | [docs/adr/](docs/adr/) |
| AI agent prompts | [.ai/prompts/](.ai/prompts/) |
| Agent skills | [.ai/skills/](.ai/skills/) |
| Power BI | [powerbi/README.md](powerbi/README.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |

### Key specs

- [0001 Nubank CSV ingestion](docs/specs/0001-nubank-csv-ingestion.md)
- [0003 Web analytics platform](docs/specs/0003-web-analytics-platform.md)
- [0004 Admin user management](docs/specs/0004-admin-user-management.md)
- [0005 Observability](docs/specs/0005-observability-and-server-hygiene.md)
- [0006 Interactive dashboard (M5)](docs/specs/0006-interactive-dashboard-data-management.md)

---

## Security

- Never commit `.env` or `data/`
- Invite-only users; no public registration
- Run [financial-cybersecurity](.ai/skills/financial-cybersecurity/SKILL.md) checklist before exposing via tunnel
- Admin audit log at `/admin` when signed in as admin

---

## License

Private — personal use only.