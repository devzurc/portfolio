# Prompt: Add Project

Use when adding a new entry to `#projects`. Attach rules and project context.

---

## Template

```
Add a new portfolio project card.

Context:
@.agents/rules.md
@.agents/project-context.md
@.agents/skills/copywriting-linkedin.md
@.agents/skills/frontend-maintenance.md

Fill in the project brief below. Leave fields blank if unknown — ask me before proceeding.

---

## Project brief

**Title:** {{TITLE}}

**Timeframe:** {{e.g. 2025 | Q1 2026 | Ongoing}}

**Problem:** {{What problem did this solve?}}

**Your role:** {{What did YOU specifically build/design/own?}}

**Architecture / approach:** {{Pipeline, APIs, LLM flow, infra — factual only}}

**Stack (tags):** {{e.g. Python, Airflow, RAG, n8n, Azure — only confirmed tools}}

**Outcome:** {{Measurable or qualitative — NO invented metrics}}

**Links (required for public projects):**
- GitHub: {{URL or "private — no link"}}
- Demo/docs/blog: {{URL or none}}

**EN one-liner (optional draft):** {{or ask agent to draft}}

**PT one-liner (optional draft):** {{or ask agent to draft}}

**Placement:** {{top of list | after PROJECT_NAME | bottom}}

---

## Agent instructions

1. Validate the brief:
   - If GitHub/demo links are missing and project is claimed as public → ask owner
   - If outcome contains numbers → ask for source
   - Refuse to imply employment at companies not listed in experience unless owner confirms

2. Inspect existing `.project-card` HTML in index.html and mirror structure exactly.

3. Deliver:
   - EN title + description HTML
   - PT title + description HTML (`.en-only` / `.pt-only` or paired blocks matching site pattern)
   - Tag list using `<span class="tag">...</span>`
   - Link row if applicable

4. Show full diff preview before writing files.

5. Remind owner to add IntersectionObserver class `.project-card` if new card uses it.

Do not commit. Do not modify unrelated sections.
```

---

## Required Fields Gate

Do not generate final HTML until you have:

| Field | Required? |
|-------|-------------|
| Title | Yes |
| Problem | Yes |
| Your role | Yes |
| Stack tags | Yes (min 2) |
| EN + PT description | Yes |
| Outcome | Yes (qualitative OK if no metrics) |
| GitHub or demo link | Yes for "showcase" projects; mark N/A if intentionally private |

---

## Copy Quality Bar

Each project card should answer:

1. **What** was built?
2. **How** (architecture one level deep)?
3. **Why** it matters (business or technical outcome)?
4. **Proof** (link)?

Bad (vague):

> Built an AI app using LLMs.

Good (specific, honest):

> Automated weekly reporting by orchestrating Snowflake extracts with Airflow and summarizing results via an LLM API — reduced manual prep for the analytics team.

(Only use metrics the owner provides.)

---

## Example Invocation

```
Add a new portfolio project card.

Title: IoT Lakehouse Ingestion Pipeline
Timeframe: 2024
Problem: Consolidate device telemetry from multiple sources into a queryable lakehouse.
My role: Designed and implemented batch ingestion and dbt models.
Stack: Python, PySpark, Delta Lake, Airflow, AWS
Outcome: Reliable daily loads for analytics; exact scale numbers in CV only.
GitHub: private — no link
Demo: none

@.agents/prompts/add-project.md
@.agents/rules.md
```

---

## Post-Add Checklist

After owner approves and agent applies changes:

- [ ] EN/PT parity checked
- [ ] Tags match skills section (no orphan tech)
- [ ] External links open correctly
- [ ] Card animates on scroll (`.project-card` observer)
- [ ] Consider LinkedIn post draft (optional, factual)
