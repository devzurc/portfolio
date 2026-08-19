# Design system

## Type

Plus Jakarta Sans is used for body and display text (400–700). IBM Plex Mono is used for metadata, labels, chips, and compact controls (400–500). Display headings use tight negative tracking; body copy uses a 1.6–1.7 line height.

## Color

Primary surfaces are `#0c0c14`, `#14141f`, `#1a1a2e`, and `#1f1f35`. Primary/secondary text is `#f0f0f5` and `#9ca3af`. Accents are teal `#00d4aa`/`#00e8bb`, purple `#a855f7`, cyan `#06b6d4`, blue `#3b82f6`, and amber `#ffcd48`. Borders use white at 6% and 12% opacity.

## Geometry

The spacing scale is 4–120px. The content maximum is 1152px. Component radii use 10px controls, 14px cards, and 16px project surfaces. Pills use a fully rounded radius. Cards use restrained dark shadows; teal glows are reserved for active or hovered emphasis.

## Reusable patterns

- Transparent header becomes a blurred elevated surface after 50px.
- Buttons are 44px minimum targets with teal primary and bordered secondary variants.
- Cards use a subtle border, elevated dark fill, and focus/hover border emphasis.
- Tags use mono text, quiet borders, and compact padding.
- Project images use cover cropping and a small hover scale.
- Focus uses a two-pixel teal outline with a three-pixel offset.

The authoritative machine-readable values remain in `assets/css/tokens.css`.
