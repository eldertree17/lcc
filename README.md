# Lamma Cricket Club — website redesign

Redesigned static pages for [lammacc.com](https://www.lammacc.com/), built to a single
shared design system while preserving the existing header, navigation and footer branding.

## Brand

| Token        | Value     | Use                                  |
|--------------|-----------|--------------------------------------|
| Island green | `#004E42` | Primary structural colour, nav, cards |
| Chimney gold | `#FCC917` | Accent — top-bars, rules, active states |
| Warm paper   | `#F6F4EC` | Page background                      |

Headings use **Crimson Text** (with a Georgia fallback) to echo cricket's traditional
English roots; body copy is **Roboto**. The signature **three-stump divider** (three
gold bars of differing heights) separates major sections on every page.

## Pages

| File | Layout |
|------|--------|
| `our-constitution.html` | Sticky sidebar contents + numbered articles. Items `01–03` (Name, Mission, Values) are fixed; `04–19` are alphabetical. Mission as large serif type, values as a card grid, cross-link to the Executive Committee, ratification stamp. |
| `the-executive-committee.html` | Featured Chairman card, committee card grid, then a Roles & Responsibilities grid (green role panel + duties). |
| `club-history.html` | Era-based timeline with gold year badges, original club photos and stump dividers between chapters. |

## Project structure

```
assets/css/lcc.css        # shared design system
assets/js/lcc.js          # nav (mobile menu + flyouts), scrollspy, active-link
build/partials/           # head.html, header.html (banner + nav), footer.html
build/pages/              # per-page body content
build/build.py            # assembles partials + bodies -> root *.html
*.html                    # generated output (committed)
```

## Building

The committed `*.html` files are generated. After editing anything in `build/`, regenerate:

```bash
python3 build/build.py
```

## Local preview

```bash
python3 -m http.server 8099
# then open http://localhost:8099/our-constitution.html
```

> Sponsor logos and history photos are referenced from `www.lammacc.com`, so they
> require an internet connection to appear in local preview.
