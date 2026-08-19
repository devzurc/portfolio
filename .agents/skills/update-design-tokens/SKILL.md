---
name: update-design-tokens
description: Make evidence-backed changes to static CSS design tokens and document their surface impact. Use when changing shared color, spacing, typography, radius, or motion values.
---

# Update design tokens

## Inputs

Token change request, visual rationale, affected components, and accessibility requirements.

## Workflow

1. Locate existing values in `assets/css/tokens.css` and all consuming selectors.
2. Confirm the v3 dashboard direction and assess contrast, hierarchy, and responsive impact.
3. Change the smallest token set; avoid introducing near-duplicate literal values.
4. Verify affected components across supported viewports and languages.

## Output

Return token mapping, affected surfaces, contrast/visual checks, and rollback note. Design owns the decision; CSS owns implementation mechanics.
