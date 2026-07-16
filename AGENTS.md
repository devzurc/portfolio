# Agent workspace — Lucas Cruz portfolio

This repo uses a **dual-layer agent system**. Edit the canonical layer first.

## Canonical sources (edit these)

| Layer | Path | Role |
|-------|------|------|
| **Always-on rules** | [`.cursor/rules/portfolio-agent-rules.mdc`](.cursor/rules/portfolio-agent-rules.mdc) | Binding agent behavior |
| **Skills** | [`.cursor/skills/`](.cursor/skills/) | Task playbooks (career, CV, frontend, SEO, AI roadmap) |
| **Repo facts** | [`.agents/project-context.md`](.agents/project-context.md) | Paths, Google Doc IDs, site structure |
| **Commands** | [`.agents/commands.md`](.agents/commands.md) | Slash-command templates |
| **Career knowledge** | [`docs/career/`](docs/career/) | Project profiles, job strategy, GitHub sync |
| **AI roadmap** | [`docs/career/goals/`](docs/career/goals/) | Senior AI Platform Specialist roadmap Jul–Dec 2026 |

## Legacy references (stable `@` paths)

[`.agents/`](.agents/) mirrors skills and prompts for commands that `@`-reference `.agents/` paths. When content diverges, **`.cursor/skills/` wins**. Re-sync with `.cursor/skills/agents-to-skills/scripts/convert.py` if needed.

## Quick start for agents

1. Read `.cursor/rules/portfolio-agent-rules.mdc` (auto-applied)
2. Read `.agents/project-context.md` for repo facts
3. Pick a skill from `.cursor/skills/` matching the task
4. Use `.agents/commands.md` for structured slash workflows

## Key commands

| Command | Purpose |
|---------|---------|
| `/continuous-career-sync` | GitHub → career knowledge → draft CV/portfolio updates |
| `/weekly-review` | Friday ritual: progress log, projects pipeline, skill matrix |
| `/sync-cv-portfolio audit` | CV ↔ site alignment check |
| `/review-portfolio` | Full hiring-impact review |

## Evidence pipeline

```text
GitHub repos → sync-github-projects.py → docs/career/projects/*.md
                                        → docs/resume/ + index.html (approval required)
docs/career/goals/ → monthly capstone repos → same pipeline
```

**Public rule:** Only use facts backed by curated profiles (`verified_outcomes`) or CV text. Roadmap skills are in-progress until repos prove them.
