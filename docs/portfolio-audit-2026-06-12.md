# Portfolio audit - 2026-06-12

## Scope checked

- Static site architecture: `index.html`, `robots.txt`, `sitemap.xml`, and assets under `assets/`.
- CV surface: live downloadable PDFs in `assets/files/cv/` and source snapshots in `docs/resume/`.
- Career evidence layer: `docs/career/INDEX.md`, `docs/career/ALIGNMENT-PLAN.md`, `docs/career/tech-stack-rollup.md`, and curated project profiles.
- Bilingual behavior: EN/PT content pattern, language toggle, nav labels, CV links, and section anchors.

## Alignment status

- The site remains a zero-build GitHub Pages portfolio using static HTML, embedded CSS, and vanilla JavaScript.
- Hero claims are still backed by the CV and career evidence layer: 5+ years, 95K+ IoT devices, 10+ automotive sources, C1 English, Europe relocation, and visa sponsorship.
- Project cards now prioritize entries marked `portfolio_worthy: true` in `docs/career/INDEX.md`.
- Private client work is represented as sanitized public copy with no private repository links, workflow IDs, credentials, endpoints, or internal identifiers.
- CV download paths resolve to existing files under `assets/files/cv/`.
- `robots.txt` and `sitemap.xml` are present and point to the GitHub Pages URL.

## Changes made during audit

- Replaced the old neon terminal-style page with a cleaner recruiter-facing design.
- Added a project-bound bitmap hero visual at `assets/images/data-ai-systems-hero.png`.
- Updated Open Graph and Twitter image metadata to the new visual asset.
- Added a `Frontend Craft` skills card including Senior HTML/CSS, semantic HTML, modern CSS, responsive UI, accessibility, SEO, and vanilla JS.
- Removed the previous non-portfolio project emphasis from the public project grid and replaced it with curated portfolio-worthy case studies.
- Preserved section IDs: `#hero`, `#skills`, `#experience`, `#projects`, `#certifications`, and `#contact`.
- Preserved EN/PT language toggle, mobile menu, CV downloads, scroll reveal, and active nav behavior.

## Remaining owner confirmations

- Confirm that "Senior HTML/CSS" should be public positioning and whether it should also be added to the CV.
- Confirm which client/product names should remain public versus anonymized, especially TK Technologies, Stok IA, and Spacecom.
- Confirm whether the Google Docs CV is still canonical after the current repo PDF/source snapshot.
- External certificate URLs were not network-validated in this local pass.

## Recommended next pass

- Run a browser/mobile QA pass before deploying to GitHub Pages.
- After owner review, sync any approved CV wording changes back to the Google Docs source and exported PDFs.
- Consider regenerating a dedicated 1200x630 social preview later if social sharing precision becomes important.
