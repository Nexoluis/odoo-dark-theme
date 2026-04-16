# AGX Dark Theme for Odoo 17

Complete dark theme for **Odoo 17 Community** backend, based on the [Catppuccin Mocha](https://github.com/catppuccin/catppuccin) palette.

## Features

- Full dark mode for all backend views: List, Form, Kanban, Calendar, Pivot
- Dark navbar, control panel, sidebars, modals, dropdowns, chatter
- Styled inputs, buttons, tables, badges, alerts and tabs
- Custom dark scrollbars
- Correct Odoo 17 SCSS variable overrides (no hacks, no inline styles)

## Color Palette

| Role | Color |
|---|---|
| Background |  |
| Surface 0 (navbar) |  |
| Surface 1 (cards) |  |
| Surface 2 (borders) |  |
| Text |  |
| Accent Blue |  |

## Installation

1. Copy  into your Odoo addons path
2. Restart Odoo: 
3. Update apps list: Settings → Apps → Update Apps List
4. Search for **AGX Dark Theme** and install
5. Hard refresh your browser ()

## Technical Notes

Odoo 17 uses its own  SCSS variable system on top of Bootstrap.
Standard Bootstrap variable overrides (, ) alone do not work.

This module correctly overrides:
-  — form and list view background
-  — main client background  
-  through  — full Odoo gray palette
-  — global text color
- All Bootstrap variables for BS components used by Odoo

Assets are injected via:
-  (prepend) — SCSS variables before Bootstrap compiles
-  (append) — CSS overrides at maximum priority

## Compatibility

| Odoo | Community | Enterprise |
|---|---|---|
| 17.0 | ✅ | ✅ |

## License

LGPL-3 — see [LICENSE](LICENSE)

## Author

[AGX OSINT SL.](https://github.com/agxosint)
