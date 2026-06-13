# Skill: SEO & Accessibility

Use this skill for `/seo-check`, `/a11y-pass`, or when editing metadata, headings, links, and semantic structure.

---

## SEO Audit Checklist

### Document head

| Item | Current pattern | Action |
|------|-----------------|--------|
| `<title>` | Dynamic via `setLang()` | EN + PT titles must stay aligned with hero |
| `<meta name="description">` | Static in `<head>` | Update when value prop changes; ~150–160 chars |
| `<meta name="author">` | Lucas Cruz | Keep |
| `og:title` | Matches EN positioning | Sync with title changes |
| `og:description` | Shorter social summary | Compelling, not duplicate of meta description |
| `og:type` | `website` | Keep |
| `og:url` | Often missing | Recommend canonical URL if owner provides domain |
| `og:image` | Often missing | Recommend 1200×630 preview image |
| `twitter:card` | Often missing | Add `summary_large_image` if og:image added |
| `<link rel="canonical">` | Often missing | Add when custom domain confirmed |

### Content SEO

- **One `<h1>`** — hero name (already present)
- **Section `<h2>`** via `.section-title` — include target keywords naturally
- **Internal anchors** — `#skills`, `#experience`, etc. (good for UX; minor SEO benefit)
- **Keyword alignment** — page should reinforce: Data Engineer, Gen. AI, pipelines, lakehouse, LLM, cloud

### Technical SEO (static site)

- Fast load — inline CSS is fine; font preconnect already used
- Mobile-friendly viewport meta — present
- No broken links — verify cert and project URLs periodically
- HTTPS — GitHub Pages default

### Anti-patterns

- Keyword stuffing in hidden text
- Duplicate `<h1>` per language (use one visible h1; lang blocks OK if one h1 total)
- Fake structured data (JSON-LD) with unverified `Person`/`Job` schema — only add with accurate fields

---

## Accessibility Audit Checklist

### Perceivable

- [ ] Text contrast ≥ 4.5:1 for body, 3:1 for large text (cyan on dark — verify `#7AFFC4` on `#080C18`)
- [ ] `alt` text on meaningful images; empty alt on decorative
- [ ] Content readable at 200% zoom
- [ ] Color not sole indicator of state (nav active uses color + context)

### Operable

- [ ] All nav and CTAs keyboard reachable
- [ ] Visible focus styles on links and buttons
- [ ] Mobile menu operable via keyboard (consider `aria-expanded` on hamburger)
- [ ] Skip link — optional enhancement (`Skip to main content`)
- [ ] No keyboard traps in mobile menu

### Understandable

- [ ] `lang` attribute on `<html>` — consider toggling or `lang="en"` with PT content marked if improving
- [ ] Consistent navigation labels EN/PT
- [ ] Form controls — N/A today (no forms); if adding contact form, require labels + errors

### Robust

- [ ] Valid, semantic HTML (`nav`, `section`, `footer`, `ul` for cert lists)
- [ ] ARIA only when native semantics insufficient
- [ ] External links: `rel="noopener noreferrer"` with `target="_blank"`

---

## Motion & Preferences

Current site uses scroll-triggered fade-ins. Recommended enhancement:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  html { scroll-behavior: auto; }
}
```

Only add if user wants a11y hardening — note in report as optional.

---

## Link Hygiene

When auditing or adding links:

```html
<!-- External -->
<a href="https://..." target="_blank" rel="noopener noreferrer">...</a>

<!-- Download CV -->
<a href="assets/files/cv/..." download="LucasCruz_CV_EN.pdf">...</a>
```

Verify:

- Cert links open valid certificate pages
- GitHub links point to public repos
- `mailto:` uses correct address

---

## Severity Rubric

| Level | Definition | Example |
|-------|------------|---------|
| **Critical** | Blocks understanding or access | Missing alt on informative image, broken heading order |
| **High** | Hurts SEO or WCAG AA | No meta description, poor contrast on body text |
| **Medium** | Best practice gap | Missing og:image, no reduced-motion support |
| **Low** | Nice to have | JSON-LD, canonical tag |

---

## Report Template

```
## SEO
- Critical: ...
- High: ...
- Quick wins: ...

## Accessibility
- Critical: ...
- High: ...
- Quick wins: ...

## Recommended patches (minimal diff)
1. ...
2. ...

## Deferred (needs owner input)
- og:image asset
- custom domain / canonical URL
```

Apply fixes only when user explicitly requests implementation.
