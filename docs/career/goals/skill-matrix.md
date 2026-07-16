# Skill matrix — Senior AI Platform Specialist

> Levels: **aware** → **building** → **production** → **teaching**  
> Last updated: 2026-06-24  
> Rule: upgrade a level only when a shipped repo or verified work proves it.

**Legend:** Current → Target (Dec 2026) · Proof project

---

## Tier 1 — must master

| Skill | Current | Target | Proof project |
|-------|---------|--------|---------------|
| Python: async, typing, Pydantic, testing | production | production | CDP Platform, `raw-llm-systems` |
| SQL / PostgreSQL: schema, indexes, query plans | production | production | Spacecom lakehouse, CDP Platform |
| LLM APIs: prompts, tool calling, structured outputs | building | production | `raw-llm-systems`, n8n assistants |
| RAG architecture: chunking, embeddings, retrieval, reranking, grounding | aware | production | `data-engineering-knowledge-rag` |
| Vector DBs: PostgreSQL + `pgvector`, HNSW/IVFFlat tradeoffs | aware | production | `data-engineering-knowledge-rag` |
| LangGraph: state, tools, checkpoints, memory, human approval | aware | production | `analytics-agent-orchestrator` |
| Evaluation: RAGAS metrics, DeepEval regression tests | aware | production | eval layer on RAG repo |
| MCP: tool/resource integration, security boundaries | aware | production | `mcp-data-catalog-server` |

---

## Tier 2 — very valuable

| Skill | Current | Target | Proof project |
|-------|---------|--------|---------------|
| LangChain for integrations / RAG | building | production | RAG + agent repos |
| LlamaIndex for document-heavy RAG | aware | building | RAG repo (compare if time) |
| LangSmith: traces, production metrics, eval workflows | aware | production | capstone + agent repo |
| OpenTelemetry: vendor-neutral traces/metrics | aware | production | capstone |
| A2A awareness for agent interoperability | aware | aware | Nov prototype if time |
| OWASP LLM security: prompt injection, data leakage, excessive agency | building | production | MCP threat model, security.md |

---

## Tier 3 — learn lightly

| Skill | Current | Target | Notes |
|-------|---------|--------|-------|
| CrewAI: role-based multi-agent workflows | aware | building | Nov comparison only |
| PydanticAI: type-safe Python agents | aware | aware | Use if a job requires it |
| AutoGen, Agno, Mastra | aware | aware | Awareness only unless job requires |

---

## Existing strengths (already proven — lead with these)

| Skill | Level | Evidence |
|-------|-------|----------|
| Data pipelines & lakehouses | production | Spacecom AWS Medallion, wDiscover DW |
| FastAPI + PostgreSQL + Redis/Celery | production | CDP Platform, muvstok-api |
| NestJS + Next.js web application architecture | production | WhatsApp CRM & Automation Platform |
| n8n + LLM workflow automation | production | Telegram, WhatsApp, Stripe workflows |
| Meta Cloud API integrations | production | WhatsApp CRM webhook parsing & outbound messages |
| Cloud deployment (AWS, Azure, Docker) | production | TK Technologies, Spacecom |
| Web scraping at scale | production | CDP automotive pricing pipeline |
| BI & governed datasets | production | Power BI, Qlik, Superset |
| English C1 + Europe relocation | verified | IELTS, CV, portfolio |

---

## Gap focus (highest leverage for senior AI signal)

1. **RAG + pgvector** — closes the biggest gap between "GenAI automation" and "AI platform engineer"
2. **Evaluation harness** — separates senior from vibe-based demos
3. **LangGraph + MCP** — proves agent orchestration and tool-platform fluency
4. **Observability + runbooks** — proves production ownership

---

## Monthly skill targets

| Month | Primary skill upgrades |
|-------|------------------------|
| Jul | Structured outputs, FastAPI service patterns, pytest |
| Aug | pgvector, hybrid retrieval, reranking, citations |
| Sep | RAGAS, DeepEval, CI regression gates |
| Oct | LangGraph state, checkpoints, human-in-the-loop |
| Nov | MCP security, audit logging, threat modeling |
| Dec | LangSmith, OTel, cost/latency dashboards, runbooks |
