# Motion specification

## Load and reveal

Content reveals once from 24px below over 600ms using `cubic-bezier(0.16, 1, 0.3, 1)`. Nearby elements receive 0/80/160/240ms stagger delays. The hero participates in the initial reveal. Intersection observation uses an 8% threshold and a -24px bottom margin.

## Navigation and states

The header transitions over 250ms after 50px of scroll. The compact mobile disclosure fades and moves from -10px with a slight scale. Buttons move upward by 1px; cards move upward by 2px; project imagery scales to 1.04. Focus states are visible without relying on hover.

## Interaction matrix

| Surface | Hover | Focus | Activation |
|---|---|---|---|
| Navigation link | Teal text | Teal outline | Smooth scroll |
| Primary button | Brighter teal, -1px | Teal outline | Navigate/download |
| Project card | Border/glow, image scale | Link outline | External link when present |
| Mobile menu | Row tint | Trapped focus | Close on selection/Escape/outside click |
| Form field | Teal border | Teal outline/border | Validate, then open mail draft |

`prefers-reduced-motion: reduce` collapses animation and transition duration to 0.01ms and disables smooth scrolling.
