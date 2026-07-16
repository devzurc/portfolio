# Project Context — Lucas Cruz Portfolio

> Reference document for AI agents. Facts below reflect the current repository state. Update this file when the portfolio structure or positioning changes.

---

## Overview

| Field | Value |
|-------|-------|
| **Owner** | Lucas Cruz |
| **Public URL** | https://devzurc.github.io/portfolio/ |
| **Primary file** | `index.html` (single-page portfolio) |
| **Stack** | Static HTML, modular CSS in `assets/css/`, vanilla JavaScript in `assets/js/site.js` |
| **Deployment** | GitHub Pages — push to `main` |
| **Audience** | Recruiters and hiring managers for Data Engineering, Gen. AI, and AI Platform roles (Europe/US English-first) |

---

## Professional Positioning

**Headline roles:** Senior Data Engineer · Gen. AI Automation Engineer · AI Platform Engineer (roadmap)

**Core narrative:** Building production data pipelines, lakehouses, and LLM/n8n automation across IoT, fintech, agribusiness, and automotive intelligence contexts. Extending into production AI platforms over enterprise data (RAG, agents, evaluation, MCP, observability).

**Niche statement:** I build production AI systems over real enterprise data: ingestion, retrieval, agents, tools, evaluation, observability, and deployment.

**Differentiators to preserve:**

- 5+ years experience (as stated on site — do not change without owner confirmation)
- Multi-cloud exposure (AWS, Azure, GCP, OCI)
- Production-scale IoT context (95K devices — verify before changing)
- Gen. AI stack: LLM integration, RAG, AI agents, prompt engineering, n8n
- Data stack: Python, Spark/PySpark, SQL, dbt, Airflow, Snowflake, Databricks, Delta Lake
- Open to **relocation across Europe**; requires **visa sponsorship**
- Advanced English (C1 / IELTS)

---

## Site Architecture

### Sections (in scroll order)

| ID | Purpose |
|----|---------|
| `#hero` | Name, roles, value prop, CTAs, headline stats |
| `#projects` | Selected work list items with rolling text and cursor follow preview |
| `#experience` | Employment timeline cards with impact bullets |
| `#skills` | Service discipline cards (Data, Gen. AI, Cloud, Governance) |
| `#certifications` | Google AI badges and verified certifications list |
| `#job-fit` | Role-fit guidance cards |
| `#contact` | Contact actions, location, CV download, relocation |

### Navigation

Fixed top nav + full-screen mobile menu overlay. Nav labels use `data-en` / `data-pt` for dynamic translation on language switch.

---

## Internationalization (i18n)

**Mechanism:** CSS class toggling on `<body>` (`lang-pt`) plus `.en-only` / `.pt-only` duplicate blocks.

**Language toggle:** `setLang('en' | 'pt')` - persists preference in `localStorage` key `lc-lang`, updates `<html lang>`, and updates `aria-pressed` on language buttons.

**Rules for editors:**

- Add paired EN + PT blocks for every new string
- Nav items: use `data-en` and `data-pt` attributes
- Update `document.title` strings inside `setLang()` when hero positioning changes
- Keep `<html lang>` updates in sync with language toggles

---

## Design System

### Typography

- **Body:** Inter (Weights: 400, 500, 600)
- **Headings:** Instrument Serif (Weights: 400)
- **Mono / labels / UI controls:** JetBrains Mono (Weights: 400, 500)

### Colors (CSS variables)

```css
--bg-primary: #0A0A0B;   /* Page background (near-black) */
--bg-elevated: #111113;  /* Elevated surfaces */
--bg-card: #161618;      /* Card backgrounds */
--accent: #00E5FF;       /* Electric cyan primary accent */
--accent-amber: #FFB800; /* Warm amber highlights / stats */
```

### Patterns

- **Minimalist Dark Canvas:** Jet-black backdrop (`#0A0A0B`) featuring a repeating vector grid line layer and localized glowing spotlights.
- **Accents:** Electric cyan is used for key links, active page tags, buttons, and hover boundaries. Warm amber marks verified metrics and certification IDs.
- **Cursor Follow Preview:** Hovering on work items shows floating thumbnail boxes tracking client pointer movement.
- **Components:** `.work-link` lists, `.job` timeline cards, `.skill-card` service grid, `.badge-card`.

---

## Assets & Links

### CV — source of truth & file locations

**Canonical editable sources (Google Docs — public export):**

| Language | Google Doc | Doc ID |
|----------|------------|--------|
| **English (EN)** | [Open Doc](https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit) | `1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8` |
| **Portuguese (PT-BR)** | [Open Doc](https://docs.google.com/document/d/1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q/edit) | `1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q` |

**Repo CV workspace (`docs/resume/`):**

| Format | Path | Purpose |
|--------|------|---------|
| **Markdown** | `markdown/LucasCruz_CV_EN.md`, `markdown/LucasCruz_CV_PT.md` | Agent-editable, git-diff friendly in-repo source |
| **Word** | `word/LucasCruz_CV_EN.docx`, `word/LucasCruz_CV_PT.docx` | Direct export from Google Docs (recruiter/ATS) |
| **PDF** | `pdf/LucasCruz_CV_EN.pdf`, `pdf/LucasCruz_CV_PT.pdf` | Repo snapshot / archive |
| **Plain text** | `source/LucasCruz_CV_EN.txt`, `source/LucasCruz_CV_PT.txt` | Raw Google export for diffing |
| **Google update note** | `google-docs-update-2026-06-17.md` | Paste-ready changes needed before next Google Docs pull |
| **Cover letter** | `markdown/LucasCruz_Cover_Letter_Europe_EN.md` | Europe-focused cover letter draft aligned from CV/career knowledge |

**Sync command (pulls latest from Google Docs):**

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

This updates `word/`, `source/`, `pdf/`, and copies PDFs to `assets/files/cv/` for the live site.

**Site download links (`index.html`):**

| Language | Path served to visitors |
|----------|-------------------------|
| EN | `assets/files/cv/LucasCruz_CV_EN.pdf` |
| PT-BR | `assets/files/cv/LucasCruz_CV_PT.pdf` |

**Recommended workflow:**

1. Edit Google Docs (EN + PT)
2. Run `sync-from-google-docs.py`
3. Update `markdown/*.md` if agents edited copy in-repo (or paste Google changes into markdown)
4. Run `/sync-cv-portfolio` to align `index.html` with CV facts

**Current audit note (2026-06-17):** Local markdown, Word, PDF, and site CV downloads are aligned. Product/client names are excluded from the public portfolio; employer TK Technologies remains where verified. Run `sync-from-google-docs.py` after Google Docs are updated to match local markdown.

**CV management skill:** `@.agents/skills/cv-management.md`

### CV document structure (EN)

Sections in order — keep EN and PT structurally aligned:

1. Header — name, titles, contact, location/relocation
2. Professional Summary
3. Technical Skills (grouped categories)
4. Work Experience (reverse chronological)
5. Notable Projects
6. Education

Use the CV as the **factual authority** for employers, dates, metrics, projects, and skills when syncing portfolio copy.

### Career knowledge (GitHub projects)

| Resource | Path |
|----------|------|
| Index | `docs/career/INDEX.md` |
| Curated profiles | `docs/career/projects/*.md` |
| Raw READMEs | `docs/career/readmes/*.md` |
| Alignment roadmap | `docs/career/ALIGNMENT-PLAN.md` |
| Job search strategy | `docs/career/JOB-SEARCH-STRATEGY.md` |
| TKTech sprint knowledge | `docs/career/tktech-sprint-knowledge.md` |
| AI roadmap & goals | `docs/career/goals/` (see `AGENTS.md`) |
| GitHub sync report | `docs/career/github-sync-report.md` |
| Sync script | `python3 docs/career/scripts/sync-github-projects.py` |

Skill: `@.agents/skills/career-knowledge.md`
Continuous sync skill: `@.agents/skills/continuous-career-sync.md`

Current sprint/process note: Lucas is working through Notion sprints at TKTech. Public-safe career knowledge lives in `docs/career/tktech-sprint-knowledge.md`; use it for customer-facing delivery, sprint ownership, mobile launch readiness, and role-fit mapping without exposing raw ticket names or private identifiers.

### Verified external profiles

| Platform | URL |
|----------|-----|
| Portfolio | https://devzurc.github.io/portfolio/ |
| LinkedIn | https://www.linkedin.com/in/lucas-cruz |
| GitHub | https://github.com/devzurc |
| Credly | https://www.credly.com/users/devzurc |
| Medium | https://medium.com/@dev.lucascruz |
| Email | dev.lucascruz@gmail.com |

Only link to repos, demos, or articles that exist. GitHub username: **devzurc**.
Flagship TK Technologies CDP links use the organization repository: `https://github.com/tktechnologies/cdp-hub`.

---

## Certifications (on-site)

Certs section groups credentials with **real verification URLs** or local certificate PDFs. Current groups include IELTS, Udemy, Coursera, Data Science Academy, Alura, the Dom Bosco education certificate, and the Google AI series (4 certificates: AI for Writing and Communicating, AI for Research and Insights, AI for Brainstorming and Planning, AI Fundamentals). When adding a cert:

1. Owner must provide certificate URL
2. Match existing HTML list structure
3. Add EN + PT group titles if creating a new category

---

## SEO Metadata (current)

- **Title (EN):** Lucas Cruz - Senior Data Engineer & Gen. AI Automation Engineer
- **Title (PT):** Lucas Cruz - Engenheiro de Dados Senior & Automacao com IA Generativa
- **Meta description:** References production data pipelines, cloud lakehouses, Gen. AI/n8n automation, and Europe relocation
- **Canonical:** `https://devzurc.github.io/portfolio/`
- **Open Graph:** `og:title`, `og:description`, `og:type=website`, `og:url`, `og:image`
- **Twitter:** summary large image metadata
- **Crawl files:** `robots.txt`, `sitemap.xml`

---

## JavaScript Features

| Feature | Function |
|---------|----------|
| Full-screen mobile menu | `toggleMenu()`, `closeMenu()` overlay |
| Language toggle | `setLang(lang)` updates elements and attributes |
| Cursor follow preview | Floating project preview moves with client mouse movements |
| Scroll animations | IntersectionObserver on reveals (`.fade-in`, `.job`, `.work-item`) |
| Active nav | Scroll listener highlights current section |

---

## What This Repo Is Not

- Not a React/Next/Vite app
- No CI/CD config in repo (GitHub Pages only)
- No backend or form submission — contact is `mailto:` and external links
- No test suite — manual browser verification expected

---

## Agent Workspace (`.agents/`)

| Path | Purpose |
|------|---------|
| `rules.md` | Binding rules for all agents |
| `project-context.md` | This file — repo facts and structure |
| `commands.md` | Slash-style reusable commands |
| `skills/*.md` | Task-specific playbooks |
| `skills/cv-management.md` | CV edit, add, remove, export, portfolio sync |
| `skills/career-knowledge.md` | GitHub project sync, curated career profiles |
| `skills/continuous-career-sync.md` | Watch GitHub signals and draft safe propagation into CV, cover letter, portfolio, and strategy |
| `prompts/*.md` | Copy-paste prompt templates |
| `prompts/update-cv.md` | CV change requests (add/edit/remove) |
| `prompts/continuous-career-sync.md` | Full GitHub-to-career sync pass |

Suggested Cursor setup: add `@.agents/rules.md` or symlink rules into `.cursor/rules/` if using Cursor Project Rules.

---

## Maintenance Checklist (periodic)

- [ ] Run `python3 docs/resume/scripts/sync-from-google-docs.py` after Google Doc edits
- [ ] `markdown/*.md` reflects latest approved CV content before regenerating DOCX/PDF
- [ ] `source/*.txt` reflects a fresh Google Docs export before treating it as source evidence
- [ ] Portfolio `#experience`, `#projects`, `#skills`, hero stats align with CV facts
- [ ] Cert links still resolve
- [ ] GitHub project links are public and representative
- [ ] `docs/career/github-sync-report.md` reviewed for new repos, README changes, new tech signals, and `needs-review` profiles
- [ ] EN/PT copy stays in sync
- [ ] Meta description reflects current job search focus
- [ ] Copyright year in footer is current
