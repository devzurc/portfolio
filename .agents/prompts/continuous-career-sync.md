# Prompt: Continuous Career Sync

Use this prompt when you want the agent to watch GitHub activity and keep the career workspace aligned across knowledge, CV drafts, cover letter, docs, and portfolio.

```markdown
Run a continuous career sync pass.

Context to read first:
@.agents/rules.md
@.agents/project-context.md
@.agents/skills/continuous-career-sync.md
@.agents/skills/career-knowledge.md
@.agents/skills/cv-management.md
@docs/career/README.md
@docs/career/ALIGNMENT-PLAN.md
@docs/career/JOB-SEARCH-STRATEGY.md
@docs/resume/markdown/LucasCruz_Cover_Letter_Europe_EN.md

Sync steps:
1. Run `python3 docs/career/scripts/sync-github-projects.py`.
2. Read `docs/career/github-sync-report.md`.
3. Identify new repos, updated READMEs, new tech signals, and project profiles needing review.
4. Update safe evidence-layer files only when the change is clear.
5. Draft, but do not apply, CV, cover letter, portfolio, and job-search wording unless I explicitly ask you to apply public-surface changes.
6. Preserve EN/PT parity for CV and website changes.
7. Do not publish private repo details, private client names, raw Notion ticket names, workflow IDs, webhook URLs, internal URLs, secrets, phone numbers, or unconfirmed metrics.

Expected output:
- Sync status and files changed.
- GitHub signals ranked by career value.
- Project profiles that need curation.
- Draft CV/cover letter/portfolio/job-strategy updates, if any.
- Owner confirmations needed.
- Next sync tasks.

Do not commit unless I explicitly ask.
```

## Optional owner input

Paste after the prompt above:

```markdown
Here are extra updates since the last sync. Sanitize before adding to public surfaces:

{{paste notes, Notion tasks, project updates, repo links, or learning notes}}
```
