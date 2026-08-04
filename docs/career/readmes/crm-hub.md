<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/crm-hub on 2026-07-31 -->

# CRM-HUB

Multi-tenant **unified inbox CRM** with AI assist. Centralize WhatsApp, Telegram, Instagram, and workflows. The dental clinic is the first production tenant.

## Quick start

This repository has **Phases 1–4 on `main`**: auth, multi-tenancy, contacts CRM, conversation inbox, WhatsApp Meta (ledger + ARQ), SSE handoff, and AI draft suggestions (no auto-send). **Phase 5 (Telegram)** is next — see [ROADMAP.md](ROADMAP.md) and [`.cursor/prompts/NEXT-SESSION.md`](.cursor/prompts/NEXT-SESSION.md).

### For humans

1. Clone the repo
2. Copy `.env.example` to `.env` (and `frontend/.env.example` → `frontend/.env`)
3. `docker compose -f docker/compose.yml up --build` (API `:8000`, worker ARQ)
4. `cd frontend && npm install && npm run dev` (UI `:3000`)
5. Read [AGENTS.md](AGENTS.md) and [`.cursor/prompts/NEXT-SESSION.md`](.cursor/prompts/NEXT-SESSION.md)

### For AI assistants (Cursor)

1. Read [AGENTS.md](AGENTS.md) first
2. Run `/context` (reads handoff + roadmap)
3. Use specialist skills in `.cursor/skills/`
4. New channel: `/new-channel` — copy `backend/app/integrations/whatsapp/` pattern

## Project structure

```
crm-hub/
├── AGENTS.md           # Constitution + bootstrap
├── .cursor/            # Rules, skills, commands, agents
├── backend/            # FastAPI (auth, tenants, contacts, conversations, integrations, ai, jobs)
├── frontend/           # Next.js inbox
├── docs/               # Domain docs + handoff/
├── adr/                # Architecture decisions
├── specs/              # Feature specifications (001–008)
├── tasks/              # Active work tracking
├── prompts/            # Versioned LLM prompts (draft-assist)
└── checklists/         # Quality gates
```

## Documentation

| Doc | Purpose |
|-----|---------|
| [AGENTS.md](AGENTS.md) | AI constitution and bootstrap |
| [`.cursor/prompts/NEXT-SESSION.md`](.cursor/prompts/NEXT-SESSION.md) | Next session priorities |
| [PRODUCT.md](PRODUCT.md) | Product vision |
| [ROADMAP.md](ROADMAP.md) | Implementation phases |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design |
| [SECURITY.md](SECURITY.md) | Security policy |
| [CHANGELOG.md](CHANGELOG.md) | Release history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide |

## License

Proprietary — Odonto Rocha / CRM-HUB.