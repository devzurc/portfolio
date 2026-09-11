# Lucas Cruz portfolio — agent guide

## Project

This is a zero-build GitHub Pages portfolio for Data Engineering, Gen. AI Engineering, and AI Platform Engineering roles. The public site is a bilingual (EN/PT-BR) single page built with `index.html`, modular CSS in `assets/css/`, and vanilla JavaScript in `assets/js/site.js`.

## Canonical agent system

| Purpose | Canonical location |
|---|---|
| Project facts | `.agents/project-context.md` |
| Reusable skills | `.agents/skills/<name>/SKILL.md` |
| Specialist definitions | `.agents/specialists/<name>.md` |
| Generated adapters | `.cursor/agents/` and `.codex/agents/` |
| Cursor rules | `.cursor/rules/` |
| Command index | `.agents/commands.md` |

Use one focused skill for every recurring workflow. Run `python3 .agents/scripts/sync-specialist-adapters.py --check` and `python3 .agents/scripts/validate-agent-system.py` after agent-system changes.

## Common commands

```bash
# Preview the static site
python3 -m http.server 8000

# Validate agent-system structure and generated adapters
python3 .agents/scripts/sync-specialist-adapters.py --check
python3 .agents/scripts/validate-agent-system.py

# Check HTML structure, local asset references, and baseline SEO metadata
python3 scripts/verify-static-site.py

# Synchronize approved CV exports from Google Docs
python3 docs/resume/scripts/sync-from-google-docs.py

# Refresh GitHub-derived career evidence
python3 docs/career/scripts/sync-github-projects.py
```

There is no package manager, build command, or lint command. Use the dependency-free static verifier plus browser checks at mobile, tablet, and desktop widths for frontend changes. Do not add a build dependency without owner approval.

## Non-negotiable constraints

- Never fabricate roles, metrics, employers, certifications, URLs, or skills. CV Markdown and curated career profiles are the public-fact authority.
- Preserve EN/PT-BR parity for every visitor-facing copy change, including metadata and language-toggle behavior.
- Keep the static-site architecture: no framework migration, backend, database, API key, or production dependency without explicit approval.
- Preserve stable section IDs, external-link safety (`target="_blank" rel="noopener noreferrer"`), and existing language-toggle patterns.
- Treat the current v3 dashboard implementation and `assets/css/tokens.css` as the active design baseline. Do not apply the retired Sauce Labs theme.
- Do not commit, deploy, modify CV artifacts, or change public claims unless the owner explicitly asks.

## Delivery workflow

1. Read `.agents/project-context.md` and the matching skill before editing.
2. Use specialists only for independent, narrowly scoped research or verification; one implementation owner makes the edits.
3. Verify the changed behavior, EN/PT-BR parity where applicable, and avoid unrelated refactors.
4. Report changed files, checks run, deferred work, and any factual confirmation required.

## Escalate before changing

- Employment dates, titles, employers, visa sponsorship messaging, metrics, certifications, or project links. Do not add relocation or Europe-only availability copy.
- The stack, deployment model, or public-site information architecture.
- Any request requiring unavailable external access, including Figma. Use supplied exports or screenshots until the relevant connector is available.
