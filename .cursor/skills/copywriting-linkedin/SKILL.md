---
name: copywriting-linkedin
description: Improves portfolio copy and LinkedIn-aligned messaging. Use when improving hero copy, experience bullets, project descriptions, or syncing tone with LinkedIn.
---

# Skill: Copywriting & LinkedIn Alignment

Use this skill when improving portfolio copy, hero messaging, experience bullets, project descriptions, or syncing tone with LinkedIn content.

---

## Audience

- **Primary:** Technical recruiters and hiring managers (EU market)
- **Secondary:** Engineering leads scanning for pipeline + Gen. AI depth
- **Language:** Professional EN (default) + PT-BR (paired blocks)

---

## Voice & Tone

| Do | Don't |
|----|-------|
| Confident, specific, outcome-oriented | Humble-brag clichés ("passionate", "rockstar") |
| Lead with systems you built | Lead with tools you "know" |
| Use strong verbs: architected, automated, orchestrated, deployed | Passive voice walls |
| Mention scale **only with owner-verified numbers** | Round up or invent metrics |
| Acknowledge relocation + visa need clearly | Hide location/sponsorship facts |

**Register:** Senior IC — credible peer, not marketing brochure.

---

## Positioning Pillars

Rotate these themes based on section:

1. **Data Engineering** — lakehouses, ETL/ELT, Spark, SQL, Airflow, cloud warehouses
2. **Gen. AI Engineering** — LLM integration, RAG, agents, prompt design, production guardrails
3. **Automation** — n8n workflows, API integrations, reducing manual ops
4. **Production mindset** — reliability, observability, data quality, security awareness

Keywords to weave naturally (not stuffed): *pipeline*, *orchestration*, *Delta Lake*, *Databricks*, *Snowflake*, *REST API*, *Docker*, *Azure*, *AWS*, *GCP*.

---

## Section Playbooks

### Hero (above the fold)

**Goal:** Answer in 5 seconds: *Who is this? What do they do? Why should I keep scrolling?*

Structure:

1. Role line — Data Engineer / Gen. AI Engineer (both EN + PT)
2. One paragraph — 2–3 sentences max
3. Stats row — only verified figures from current site or owner input

Formula:

> [Role] building [system type] with [core stack]. [Years/context domains]. I focus on [differentiator].

### Experience bullets

Use **impact + method + tech** pattern:

```
• [Outcome or scope] by [action] using [tech stack]
```

Rules:

- 3–5 bullets per role
- Most recent role gets strongest detail
- Past tense for previous jobs; present for current
- No bullet without something concrete (pipeline, platform, team, scale)

### Projects

Structure per card:

1. **Title** — clear product/system name
2. **One-liner** — problem solved
3. **Body** — architecture + your contribution (2–4 sentences or bullets)
4. **Tags** — stack only (existing `.tag` pattern)
5. **Links** — GitHub/demo/docs (real URLs only)

### Contact

Keep friction low. Reinforce:

- Open to Europe opportunities
- Visa sponsorship required
- Email + LinkedIn prominent

---

## EN / PT-BR Guidelines

| Aspect | Guidance |
|--------|----------|
| Pairing | Every EN block needs PT sibling |
| Titles | PT: "Engenheiro de Dados", "IA Generativa" — match site conventions |
| Tone | PT-BR professional, not European Portuguese unless owner requests |
| Length | PT can be ~5–15% longer; avoid truncation in cards |
| Tech terms | Often kept in English (Airflow, RAG, Lakehouse) — consistent with current site |

After copy edits, remind implementer to update:

- `document.title` strings in `setLang()` if headline changed
- `<meta name="description">` if value prop changed

---

## LinkedIn Sync Workflow

When user provides LinkedIn headline/about or asks for cross-platform consistency:

1. Extract **3 core claims** from portfolio hero + latest role (or `@docs/resume/pdf/LucasCruz_CV_EN.pdf` / Google Doc)
2. Propose LinkedIn **headline** (220 chars max) and **about** opening (2 lines)
3. Flag any LinkedIn claim **not** supported on portfolio → remove or add to site first
4. Optional: suggest one **post hook** when a new project goes live (factual, no hype)

### LinkedIn headline templates (adapt, don't copy blindly)

```
Data Engineer | Gen. AI · Lakehouses · LLM Automation · Python · Airflow · Cloud
```

```
Engenheiro de Dados & IA Generativa | Pipelines · RAG · n8n · AWS/Azure/GCP
```

---

## Fabrication Guardrails

Before finalizing copy, ask:

- [ ] Is every metric traceable to owner or existing site content?
- [ ] Is every employer name and date correct?
- [ ] Does every project link resolve?
- [ ] Are cert names spelled exactly as issued?

If any answer is no → **stop** and request source material.

---

## Deliverable Format

```
## EN (proposed)
...

## PT-BR (proposed)
...

## Rationale
- Recruiter scan: ...
- Keywords added: ...

## Owner must confirm
- [ ] ...
```

Do not apply HTML edits until owner approves proposed copy.
