<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/sabia-hub on 2026-07-31 -->

# Sabia Hub

Sabia Hub is a planned multi-tenant, event-driven customer operations platform. It will unify conversations, customer identity, sales, marketing, advertising, automation, knowledge, and governed AI inside isolated workspaces.

**Current lifecycle:** `planned` — the project has a conditional go for Phase 0
validation and a choice-neutral Sprint 1 engineering skeleton. Sprint 2, provider
features, production tenants, and full roadmap implementation remain blocked by the
[readiness gates](docs/delivery/readiness.md); no production capability is claimed.

## Current execution gate

The approved next step is to assign named owners and execute the
[dependency-ordered Phase 0 backlog](docs/delivery/execution-plan.md#dependency-ordered-phase-0-backlog).
Customer discovery, provider accounts, four evidence spikes, ADRs 0006–0009, product
economics, and operational ownership must close before Sprint 2. Evidence is governed
by the [engineering process](docs/delivery/engineering-process.md#execution-evidence).

## Product thesis

The first product loop is:

```text
Inbound conversation
→ verified event
→ customer identity
→ team assignment
→ AI-assisted response
→ lead qualification
→ opportunity and follow-up
→ measurable outcome
```

The initial target hypothesis is a WhatsApp-heavy SMB or mid-market sales and support team. Phase 0 discovery must validate the ICP, buyer, dominant workflow, message volume, willingness to pay, and provider-access assumptions before scope is locked.

## Platform principles

- One organization may own many isolated workspaces.
- Customers connect their own official provider accounts and resources.
- PostgreSQL is the durable operational source of truth.
- Provider events are verified and durably recorded before asynchronous processing.
- Services communicate through versioned APIs and events.
- Delivery is at-least-once; commands, events, workflow steps, and external sends are idempotent.
- Realtime improves the experience but is never the data authority.
- Entitlements, permissions, and contextual policy are separate decisions.
- AI begins in read and suggest modes; external actions require typed tools, fresh authorization, policy, and approval.
- Provider limitations, health, and data coverage remain visible.
- Deployment cells are the long-term isolation and scaling unit.
- Services are split by business capability, not by screen, table, or button.

## Canonical documentation

| Area | Documents |
|---|---|
| Overview | [Project background](docs/overview.md) |
| Product | [Vision](docs/product/vision.md), [goals and metrics](docs/product/goals-and-metrics.md), [product epic index](docs/product/feature-specs.md) |
| Product domains | [Connectors](docs/product/connectors.md), [CRM and automation](docs/product/crm-and-automation.md), [AI](docs/product/ai.md) |
| Architecture | [System](docs/architecture/system.md), [tenancy and data](docs/architecture/tenancy-and-data.md), [security and operations](docs/architecture/security-and-operations.md) |
| Decisions | [ADR 0001: Event-driven microservices](docs/architecture/adrs/0001-event-driven-microservices.md), [ADR 0002: Python and FastAPI backend](docs/architecture/adrs/0002-python-fastapi-backend.md), [ADR 0003: Google and Microsoft authentication](docs/architecture/adrs/0003-google-microsoft-authentication.md), [ADR 0004: Vercel and React frontend platform](docs/architecture/adrs/0004-vercel-react-frontend-platform.md), [ADR 0005: Obsidian and PostgreSQL knowledge](docs/architecture/adrs/0005-obsidian-postgresql-knowledge.md) |
| Delivery | [Roadmap](docs/delivery/roadmap.md), [execution plan](docs/delivery/execution-plan.md), [engineering process](docs/delivery/engineering-process.md), [readiness audit](docs/delivery/readiness.md) |

## Status vocabulary

Every capability uses one of these labels:

| Status | Meaning |
|---|---|
| `planned` | Approved target; implementation has not started |
| `in progress` | Code or operational work is underway |
| `implemented` | Code exists and automated checks pass |
| `verified` | Required security, reliability, and product acceptance gates pass |
| `provider accepted` | A provider integration passes real external acceptance tests |

## Repository start rules

1. Do not claim implementation from documentation or UI alone.
2. Every code change maps to an epic and acceptance criterion.
3. Every service and event has an owner and versioned contract.
4. Every tenant-owned path is tested with at least two workspaces and restricted database roles.
5. No provider is marked live from OAuth or a health probe alone.
6. No external AI action bypasses the owning domain service.
7. Major architecture changes require an ADR.
8. Never store credentials, personal data, raw provider payloads, or production evidence in this repository.

## Sprint 1 local workflow

The committed skeleton contains no product capability. It provides the accepted
frontend/backend boundaries, generated OpenAPI contract, application/worker shells,
local PostgreSQL and Redis, a non-durable in-memory messaging adapter, and an
OpenTelemetry Collector.

Required runtimes are pinned in `.node-version` and `.python-version`. The host must
provide Docker Compose, Node.js 24 LTS with Corepack, and `uv`.

```bash
make bootstrap
make check
make dev
```

`make dev` starts the web shell on port 3000, gateway on 8000, control plane on 8001,
data plane on 8002, Storybook on 6006, PostgreSQL, Redis, the worker shell, and the
local Collector. Stop it with `make down`.

The local messaging adapter is intentionally non-durable and cannot provide
`SPIKE-EVENT` or production evidence. Cloud deployment, provider callbacks, tenant
models, and authorization remain gated.

## Technology direction

- Next.js with TypeScript is the frontend.
- Vercel deploys the frontend; Vercel Labs, templates, and v0 may accelerate
  prototyping but all generated code is reviewed and owned by Sabia Hub.
- Tailwind CSS and source-owned shadcn/ui components form the design system;
  TanStack Table and Recharts support operational dashboards and reporting.
- Python 3.13+ and FastAPI implement the complete backend.
- The browser uses the public FastAPI gateway/BFF through a generated OpenAPI client.
- Domain modules and independently scalable Python workers own backend behavior.
- PostgreSQL is authoritative; Azure Service Bus carries durable jobs and events.
- Users sign up and sign in with Google or Microsoft through OpenID Connect.
- FastAPI completes the authorization-code flow, validates provider tokens, resolves the
  Sabia principal, and issues the application session; provider tokens are never used
  as Sabia authorization.