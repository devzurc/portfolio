# Career knowledge base

Private-to-you working area for AI agents to understand **what you built**, **with which stack**, and **in what context** — before anything goes on the portfolio or CV.

## Recommended approach (hybrid)

| Layer | Folder | Purpose |
|-------|--------|---------|
| **Raw mirror** | `readmes/` | Auto-synced README from GitHub — evidence, not marketing copy |
| **Curated truth** | `projects/` | One profile per repo — problem, your role, stack, verified outcomes |
| **Rollups** | `INDEX.md`, `tech-stack-rollup.md` | Generated indexes for agents and alignment work |
| **Next phase** | `ALIGNMENT-PLAN.md` | Checklist to sync CV ↔ portfolio ↔ projects |

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
4. Regenerate `INDEX.md` and `tech-stack-rollup.md`

### Config (`.sync-config.json`)

| Key | Default | Meaning |
|-----|---------|---------|
| `github_user` | `devzurc` | Account to scan |
| `exclude_repos` | `My-Profile` | Skip profile/config repos |
| `include_private` | `false` | Do not pull private repos into this public portfolio workspace |
| `include_forks` | `false` | Skip forks |

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

Commands: `/sync-github-career`, `/curate-project <repo>`

---

## Current snapshot

Current public-safe snapshot: **14 curated project profiles** indexed. Private sync is disabled, and private/client work is represented only through sanitized summaries with no live internal identifiers.

### TK / Gen. AI projects (curated)

| Slug | Canonical GitHub |
|------|------------------|
| `cdp-hub` | tktechnologies/cdp-hub |
| `muvstok-api` | cdp-hub monorepo / `muvstok-api/` |
| `n8n-stripe-checkout` | tktechnologies/n8n-stripe |
| `n8n-instagram-assistant` | devzurc/instagram-n8n |
| `n8n-telegram-assistant` | devzurc/nox-telegram-chatbot |
| `n8n-clerk-followup` | devzurc/clerk-trial-followup |

Aliases documented in `.repo-manifest.json`.
