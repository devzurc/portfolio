<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/carparts-price-webscraper on 2026-07-31 -->

# CDP Parts Scraper

> **Versão:** 0.6.27 · **Atualizado em:** 12/04/2026

## O que é

Sistema de comparação automatizada de preços de peças automotivas e posições de mercado (**MeliBox**): API **FastAPI** que orquestra scrapers **Playwright** (um processo Chromium partilhado), persiste em **PostgreSQL** e integra com **n8n** e Google Sheets para o fluxo CDP.

**Documentação em português (índice):** [**docs/README.md**](docs/README.md) — instalação, arquitetura, uso, n8n, dados, agentes.

**Assistentes de IA:** [**AGENTS.md**](AGENTS.md) → [**`.agent/START_HERE.md`**](.agent/START_HERE.md) (contexto canónico v0.6.20+).

## Stack

- **Python** ≥ 3.12 · **FastAPI** · **Playwright** (Chromium) · **SQLAlchemy 2** + **Alembic** · **Pydantic v2**
- **PostgreSQL** · **Redis** (infra; Celery planeado)
- **n8n** (workflows no repositório: `webscraper_analise` / `webscraper_resultado`)
- **Azure** Container Apps (deploy via `scripts/deploy-azure.sh`; infra: `muvstok*`)

## Início rápido

```bash
make setup    # dependências, .env, Postgres/Redis, migrações
make dev      # API em [REDACTED_URL]
make test     # testes
```

Configurar `.env` a partir de `.env.example`. Detalhes: [docs/setup.md](docs/setup.md).

## API (resumo)

| Método | Caminho | Auth |
|--------|---------|------|
| POST | `/api/v1/jobs` | `X-Api-Key` |
| GET | `/api/v1/jobs/{id}` | `X-Api-Key` |
| POST | `/api/v1/lookup` | `X-Api-Key` |
| GET | `/api/v1/health` | não |
| GET | `/metrics` | não (Prometheus) |

OpenAPI: `[REDACTED_URL] (com o servidor a correr).

## Arquitetura (resumo)

```
n8n / cliente  →  FastAPI  →  Orchestrator  →  BrowserPool + scrapers
                      ↓              ↓
                 PostgreSQL     callback HTTP → n8n → Google Sheets
```

Mais detalhe: [docs/arquitetura.md](docs/arquitetura.md) e [docs/SYSTEM_OVERVIEW.md](docs/SYSTEM_OVERVIEW.md).

## Documentação adicional

| Documento | Conteúdo |
|-----------|-----------|
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões (inglês, Keep a Changelog) |
| [CLAUDE.md](CLAUDE.md) | Convenções para assistentes / desenvolvimento |
| [docs/CDP_USER_GUIDE.md](docs/CDP_USER_GUIDE.md) | Comandos `.analisar` / `.sku` (Telegram e e-mail) |
| [docs/TELEGRAM_ONBOARDING.md](docs/TELEGRAM_ONBOARDING.md) | Primeiro uso do bot no Telegram (EN + pt-BR) |
| [docs/SHEETS_GUIDE.md](docs/SHEETS_GUIDE.md) | Colunas `CDP_SKUs` e `CDP_Resultados` |
| [docs/n8n.md](docs/n8n.md) | Workflows, variáveis de ambiente, jitter Sheets |
| [docs/n8n/README.md](docs/n8n/README.md) | Índice técnico dos workflows JSON |
| [n8n/N8N_AUTOMATION_GUIDE.md](n8n/N8N_AUTOMATION_GUIDE.md) | n8n ↔ API (inglês, guia longo) |
| [n8n/N8N_WEBHOOK_CALLBACK.md](n8n/N8N_WEBHOOK_CALLBACK.md) | Webhook test vs produção |

## Deploy Azure (exemplo)

```bash
set -a && source .azure-deploy.env && set +a
export API_KEY
./scripts/deploy-azure.sh dev    # ou prod; --skip-n8n para omitir n8n
```

Variáveis públicas n8n e OAuth: ver cabeçalho de `n8n/scripts/deploy-n8n-azure.sh` e [n8n/N8N_AUTOMATION_GUIDE.md](n8n/N8N_AUTOMATION_GUIDE.md).

Histórico de logs da API no Azure (KQL, jobs completos): [docs/AZURE_LOG_ANALYTICS.md](docs/AZURE_LOG_ANALYTICS.md).
Teste de lote (1106 SKUs → 12 jobs): checklist [docs/BATCH_RUN_VERIFICATION.md](docs/BATCH_RUN_VERIFICATION.md) e `./scripts/verify_batch_run.sh`.

**Workflows atuais:** `n8n/workflows/webscraper_analise.json` (dispatcher) e `n8n/workflows/webscraper_resultado.json` (receiver). Comandos Telegram/Gmail: `.analisar`, `.sku`. **Gmail:** assunto fixo **`CDP Webscraper`** (`filters.q` no trigger); comandos no corpo. **Receiver:** jitter **10 / 20 / … / 60 s** (um valor por execução, passo 10 s) antes das gravações Sheets e ramo **bulk** (>3 SKUs → CSV anexo); ver [docs/n8n/webscraper_resultado.md](docs/n8n/webscraper_resultado.md).

## Comandos de desenvolvimento

```bash
make dev          # API + Postgres + Redis
make test         # pytest
make lint         # ruff + mypy
make migrate      # alembic upgrade head
make docker-up    # stack completa (Docker Compose)
```

## Novo scraper

1. Criar `src/scrapers/newsite.py` herdando `BaseScraper`
2. Implementar `site_id`, `site_name`, `login()`, `search_sku()`
3. Registar em `src/scrapers/__init__.py`
4. Credenciais em `.env.example` + `src/config.py`
5. Testes em `tests/test_scrapers/`

Referência: `src/scrapers/gm.py`.