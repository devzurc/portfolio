# Senior AI Platform Specialist — goals system

> Living workspace for the Jul–Dec 2026 roadmap: build production AI systems, track progress, and wire evidence into CV, portfolio, and job search.

## North star

By **December 31, 2026**, prove with shipped, public artifacts that you can design and operate an end-to-end production AI system:

- FastAPI backend
- PostgreSQL + `pgvector`
- Ingestion pipeline
- RAG with hybrid retrieval, metadata filters, reranking
- LangGraph agent orchestration
- MCP tools/server
- Memory layer
- Eval harness with RAGAS + DeepEval
- LangSmith / OpenTelemetry observability
- Dockerized deployment
- Cost, latency, quality, and security runbooks

## Positioning niche

> I build production AI systems over real enterprise data: ingestion, retrieval, agents, tools, evaluation, observability, and deployment.

Use this line in hero copy, CV summary, cover letter, LinkedIn, and interview intros. It is stronger than "I know LangChain and CrewAI."

## Title targets

- Senior AI Engineer
- AI Platform Engineer
- Applied AI Engineer
- GenAI Systems Engineer
- RAG / Agentic AI Specialist
- AI Data Platform Engineer

## How this folder connects to the rest of the repo

| File | Purpose |
|------|---------|
| `senior-ai-roadmap.md` | Monthly themes, tasks, exit criteria, repo targets |
| `skill-matrix.md` | Tier 1/2/3 stack with current vs target levels |
| `projects-pipeline.md` | Capstone repos, status, CV/portfolio mapping |
| `progress-log.md` | Weekly cadence log (build, measure, explain, harden) |
| `job-applications.md` | Parallel job search tracker (US/EU English roles) |

### Evidence pipeline

```text
docs/career/goals/          ← strategy and tracking (this folder)
        ↓
Monthly capstone repos      ← separate public GitHub repos under devzurc
        ↓
sync-github-projects.py     ← mirrors READMEs, creates stubs
        ↓
docs/career/projects/*.md   ← curated profiles (portfolio_worthy / cv_worthy)
        ↓
docs/resume/ + index.html   ← public surfaces (approval required)
```

**Rule:** Public copy only uses facts backed by curated project profiles or CV text. Do not claim roadmap skills until a repo proves them.

## Job search strategy (parallel, not sequential)

Apply **now** as Senior Data Engineer / GenAI Engineer with current evidence. Each monthly milestone strengthens applications already in flight. See `job-applications.md` for tracker and `JOB-SEARCH-STRATEGY.md` for role families.

## Weekly routine

| Day | Action |
|-----|--------|
| Monday | Choose one measurable system improvement; log it in `progress-log.md` |
| Tuesday–Wednesday | Implement |
| Thursday | Evaluate and observe (metrics, traces, cost) |
| Friday | Write one technical note; update `progress-log.md` |
| Weekend | Polish portfolio or compare one Tier 3 tool lightly |

The senior habit: **build, measure, explain, harden**.

## Agent commands

- `/weekly-review` — Friday ritual: update progress log, check projects pipeline, propose CV/portfolio deltas
- `/continuous-career-sync` — GitHub sync; routes new AI-platform repos into goals pipeline
- `/curate-project <repo>` — Fill curated profile after a milestone ships

## Using with Cursor

```
@docs/career/goals/senior-ai-roadmap.md
@docs/career/goals/skill-matrix.md
@docs/career/goals/projects-pipeline.md
@.cursor/skills/ai-roadmap-tracking/SKILL.md
```
