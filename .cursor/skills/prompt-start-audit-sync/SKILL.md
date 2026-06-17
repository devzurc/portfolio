---
name: prompt-start-audit-sync
description: Starts a full portfolio, CV, career, and job-fit alignment audit session. Use for /start-audit-sync or when beginning a comprehensive repo and career audit.
disable-model-invocation: true
---

# Prompt: Start Audit and Sync Session

Use this prompt at the start of a new AI-agent chat when you want a full repo/career/portfolio alignment pass.

```markdown
Read the whole project and run a careful portfolio/career audit.

Context to read first:
@.agents/rules.md
@.agents/project-context.md
@.agents/skills/portfolio-review.md
@.agents/skills/frontend-maintenance.md
@.agents/skills/seo-accessibility.md
@.agents/skills/career-knowledge.md
@.agents/skills/cv-management.md
@.agents/skills/continuous-career-sync.md
@docs/career/README.md
@docs/career/ALIGNMENT-PLAN.md
@docs/career/JOB-SEARCH-STRATEGY.md
@docs/career/tktech-sprint-knowledge.md
@docs/career/github-sync-report.md

Audit goals:
1. Inspect tracked project files and important ignored/local generated areas safely.
2. Do not treat `.git/`, `.venv/`, `__pycache__/`, or third-party package files as portfolio source files.
3. Check `index.html`, `assets/css/*.css`, `assets/js/site.js`, `robots.txt`, `sitemap.xml`, local assets, CV files, career knowledge, and agent docs.
4. Verify local links/assets, section IDs, nav anchors, EN/PT parity, CV download paths, sitemap date, and JavaScript section wiring.
5. Check that public portfolio claims are backed by the CV or `docs/career/projects/*.md`.
6. Flag stale Google Docs/source export drift before running any sync script.
7. Preserve privacy: do not publish workflow IDs, webhook URLs, private client names, phone numbers, secrets, internal URLs, or raw Notion ticket names.
8. If I paste Notion sprint tasks, map them into public-safe career evidence and job-search strategy notes.
9. Check the continuous career sync loop: latest GitHub report, needs-review project profiles, new tech signals, and whether CV/cover letter/portfolio drafts are waiting on owner confirmation.

Expected output:
- Executive summary of alignment status.
- Issues found, ranked by severity.
- Fixes applied, if I asked you to apply fixes.
- Remaining owner confirmations.
- Tasks for next sprint.
- Suggestions to improve portfolio/CV/job search positioning.
- Role-fit recommendations using `docs/career/JOB-SEARCH-STRATEGY.md`.
- Continuous sync health: GitHub signals, curation backlog, and public-surface drafts needed.

Implementation rules:
- Make minimal, focused edits when the issue is clear.
- Preserve bilingual EN/PT content.
- Do not invent metrics, employers, project links, certifications, dates, or outcomes.
- Do not commit unless I explicitly ask.
- Before ending, run local verification checks and summarize what passed or could not be checked.
```

## Optional add-on for Notion tasks

Paste after the prompt above:

```markdown
Here are my current Notion sprint tasks. Sanitize them before adding to public repo docs. Map each task to:
1. career signal,
2. possible CV/portfolio wording,
3. job roles it supports,
4. owner confirmations needed.

Tasks:
{{paste tasks or screenshot transcription here}}
```
