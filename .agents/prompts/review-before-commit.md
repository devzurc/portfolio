# Prompt: Review Before Commit

Run before any git commit touching portfolio content. Use with `/pre-commit-review`.

---

## Template

```
Pre-commit review for portfolio changes.

@.agents/rules.md
@.agents/project-context.md
@.agents/skills/seo-accessibility.md

Review the current git diff (staged + unstaged). If no diff, say so and stop.

Do NOT commit unless I explicitly ask afterward.

---

## Review dimensions

### 1. Factual integrity (blocking)
- Any new metrics, employers, dates, certs, or project claims?
- Any new URLs? Do they look plausible and owner-provided?
- Any inflated language that implies unverified production scale?

Flag as **BLOCK** if fabrication risk exists.

### 2. Bilingual parity (blocking)
- Every new/changed user string has EN + PT?
- Nav `data-en` / `data-pt` updated if labels changed?
- `setLang()` title strings updated if positioning changed?

### 3. Scope (warning)
- Changes limited to intended files?
- Unrelated formatting or drive-by refactors?

### 4. UX & content quality (warning)
- Recruiter scan improved or harmed?
- Section still scannable (bullets, tags, concise paragraphs)?

### 5. Frontend regressions (warning)
- Mobile menu, lang toggle, scroll spy, fade-ins still wired?
- Section IDs and nav hrefs intact?
- CSS variables preserved?

### 6. SEO & a11y (info)
- Meta description / og tags need update for copy changes?
- New links missing `rel="noopener noreferrer"`?
- Heading hierarchy still valid?
- New images missing alt?

### 7. Secrets & assets (blocking)
- No `.env`, tokens, private keys, or internal URLs?
- CV paths still valid if touched?
- If portfolio experience/projects changed: do facts match `@docs/resume/pdf/LucasCruz_CV_EN.pdf` or owner-confirmed Google Doc?

### 8. CV sync (warning)
- Employment dates, titles, employers aligned with CV?
- New metrics on site exist on CV?
- PDFs in `docs/resume/pdf/` and `assets/files/cv/` updated if CV changed this session?

---

## Output format

```markdown
## Verdict
🟢 Safe to commit | 🟡 Commit with fixes | 🔴 Do not commit

## Blocking issues
- ...

## Warnings
- ...

## Suggested fixes (minimal)
1. ...

## EN/PT gaps
- ...

## Owner must confirm
- [ ] ...

## Suggested commit message
<1-2 sentences, why-focused, imperative mood>

## Files touched summary
| File | Nature of change |
|------|------------------|
| index.html | ... |
```

---

## Verdict Rules

| Verdict | When |
|---------|------|
| 🔴 **Do not commit** | Unverified claims, missing PT/EN pair, secrets, broken nav IDs |
| 🟡 **Commit with fixes** | Minor a11y/SEO gaps, small scope creep, fixable in same session |
| 🟢 **Safe to commit** | All checks pass; copy aligned with rules |

---

## Commit Message Guidelines

Good:

```
Tighten hero copy for DE + Gen. AI positioning in EN and PT.

Recruiters scan the hero first; this clarifies lakehouse and LLM automation focus without changing verified stats.
```

Bad:

```
Update index.html
```

---

## Example Invocation

```
/pre-commit-review

@.agents/prompts/review-before-commit.md

I changed the projects section. Review diff and suggest commit message.
```

---

## After Review

If verdict is 🟢 or owner fixes 🟡 items:

```
Commit with message: "<approved message>"
```

Agent should only then run git add/commit per user rules — never proactively.
