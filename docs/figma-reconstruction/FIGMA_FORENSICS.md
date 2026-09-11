# Figma reconstruction forensics

## Evidence status

The implementation brief identifies a downloaded React/Tailwind export as the authoritative rendering evidence. That export, its source URL, and reference captures are not present in this workspace as of 2026-08-19. The current committed static site is therefore the only inspectable implementation evidence. Exact-source assertions and pixel-difference acceptance remain pending ingestion of the export or reference PNGs.

## Reconstructed component tree

`site-header` → brand, desktop navigation, language control, resume disclosure, mobile disclosure

`main` → hero → projects → skills → experience → certifications → role fit → contact

`footer` → brand/role and copyright

Shared patterns are section headers, project rows, tags, timeline cards, skill cards, credential cards, role-fit cards, buttons, icon controls, and reveal states.

## Geometry and asset inventory

- Content container: 1152px maximum with responsive 20–32px gutters.
- Header: 76px desktop, 64px mobile; glass state begins after 50px scroll.
- Grid: 48px hero background grid.
- Hero title: 96px desktop, 72px tablet, 48px mobile.
- Breakpoints: 640px, 768px, and 1024px are the reconstruction contract.
- Project raster assets: `assets/images/projects/automotive-price-intelligence.jpg`, `omnichannel-ai-crm.jpg`, and `iot-data-lakehouse.jpg`.
- Icons: dependency-free inline SVG for social links; typographic marks remain in skill cards.
- Fonts: Plus Jakarta Sans and IBM Plex Mono from Google Fonts.

## Current-to-reference map

The header, hero, projects, skills, experience, contact, and footer are Figma-derived surfaces. Certifications and Role Fit are intentional portfolio extensions and are excluded from strict shared-section pixel thresholds. Stable IDs, bilingual blocks, verified URLs, CV files, metadata, and GitHub Pages delivery take precedence over the export runtime.

## Exclusions

Figma hosting chrome/badge, React, Tailwind, Motion runtime, custom cursor, parallax, pinning, and GSAP are excluded. No platform chrome may be masked unless it occurs outside the portfolio canvas.
