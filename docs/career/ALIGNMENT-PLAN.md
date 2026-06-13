# Alignment plan - CV · Portfolio · Career knowledge

> **Status:** Implemented in repo on 2026-06-12. Google Docs/PDF CV exports still need a source-of-truth sync after owner review.

This plan connects three surfaces:

| Surface | Location | Audience |
|---------|----------|----------|
| **Career knowledge** | `docs/career/` | You + AI (full detail) |
| **CV** | Google Docs + `docs/resume/` | Recruiters, ATS |
| **Portfolio** | `index.html` | Recruiters, quick scan |

**Rule:** Public copy (CV + portfolio) only uses facts backed by `docs/career/projects/*.md` with `verified_outcomes` or CV text.

---

## Phase 0 — Inventory (done / in progress)

- [x] CV synced from Google Docs (`docs/resume/`)
- [x] GitHub READMEs + project stubs (`docs/career/`)
- [x] Curate every `projects/*.md` with `status: needs-review` into active, client-work, learning, archived, or engagement-complete
- [x] Flag `portfolio_worthy` and `cv_worthy` per project
- [x] Resolve EN/PT CV inconsistencies in markdown (8+ vs 10+ sites, security/governance parity, TK work mode)

---

## Phase 1 — Curate career knowledge

For each repo in `INDEX.md`:

1. Read `readmes/<repo>.md`
2. Complete `projects/<repo>.md`:
   - Employer / client context (or Personal)
   - Date range aligned with CV experience
   - Stack (verified only)
   - Outcomes (metrics only if documented)
3. Mark noise repos `status: archived` or `learning` (exclude from portfolio)

**Priority repos** (match CV / target roles):

| Repo | CV / portfolio link today |
|------|---------------------------|
| `cdp-hub` | CV: Automotive Market Price Intelligence Platform (TK Technologies) |
| `muvstok-api` | Component of CDP — cite under platform work, not separate card |
| `n8n-telegram-assistant` | CV: conversational AI chatbot bullet (TK Technologies) |
| `n8n-stripe-checkout` | Stok IA checkout automation — portfolio optional |
| `n8n-instagram-assistant` | TK social automation — portfolio optional |
| `n8n-clerk-followup` | Stok IA trial lifecycle — internal; CV one-liner only |
| `dbt-snowflake-airflow` | Learning/lab profile only; demoted from CV/site until verified |
| `stock-market-lakehouse` | Learning/lab profile only; README evidence is missing |
| `project_dashboard_heroby` | wDiscover / IoT-adjacent client work |
| `project_etl_emissaoCO2` | Medallion / ETL practice |
| Others | Training or client ops — curate honestly |

See `.repo-manifest.json` for GitHub name aliases (e.g. `instagram-n8n` → `n8n-instagram-assistant`).

---

## Phase 2 — CV alignment

Use `@.agents/skills/cv-management.md` + `@docs/career/projects/`.

| Check | Action |
|-------|--------|
| Notable Projects on CV | Each row must have `cv_worthy: true` profile |
| Experience bullets | Supported by at least one project or employer note |
| Skills section | Union of stacks from curated profiles (no orphan keywords) |
| EN ↔ PT | Same roles, dates, metrics; translate meaning not inflate |

Command: `/sync-cv-portfolio audit`

---

## Phase 3 — Portfolio alignment

Map CV + career profiles → `index.html` sections:

| Portfolio section | Source |
|-------------------|--------|
| `#hero` | CV summary + top 3 differentiators |
| `#skills` | `tech-stack-rollup.md` + CV skills (deduped) |
| `#experience` | CV work experience (shortened for web) |
| `#projects` | `portfolio_worthy: true` profiles only (max 4–6 cards) |

Command: `/improve-section` per section after audit.

**Do not** add project cards without GitHub link or `portfolio_worthy: true`.

---

## Phase 4 — Ongoing maintenance

| Trigger | Action |
|---------|--------|
| New GitHub repo | `sync-github-projects.py` → curate profile |
| CV edit in Google Doc | `sync-from-google-docs.py` → `/sync-cv-portfolio` |
| New job / contract | Update CV first → career profile → portfolio |

---

## Remaining manual follow-up

1. Review the EN/PT markdown CV changes.
2. Apply approved copy to the canonical Google Docs.
3. Run `python3 docs/resume/scripts/sync-from-google-docs.py` to refresh Word/PDF/source snapshots and live CV PDFs.
4. Run `/pre-commit-review` before committing.

---

## Open questions for you

1. Which client names are OK **on the public portfolio** vs anonymized?
2. Are the `10+` automotive sites and TK hybrid/6-month contract wording, expected through Aug 2026, approved for final Google Docs?
3. Should any learning/lab profiles be expanded with verified evidence before returning to the CV/site?
