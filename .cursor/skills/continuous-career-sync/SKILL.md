---
name: continuous-career-sync
description: Watches GitHub signals and keeps career knowledge, CV drafts, cover letter, and portfolio aligned. Use when running continuous career sync, GitHub-to-career propagation, or proactive career workspace updates.
---

# Skill: Continuous Career Sync

Use when Lucas wants the portfolio workspace to watch GitHub and keep career knowledge, CV drafts, cover letter, docs, and website copy aligned with new work evidence.

---

## Purpose

This skill turns new work signals into a controlled sync loop:

1. **Ingest** raw GitHub evidence.
2. **Curate** project truth in `docs/career/projects/*.md`.
3. **Propagate** approved facts into CV, cover letter, portfolio, job strategy, and audit docs.

The agent should be proactive, but not reckless. GitHub can prove that a repo, README, language, or code direction exists; it does not prove employer context, dates, personal contribution, private client permission, or business outcomes.

---

## Source-of-truth loop

| Layer | Path | Rule |
|-------|------|------|
| GitHub mirror | `docs/career/readmes/*.md` | Auto-sync evidence, not final copy |
| Sync report | `docs/career/github-sync-report.md` | First file to inspect after every sync |
| Curated profiles | `docs/career/projects/*.md` | Main AI career knowledge source |
| Role strategy | `docs/career/JOB-SEARCH-STRATEGY.md` | Update when evidence changes role fit |
| CV source | `docs/resume/markdown/*.md` + Google Docs | CV facts must stay EN/PT aligned |
| Cover letter | `docs/resume/markdown/LucasCruz_Cover_Letter_Europe_EN.md` | Keep aligned with strongest current narrative |
| Portfolio | `index.html` | Public subset of curated and CV-backed facts |
| Agent context | `.agents/project-context.md`, `.agents/prompts/start-audit-sync.md` | Keep workflow discoverable |
| AI roadmap | `docs/career/goals/` | Senior AI Platform Specialist tracking — use `@.cursor/skills/ai-roadmap-tracking/SKILL.md` |

Use `@.cursor/skills/career-knowledge/SKILL.md` for project curation and `@.cursor/skills/cv-management/SKILL.md` before changing CV-related content.

---

## Safe automation boundary

### Safe to update automatically

- `docs/career/readmes/*.md`
- `docs/career/INDEX.md`
- `docs/career/tech-stack-rollup.md`
- `docs/career/github-sync-report.md`
- New `docs/career/projects/<repo>.md` stubs with `status: needs-review`

### Draft only until Lucas approves

- CV bullets, skills, summaries, and notable projects
- Cover letter paragraphs
- Portfolio project cards, hero stats, experience bullets, and skills tags
- Job-search positioning that depends on private context

### Always ask before publishing

- Employers, dates, titles, metrics, client names, private repo details, internal URLs, workflow IDs, webhook URLs, raw Notion ticket names, phone numbers, secrets, and unpublished outcomes.

---

## Sync workflow

1. Read `@.agents/rules.md`, `@.agents/project-context.md`, this skill, `@.agents/skills/career-knowledge.md`, and `@.agents/skills/cv-management.md`.
2. Run:

   ```bash
   python3 docs/career/scripts/sync-github-projects.py
   ```

3. Open `docs/career/github-sync-report.md`.
4. Inspect:
   - New or updated README mirrors.
   - New `status: needs-review` project stubs.
   - Newly seen tech stack signals.
   - Recently pushed repos that may indicate active learning or delivery.
5. For each signal, classify it:

| Classification | Meaning | Action |
|----------------|---------|--------|
| `public-evidence` | Public repo/README supports a project or skill | Curate profile and propose public copy |
| `private-evidence` | Real work, but sensitive or private | Add sanitized career note only |
| `learning-signal` | Course, lab, tutorial, experiment | Use for skills only; do not make it flagship |
| `needs-owner` | Missing dates, role, outcome, employer, permission | Ask Lucas or leave TODO |
| `ignore` | Fork, duplicate, stale, profile/config repo | Exclude from public narrative |

6. Update safe evidence-layer files when the change is clear.
7. Draft public-surface updates only from curated profiles or CV-backed facts.
8. End with:
   - What changed automatically.
   - What should be curated next.
   - Draft CV/cover letter/portfolio changes, if any.
   - Owner confirmations needed.

---

## Propagation rules

| Trigger | Allowed next step |
|---------|-------------------|
| New repo | Create or review project profile; decide portfolio/CV worthiness |
| README changed | Compare with curated profile; update problem, stack, architecture, evidence if public-safe |
| New tech appears | Add to `tech-stack-rollup.md`; draft CV/site skill update only if backed by project work |
| Project becomes mature | Propose CV notable project and portfolio card |
| Current work changes | Update `tktech-sprint-knowledge.md` or project profile first, then draft CV/site wording |
| Target role shifts | Update `JOB-SEARCH-STRATEGY.md`, then propose hero/CV summary changes |
| AI platform repo appears or updates | Route to `docs/career/goals/projects-pipeline.md` via `@.cursor/skills/ai-roadmap-tracking/SKILL.md`; update skill matrix when proven |

### AI platform repo slugs

When sync detects these repos, flag for goals pipeline (not generic career flow only):

`raw-llm-systems`, `data-engineering-knowledge-rag`, `analytics-agent-orchestrator`, `mcp-data-catalog-server`, `mcp-warehouse-assistant`, `ai-data-operations-platform`

---

## Output format

```markdown
## Sync status
<what was checked and what changed>

## GitHub signals
- <repo/signal/status>

## Safe updates applied
- <files changed>

## Draft public updates
- CV:
- Cover letter:
- Portfolio:
- Job strategy:

## Owner confirmations needed
- [ ] <fact or permission>

## Next sync tasks
- <highest leverage follow-up>
```
