# Portfolio audit - 2026-06-17

## Scope checked

- Project-owned files excluding Git internals, ignored virtualenv packages, and ignored `__pycache__` output: 92 files.
- Static site: `index.html`, `assets/css/*.css`, `assets/js/site.js`, local image/CV/certificate assets, `robots.txt`, and `sitemap.xml`.
- Career knowledge: `docs/career/`, curated project profiles, README mirrors, alignment plan, and sync script.
- Resume surfaces: markdown CVs, source exports, PDFs, DOCX files, and served CV PDFs.
- Agent workspace: `.agents/` rules, prompts, skills, and project context.

## Changes made in this pass

- Wired the existing `#job-fit` / Roles section into CSS and JavaScript.
- Added responsive styling for role-fit cards and included the section in scroll offset and active navigation.
- Updated `sitemap.xml` `lastmod` to `2026-06-17`.
- Added `docs/career/tktech-sprint-knowledge.md` for public-safe Notion sprint/task mapping.
- Added `docs/career/JOB-SEARCH-STRATEGY.md` for target roles, filters, interview stories, and next portfolio improvements.
- Added `.agents/prompts/start-audit-sync.md` and registered `/start-audit-sync` in `.agents/commands.md`.
- Updated agent rules/context/skills so future sessions know about `#job-fit`, job-search strategy, and sprint knowledge.
- After owner approval, promoted customer-facing TKTech delivery and mobile launch readiness into `index.html`, local CV markdown, Word exports, PDF archives, and served CV downloads.

## Verification completed

- Local HTML anchor and asset references resolve.
- CSS `url(...)` assets resolve.
- EN/PT marker counts match in `index.html`.
- Python scripts compile with `python3 -m py_compile`.
- Word CVs regenerated from markdown with `docs/resume/scripts/build-word.py`.
- PDF CVs regenerated from markdown with `docs/resume/scripts/build-basic-pdf.py`.
- Served CV PDFs match archived CV PDFs by SHA-256.
- Served education certificate PDFs match archived certificate PDFs by SHA-256.
- Ignored `.venv` and `__pycache__` files are not tracked.

## Findings

1. **Fixed: Roles section was only partially implemented.** The HTML existed, but CSS styling, responsive grid support, scroll margin, pointer highlight support, and active nav inclusion were missing.
2. **Still true: Google Docs/source exports are stale.** Do not run `docs/resume/scripts/sync-from-google-docs.py` until the canonical Google Docs are updated, or current local CV/PDF wording may regress.
3. **Historical audit docs are snapshots.** Older notes mention risks that were later resolved; keep them as history, but use the newest audit when deciding current work.
4. **Public-safety risk remains managed.** New sprint/task knowledge is intentionally sanitized and should not expose raw Notion tickets, private customer names, workflow IDs, webhook URLs, secrets, or app-store account details.

## Recommended next tasks

1. Add measured outcomes for current automations if available: demos delivered, customers trained, manual hours reduced, response-time changes, or workflows moved to production.
2. Confirm which TKTech product/client names can be public.
3. Consider a sanitized CDP case study and an AI automation suite case study for deeper technical review by hiring managers.
4. Update Google Docs CVs to match the current local markdown/PDF wording, then run the Google sync script.
