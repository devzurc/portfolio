---
name: audit-component-accessibility
description: Audit one component for WCAG 2.2 AA keyboard, semantic, contrast, and assistive-technology issues. Use before or after an interactive component change.
---

# Audit component accessibility

## Inputs

Component selector/path, its states, supported languages, and target browsers/devices.

## Workflow

1. Inspect names, roles, values, semantics, focus order, visible focus, keyboard operation, target size, contrast, and reduced motion.
2. Test default and conditional states, including opened menus or dialogs.
3. Report each issue with WCAG criterion, evidence, severity, specific fix, and testable acceptance criterion.

## Output

Return an audit only. One implementation owner applies fixes; `qa-verifier` independently retests them.
