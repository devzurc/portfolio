---
name: prompt-improve-section
description: Improves copy and structure for one portfolio section with EN/PT parity. Use for /improve-section or targeted section copy improvements.
disable-model-invocation: true
---

# Prompt: Improve Section

Copy into Cursor chat with section context. Attach `@.agents/rules.md` and `@.agents/project-context.md`.

---

## Template

```
Improve the portfolio section: {{SECTION_ID}}

Context files:
@.agents/rules.md
@.agents/project-context.md
@.agents/skills/copywriting-linkedin.md

Section ID: {{SECTION_ID}}
<!-- Valid: hero | projects | skills | experience | job-fit | certifications | contact -->

My goal for this section:
{{GOAL}}
<!-- e.g. "Stronger Gen. AI keywords for EU recruiters" or "Shorter hero paragraph" -->

Constraints:
- Do NOT invent metrics, employers, projects, or links
- Provide EN + PT-BR copy for every change
- Match existing HTML/CSS patterns in index.html
- Minimal diff — this section only

Process:
1. Quote the current section content (brief excerpt)
2. Diagnose issues for recruiter readability
3. Propose improved EN copy
4. Propose improved PT-BR copy
5. Show exact HTML snippets to replace/add
6. List "Owner must confirm" items if any claim is new or changed

Wait for my approval before editing index.html.
```

---

## Section-Specific Hints

### `hero`

Focus: role clarity, value prop, stat credibility, CTA labels.  
If changing stats → owner must confirm numbers.  
Update meta description + `setLang()` title if headline shifts.

### `skills`

Focus: grouping, removing redundant tags, prioritizing DE + Gen. AI clusters.  
Do not add tools unless owner confirms production use.

### `experience`

Focus: impact bullets (outcome + action + tech), reverse chronological integrity.  
Never change dates/titles/companies without explicit owner input.

### `job-fit`

Focus: target role clarity, growth environment, role-search filters, and public-safe evidence.
Do not add customer-facing or sprint-process claims unless they are backed by owner notes or `docs/career/tktech-sprint-knowledge.md`.

### `projects`

Focus: problem → architecture → outcome; real links only.  
Consider `/add-project` prompt for new cards instead of rewriting all.

### `certifications`

Focus: accurate names, working URLs, logical grouping.  
New certs require certificate URL from owner.

### `contact`

Focus: relocation/visa clarity, link prominence, CV download UX.  
Do not change email or social URLs without owner confirmation.

---

## Example Invocation

```
Improve the portfolio section: hero

My goal: Tighten the hero paragraph for senior DE + Gen. AI roles in Europe; keep 5+ years and IoT scale if already verified.

@.agents/prompts/improve-section.md
@.agents/rules.md
@.agents/project-context.md
```
