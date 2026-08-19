---
name: add-bilingual-content
description: Add or revise matched EN and PT-BR portfolio content without breaking language switching or factual evidence. Use for any visitor-facing copy change.
---

# Add bilingual content

## Inputs

Approved source facts, EN and PT-BR copy, target section, and verification URLs where relevant.

## Workflow

1. Verify every factual claim in CV text or curated `verified_outcomes`.
2. Follow the existing `.en-only` / `.pt-only` or `data-en` / `data-pt` pattern.
3. Preserve the language switcher’s title, HTML-language, and `aria-pressed` behavior where applicable.
4. Test both languages for parity, wrapping, and broken hidden content.

## Output

Return a fact-source map, affected selectors, EN/PT parity check, and reviewer-ready diff summary.
