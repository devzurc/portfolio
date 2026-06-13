# Portfolio audit - 2026-06-13

## Scope checked

- Static portfolio surface: `index.html`, `assets/css/*.css`, `assets/js/site.js`, image/CV/certificate paths, and section flow.
- Career evidence layer: `docs/career/INDEX.md`, `docs/career/projects/*.md`, `docs/career/readmes/*.md`, and `docs/career/tech-stack-rollup.md`.
- Adjacent project artifact: `AI Engineer Portfolio/` React/Figma export.
- Local validation: checked local `href`/`src` references in `index.html`, CSS `url(...)` references, and WhatsApp project references after the update.

## Changes made in this pass

- Updated the TK Technologies engagement from the previous shorter completed-contract wording to a current 6-month contract, expected through Aug 2026.
- Added the sanitized WhatsApp project profile at `docs/career/projects/n8n-whatsapp-assistant.md`.
- Added a public-safe README snapshot at `docs/career/readmes/n8n-whatsapp-assistant.md`.
- Added the WhatsApp project to `docs/career/INDEX.md` as private, active, portfolio-worthy, and not CV-default.
- Updated `docs/career/README.md` and `docs/career/tech-stack-rollup.md` from 14 to 15 curated project profiles.
- Added the public site project card: **WhatsApp Support & Sales Intake**.
- Added `WhatsApp APIs` to the workflow orchestration skill group.

## Current UX assessment

The static site is already aimed at recruiter scan behavior: strong role headline, visible relocation signal, CV downloads above the fold, quick proof metrics, curated project cards, and direct contact options.

The project section now communicates a stronger multi-channel automation story: CDP, Telegram, WhatsApp, Instagram, Stripe, Clerk, and IoT lakehouse. This is useful for tech leads because it shows applied integration work rather than generic AI claims.

Private work is clearly labeled as sanitized, which is the right trust posture. The portfolio should keep using this pattern: describe problem, architecture, stack, and verified behavior; never expose operational identifiers.

## Key findings

1. **Good recruiter path:** hero -> proof metrics -> selected projects -> skills -> experience -> certificates -> contact is a sensible flow for hiring review.
2. **Good tech-lead path:** the CDP card gives architectural depth, while private automation cards show concrete workflow/API integration patterns.
3. **Main privacy risk:** `docs/career/` is in a public portfolio repo, so private project profiles must stay sanitized. The new WhatsApp profile follows that rule.
4. **Maintenance risk:** bilingual EN/PT content is duplicated directly in `index.html`. This is fine for a static site, but it can drift as more projects are added.
5. **Project density risk:** the project grid now has seven cards. It is still readable, but the next UX pass should consider grouping automation projects or adding a lightweight "case studies / supporting automations" split.
6. **Adjacent artifact risk:** `AI Engineer Portfolio/` still contains generic Figma-export placeholder links, example demos, and sample contact addresses. It is not the active site, but it can confuse future maintenance or accidental deployment.
7. **Deploy readiness risk:** the active `index.html` depends on `assets/css/` and `assets/js/`, and those directories are currently untracked in the working tree. They must be added before a GitHub Pages deployment/commit.

## Recommended next improvements

1. Create 2 or 3 deeper sanitized case-study pages: CDP Platform, Telegram/WhatsApp messaging automation, and IoT lakehouse. Recruiters scan cards; tech leads often want one click deeper.
2. Add a compact "What I can own" strip near contact: data pipelines, AI workflow automation, cloud deployment, stakeholder reporting, and bilingual business communication.
3. Decide the future of `AI Engineer Portfolio/`: remove it, move it to an archive folder, or bring its content in sync. Do not leave placeholder contact/project content as an active alternative.
4. Add a small local validation script for link checks, CSS asset checks, and required bilingual pairs before deploy.
5. Consider generating project cards from a JSON/YAML data source later. That would reduce bilingual drift and keep `docs/career` closer to the public site.
6. Add visual/browser QA before deployment: desktop, tablet, and mobile screenshots in EN and PT, especially the project grid after adding WhatsApp.
7. Stage the active static assets (`assets/css/`, `assets/js/`, and any referenced image/file assets) together with `index.html` so the deployed site matches local behavior.

## Verification completed

- `index.html` local `href`/`src` references resolve.
- CSS image references resolve.
- TK Technologies contract wording now uses current/extended language across the public site and resume sources.
- WhatsApp project references exist in `index.html` and `docs/career`.
- No private WhatsApp endpoint, phone number, workflow ID, instance name, token, or customer identifier was added to public portfolio copy.
