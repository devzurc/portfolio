# AI platform projects pipeline

> Tracks capstone repos from roadmap → curated profile → CV → portfolio.  
> Update after each repo ships and after `/continuous-career-sync` or `/weekly-review`.

| Repo (planned) | Month | Status | GitHub URL | Career profile | portfolio_worthy | cv_worthy | Portfolio card | CV bullet |
|----------------|-------|--------|------------|----------------|------------------|-----------|----------------|-----------|
| `raw-llm-systems` | Jul 2026 | planned | — | — | — | — | — | — |
| `data-engineering-knowledge-rag` | Aug 2026 | planned | — | — | — | — | — | — |
| `data-engineering-knowledge-rag` (eval) | Sep 2026 | planned | — | — | — | — | — | — |
| `analytics-agent-orchestrator` | Oct 2026 | planned | — | — | — | — | — | — |
| `mcp-data-catalog-server` | Nov 2026 | planned | — | — | — | — | — | — |
| `mcp-warehouse-assistant` | Nov 2026 | planned | — | — | — | — | — | — |
| `ai-data-operations-platform` | Dec 2026 | planned | — | — | — | — | — | — |

---

## Existing work (already in pipeline)

| Repo / project | Status | GitHub | portfolio_worthy | cv_worthy | Notes |
|----------------|--------|--------|------------------|-----------|-------|
| `cdp-hub` | active | [tktechnologies/cdp-hub](https://github.com/tktechnologies/cdp-hub) (public) · devzurc mirror (private) | true | true | Flagship DE + GenAI platform |
| `whatsapp-automation-platform` | active | private mirror | true | true | Multi-channel CRM & WhatsApp automation |
| `n8n-telegram-assistant` | active | private mirror | true | true | Conversational AI + RAG-adjacent |
| `n8n-whatsapp-assistant` | active | no mirror | true | false | Sanitized profile only |
| `n8n-stripe-checkout` | active | private mirror | true | true | Automation platform proof |
| `spacecom-iot-lakehouse` | client-work | no public repo | true | true | Lakehouse at scale |

---

## Workflow when a milestone ships

1. Create public repo under `devzurc` with README, docs, and clean commits.
2. Run `python3 docs/career/scripts/sync-github-projects.py`.
3. Curate `docs/career/projects/<repo>.md`:
   - Set `portfolio_worthy: true` when ready for site
   - Set `cv_worthy: true` when ready for CV
   - Fill `verified_outcomes` with measured facts only
4. Update this table.
5. Propose CV bullet + portfolio card (approval required).
6. Update `skill-matrix.md` levels for proven skills.

---

## Portfolio section plan

The `#projects` section on `index.html` will grow with AI platform cards as repos ship. Until then, the hero and `#job-fit` carry the AI platform positioning niche. Do not add placeholder cards without a live repo link.
