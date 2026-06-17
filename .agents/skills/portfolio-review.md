# Skill: Portfolio Review

Use this skill for `/review-portfolio` — a holistic hiring-manager and recruiter lens on the entire site.

---

## Review Principles

1. **First impression in 10 seconds** — hero must land role + value
2. **Credibility over flair** — animations and aesthetics support, not replace, substance
3. **Evidence chain** — claims in hero should echo in experience and projects
4. **Friction to contact** — how fast can a recruiter email or download CV?
5. **Truth safety** — flag anything that reads inflated or unsupported

---

## Review Workflow

### Step 1 — Recruiter skim simulation

Read top to bottom once without editing. Note:

- What role would you pitch this candidate for?
- What's the single strongest proof point?
- What's confusing or missing?
- Would you download the CV?

### Step 2 — Section scoring

Score each section **1–5** (5 = excellent for target roles):

| Section | Criteria |
|---------|----------|
| Hero | Role clarity, differentiation, CTA, stats credibility |
| Skills | Grouping logic, relevance to DE + Gen. AI, not a laundry list |
| Experience | Reverse chronological, impact bullets, tech keywords |
| Projects | Real links, architecture clarity, outcome honesty |
| Job fit | Target roles, growth environment, search filters, evidence alignment |
| Certifications | Verifiable URLs, relevant to target roles |
| Contact | Location/relocation/visa clarity, link prominence |
| Footer | Professional, consistent |

### Step 3 — Cross-section consistency

Check alignment:

| Claim location | Must align with |
|----------------|-----------------|
| Hero stats | Experience or projects |
| Skill tags | Experience bullets / projects |
| Gen. AI positioning | At least one project or role proof |
| Years of experience | CV and LinkedIn (owner verifies) |
| Google Docs CV | `project-context.md` — EN + PT links |

### Step 4 — i18n parity

- Every `.en-only` block has `.pt-only` counterpart
- Nav `data-en` / `data-pt` complete
- Title switch in `setLang()` matches positioning
- No orphaned English in PT mode

### Step 5 — Technical quality (light)

- Mobile nav functional
- No obvious layout breaks
- Meta description matches hero
- External links credible

---

## Red Flag Catalog

Stop and escalate to owner if found:

| Red flag | Risk |
|----------|------|
| Metric with no source | Credibility loss in interviews |
| Project without repo/demo | Looks like vaporware |
| Cert link broken | Easy to verify failure |
| Skills with zero backing | Keyword stuffing perception |
| EN/PT mismatch in meaning | Unprofessional for bilingual market |
| Outdated copyright year | Neglect signal |

---

## Competitive Benchmark (DE + Gen. AI)

Strong portfolios in this space usually show:

- **At least one** pipeline/lakehouse narrative with stack depth
- **At least one** LLM/automation narrative (RAG, agents, n8n, API)
- Clear **cloud** footprint (not just logos)
- **GitHub** activity or pinned repos linked from projects
- CV PDF **one click** from hero or contact

Gap analysis: list which of the above are weak or missing (without inventing content to fill gaps).

---

## Output Template

```markdown
## Executive summary
<3 sentences>

## Scores
| Section | Score | One-line note |
|---------|-------|---------------|
| Hero | /5 | |
| Skills | /5 | |
| ... | | |

## Top 5 prioritized actions
1. **[Impact: High]** ...
2. ...

## Quick wins (< 30 min)
- ...

## Medium efforts (copy or structure)
- ...

## Large efforts (defer unless requested)
- ...

## Factual verification needed
- [ ] ...

## i18n issues
- ...

## Do not change without owner
- ...
```

---

## Implementation Policy

- **Review mode:** report only, no file edits
- **Fix mode:** only after user says "implement #1 and #2" (or similar)
- When implementing, use `@.agents/skills/frontend-maintenance.md` for HTML/CSS and `@.agents/skills/copywriting-linkedin.md` for copy

---

## Periodic Review Triggers

Suggest full review when:

- New job or project added
- Job search focus shifts (e.g. pure DE vs Gen. AI heavy)
- CV PDF updated
- Before major LinkedIn push or conference application
