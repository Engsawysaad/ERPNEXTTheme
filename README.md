# ERPNext Custom Theme

A custom theme app for ERPNext based on ThemeRef styling.

## Features

- **Modern Color Palette**: Dark navy primary (#0f172a) with cyan accent (#0891b2)
- **Custom Typography**: Plus Jakarta Sans (body) + Space Grotesk (headings)
- **Website Theme**: Styling for public ERPNext pages
- **Desk Theme**: Styling for admin/desk interface

## Installation

```bash
bench get-app https://github.com/Engsawysaad/ERPNEXTTheme
bench --site yoursite.local install-app erpnext_custom_theme
bench --site yoursite.local clear-cache
```

## Color Palette

| Color | Hex |
|-------|-----|
| Primary | #0f172a |
| Accent | #0891b2 |
| Accent Light | #22d3ee |
| Surface | #ffffff |
| Border | #e2e8f0 |
| Success | #10b981 |

## Requirements

- Frappe >= 16.0.0
- ERPNext >= 16.0.0

## License

MIT
