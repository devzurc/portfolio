# Portfolio Agent Rules

These rules apply to **every AI agent** working in this repository. Read `.agents/project-context.md` before making changes.

---

## Mission

Help maintain and improve Lucas Cruz's personal portfolio for **Data Engineering** and **Gen. AI Engineering** hiring audiences. Every change should increase clarity, credibility, and recruiter scan-ability — not visual noise.

---

## Non-Negotiables

### 1. Never fabricate credentials

Do **not** invent or embellish:

- Job titles, employers, dates, or responsibilities
- Project outcomes, metrics, or scale claims
- Certifications, badges, or credential URLs
- GitHub repos, demos, papers, or blog posts
- Skills the owner has not demonstrated elsewhere in the repo or CV

When information is missing, **ask the user** or leave a clearly marked placeholder (`<!-- TODO: confirm metric with owner -->`). Prefer under-stating over over-claiming.

**CV authority:** Google Docs (see `.agents/project-context.md`) and exported PDFs in `docs/resume/pdf/` are the canonical record for employment, dates, metrics, and projects. Portfolio copy must not contradict the CV. For CV edits, use `@.agents/skills/cv-management.md` — never change the CV in isolation without considering portfolio sync.

### 2. Preserve bilingual content (EN / PT-BR)

The site uses a dual-language pattern:

- `.en-only` and `.pt-only` blocks for section copy
- `data-en` / `data-pt` on nav links
- `setLang('en' | 'pt')` toggles visibility and updates `document.title`

**Every user-facing text change must exist in both languages** unless the user explicitly requests a single-language edit. Keep tone and meaning aligned; do not translate literally if it hurts readability — adapt for PT-BR professional norms.

### 3. Scope discipline

- **Default scope:** `index.html`, files under `assets/`, and CV workflow files under `docs/resume/` when doing CV work
- Do not refactor unrelated sections when fixing one issue
- Do not introduce frameworks, build tools, or npm unless the user explicitly requests a stack change
- Do not modify `.agents/` unless the user asks to update agent workspace docs

### 4. Static-site constraints

This is a **GitHub Pages static site**:

- No server-side rendering, databases, or API keys in the repo
- Keep all CSS/JS compatible with modern browsers without a bundler
- Keep styles in `assets/css/` and behavior in `assets/js/site.js` unless a tiny local exception is clearly justified
- External links open in new tabs where appropriate (`target="_blank"` + `rel="noopener noreferrer"` when adding new external links)

---

## Positioning Guidelines

Lead with **production-ready systems**, not buzzwords.

| Emphasize | De-emphasize |
|-----------|--------------|
| Data pipelines, lakehouses, orchestration | Generic "AI enthusiast" language |
| LLM workflows, RAG, agents, automation (n8n) | Vague "passion for technology" |
| Cloud platforms (AWS, Azure, GCP, OCI) | Tool lists without context |
| Measurable outcomes **only when verified** | Inflated or rounded-up numbers |
| Open to Europe relocation + visa sponsorship | Ambiguous location signals |

Target roles: **Data Engineer**, **Gen. AI Engineer**, **ML/Data platform adjacent roles** with automation focus.

---

## Code & Markup Standards

### HTML semantics

- Use `<section>`, `<nav>`, `<footer>`, headings in logical order (`h1` → `h2` → `h3`)
- Every interactive control needs an accessible name (`aria-label` or visible text)
- Images require meaningful `alt` text; decorative images use `alt=""`
- Anchor links must match existing section IDs: `#hero`, `#projects`, `#skills`, `#experience`, `#job-fit`, `#certifications`, `#contact`

### CSS

- Extend existing CSS variables in `:root` — do not hard-code one-off colors
- Preserve responsive breakpoints and mobile nav behavior
- Test mentally at ~375px, ~768px, and ~1280px widths
- Avoid layout shifts when toggling EN/PT (both blocks occupy the DOM; visibility is toggled)

### JavaScript

- Keep the existing deferred `assets/js/site.js` loading pattern unless there is a strong reason to change it
- Do not break `setLang`, mobile menu, scroll spy, or IntersectionObserver fade-ins
- Prefer progressive enhancement; site must remain readable if JS fails

---

## UX & Recruiter Readability

Recruiters scan in **~10–30 seconds**. Optimize for:

1. **Hero:** role clarity + one strong value proposition
2. **Experience:** company, title, dates, 3–5 impact bullets with tech keywords
3. **Projects:** problem → approach → stack → outcome (with real links)
4. **Skills:** grouped by domain, not an alphabet soup
5. **Contact:** low friction — email, LinkedIn, CV download

Avoid walls of text. Prefer scannable bullets, consistent date formats, and visible tech tags.

---

## SEO & Social

- Keep `<title>` and `<meta name="description">` aligned with hero positioning
- Update Open Graph tags when headline/value prop changes
- Use natural keywords: *Data Engineer*, *Gen. AI*, *LLM*, *RAG*, *Airflow*, *Databricks*, *Snowflake*, etc.
- Do not keyword-stuff

---

## Git & Commits

- **Never commit** unless the user explicitly asks
- Before suggesting a commit, run through `.agents/prompts/review-before-commit.md`
- Do not commit secrets, `.env` files, or draft copy with unverified claims
- Keep commit messages focused on *why* the portfolio change helps hiring narrative

---

## Workflow in Cursor

1. Read `.agents/project-context.md` for repo facts
2. Use a skill from `.agents/skills/` when the task matches (frontend, SEO, copy, review)
3. Use a command from `.agents/commands.md` or prompt from `.agents/prompts/` for structured tasks
4. Show a concise summary of changes and flag anything that needs owner verification
5. If changing copy with metrics or employer details, **list what must be confirmed** before merge

---

## Escalation

Stop and ask the user when:

- Adding a new project without repo/demo links
- Changing employment dates, titles, or employers
- Adding certifications or stats not present in current content
- Restructuring the entire page or migrating off static HTML
- Copy changes that could affect visa/relocation messaging
