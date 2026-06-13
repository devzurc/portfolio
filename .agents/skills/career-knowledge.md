# Skill: Career Knowledge

Use when curating GitHub projects, syncing career data, or preparing portfolio/CV alignment from real work evidence.

---

## Purpose

`docs/career/` is the **evidence layer** between raw GitHub repos and public surfaces (CV, portfolio).

| Layer | Trust level | Use |
|-------|-------------|-----|
| `readmes/*.md` | Raw snapshot | What the repo claims |
| `projects/*.md` | Curated by owner | What you actually did — AI and alignment source |
| CV / portfolio | Public | Subset of curated truth |

**Never invent** employers, metrics, or stack on public surfaces without a backing `projects/*.md` or CV entry.

---

## Folder map

```
docs/career/
├── INDEX.md              # Repo manifest (generated)
├── tech-stack-rollup.md  # Stack frequency (generated)
├── readmes/<repo>.md     # GitHub README mirror
├── projects/<repo>.md    # Curated profile (edit these)
├── ALIGNMENT-PLAN.md     # CV ↔ portfolio roadmap
└── scripts/sync-github-projects.py
```

---

## Sync workflow

```bash
python3 docs/career/scripts/sync-github-projects.py
```

Behavior:

- Pulls READMEs into `readmes/`
- Creates `projects/<repo>.md` stub only if missing (**never overwrites** curated profiles)
- Regenerates `INDEX.md` and `tech-stack-rollup.md`
- Respects `.sync-config.json` (excludes, private repos)

After sync: review new stubs with `status: needs-review`.

---

## Curating a project profile

Open `projects/<repo>.md` and complete:

| Field | Required for alignment |
|-------|------------------------|
| `employer` | Links repo to CV experience |
| `period` | Aligns timeline |
| `role` | Your contribution |
| `stack` | Verified technologies |
| `verified_outcomes` | Metrics allowed on CV/portfolio |
| `portfolio_worthy` | Show on `index.html`? |
| `cv_worthy` | CV Notable Projects? |
| `status` | `active` \| `archived` \| `learning` \| `client-work` |

Template: `projects/_template.md`

### Status guidance

| Status | Meaning |
|--------|---------|
| `active` | Representative work; may surface publicly |
| `client-work` | Real delivery; check if client name is publishable |
| `learning` | Tutorial/training — mention skills, not as flagship project |
| `archived` | Old/duplicate — exclude from portfolio |
| `needs-review` | Auto stub — owner must curate |

---

## Mapping to CV & portfolio

| CV section | Career source |
|------------|---------------|
| Work Experience | `employer` + bullets from profiles on that employer |
| Notable Projects | `cv_worthy: true` profiles |
| Skills | Union of `stack` from active profiles + CV |
| Portfolio `#projects` | `portfolio_worthy: true` (max 4–6) |

Cross-check: `@docs/career/ALIGNMENT-PLAN.md`

---

## Privacy & public repo warning

Portfolio repo is **public**. Do not commit:

- Private repo READMEs with secrets (if `include_private: true`)
- Client names under NDA without owner approval
- Credentials, internal URLs, `.env` values

If adding sensitive private work, redact in `projects/*.md` or use a separate private knowledge repo.

---

## Agent commands

| Command | Action |
|---------|--------|
| `/sync-github-career` | Run sync script + summarize new/changed readmes |
| `/curate-project <repo>` | Interview owner, fill `projects/<repo>.md` |
| `/sync-cv-portfolio audit` | Compare CV, career profiles, index.html |

---

## Deliverable format (curate task)

```markdown
## Repo: <name>

## Proposed frontmatter updates
...

## One-liner (EN)
...

## Suggested CV bullet (if cv_worthy)
...

## Suggested portfolio card (if portfolio_worthy)
...

## Owner must confirm
- [ ] ...
```

Wait for approval before editing CV or `index.html`.
