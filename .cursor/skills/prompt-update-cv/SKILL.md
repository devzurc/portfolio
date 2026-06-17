---
name: prompt-update-cv
description: Handles CV add, edit, or remove operations with Google Docs workflow. Use for CV update requests, new roles, bullets, skills, or CV-portfolio sync audits.
disable-model-invocation: true
---

# Prompt: Update CV

Use for any CV add, edit, or remove operation. Attach rules, project context, and CV skill.

---

## Master Template

```
CV update request

@.agents/rules.md
@.agents/project-context.md
@.agents/skills/cv-management.md

Operation: {{add | edit | remove}}
Section: {{summary | skills | experience | projects | education | header}}
Language: {{both | en | pt}}  <!-- default: both -->

Details:
{{DESCRIBE THE CHANGE — facts, dates, metrics, wording preferences}}

Reference (if available):
@docs/resume/markdown/LucasCruz_CV_EN.md
@docs/resume/markdown/LucasCruz_CV_PT.md
@docs/resume/source/LucasCruz_CV_EN.txt

Instructions:
1. Use Google Docs as canonical target (draft text for owner to paste):
   - EN: https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit
   - PT: https://docs.google.com/document/d/1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q/edit
2. Do NOT invent employers, dates, or metrics
3. Show before → after for edits
4. List portfolio sync items (index.html) separately
5. Do not edit index.html until I approve

Output using the deliverable format in cv-management.md.
```

---

## Quick Templates

### Add experience role

```
CV update — add experience

Company: {{COMPANY}}
Title: {{TITLE}}
Location: {{CITY}} — {{COUNTRY}} ({{Remote|Hybrid|On-site}})
Dates: {{START}} – {{END}}
Type: {{Contract|Full-time}}

Bullets (rough notes — refine with impact + tech):
- {{bullet 1}}
- {{bullet 2}}
- {{bullet 3}}

Also sync to portfolio #experience? {{yes | no | propose}}

@.agents/prompts/update-cv.md
```

### Edit one bullet

```
CV update — edit experience bullet

Role: {{TITLE}} at {{COMPANY}}
Current bullet: "{{paste exact bullet}}"
Desired change: {{what to improve or new fact — owner-verified only}}

@.agents/prompts/update-cv.md
```

### Remove item

```
CV update — remove

Section: {{experience | projects | skill}}
Item: {{exact title or company name}}
Reason: {{e.g. space, outdated, duplicate}}
Also remove from portfolio? {{yes | propose mapping}}

@.agents/prompts/update-cv.md
```

### Add skill

```
CV update — add skill

Skill: {{NAME}}
Category: {{Gen. AI | Data Engineering | ...}}
Evidence: {{role or project that proves usage}}

@.agents/prompts/update-cv.md
```

### Full sync check

```
CV ↔ portfolio sync audit

Compare:
@docs/resume/pdf/LucasCruz_CV_EN.pdf
@index.html

List mismatches in employers, dates, projects, skills, or metrics.
Do not fix — report only unless I say "apply fixes."

@.agents/skills/cv-management.md
```

---

## Post-Update Checklist (owner)

After pasting into Google Docs:

- [ ] Run `python3 docs/resume/scripts/sync-from-google-docs.py`
- [ ] Update `docs/resume/markdown/*.md` if copy was drafted in chat
- [ ] Approve portfolio HTML changes if any
- [ ] Run `/pre-commit-review`
