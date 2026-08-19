---
name: agent-system-maintenance
description: Maintain the portable Codex and Cursor agent system from canonical rules, skills, and specialist definitions. Use when changing agent instructions, playbooks, or adapters.
---

# Agent-system maintenance

## Canonical locations

- Repo instructions: `AGENTS.md`
- Rules: `.cursor/rules/`
- Skills: `.agents/skills/<skill-name>/SKILL.md`
- Specialist definitions: `.agents/specialists/`
- Generated adapters: `.cursor/agents/` and `.codex/agents/`

## Workflow

1. Change only canonical sources first; keep skills focused with a precise trigger and progressive disclosure.
2. Keep specialists narrow and read-only by default. A specialist returns evidence and acceptance criteria; one implementation owner writes; QA independently verifies.
3. Generate adapters with `python3 .agents/scripts/sync-specialist-adapters.py`.
4. Validate with `python3 .agents/scripts/validate-agent-system.py` and `python3 .agents/scripts/sync-specialist-adapters.py --check`.
5. Check `AGENTS.md` remains under 32 KiB and that no stale `.cursor/skills/`, flat `.agents/skills/*.md`, or `.agents/prompts/` references remain.

## Output

Return changed canonical sources, generated artifacts, validation results, and any migration/deprecation notes. Never install plugins automatically.
