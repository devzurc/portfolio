# Changelog

All notable changes to the Lucas Cruz portfolio project will be documented in this file.

## [2.0.0] - 2026-07-16

### Added
- **Complete Visual Redesign (Wibify Inspired):**
  - Ground-up theme refactor using deep near-black background (`#0A0A0B`) and vibrant accents (Electric Cyan `#00E5FF` primary, Warm Amber `#FFB800` secondary).
  - SVG Film grain noise overlay texture added globally on page canvas.
  - Staggered word-by-word reveal animations for main hero headings.
  - Hover text-roll letters scroll effect for work item titles.
  - Custom cursor-following image preview container that matches item datasets on mouse hover.
  - Full-screen navigation menu toggle for mobile and responsive modes.

### Changed
- **Typography stack:** Imported Instrument Serif for premium heading styles, Inter for body layouts, and JetBrains Mono for tags/credentials.
- **Navigation structure:** Simplified primary links to Work, Experience, Skills, Contact. Secondary paths moved to contact panels and footers.
- **Selected Work Section:** Refactored cards into a list format where each item is clean and styled with numeric watermarks and categories.
- **Skills Section:** Redesigned standard tabs into a 4-column service card layout (Data Engineering, Gen. AI & Automation, Cloud Infrastructure, Delivery & Governance).
- **Responsive Adaptations:** Reworked breakpoints for vertical/horizontal spacing, button scaling, and touch-sensitive elements.

### Fixed
- **Duplicates Audit:** Consolidated "WhatsApp CRM & Automation Platform" and "WhatsApp Support & Sales Intake" into a single cohesive project card, eliminating content overlap.
- Removed duplicated CSS blocks and unreferenced variables like `--surface-deep-card`.
- Corrected media query constraints to maintain layout ratios on smaller screens.
