# Portfolio audit - 2026-06-15

## Scope checked

- Static site: `index.html`, `assets/css/*.css`, `assets/js/site.js`, `robots.txt`, `sitemap.xml`, local CV/certificate assets, and public GitHub Pages deployment.
- Resume surfaces: `docs/resume/markdown/`, `docs/resume/word/`, `docs/resume/pdf/`, `docs/resume/source/`, and served PDFs in `assets/files/cv/`.
- Career knowledge: `docs/career/INDEX.md`, project profiles, rollups, alignment plan, and sanitized README snapshots.
- Agent knowledge: `.agents/project-context.md`, `.agents/rules.md`, and command/playbook assumptions.
- External reachability sampled with `curl` for public portfolio, GitHub, CVs, certificate PDFs, and credential URLs.

## Changes made in this pass

- Fixed the public CDP Platform links from `github.com/devzurc/cdp-hub` to `github.com/tktechnologies/cdp-hub` in `index.html`.
- Updated CDP and `muvstok-api` career knowledge links to the reachable TK Technologies repository.
- Updated `sitemap.xml` `lastmod` to `2026-06-15`.
- Corrected `.agents/project-context.md` and `.agents/rules.md` so future agents follow the current external CSS/JS, Inter/IBM Plex Mono, and projects-before-skills structure.
- Clarified `docs/career/ALIGNMENT-PLAN.md` around the current Google Docs/source text drift.

## Alignment status

- Local site copy, local PDF downloads, DOCX exports, markdown CV sources, and the main career evidence layer are aligned around the current positioning: Senior Data Engineer + Gen. AI Automation Engineer, 5+ years, Curitiba, Europe relocation, visa sponsorship, C1 English, TK Technologies current contract through expected Aug 2026, 95K+ IoT devices, and 10+ automotive sources.
- `assets/files/cv/*.pdf` and `docs/resume/pdf/*.pdf` are byte-identical for EN and PT-BR.
- `docs/resume/word/*.docx` matches the updated markdown wording.
- Before this pass, the deployed GitHub Pages HTML matched local `index.html` byte-for-byte. After this pass, a commit/push is needed for the live site to receive the CDP link fix and sitemap date.

## Findings

1. **Fixed: flagship project links were broken.** `https://github.com/devzurc/cdp-hub` and `/tree/main/docs` returned 404. The reachable repository is `https://github.com/tktechnologies/cdp-hub`.
2. **Remaining: Google export/source snapshots are stale.** `docs/resume/source/LucasCruz_CV_PT.txt` still has older wording such as "Disponivel para trabalho presencial, hibrido ou remoto" instead of the current Europe relocation/visa line. Do not run `sync-from-google-docs.py` until Google Docs are updated, or it may overwrite aligned local outputs.
3. **Fixed: agent knowledge drift.** `.agents/project-context.md` still described embedded CSS, older fonts, older colors, and a skills-before-projects flow. It now matches the active static site.
4. **Historical audit drift:** `docs/portfolio-audit-2026-06-13.md` mentions an `AI Engineer Portfolio/` artifact and untracked assets. Current `git ls-files` and `git status --short` show the active assets are tracked and that artifact is not present in the repo.
5. **Machine-verification limits:** LinkedIn returned 999 and Medium returned 403/Cloudflare challenge to automated checks. Treat these as blocked-by-platform, not confirmed broken.

## Verification completed

- Live portfolio: HTTP 200.
- Live EN/PT CV PDFs: HTTP 200.
- Local EN/PT served CV PDFs match archived PDFs by SHA-256.
- Local certificate PDFs: HTTP 200 on GitHub Pages.
- `tktechnologies/cdp-hub` and `/tree/main/docs`: HTTP 200.
- GitHub profile: HTTP 200.
- Coursera, Udemy, Data Science Academy, and Alura certificate links sampled: reachable with HTTP 200, with Data Science Academy requiring GET rather than HEAD.
- Working tree was clean before the audit edits.
