# Visual QA harness

Install and run from this directory with `npm install` followed by `npm test`. Dependencies are development-only and do not affect GitHub Pages.

The suite captures deterministic, reduced-motion full pages for all required viewports and fails on console errors, page errors, failed requests, horizontal overflow, broken language/menu behavior, missing anchors, or form-validation regressions. Generated output belongs under `artifacts/` and is ignored.

Authoritative reference PNGs were not available during reconstruction. When supplied, store them under `reference/` with names such as `1440x900.png`, run `npm test`, then run `npm run compare`. The comparison writes diff PNGs, 50/50 overlays, and a JSON manifest, and fails above a 0.5% differing-pixel ratio. Add section crops only after matching fonts, state, scroll position, and device scale factor 1. Do not mask portfolio differences.
