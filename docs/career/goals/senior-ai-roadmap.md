# Senior AI Platform Specialist — roadmap (Jul–Dec 2026)

> Monthly capstones ship as **separate public GitHub repos** under `devzurc`, synced into `docs/career/projects/`, then surfaced on CV and portfolio when `portfolio_worthy: true`.

**Deadline:** December 31, 2026  
**Job search:** Parallel from day one — apply as Senior Data Engineer / GenAI Engineer while building.

---

## July 2026 — Foundation + raw LLM systems

**Goal:** Prove you understand primitives without framework magic.

**Repo:** `raw-llm-systems` (planned)

| Task | Status |
|------|--------|
| Build raw LLM API scripts with tool calling and structured outputs | pending |
| Create Pydantic schemas for model responses | pending |
| Build FastAPI service with `/chat`, `/embed`, `/health` | pending |
| Add Docker Compose with PostgreSQL | pending |
| Add tests with `pytest` | pending |
| Write ADR: "Why structured outputs and tool schemas matter" | pending |

**Exit criteria:**

- FastAPI service runs in Docker Compose
- Structured outputs and tool schemas documented in ADR
- Tests pass in CI or local pytest run

---

## August 2026 — Production RAG core

**Goal:** Build your real RAG platform over data-engineering / enterprise-data content.

**Project:** Data Engineering Knowledge RAG  
**Repo:** `data-engineering-knowledge-rag` (planned)

| Task | Status |
|------|--------|
| Ingest Markdown, PDFs, CSV docs, dbt docs, SQL files | pending |
| Store documents, chunks, metadata, embeddings in PostgreSQL + `pgvector` | pending |
| Implement semantic search, keyword search, metadata filters | pending |
| Add reranking | pending |
| Add source citations | pending |
| Add "answer only from context" behavior | pending |
| Create 50 golden Q&A pairs | pending |

**Exit criteria:**

- RAG API works through FastAPI
- Can compare chunking strategies
- Can explain recall, precision, faithfulness, latency, and cost

---

## September 2026 — Evaluation specialist layer

**Goal:** Stop trusting vibes.

**Repo:** Extend `data-engineering-knowledge-rag` (eval layer)

| Task | Status |
|------|--------|
| Add RAGAS: context precision, context recall, faithfulness, response relevancy | pending |
| Add DeepEval tests in CI | pending |
| Create eval datasets: easy, ambiguous, adversarial, out-of-scope | pending |
| Add prompt regression tests | pending |
| Add retrieval regression tests | pending |
| Track quality before/after every retrieval change | pending |

**Exit criteria:**

- Pull requests fail if quality drops
- Dashboard or report showing eval scores over time
- Can explain which metric caught which failure

---

## October 2026 — LangGraph agent system

**Goal:** Move from chatbot to controlled agent workflow.

**Project:** Analytics Agent Orchestrator  
**Repo:** `analytics-agent-orchestrator` (planned)

| Task | Status |
|------|--------|
| Build LangGraph agent with explicit state | pending |
| Add tools: search docs, query metadata, summarize tables, create task | pending |
| Add conditional routing | pending |
| Add memory: short-term thread state and long-term user/project facts | pending |
| Add checkpointing | pending |
| Add human approval before risky actions | pending |
| Add retries, timeouts, and failure paths | pending |

**Exit criteria:**

- Agent answers documentation questions
- Agent inspects data catalog metadata
- Agent asks for approval before sensitive tools
- Agent traces show every step clearly

---

## November 2026 — MCP + multi-agent integration

**Goal:** Become tool-platform fluent.

**Repos:**

- `mcp-data-catalog-server` (planned)
- `mcp-warehouse-assistant` (planned)

| Task | Status |
|------|--------|
| Build one MCP server exposing safe read-only tools | pending |
| Add schemas, validation, auth assumptions, rate limits | pending |
| Connect MCP tools to LangGraph agent | pending |
| Write threat model | pending |
| Add audit logging for tool calls | pending |
| Build small CrewAI comparison over same task | pending |
| Read A2A conceptually; tiny interoperability prototype if time remains | pending |

**Exit criteria:**

- Can explain MCP tools vs API endpoints
- Can explain MCP security risks: confused deputy, SSRF, token passthrough, session hijacking
- Can justify LangGraph as main production orchestrator and CrewAI as secondary tool

---

## December 2026 — Production AI platform capstone

**Goal:** Package everything into a senior portfolio artifact.

**Project:** AI Data Operations Platform  
**Repo:** `ai-data-operations-platform` (planned)

**Must include:**

- Ingestion pipeline
- PostgreSQL + `pgvector`
- RAG service
- LangGraph agent
- MCP server
- Evaluation suite
- LangSmith traces
- OpenTelemetry instrumentation
- Docker Compose deployment
- CI/CD checks
- Cost/latency dashboard
- Security notes and runbook
- Architecture diagram
- Demo video or public walkthrough

**Final deliverables per repo:**

- `README.md` — business problem, architecture, setup, demo
- `docs/architecture.md`
- `docs/evaluation.md`
- `docs/security.md`
- `docs/observability.md`
- `docs/runbook.md`
- `adrs/` — key technical decisions
- Public GitHub repo with clean commits

---

## Skill stack reference

See `skill-matrix.md` for Tier 1/2/3 breakdown and current vs target levels.

## Progress tracking

- Weekly entries: `progress-log.md`
- Repo status and CV/portfolio mapping: `projects-pipeline.md`
- Applications: `job-applications.md`
