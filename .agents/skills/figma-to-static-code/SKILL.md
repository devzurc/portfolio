---
name: figma-to-static-code
description: Turn approved Figma evidence into a minimal static HTML/CSS/JS implementation plan. Use when a Figma frame, screenshot, export, or design link is supplied.
---

# Figma to static code

## Inputs

Figma link/frame or exported reference, target section, breakpoint expectations, assets, and bilingual copy.

## Workflow

1. Use an available Figma connector only when already configured; otherwise use supplied screenshots/specifications.
2. Map frame elements to existing selectors and tokens; identify missing assets and unspecified states.
3. Preserve the zero-build static stack. Do not add a dependency or reproduce an inaccessible interaction.
4. Produce implementation and visual-verification criteria for 390px, 768px, and 1440px.

## Output

Return the frame-to-code map, token decisions, responsive notes, asset list, and bounded implementation plan.
