<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/ORBITAI-CRM on 2026-07-31 -->

# WhatsApp Automation Platform

Production-oriented platform for official WhatsApp Cloud API automation (n8n + PostgreSQL) and a marketing CRM (NestJS + Next.js) for agent inbox, tickets, and leads.

## Architecture

**Automation flow:**

1. Customer sends a WhatsApp message.
2. Meta posts official Cloud API `messages` webhooks to n8n.
3. n8n normalizes the payload and calls PostgreSQL `record_customer_interaction`.
4. PostgreSQL decides welcome, return ack (12h/24h cooldown), and staff notification flags.
5. n8n sends welcome or return ack through the official WhatsApp Business Cloud node.
6. n8n sends Slack staff notifications or records them as pending.

**CRM flow:** Agents log into `apps/web`, read conversations, and reply via `apps/api` → Meta Graph API → `record_agent_outbound_message`.

See [Architecture](docs/architecture.md), [CRM Platform](docs/crm-platform.md), and [Customer auto-reply spec](docs/specs/customer-auto-reply.md).

## Azure DEV

Prerequisites:

- Node.js 20+ and pnpm 9+
- Azure CLI for deployment scripts and smoke checks
- `curl`, `psql`, and `jq` or Node.js for operations

DEV is hosted in Azure Container Apps:

| Service | URL |
|---------|-----|
| CRM Web | [REDACTED_URL] |
| CRM API | [REDACTED_URL] |
| Platform n8n | [REDACTED_URL] |

Prepare deploy/smoke environment:

```bash
cp .env.example .env
pnpm install
make azure-smoke-platform
```

Do not use localhost as the DEV environment. Local execution is only for isolated lab reproduction when explicitly requested.

Seed the first admin agent (after migrations):

```bash
pnpm --filter @whatsapp/api seed:admin
```

Run Azure DEV smoke checks:

```bash
make azure-smoke-platform
```

## Environment Variables

Use `.env.example` as the contract. Never commit `.env` or real secrets.

Production secrets should live in Azure Key Vault or Azure Container Apps secrets:

- PostgreSQL password or full connection URI (`DATABASE_URL`)
- Meta WhatsApp tokens (`WHATSAPP_ACCESS_TOKEN`, `META_APP_SECRET`)
- n8n API key and encryption key (`N8N_API_KEY`, `N8N_ENCRYPTION_KEY`)

## n8n Workflow

Starter workflow:

```text
n8n/workflows/whatsapp-first-message.workflow.json
```

Live workflow: `wpp-nox-agent` (`xSRDDdUOOASvFyqf`) on dedicated platform n8n (`ca-platform-n8n-dev`). Import it into n8n, replace PostgreSQL and WhatsApp API credentials, bind the `WhatsApp TK Technologies` `whatsAppApi` credential, verify `WHATSAPP_PHONE_NUMBER_ID` or select the sender phone number in the WhatsApp send nodes, and activate after the Meta webhook verification workflow is active. Before real inbound tests, run `make meta-app-webhook-status`, `make meta-webhook-status`, and `make n8n-live-status`.

Azure DEV inbound incident runbook: [Azure DEV WhatsApp Inbound Recovery](docs/azure-dev-whatsapp-inbound-recovery.md).

## Azure Deployment

PostgreSQL in Brazil South (`brazilsouth`); CRM and platform n8n in `eastus2`. Provision with modular Bicep.

```bash
cp .env.example .env
make azure-preflight
make azure-deploy-postgres
make azure-migrate-metadata
make azure-deploy-crm
make azure-deploy-n8n
make azure-import-n8n-workflows
```

See [Azure Infrastructure](docs/azure-infrastructure.md) and [Deployment](docs/deployment.md) for details.

## Documentation

- [Customer auto-reply spec](docs/specs/customer-auto-reply.md) (welcome FAQ list + 12h return ack)
- [FAQ menu v1](docs/specs/faq-menu-v1.md)
- [Outbound message paths](docs/specs/outbound-message-paths.md)
- [Assist isolation](docs/specs/assist-isolation.md)
- [Campaigns compliance](docs/specs/campaigns-compliance.md)
- [Role visibility](docs/specs/role-visibility.md)
- [Parked backlog](docs/specs/parked-backlog.md)
- [CRM Platform](docs/crm-platform.md)
- [Instagram integration](docs/instagram-integration.md)
- [Architecture](docs/architecture.md)
- [Database](docs/database.md)
- [Deployment](docs/deployment.md)
- [n8n Workflow](docs/n8n-workflow.md)
- [n8n Platform](docs/n8n-platform.md)
- [Operations](docs/operations.md)
- [Azure DEV WhatsApp Inbound Recovery](docs/azure-dev-whatsapp-inbound-recovery.md)
- [Security](docs/security.md)
- [Azure Infrastructure](docs/azure-infrastructure.md)
- [i18n](docs/i18n.md)
- [Privacy policy](docs/privacy-policy.md)
- [Plan and status](docs/plan-next-steps.md) → `.ai/TASKS.md` / `.ai/STATE.md`

## AI Assistant Context

This repo uses `.ai/` as the coding-agent source of truth. `.agents/AGENTS.md` is a lightweight workspace entrypoint that points back to `.ai/`.

Start with:

- `.agents/AGENTS.md`
- `.ai/prompts/new-session.md`
- `.ai/STATE.md` and `.ai/TASKS.md`
- `.ai/rules/security.md`
- `.ai/architecture/overview.md`
- `.ai/skills/*/SKILL.md`