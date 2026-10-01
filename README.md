# Danis Associates — website

Static website for Danis Associates, Certified Public Accountants in
Public Practice & Tax Consultants, Dar es Salaam. Plain HTML: no build step,
no dependencies.

Pages: `index.html` (home), four service-line pages (Audit & Assurance, Tax,
Advisory, Outsourcing), four industry pages, `about.html`,
`compliance-calendar.html` and `contact.html`.

- `assets/site.css` — shared styles for every page
- `assets/logo-maroon.png`, `assets/logo-white.png` — logo for light and dark backgrounds
- `tools/build.py` — generates all the pages (shared header, footer and side panel)

## Editing

Change the content or contact details in `tools/build.py`, then run
`python3 tools/build.py` and commit the regenerated `.html` files.
Don't edit the `.html` files directly: they are overwritten on the next build.

## Contact details used

| Where                    | Value                              |
|--------------------------|------------------------------------|
| WhatsApp buttons         | +255 755 656 369 (Tax & Legal)     |
| Office phone / Call us   | +255 767 889 960                   |
| Other office lines       | 0628 304 441 · 0755 738 183        |
| Email                    | infodanisassociates@gmail.com      |
| Postal address           | P.O. Box 2786, Dar es Salaam       |

To change the WhatsApp number, edit `WHATSAPP` at the top of `tools/build.py` and rebuild.

## Preview

Double-click `index.html` to open it in your browser.

## Put it online (free)

- **GitHub Pages**: repository Settings → Pages → Deploy from a branch → `main`, `/ (root)`.
- **Netlify Drop**: drag this folder onto https://app.netlify.com/drop.

To use a custom domain, point it at the host using that host's custom-domain instructions.
