# Career knowledge base

Private-to-you working area for AI agents to understand **what you built**, **with which stack**, and **in what context** — before anything goes on the portfolio or CV.

## Recommended approach (hybrid)

| Layer | Folder | Purpose |
|-------|--------|---------|
| **Raw mirror** | `readmes/` | Auto-synced README from GitHub — evidence, not marketing copy |
| **Curated truth** | `projects/` | One profile per repo — problem, your role, stack, verified outcomes |
| **Rollups** | `INDEX.md`, `tech-stack-rollup.md`, `github-sync-report.md` | Generated indexes, stack signals, and latest GitHub change report |
| **Next phase** | `ALIGNMENT-PLAN.md` | Checklist to sync CV ↔ portfolio ↔ projects |
| **Job strategy** | `JOB-SEARCH-STRATEGY.md` | Role-fit thinking, search filters, interview story bank |
| **Sprint/process knowledge** | `tktech-sprint-knowledge.md` | Public-safe Notion sprint/task mapping for TKTech delivery work |

**Do not** mirror entire codebases. README + curated profiles are enough for AI and recruiters.

### Why not clone all repos?

- Noise (training repos, forks, old experiments)
- Secret leakage risk (`.env`, credentials in history)
- Huge repo size and stale code
- README + your notes capture **intent and outcomes** — what hiring managers care about

### When README is weak or missing

Edit `projects/<repo>.md` manually. The sync script creates stubs with `status: needs-review`.

---

## Folder layout

```
docs/career/
├── README.md                 ← you are here
├── ALIGNMENT-PLAN.md         ← portfolio + CV alignment (next step)
├── JOB-SEARCH-STRATEGY.md    ← target roles, filters, and role-fit strategy
├── tktech-sprint-knowledge.md ← Notion sprint/process evidence, sanitized
├── github-sync-report.md      ← generated GitHub change report for agents
├── INDEX.md                  ← generated repo table
├── tech-stack-rollup.md      ← generated stack frequency
├── .sync-config.json         ← sync rules
├── readmes/                  ← raw README snapshots
├── projects/                 ← curated career profiles
│   ├── _template.md
│   └── <repo>.md
└── scripts/
    └── sync-github-projects.py
```

---

## Sync from GitHub

Requires [GitHub CLI](https://cli.github.com/) (`gh auth login`).

```bash
python3 docs/career/scripts/sync-github-projects.py
```

This will:

1. List repos for `devzurc` (see config)
2. Save each README to `readmes/<repo>.md`
3. Create `projects/<repo>.md` stub if missing (never overwrites curated profiles)
4. Regenerate `INDEX.md` and `tech-stack-rollup.md` when content changes
5. Write `github-sync-report.md` with new/updated README mirrors, new stubs, recent pushes, stack signals, and `needs-review` profiles

### Continuous career sync

Use `/continuous-career-sync` when you want an agent to act like a career sync partner:

1. Run the GitHub sync script.
2. Read `github-sync-report.md`.
3. Curate new or changed project profiles.
4. Draft CV, cover letter, portfolio, and job-strategy updates from curated facts.
5. Ask for owner confirmation before publishing public claims, metrics, employers, dates, or private-client context.

### Config (`.sync-config.json`)

| Key | Default | Meaning |
|-----|---------|---------|
| `github_user` | `devzurc` | Personal GitHub account to scan (public + private) |
| `github_orgs` | `[]` | Not used — org repos (e.g. tktechnologies) are out of scope |
| `exclude_repos` | `My-Profile`, `portfolio` | Skip profile/config repos |
| `include_private` | `true` | Include private `devzurc` repos when `gh` is authenticated as devzurc |
| `private_sync_mode` | `sanitized` | Redact URLs/tokens before writing README mirrors to this public repo |
| `include_forks` | `false` | Skip forks |

**Important:** `gh auth status` must show account **devzurc**. If logged in as another account (e.g. tktechnologies), only public `devzurc` repos sync (~10 of ~20).

---

## Privacy warning

**This portfolio repo is public on GitHub.** Anything committed under `docs/career/` is visible if pushed.

| Content | Safe in public portfolio repo? |
|---------|-------------------------------|
| Public repo READMEs | Yes |
| Redacted project profiles (no client secrets) | Usually yes |
| Private repo details, client names, internal metrics | **No** — use a private repo or keep `include_private: false` and redact profiles |

If you add private project knowledge, either:

1. Move `docs/career/` to a **private** repo and reference it from Cursor locally, or
2. Keep only **sanitized** profiles here (generic client, no secrets).

---

## Curating a project profile

1. Open `projects/<repo>.md`
2. Fill YAML frontmatter — especially `employer`, `period`, `stack`, `verified_outcomes`
3. Set `portfolio_worthy: true` or `cv_worthy: true` when ready for public surfaces
4. Write a recruiter-grade **one-liner** and **outcomes** (no invented metrics)

Template: `projects/_template.md`

---

## Using with Cursor / agents

```
@docs/career/INDEX.md
@docs/career/projects/dbt-snowflake-airflow.md
@.agents/skills/career-knowledge.md
```

Commands: `/sync-github-career`, `/continuous-career-sync`, `/curate-project <repo>`

---

## Current snapshot

Current snapshot: **devzurc-only** sync (public + private). Org repos are not pulled; private work is mapped through your `devzurc` mirrors and hand-curated `projects/*.md` profiles.

Current process snapshot: Notion sprint work and customer-facing TKTech delivery evidence is summarized in `tktech-sprint-knowledge.md`. Use it for role-fit and CV/portfolio suggestions only after checking public-safety notes.

### TK / Gen. AI projects (curated)

| Slug | GitHub mirror (`devzurc`) |
|------|---------------------------|
| `cdp-hub` | devzurc/cdp-hub |
| `muvstok-api` | devzurc/muvstok-api (also inside CDP monorepo) |
| `carparts-price-webscraper` | devzurc/carparts-price-webscraper |
| `marketing-socialmedia-app` | devzurc/marketing-socialmedia-app |
| `n8n-stripe-checkout` | devzurc/n8n-stripe-checkout |
| `n8n-instagram-assistant` | devzurc/n8n-instagram-assistant |
| `n8n-telegram-assistant` | devzurc/n8n-telegram-assistant |
| `n8n-clerk-followup` | devzurc/n8n-clerk-followup |
| `n8n-whatsapp-assistant` | no mirror — sanitized profile only |

Aliases documented in `.repo-manifest.json`.
