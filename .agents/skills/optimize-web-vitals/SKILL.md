---
name: optimize-web-vitals
description: Diagnose and improve static-site Core Web Vitals with measured evidence. Use for LCP, FCP, INP/TBT, CLS, image, or render-blocking work.
---

# Optimize Web Vitals

## Inputs

Measurement URL/environment, target metric, trace or Lighthouse report, and allowed scope.

## Workflow

1. Capture a reproducible baseline and name the tested device/network profile.
2. Identify critical request chains, LCP element/resource, image dimensions/format, blocking CSS, and main-thread tasks.
3. Propose the smallest measured change first; preserve layout stability and accessibility.
4. Re-measure after implementation and report before/after values with variance caveats.

## Output

Return evidence, ranked actions, expected impact, regression risks, and verification commands. Do not claim an improvement without a comparable measurement.
