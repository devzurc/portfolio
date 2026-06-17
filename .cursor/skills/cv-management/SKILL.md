---
name: cv-management
description: Manages CV content, exports, and portfolio sync for Lucas Cruz's CV. Use when adding, editing, or removing CV content, exporting PDFs, or syncing CV facts to the portfolio.
---

# Skill: CV Management

Use this skill when adding, editing, or removing content on Lucas Cruz's CV, exporting PDFs, or syncing CV facts to the portfolio.

---

## Source of Truth Hierarchy

```
Google Docs (editable, public)  →  docs/resume/{word,pdf,source}  →  assets/files/cv/*.pdf  →  index.html
                                      ↑ markdown/ (agent-friendly)         ↑ site downloads
```

| Language | Google Doc |
|----------|------------|
| **EN** | https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit |
| **PT-BR** | https://docs.google.com/document/d/1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q/edit |

### Repo formats (`docs/resume/`)

| Folder | Files | Use |
|--------|-------|-----|
| `markdown/` | `LucasCruz_CV_EN.md`, `LucasCruz_CV_PT.md` | Primary in-repo editing for AI agents; git diffs |
| `word/` | `*.docx` | Pulled from Google Docs export (ATS/recruiters) |
| `pdf/` | `*.pdf` | Archive snapshot |
| `source/` | `*.txt` | Raw Google text export for quick diff |
| `scripts/` | `sync-from-google-docs.py`, `build-word.py` | Automation |

**Pull latest from Google Docs:**

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

Updates `word/`, `source/`, `pdf/`, and copies PDFs to `assets/files/cv/`.

**Agent workflow:**

1. Draft changes in chat OR edit `markdown/*.md` directly
2. Owner applies to Google Docs (or vice versa — Google is canonical for Word/PDF)
3. Run sync script
4. Run `/sync-cv-portfolio` if site copy should match

---

## CV Structure (keep EN ↔ PT aligned)

| # | Section | Notes |
|---|---------|-------|
| 1 | **Header** | Name, `Data Engineer \| Gen. AI Engineer`, phone, email, LinkedIn, portfolio URL, location, relocation, visa |
| 2 | **Professional Summary** | 3–4 lines; years, domains, stack keywords, English level, Europe intent |
| 3 | **Technical Skills** | Grouped rows (Gen. AI, Data Eng, Orchestration, Cloud, Lakehouses, DBs, BI, Security/Governance, DevOps, Languages) |
| 4 | **Work Experience** | Reverse chronological; `Title – Company \| Location (mode)` + date range + 3–5 bullets |
| 5 | **Notable Projects** | Title · stack · context · date; 1–3 bullets each |
| 6 | **Education** | Degree, institution, location, graduation date, majors line |

Do not reorder sections without owner approval. Do not add photo, age, or marital status.

---

## Bullet Quality Standard

Use **impact + action + tech** (same as portfolio):

```
• [Outcome/scope] by [what you did] using [stack/tools]
```

Rules:

- Past tense for ended roles; present for current contract if applicable
- Metrics only when owner confirms (e.g. ~30%, 95K devices, 10+ sites)
- No filler bullets ("responsible for", "helped with") without concrete deliverable
- 3–5 bullets per role; trim weakest bullet when adding new ones to stay on 2 pages

---

## Operations Playbook

### A. Update Professional Summary

**Inputs needed:** target role emphasis (DE vs Gen. AI), any new domain, unchanged facts to preserve.

**Process:**

1. Read current summary from PDF or owner paste
2. Propose EN paragraph (≤4 lines)
3. Propose PT-BR equivalent (professional PT-BR, not literal translation)
4. List keywords added/removed
5. Flag portfolio sync: hero `#hero` desc, `<meta name="description">`, `setLang()` titles

**Do not** change years of experience or English level without owner confirmation.

---

### B. Add / edit / remove skill tags

**Add skill:**

1. Confirm owner has used it in production (role bullet or project)
2. Place in correct category row; keep comma-separated style matching doc
3. Mirror in PT doc (tech terms often stay English)
4. Sync `#skills` skill-card tags in `index.html` if skill is showcase-worthy

**Remove skill:**

1. Confirm not backing any experience/project bullet
2. Remove from EN + PT docs
3. Remove from portfolio `#skills` if present
4. Note LinkedIn skills audit (manual, outside repo)

---

### C. Add work experience entry

**Required fields:**

| Field | Example |
|-------|---------|
| Title | Gen. AI Engineer |
| Company | TK Technologies |
| Location | Curitiba, PR – Brazil |
| Mode | Hybrid / Remote / On-site |
| Dates | Feb 2026 – May 2026 |
| Type | Contract / Full-time (optional) |

**Process:**

1. Insert at top of Work Experience (most recent first)
2. Draft 3–5 EN bullets — owner reviews facts
3. Draft PT-BR bullets
4. Check date gaps/overlaps with existing roles
5. Portfolio sync map:

| CV | Portfolio |
|----|-----------|
| New role | `#experience` `.job` block |
| Key metric | hero stats only if headline-worthy |
| Project overlap | `#projects` — avoid duplicate narrative; cross-link |

---

### D. Edit existing role

1. Identify company + date range (never change without owner saying so)
2. Show before/after for each bullet changed
3. If metric changes, require explicit owner confirmation
4. Update matching `.job` block in `index.html` EN + PT

---

### E. Remove work experience / shorten history

1. Confirm removal reason (relevance, space, NDA, typo duplicate)
2. Remove from EN + PT docs
3. Remove portfolio `#experience` entry
4. Scan hero/projects for orphaned references to that employer
5. Warn if gap in timeline appears — suggest honest date alignment

---

### F. Add / edit / remove Notable Project

**Add project — required:**

- Title
- Stack (inline after title, middle-dot separated)
- Context (company name or "Personal Project")
- Date (month year)
- 1–3 bullets

**Process:**

1. Avoid duplicating a full role bullet verbatim — projects should add architecture detail or personal angle
2. Sync to `#projects` `.project-card` via `@.agents/prompts/add-project.md`
3. Remove from CV + portfolio if owner deprecates project

---

### G. Education changes

Only edit with owner-provided facts (degree name, institution, date, majors). Sync only if portfolio gains an education section in future.

---

### H. Header / contact changes

Fields: phone, email, LinkedIn, portfolio URL, relocation line.

Any URL change must be verified live. Update `index.html` `#contact` and CV download paths if portfolio URL changes.

---

## PDF Export Workflow

After Google Doc edits, run the sync script (replaces manual export):

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

This downloads `.docx`, `.txt`, `.pdf` for EN + PT and copies PDFs to `assets/files/cv/`.

**Optional:** Regenerate Word from markdown only when markdown was edited in-repo and Google Doc is not yet updated:

```bash
docs/resume/.venv/bin/python docs/resume/scripts/build-word.py
```

Prefer Google Doc export (`sync-from-google-docs.py`) when the Doc is canonical.

Agent can run the sync script when asked. Verify file sizes and dates after sync.

---

## Portfolio Sync Matrix

When CV changes, check these `index.html` targets:

| CV section | Portfolio section | Sync action |
|------------|-------------------|-------------|
| Summary | `#hero` `.hero-desc` | Align value prop EN + PT |
| Summary | `<meta name="description">`, `og:description` | If positioning shifted |
| Skills rows | `#skills` `.skill-card` | Add/remove `.tag` spans |
| Work Experience | `#experience` `.job` | Add/edit/remove blocks |
| Notable Projects | `#projects` `.project-card` | Add/edit/remove cards |
| Header stats | `#hero` `.hero-stats` | Only verified headline metrics |
| Certs (if added to CV) | `#certifications` | Requires credential URL |

**Rule:** Portfolio may show a subset of CV detail, but must not **contradict** dates, titles, employers, or metrics.

---

## EN / PT Parity Checklist

- [ ] Same roles present in both docs (translated titles OK)
- [ ] Same date ranges
- [ ] Same employers and locations
- [ ] Bullets equivalent in meaning (not word-for-word)
- [ ] Skills categories match
- [ ] Projects list matches
- [ ] Education matches

---

## Anti-Patterns

| Avoid | Why |
|-------|-----|
| Editing only EN doc | PT drifts; Brazilian recruiters see stale CV |
| Updating portfolio without CV | Factual split in interviews |
| Inventing metrics to strengthen bullets | Credibility risk |
| Adding skills with no supporting bullet | Keyword stuffing |
| Keeping 3+ page CV | Recruiter drop-off; trim projects or older role detail |
| Editing PDF binary in repo | Always re-export from Google Doc |

---

## Deliverable Format

For any CV task, output:

```markdown
## Operation
<add | edit | remove> — <section> — <item>

## EN (paste into Google Doc)
...

## PT-BR (paste into Google Doc)
...

## Portfolio sync (optional)
- [ ] index.html: <section> — <action>

## Owner actions
1. Paste into Google Docs (EN + PT links above)
2. Export PDFs → docs/resume/pdf/ + assets/files/cv/
3. Approve portfolio diff if proposed

## Verification
- [ ] Dates consistent
- [ ] No fabricated metrics
- [ ] EN/PT parity
```

Wait for owner approval before editing `index.html` unless they say "apply all."
