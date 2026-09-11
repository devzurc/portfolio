# Alignment plan - CV · Portfolio · Career knowledge

> **Status (2026-09-11):** Local markdown, Word, source txt, site PDFs, and unpublished `index.html` are aligned on Florianópolis, TK **Feb 2026 – Present**, OrbitAI, and Car Parts Price Searcher. Canonical Google Docs are still stale (Curitiba / Europe / May 2026). Paste `docs/resume/google-docs-update-2026-09-10.md` before running `sync-from-google-docs.py`. Do not commit or push until the owner asks.

This plan connects three surfaces:

| Surface | Location | Audience |
|---------|----------|----------|
| **Career knowledge** | `docs/career/` | You + AI (full detail) |
| **CV** | Google Docs + `docs/resume/` | Recruiters, ATS |
| **Portfolio** | `index.html` | Recruiters, quick scan |
| **Job search strategy** | `docs/career/JOB-SEARCH-STRATEGY.md` | Role targeting, filters, interview prep |
| **Sprint/process knowledge** | `docs/career/tktech-sprint-knowledge.md` | Public-safe current delivery context |
| **AI roadmap & goals** | `docs/career/goals/` | Senior AI Platform Specialist roadmap and progress tracking |

**Rule:** Public copy (CV + portfolio) only uses facts backed by `docs/career/projects/*.md` with `verified_outcomes` or CV text.

**CV source of truth (2026-09-11):** `docs/resume/markdown/*.md` is canonical until Google Docs match the 2026-09-10 paste pack. Local PDFs were rebuilt from markdown because a Google export would still pull Curitiba/Europe copy. After Google Docs are updated, run `python3 docs/resume/scripts/sync-from-google-docs.py` and re-check header, TK dates, and project names.

Locked facts:

- Home city: Florianópolis, Santa Catarina. Employer cities may stay Curitiba.
- Visa sponsorship required. No Europe relocation line.
- TK Technologies: Feb 2026 – Present (no expected end date).
- Public flagship names: OrbitAI; Car Parts Price Searcher.

See `docs/career/alignment-note-2026-09-11.md` for the fact matrix and LinkedIn checklist.

---

## Phase 0 — Inventory (done / in progress)

- [x] CV markdown restored to compact draft (`docs/resume/markdown/`)
- [x] GitHub READMEs + project stubs (`docs/career/`) — last sync 2026-09-11
- [x] Park private `needs-review` hubs (`crm-hub`, `sabia-hub`, `invest-hub`, `my-finance`) as `private-evidence`
- [x] Curate `franq-data-lakehouse-challenge` as public **learning** (not CV/portfolio)
- [x] Flag `portfolio_worthy` and `cv_worthy` per project
- [x] Resolve EN/PT CV inconsistencies in markdown
- [ ] Owner paste into Google Docs, then Google export sync

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
| `cdp-hub` | CV: Car Parts Price Searcher (TK Technologies) |
| `whatsapp-crm-platform` (`ORBITAI-CRM`) | CV/site: OrbitAI |
| `muvstok-api` | Component of CDP — cite under platform work, not separate card |
| `n8n-telegram-assistant` | CV: conversational AI chatbot bullet (TK Technologies) |
| `n8n-stripe-checkout` | Stok IA checkout automation — portfolio optional |
| `n8n-instagram-assistant` | TK social automation — portfolio optional |
| `n8n-clerk-followup` | Stok IA trial lifecycle — internal; CV one-liner only |
| `franq-data-lakehouse-challenge` | Public learning lakehouse; keep off CV until owner promotes |
| `dbt-snowflake-airflow` | Learning/lab profile only |
| `stock-market-lakehouse` | Learning/lab profile only |
| `project_dashboard_heroby` | wDiscover / IoT-adjacent client work |
| `sabia-hub`, `crm-hub`, `invest-hub`, `my-finance` | Parked private-evidence |
| Others | Training or client ops — curate honestly |

See `.repo-manifest.json` for GitHub name aliases (e.g. `n8n-instagram-assistant` canonical mirror under `devzurc`).

---

## Phase 2 — CV alignment

Use `@.agents/skills/cv-management/SKILL.md` + `@docs/career/projects/`.

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
| `#job-fit` | `JOB-SEARCH-STRATEGY.md` + owner-confirmed sprint/customer-facing evidence |

Show public project links only where a public URL and publication permission exist. Approved private work may appear as sanitized evidence when `portfolio_worthy: true`; never substitute a generic GitHub link or expose repository details.

---

## Phase 4 — Ongoing maintenance

| Trigger | Action |
|---------|--------|
| New GitHub repo | `sync-github-projects.py` → curate profile |
| GitHub README or stack changed | `/continuous-career-sync` → inspect `github-sync-report.md` → update curated profile before public copy |
| CV edit in Google Doc | `sync-from-google-docs.py` → `/sync-cv-portfolio` |
| New job / contract | Update CV first → career profile → portfolio |
| New Notion sprint/task batch | Update `tktech-sprint-knowledge.md` → map to `JOB-SEARCH-STRATEGY.md` → propose CV/portfolio wording |
| New target role type | Update `JOB-SEARCH-STRATEGY.md` → audit hero/job-fit/CV summary |

---

## Remaining manual follow-up

1. ~~Review the EN/PT markdown CV changes.~~ Done 2026-06-17.
2. **Open:** Apply `docs/resume/google-docs-update-2026-09-10.md` in both Google Docs, then `python3 docs/resume/scripts/sync-from-google-docs.py`.
3. Re-run `/sync-cv-portfolio audit` after Google export if wording diverges from markdown.
4. Un-park private-evidence profiles only after owner curation (`sabia-hub`, `crm-hub`, `invest-hub`, `my-finance`).
5. Run `/continuous-career-sync` when GitHub activity or learning signals change.
6. Run `/pre-commit-review` before committing. **Do not commit or push until the owner asks.**
7. Manual LinkedIn check (location Florianópolis, no Europe relocation, TK Present, OrbitAI).

---

## Open questions for you

1. ~~Which client names are OK on the public portfolio vs anonymized?~~ No product/client names on portfolio except approved OrbitAI; employer TK Technologies OK.
2. ~~Are the `10+` automotive sites and TK hybrid/6-month contract wording approved?~~ Confirmed 2026-06-17; expected-Aug end date removed 2026-09-11 (contract is Present).
3. Should `franq-data-lakehouse-challenge` be promoted to CV/portfolio, or stay learning-only?
4. Should any other learning/lab profiles be expanded with verified evidence before returning to the CV/site?
