---
name: frontend-maintenance
description: Fixes layout, styles, navigation, and structural HTML in the static portfolio. Use when fixing layout bugs, responsive issues, animations, or making small structural HTML changes.
---

# Skill: Frontend Maintenance

Use this skill when fixing layout bugs, updating styles, adjusting navigation, or making small structural HTML changes in the static portfolio.

---

## When to Apply

- Broken mobile menu or nav highlight
- Responsive layout issues (overflow, clipped text, bad spacing)
- Animation or fade-in regressions
- New UI component that must match existing design language
- CV dropdown, language toggle, or footer tweaks

---

## Pre-Flight

1. Read `@.agents/project-context.md` — single file `index.html`, embedded CSS/JS
2. Read `@.agents/rules.md` — bilingual and no-fabrication rules
3. Identify the smallest DOM/CSS/JS surface area to change

---

## Architecture Reminders

| Layer | Location | Notes |
|-------|----------|-------|
| Structure | `index.html` body | Section IDs are anchor targets |
| Styles | `<style>` in `<head>` | Use `:root` variables |
| Behavior | `<script>` before `</body>` | Lang, menu, observers |

### i18n pattern

```html
<p class="hero-desc en-only">English text</p>
<p class="hero-desc pt-only">Texto em português</p>
```

Nav links:

```html
<a href="#skills" data-en="Skills" data-pt="Skills">Skills</a>
```

**Never** replace this with JS string tables unless the user requests a refactor.

---

## Change Protocol

### 1. Match existing patterns

Before adding a new component, find the closest existing one:

- Buttons → `.btn`, `.btn-primary`, `.btn-outline`
- Tech labels → `.tag`
- Cards → `.skill-card`, `.project-card`, `.job`
- Section headers → `.section-label`, `.section-title`

### 2. CSS rules

- Add new rules near related section comments (e.g. `/* ── NAV ── */`)
- Prefer flex/grid patterns already used in that section
- Use `clamp()` or existing breakpoints — check `@media` blocks before adding new ones
- Avoid `!important` unless fixing a specific override bug

### 3. JS rules

Functions to preserve:

- `setLang(lang)` — toggles `.lang-pt` on body
- `toggleMenu()` / `closeMenu()` — mobile nav
- IntersectionObserver — `.fade-in`, `.job`, `.project-card`
- Scroll spy — updates `.nav-links a.active`

If you add new animated elements, register them with the same observer pattern:

```javascript
document.querySelectorAll('.your-new-class').forEach((el, i) => {
  el.dataset.delay = i * 80;
  observer.observe(el);
});
```

### 4. External links

New external links should include:

```html
<a href="..." target="_blank" rel="noopener noreferrer">
```

---

## Responsive Checklist

Verify mentally or in browser at:

| Viewport | Focus |
|----------|-------|
| ≤480px | Hamburger visible, no horizontal scroll, tap targets ≥44px |
| 768px | Grid columns collapse gracefully |
| ≥1280px | Hero and section max-widths readable |

Common fixes:

- `overflow-x: hidden` on body (already set — don't remove)
- Reduce padding in `.section-wrap` on mobile
- Ensure `.pt-only` / `.en-only` blocks don't double vertical space (only one visible)

---

## Accessibility Minimum

- Interactive elements: keyboard focus visible
- Icon-only buttons: `aria-label`
- Expand/collapse: `aria-expanded` if adding new toggles
- Respect `prefers-reduced-motion` when adding new animations (optional enhancement)

---

## Verification Steps

After edits, confirm:

1. EN and PT toggle works; title updates
2. Mobile menu opens/closes; outside click closes
3. Nav scroll spy still highlights correct section
4. No console errors on load
5. CV download links still resolve
6. Fade-in animations still fire on scroll

---

## Anti-Patterns

| Avoid | Why |
|-------|-----|
| Splitting into multiple CSS files without request | Breaks current zero-build setup |
| Introducing jQuery or React | Scope creep |
| Removing duplicate EN/PT blocks "to DRY" | Breaks i18n model |
| Hard-coded colors outside `:root` | Drifts from design system |
| Changing section IDs | Breaks nav and inbound links |

---

## Output Format

When reporting completed work:

```
## Changed
- <file>: <what>

## Verify
- [ ] Desktop EN/PT
- [ ] Mobile menu
- [ ] Section: ...

## Not changed
- <anything intentionally left alone>
```
