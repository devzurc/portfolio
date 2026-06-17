---
name: agents-to-skills
description: Reads the project `.agents/` workspace (skills, prompts, rules, commands) and creates or updates Cursor Agent Skills in `.cursor/skills/`. Use when migrating `.agents/` playbooks to Cursor skills, syncing agent docs to skills, or when the user asks to read agents and create skills.
disable-model-invocation: true
---

# Agents to Skills

Convert the project `.agents/` workspace into native Cursor Agent Skills.

**CRITICAL: Preserve the exact body content from source files. Do not modify, reformat, or "improve" it — copy verbatim after frontmatter.**

## Source layout

| Path | Role | Cursor destination |
|------|------|-------------------|
| `.agents/skills/*.md` | Task playbooks | `.cursor/skills/{name}/SKILL.md` |
| `.agents/prompts/*.md` | Slash-style invocations | `.cursor/skills/prompt-{name}/SKILL.md` |
| `.agents/rules.md` | Binding rules | Keep in `.agents/`; optionally `.cursor/rules/portfolio-agent-rules.mdc` |
| `.agents/project-context.md` | Repo facts | Keep in `.agents/`; reference from skills via `@.agents/project-context.md` |
| `.agents/commands.md` | Command index | Keep in `.agents/`; do not duplicate unless user asks |

Do **not** delete `.agents/` originals unless the user explicitly requests removal after verifying skills work.

## Conversion format

### Agent skill → SKILL.md

```markdown
---
name: portfolio-review
description: Runs holistic hiring-manager review of the portfolio site. Use for /review-portfolio, full-site hiring impact review, or recruiter lens assessment.
---

# Skill: Portfolio Review
(original body unchanged)
```

Changes: add `name` (from filename without `.md`) and `description` (third person, WHAT + WHEN). Keep body exactly.

### Agent prompt → SKILL.md

```markdown
---
name: prompt-start-audit-sync
description: Starts a full portfolio, CV, career, and job-fit alignment audit session. Use for /start-audit-sync or when beginning a comprehensive repo audit.
disable-model-invocation: true
---

# Prompt: Start Audit and Sync Session
(original body unchanged)
```

Changes: prefix skill `name` with `prompt-`, add `disable-model-invocation: true` (prompts are user-triggered, not auto-invoked).

### Description rules

1. Write in **third person**
2. Include **WHAT** the skill does and **WHEN** to use it
3. Pull trigger phrases from the source's "Use when…" / "Use this skill…" / command names in `.agents/commands.md`
4. Max 1024 characters; `name` max 64 chars, lowercase hyphens only

## Workflow

```
Task Progress:
- [ ] Step 1: Inventory `.agents/`
- [ ] Step 2: Create `.cursor/skills/` if missing
- [ ] Step 3: Convert each `.agents/skills/*.md`
- [ ] Step 4: Convert each `.agents/prompts/*.md` (prefix `prompt-`)
- [ ] Step 5: Report summary; suggest rules migration if needed
```

### Step 1 — Inventory

List:

- `.agents/skills/*.md`
- `.agents/prompts/*.md`
- `.agents/rules.md`, `.agents/project-context.md`, `.agents/commands.md`

Read `.agents/project-context.md` § Agent Workspace for the canonical file map.

### Step 2 — Create destination

Ensure `.cursor/skills/` exists in the project root.

### Step 3–4 — Convert files

For each source file:

1. Read with the Read tool (not terminal)
2. Derive `name` from filename (`portfolio-review.md` → `portfolio-review`; prompts → `prompt-{basename}`)
3. Write `.cursor/skills/{name}/SKILL.md` with frontmatter + **exact** original content
4. Use the Write/StrReplace tool (not terminal) for file creation

**Skip** if destination SKILL.md already exists and user did not ask to refresh — report as skipped.

### Step 5 — Report

Summarize in a table:

| Source | Cursor skill | Status |
|--------|--------------|--------|
| `.agents/skills/portfolio-review.md` | `portfolio-review` | created / updated / skipped |

Note:

- `@.agents/...` references in skill bodies remain valid — do not rewrite unless user asks
- For always-on rules, suggest creating `.cursor/rules/portfolio-agent-rules.mdc` from `.agents/rules.md` (separate from this skill; see create-rule skill)
- To undo, delete `.cursor/skills/{name}/` directories created in this run

## Parallel execution

If the Task tool is available and there are 5+ files, dispatch general-purpose subagents in parallel:

- One for `.agents/skills/*.md`
- One for `.agents/prompts/*.md`

Each subagent: read sources, write SKILL.md files preserving bodies exactly, return created paths.

## Quick regenerate

From project root, run the bundled script when the user wants a full refresh:

```bash
python3 .cursor/skills/agents-to-skills/scripts/convert.py
```

The script overwrites existing Cursor skills derived from `.agents/`. Review the summary output before committing.

## Additional resources

- Skill inventory and description map for this repo: [reference.md](reference.md)
- Cursor rules/commands migration (different source): use the `migrate-to-skills` skill for `.cursor/rules/*.mdc` and `.cursor/commands/*.md`
