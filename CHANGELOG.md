# Changelog

All notable changes to the Lucas Cruz portfolio project will be documented in this file.

## [Unreleased] - 2026-07-16

### Added
- **Sauce Labs Design System integration:**
  - Added new 13-color theme variables (obsidian canvas `#132322`, Mint Frost `#edf7f5`, Deep Abyss `#0e1a19`, Neon Pulse `#3ddc91`, Signal Yellow `#ffcd48`) to `assets/css/tokens.css`.
  - Added layout spacing and radius tokens (`--radius-largecards: 60px`, `--radius-cards: 20px`, `--radius-buttons: 56px`, etc.).
  - Added interactive category-tab switching logic in `assets/js/site.js`.
  - Added styling for category tabs and target active content panels in `assets/css/sections.css`.
- **Agent Rules & Synced Content:**
  - Added styling constraints and Sauce Labs design rules to `.cursor/rules/portfolio-agent-rules.mdc` to guide future agent generations.
  - Synced project repositories, career rollups, and descriptions from GitHub via `docs/career/scripts/sync-github-projects.py`.

### Changed
- **Redesign & Aesthetics:**
  - Redesigned the primary buttons to have a `56px` radius (pill-shaped) with solid `#3ddc91` (Neon Pulse) background and `#132322` text.
  - Redesigned secondary buttons to be ghost buttons with white borders.
  - Changed body background to flat obsidian `#132322` (removed heavy gradients).
  - Simplified header navigation to flat obsidian `#132322` with backdrop-filter blur and pill-shaped active states.
  - Reorganized the **Skills** section into a single premium Mint Frost card `#edf7f5` featuring a horizontal row of category tab buttons (Gen. AI, Data Eng, Orchestration, etc.) that filter skills on click.
  - Changed standard card radius to `20px` (standard) and `60px` (large cards) throughout all sections.
  - Removed multi-color gradients and heavy border glow/sweep animations on cards to maintain flat depth alignment.
  - Simplified the Hero section proof metrics to use flat Deep Abyss cards.
  - Restricted typography weights to `400` (regular) and `500` (medium) for display and headings to match geometric sans humanist styling.

### Fixed
- Updated media queries in `assets/css/responsive.css` to properly scale down large card border-radiuses from `60px` to `20px` on mobile viewports.
- Balanced CSS selectors and fixed a potential syntax error (unclosed brace lint issue) in `assets/css/sections.css`.
