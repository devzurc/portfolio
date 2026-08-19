---
name: add-dashboard-widget
description: Add a static dashboard widget with clear hierarchy, responsive behavior, and defined loading/empty/error states. Use when adding dashboard-style content.
---

# Add dashboard widget

## Inputs

Widget purpose, verified content/data, target section, EN/PT copy, and any approved visual reference.

## Workflow

1. Ask for missing facts and define the user decision the widget supports.
2. Specify default, loading, empty, error, and populated states; mark live-data states not applicable for static-only content.
3. Reuse `assets/css/tokens.css` and the current v3 dashboard patterns; add semantic HTML and an accessible table/text alternative for charts.
4. Verify 390px, 768px, and 1440px in EN and PT, then hand off to QA.

## Output

Provide the scoped files, state specification, responsive behavior, accessibility criteria, and verification result. Do not invent data.
