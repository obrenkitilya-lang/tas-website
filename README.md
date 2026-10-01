# Danis Associates — website

Static website for Danis Associates, Certified Public Accountants in
Public Practice & Tax Consultants, Dar es Salaam. Plain HTML: no build step,
no dependencies.

Pages: home, services and industries overviews, four service-line pages
(Audit & Assurance, Tax, Advisory, Outsourcing), four industry pages, About,
Compliance calendar and Contact.

- `assets/site.css` — shared styles for every page
- `assets/logo-maroon.png`, `assets/logo-white.png` — logo for light and dark backgrounds
- `assets/img/` — illustrations for each service and industry
- `tools/build.py` — generates all the pages (shared header and footer)
- `tools/art.py` — generates the illustrations

## Using real photos

Save a photo in `assets/img/` (e.g. `audit.jpg`), change that page's
`"image"` value in `tools/build.py`, then rebuild.

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
