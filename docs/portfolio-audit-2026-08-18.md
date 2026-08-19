# Portfolio Audit Report — 2026-08-18

## Executive summary

The portfolio clearly positions Lucas Cruz for Senior Data Engineering and Gen. AI Automation roles, with credible delivery evidence, direct contact paths, and a strong recruiter-friendly information architecture. The rendered dashboard is responsive and visually cohesive, but its largest visual asset, scroll behavior, and a small group of accessibility defects materially reduce its mobile experience. The most important governance issue is that the checked-in rules describe an older Sauce Labs visual system rather than the current v3 dashboard.

**Audit scope:** repository `main` and the deployed GitHub Pages site at 390px, 768px, and 1440px, in English and PT-BR. This is a report-only audit; no production files were changed.

## Baseline and methodology

| Area | Result |
|---|---|
| Architecture | Static GitHub Pages site: `index.html`, six CSS files, one vanilla-JS file; no build system, dependency manifest, test suite, or CI configuration. |
| Rendered responsive check | No horizontal overflow observed at 390px or 1440px. Mobile sidebar correctly becomes a top bar and hamburger menu. |
| Lighthouse mobile run | Performance **51**, Accessibility **94**, Best Practices **100**, SEO **100**. |
| Core measurements | FCP **2.8s**; LCP **8.9s**; Speed Index **3.8s**; TBT **760ms**; CLS **0.002**; transfer **~1.2MiB**. |
| i18n | EN/PT controls, title, `lang`, and duplicated text blocks rendered correctly in the reviewed flows. No orphaned visible English was found in PT-BR mode. |
| Dashboard scope | This is a dashboard-style portfolio shell, not a live analytics application. Loading, empty, error, and chart-interaction states are currently not applicable. |

## Recruiter assessment

| Section | Score | Current state |
|---|---:|---|
| Hero | 4/5 | Role, CTA, relocation, and proof points are immediately legible. The banner competes with content and slows the first impression on mobile. |
| Projects | 4/5 | Clear public/private distinction, useful technology labels, and one public flagship link. Private entries necessarily provide less inspectable proof. |
| Experience | 4/5 | Strong chronological evidence and concrete data/AI delivery language. Some claims still require the existing CV-evidence workflow before copy changes. |
| Skills | 4/5 | Grouped by discipline rather than a keyword dump; appropriately supports the target roles. |
| Certifications | 4/5 | Verification links and grouped credential presentation are strong; semantics need correction. |
| Job fit | 4/5 | Clearly frames immediate role fit and the AI Platform growth track without overstating it. |
| Contact | 5/5 | Email, CV downloads, location, relocation, and visa context are easy to find. |
| Footer | 3/5 | Current and concise, but its low-contrast text misses WCAG AA. |

## Prioritized findings

| Area | Current state and evidence | Issue | Severity | Recommended fix | Effort |
|---|---|---|---|---|---|
| Performance | Mobile Lighthouse reports LCP 8.9s and TBT 760ms. The 739KB `ai-banner.png` is CSS-discovered as the LCP element; the avatar is 412KB. | The largest visual content arrives too late and dominates the page budget. | High | Export responsive AVIF/WebP versions, serve an appropriate size, make the LCP request discoverable in HTML or preload it, and use `fetchpriority="high"` when appropriate. | 0.5–1 day |
| Performance | Lighthouse attributes ~394ms forced reflow to `site.js` scroll-spy layout reads; style/layout work is ~2.0s of ~2.8s main-thread work. | A scroll listener repeatedly reads offsets during scrolling. | High | Replace offset-based polling with an IntersectionObserver-based active-nav model, or cache section bounds and update only on resize. | 0.5 day |
| Accessibility | Lighthouse reports 4.02:1 contrast for hero social links and footer text against `#0c0c14`. | Small text does not meet WCAG 2.2 AA's 4.5:1 contrast threshold. | High | Promote these elements from `--text-tertiary` to a token with AA contrast, retaining hover states. | < 30 min |
| Accessibility | Credential card headings are `h4` after an `h2`; Lighthouse reports invalid heading order. | Screen-reader document structure skips a level. | Medium | Use `h3` for credential titles or establish an intervening `h3` section heading. | < 30 min |
| Accessibility | The mobile logo exposes visible text `LC` but is named `Lucas Cruz home`; Lighthouse reports a label/content-name mismatch. | Accessible name excludes visible text. | Medium | Include `LC` in the accessible name or hide the decorative mark from the accessibility tree. | < 30 min |
| Accessibility | Many sidebar links, language buttons, social links, certificate links, and footer links render below 44×44 CSS pixels. | Mobile touch targets are inconsistent. | Medium | Apply minimum target dimensions or increase tappable padding without changing visual density. | 0.5 day |
| Accessibility | The menu toggles `aria-expanded` and closes on Escape, but the overlay has no dialog semantics, focus placement, focus trap, or focus restoration contract. | Keyboard navigation is workable but not robust for an overlay menu. | Medium | Add `role="dialog"`, `aria-modal`, focus the first menu item on open, trap focus, and return focus to the burger on close. | 0.5–1 day |
| HTML/JS | `onclick="location.href='#contact'"` is the only inline behavior; the rest of the page uses `site.js`. | Inconsistent behavior ownership makes verification and future changes harder. | Low | Replace the inline handler with a regular anchor or a named listener in `site.js`. | < 30 min |
| CSS/structure | CSS is sensibly split into tokens, base, layout, components, sections, and responsive files. Stale selectors such as `.hero-bg`, `.hero-bg-glow`, `.cursor-preview`, and `.grain` remain; `data-ai-systems-hero.png` is a 1.64MB social asset rather than page-rendered content. | Small amount of dead styling and a large metadata asset increase maintenance and social-image cost. | Low | Remove proven-unused selectors and re-export the Open Graph image at its required dimensions with modern compression. | 0.5 day |
| Design governance | The deployed dashboard uses `#0c0c14`, Plus Jakarta Sans, 600/700 weights, gradients, and shadows. Canonical rules require the older green Sauce Labs theme, Inter, 400/500 weights, and no gradients. | Rules and project context will steer future agents toward an obsolete visual system. | High | Treat v3 dashboard tokens as authoritative and update rules/context only in the approved agent-system phase. Do not restyle the site to match obsolete rules. | Structural |
| Responsiveness | 390px layout has no overflow and correctly changes navigation. Page height is approximately 8,154px; proof content, credentials, and contact become long single-column flows. | The page is usable but scroll-heavy on small devices. | Low | After performance work, reassess disclosure/ordering of proof and credentials; preserve content rather than hiding evidence. | 0.5–1 day discovery |
| SEO | Canonical URL, robots, sitemap, `hreflang`, Open Graph/Twitter metadata, JSON-LD Person schema, and one visible H1 are present. Lighthouse SEO score is 100. Sitemap `lastmod` remains `2026-07-31`. | SEO foundation is strong; sitemap freshness is stale relative to the current audit date. | Low | Update `lastmod` only whenever the public page actually changes. | < 10 min |
| Dashboard UX | Dashboard language helps scanability: sidebar, profile card, proof metrics, cards, and clear section ordering. No live data visualization exists. | Future widgets could become dense or ambiguous without explicit loading/empty/error and accessible data-table requirements. | Deferred | Add those requirements to the future `add-dashboard-widget` skill; no product UI change is currently required. | Structural |

## Roadmap

### Quick wins — under 30 minutes each

1. Correct low-contrast social/footer text.
2. Repair credential heading order.
3. Align the mobile-logo accessible name with visible content.
4. Replace the inline contact handler.
5. Remove verified-unused CSS selectors.
6. Update sitemap `lastmod` with the next actual page deployment.

### Medium work — half to one day per item

1. Re-export and serve responsive banner/avatar/social images; make the LCP asset high priority and directly discoverable.
2. Refactor scroll spy to eliminate repeated layout reads.
3. Make tap-target sizing consistent.
4. Fully harden focus behavior for the mobile menu.
5. Reassess the mobile order and disclosure of the proof, credentials, and job-fit sections after faster loading is in place.

### Structural work — plan before implementation

1. Establish the current v3 dashboard design tokens as the sole source of truth.
2. Add deterministic static checks for i18n parity, links, semantic heading order, image sizes, and agent-adapter drift.
3. Consolidate the Codex + Cursor agent system around canonical `.agents/skills/<name>/SKILL.md` skills and generated specialist adapters.
4. Define accessible widget requirements before adding live dashboard/data-visualization features.

## Factual verification and constraints

- Keep existing CV-backed metrics, dates, employers, and credentials unchanged until the CV/career-evidence workflow approves a change.
- Preserve EN/PT-BR parity for every future public copy change.
- Do not add private-work metrics, project links, or certificates without verified evidence.
- No evidence of a broken public project, CV, or certificate link was established by this audit; repeat link checks before any major application campaign.

## Phase 1 approval matrix

Select one status for each group before any site or agent-system work begins.

| Group | Included work | Default recommendation | Status |
|---|---|---|---|
| A — Accessibility quick wins | Contrast, heading order, accessible label, inline handler cleanup | Accept | Pending |
| B — Performance | Responsive image pipeline, LCP priority/discovery, scroll-spy refactor | Accept | Pending |
| C — Mobile usability | Tap targets and modal focus behavior | Accept | Pending |
| D — Low-risk hygiene | Dead CSS and sitemap freshness | Accept | Pending |
| E — Content/layout discovery | Mobile information density review | Defer until A–C are complete | Pending |
| F — Agent-system rebuild | AGENTS.md, rules, skills, specialists, adapters, validation | Accept as a separate branch after this report is reviewed | Pending |

## Verification record

- Reviewed source structure, semantic outline, CSS token usage, JavaScript behavior, assets, `robots.txt`, `sitemap.xml`, and current agent documentation.
- Rendered the deployed portfolio at desktop and phone widths; verified no horizontal overflow in the sampled viewports.
- Verified English and Portuguese rendering, menu toggling, Escape close behavior, language persistence behavior, and primary navigation state.
- Ran Lighthouse on the deployed public page. Results are environment-sensitive and should be rerun after performance changes rather than treated as a fixed production SLA.
