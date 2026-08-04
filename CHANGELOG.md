# Changelog

All notable changes to the Lucas Cruz portfolio project will be documented in this file.

## [Unreleased]

## [3.0.0] - 2026-08-04

### Added
- **Real Profile Photo:** Updated `assets/images/profile-avatar.png` with Lucas Cruz's official headshot.
- **AI Engineering Banner Image:** Added futuristic high-tech AI & Data Engineering banner background (`assets/images/ai-banner.png`) to `.dashboard-banner`.
- **Complete Dashboard Layout Redesign:**
  - Ground-up layout shift from full-width vertical scroll to **sidebar + main content dashboard** inspired by modern developer portfolios.
  - Fixed left sidebar with icon-based vertical navigation (Home, Projects, Experience, Skills, Contact), external links (GitHub, LinkedIn, Medium), language toggle, and CV download.
  - **Gradient banner** (purple → cyan → blue) spanning the top of the main content area.
  - **Profile card** with circular avatar, name, title, and dual CTAs overlapping the banner.
  - Mobile top bar with hamburger menu replaces sidebar on ≤768px viewports.
  - Profile avatar image added at `assets/images/profile-avatar.png`.
  - "Key numbers" panel in the About section with proof items (5+ years, 95K+ IoT, 10+ sources, C1 IELTS).

### Changed
- **Design system overhaul (`tokens.css`):** New deep navy color palette (`#0c0c14` primary), teal-cyan accent (`#00d4aa`), purple secondary (`#a855f7`), updated border and shadow tokens.
- **Typography:** Switched from Inter to **Plus Jakarta Sans** (400/500/600/700) for headings and body. IBM Plex Mono retained for labels and tags.
- **Layout architecture (`layout.css`):** Replaced fixed top nav with sidebar component. Main content offset by sidebar width with responsive collapse.
- **All section styles updated** to card-based dashboard aesthetic with hover transitions and refined spacing.
- **Responsive breakpoints** reworked: sidebar collapse at 768px, narrower sidebar at 1100px, small phone optimizations at 480px.
- **JavaScript (`site.js`):** Scroll-spy now targets sidebar nav links. Profile card added to IntersectionObserver reveal list.

### Preserved
- All section IDs (`#hero`, `#projects`, `#experience`, `#skills`, `#certifications`, `#job-fit`, `#contact`).
- Full i18n system (EN/PT toggle with `.en-only`/`.pt-only` blocks, `data-en`/`data-pt` attributes).
- All SEO metadata (title, meta description, OG tags, Twitter cards, JSON-LD Person schema, canonical URL).
- All content: projects, experience entries, skills cards, certifications, role-fit cards, contact info.
- All external links (LinkedIn, GitHub, Medium, Credly, Coursera, Udemy, Alura verification URLs).
- CV download paths unchanged (`assets/files/cv/LucasCruz_CV_EN.pdf`, `LucasCruz_CV_PT.pdf`).
- `prefers-reduced-motion` support, skip-link, keyboard navigation.

## [2.0.1] - 2026-07-16

### Changed
- **CRM Platform Copy Enrichment:**
  - Upgraded "WhatsApp CRM" to "Omnichannel AI CRM Platform" across all portfolio components, CV files (English and Portuguese), and career evidence indexes.
  - Added new specifications detailing integrations with Telegram, Email, Meta/Google Ads APIs, role-based access control (RBAC), and LLM auto-replies/insights layers.

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
