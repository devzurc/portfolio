# Agent Commands

Reusable command templates for Cursor. Paste the command block into chat, or create **Cursor Custom Commands** / **Rules** that reference these files.

**Usage pattern:**

```
@.agents/rules.md @.agents/project-context.md
<command below>
```

---

## `/review-portfolio`

Full-site review for hiring impact, UX, accessibility, and factual consistency.

```
/review-portfolio

Run a senior-level portfolio review using @.agents/skills/portfolio-review.md.

Scope: entire site (index.html).
Output:
1. Executive summary (3 sentences max)
2. Top 5 fixes ranked by recruiter impact
3. Section-by-section notes (hero, projects, skills, experience, job-fit, certs, contact)
4. Red flags: unverified claims, broken patterns, EN/PT mismatches
5. Quick wins vs. larger refactors

Do not edit files unless I ask you to implement fixes.
```

---

## `/start-audit-sync`

Start a new session with a full project, portfolio, CV, career knowledge, and job-fit alignment audit.

```
/start-audit-sync

Use @.agents/prompts/start-audit-sync.md.

Read the required context files, audit the repo, verify local integrity, map any pasted Notion sprint tasks into public-safe career knowledge, and return:
1. Alignment status
2. Issues ranked by severity
3. Fixes applied or proposed
4. Next sprint tasks
5. Job-fit and role-search suggestions

Do not commit unless I explicitly ask.
```

---

## `/improve-section`

Targeted copy and structure improvement for one section.

```
/improve-section <section-id>

Use @.agents/prompts/improve-section.md with section: <section-id>
Valid IDs: hero | projects | skills | experience | job-fit | certifications | contact

Before editing:
- Read @.agents/rules.md and @.agents/project-context.md
- List assumptions and questions

Then propose EN + PT copy improvements and minimal HTML changes.
Wait for my approval before applying.
```

**Examples:**

- `/improve-section hero`
- `/improve-section experience`
- `/improve-section projects`

---

## `/add-project`

Safely add a new project card with verified links only.

```
/add-project

Follow @.agents/prompts/add-project.md.

I will provide project details. You must:
1. Ask for any missing required fields
2. Refuse to invent metrics, employers, or URLs
3. Draft EN + PT project card HTML matching existing .project-card structure
4. Suggest where it fits in #projects order (most recent / most relevant first)

Show the diff preview before writing files.
```

---

## `/seo-check`

SEO and social metadata audit without changing page content.

```
/seo-check

Use @.agents/skills/seo-accessibility.md (SEO sections only).

Audit:
- <title>, meta description, og:* tags
- Heading hierarchy and keyword alignment
- Missing canonical, og:image, twitter:card (if applicable)
- Link rel attributes on external URLs

Output a checklist with severity (critical / nice-to-have).
Do not modify index.html unless I say "apply SEO fixes".
```

---

## `/pre-commit-review`

Final gate before git commit.

```
/pre-commit-review

Run @.agents/prompts/review-before-commit.md against current git diff.

Report:
- Factual integrity issues
- EN/PT parity gaps
- Accessibility regressions
- Scope creep (unrelated changes)
- Suggested commit message (1–2 sentences, why-focused)

Do not commit unless I explicitly ask.
```

---

## `/frontend-fix`

Small UI/CSS/JS maintenance task.

```
/frontend-fix <description>

Use @.agents/skills/frontend-maintenance.md.

Task: <description>

Constraints:
- Minimal diff
- Preserve design tokens and i18n pattern
- No new dependencies
- Describe how to verify on mobile + desktop
```

---

## `/linkedin-sync`

Align portfolio messaging with LinkedIn profile copy.

```
/linkedin-sync

Use @.agents/skills/copywriting-linkedin.md.

Compare hero + experience positioning with LinkedIn-style headline/about text I provide.
Suggest EN improvements for both portfolio and LinkedIn post snippets.
Do not invent achievements — flag gaps for me to fill.
```

---

## `/a11y-pass`

Accessibility-focused pass.

```
/a11y-pass

Use @.agents/skills/seo-accessibility.md (accessibility sections).

Check: contrast, focus order, aria labels, keyboard nav, motion preferences, semantic structure.
Prioritize fixes that help screen readers and keyboard users without redesigning the site.
```

---

## `/update-cv`

Add, edit, or remove CV content with EN + PT drafts for Google Docs.

```
/update-cv

Follow @.agents/prompts/update-cv.md and @.agents/skills/cv-management.md.

Operation: {{add | edit | remove}}
Section: {{summary | skills | experience | projects | education | header}}

I will describe the change below. You must:
1. Draft paste-ready text for EN and PT Google Docs (links in project-context.md)
2. Never invent dates, employers, or metrics
3. Show portfolio sync impact (index.html) without editing until I approve
4. Remind me to export PDFs to docs/resume/pdf/ and assets/files/cv/
```

**Examples:**

- `/update-cv` — add a new contract role with 4 bullets
- `/update-cv` — remove an outdated project from Notable Projects
- `/update-cv` — tighten Professional Summary for Gen. AI focus

---

## `/sync-cv-portfolio`

Audit or apply alignment between CV PDF and portfolio site.

```
/sync-cv-portfolio {{audit | apply}}

Use @.agents/skills/cv-management.md (Portfolio Sync Matrix).

Sources:
@docs/resume/pdf/LucasCruz_CV_EN.pdf
@index.html

If audit: list mismatches by severity (factual BLOCK vs cosmetic).
If apply: propose minimal index.html diffs for EN + PT only where CV is authoritative.
Wait for approval before writing files.
```

---

## `/sync-cv-from-google`

Pull latest CV files from public Google Docs.

```
/sync-cv-from-google

Run: python3 docs/resume/scripts/sync-from-google-docs.py

Then confirm:
- docs/resume/word/, pdf/, source/ updated
- assets/files/cv/ PDFs updated for site downloads
- Remind me to update markdown/*.md if Google Doc changed
- Suggest /sync-cv-portfolio if portfolio may be out of date
```

---

## `/export-cv-reminder`

Checklist after owner edits Google Docs (alias for sync + verify).

```
/export-cv-reminder

Same as /sync-cv-from-google with a short verification checklist.
```

---

## `/sync-github-career`

Pull GitHub repo READMEs and refresh career knowledge index.

```
/sync-github-career

Run @.agents/skills/career-knowledge.md workflow:
1. Execute python3 docs/career/scripts/sync-github-projects.py
2. Summarize repos synced, new readmes, stubs created
3. List projects still status: needs-review
4. Do not edit portfolio or CV unless I ask
```

---

## `/continuous-career-sync`

Watch GitHub and keep the career workspace ready to sync into CV, cover letter, docs, portfolio, and job-search strategy.

```
/continuous-career-sync

Use @.agents/prompts/continuous-career-sync.md and @.agents/skills/continuous-career-sync.md.

Run the GitHub sync script, inspect docs/career/github-sync-report.md, and:
1. Apply safe evidence-layer updates only:
   - docs/career/readmes/*.md
   - docs/career/INDEX.md
   - docs/career/tech-stack-rollup.md
   - docs/career/github-sync-report.md
   - new docs/career/projects/*.md stubs with status: needs-review
2. Rank new GitHub signals by career value.
3. List projects that need owner curation.
4. Draft CV, cover letter, portfolio, and job-strategy updates without applying them unless I explicitly ask.
5. Preserve EN/PT parity and public-safety rules.

Do not commit unless I explicitly ask.
```

---

## `/curate-project`

Fill in a curated project profile from README + owner input.

```
/curate-project <repo-name>

Use @.agents/skills/career-knowledge.md and:
@docs/career/readmes/<repo-name>.md
@docs/career/projects/<repo-name>.md

Ask me for missing employer, dates, outcomes, and whether portfolio_worthy / cv_worthy.
Propose updated projects/<repo-name>.md content; wait for approval before writing.
```

---

## Command Aliases (optional)

| Alias | Maps to |
|-------|---------|
| `/review` | `/review-portfolio` |
| `/section` | `/improve-section` |
| `/project` | `/add-project` |
| `/seo` | `/seo-check` |
| `/commit-check` | `/pre-commit-review` |
| `/cv` | `/update-cv` |
| `/cv-sync` | `/sync-cv-portfolio` |
| `/cv-pull` | `/sync-cv-from-google` |
| `/career-sync` | `/sync-github-career` |
| `/career-watch` | `/continuous-career-sync` |
| `/curate` | `/curate-project` |

---

## Creating Cursor Custom Commands

In Cursor: **Settings → Cursor Settings → Rules, Commands** (or project `.cursor/commands` if configured).

Point each command to the corresponding block above and attach:

- `@.agents/rules.md`
- `@.agents/project-context.md`
- Relevant skill or prompt file

This keeps behavior consistent across sessions.
