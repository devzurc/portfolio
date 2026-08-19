# Static implementation map

| Reference surface | Static implementation |
|---|---|
| Header/navigation | `index.html` `.site-header`; `assets/css/layout.css`; `assets/js/site.js` |
| Hero/grid/glows/stats | `#hero`, `.hero-backdrop`, `.stats-grid` |
| Projects | `#projects`, `.project-list`, `.project-card` |
| Skills | `#skills`, `.skills-grid`, `.skill-card` |
| Experience | `#experience`, `.timeline`, `.timeline-card` |
| Contact | `#contact`, `.contact-layout`, mailto form behavior |
| Footer | `footer`, `.footer-inner` |

Certifications and Role Fit are intentional Figma-native extensions. EN/PT controls, bilingual duplicate blocks, verified public claims, stable anchors, and CV downloads are preserved. The production path stays dependency-free; Playwright and image-diff packages are isolated under `qa/visual/`.

Pixel acceptance cannot be evaluated until authoritative reference screenshots or the named export are supplied. Once present, place normalized PNGs in `qa/visual/reference/` using the viewport names documented in the harness README and run `npm test` from that directory.
