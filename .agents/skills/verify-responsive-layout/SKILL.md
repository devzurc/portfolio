---
name: verify-responsive-layout
description: Verify responsive layout, overflow, readable reflow, and touch ergonomics at required viewports in EN and PT-BR. Use after layout-affecting changes.
---

# Verify responsive layout

## Inputs

Changed paths/selectors and states to test.

## Workflow

1. Check 390px, 768px, and 1440px in EN and PT-BR.
2. Inspect horizontal overflow, clipping, fixed elements, text wrapping, focus visibility, target sizes, and content order.
3. Record evidence by viewport/language and distinguish defects from intentional density.

## Output

Return a pass/fail matrix, discovered regressions, and exact reproduction steps. Do not fix issues while acting as independent verifier.
