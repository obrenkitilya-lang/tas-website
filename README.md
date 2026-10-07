# Tax & Accounting Solutions — website

Static website for Tax & Accounting Solutions, a tax and accounting practice
in Dar es Salaam. Plain HTML: no build step needed to view or host it.

Pages: home, services and "who we help" overviews, four service pages
(Tax, Accounting, Business Registration, Advisory), three client pages
(small businesses and startups, established companies, NGOs), About,
Compliance calendar and Contact.

- `assets/site.css` — shared styles for every page
- `assets/img/` — illustrations for each service and client group
- `tools/build.py` — generates all the pages (shared header and footer)
- `tools/art.py` — generates the illustrations

## Editing

Change the content or contact details at the top of `tools/build.py`, then run
`python3 tools/build.py` and commit the regenerated `.html` files.
Don't edit the `.html` files directly: they are overwritten on the next build.

Contact details used: phone and WhatsApp +255 755 656 369,
email obrenkitilya@gmail.com (change `EMAIL` to md@tas.co.tz once the
domain email is live).

## Using real photos

Save a photo in `assets/img/` (e.g. `tax.jpg`), change that page's `"image"`
value in `tools/build.py`, then rebuild.

## Preview

Open `index.html` in your browser.

## Put it online (free)

- **GitHub Pages**: repository Settings → Pages → Deploy from a branch → `main`, `/ (root)`.
- **Netlify Drop**: drag this folder onto https://app.netlify.com/drop.

To use tas.co.tz, point the domain at the host using that host's custom-domain instructions.
