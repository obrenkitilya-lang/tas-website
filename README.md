# Tax & Accounting Solutions — website

A one-page static site: a single `index.html` with no build step and no dependencies.

## 1. Fill in your details

Open `index.html` and use find-and-replace on these placeholders:

| Placeholder        | Replace with                                   | Example                      |
|--------------------|------------------------------------------------|------------------------------|
| `255XXXXXXXXX`     | WhatsApp/phone number, digits only, with 255   | `255712345678`               |
| `+255 XXX XXX XXX` | The same number, formatted for people to read  | `+255 712 345 678`           |
| `you@example.com`  | Your email                                     | `info@tas.co.tz`             |
| `[YOUR AREA]`      | Your area in Dar es Salaam                     | `Mikocheni`                  |
| `[YOUR HOURS]`     | Opening hours                                  | `Mon–Fri 8:00–17:00`         |

Every "Chat on WhatsApp" button opens WhatsApp with this message already typed:
"Hello Tax & Accounting Solutions, I would like help with: ".

## 2. Preview

Double-click `index.html` to open it in your browser.

## 3. Put it online (free options)

- **Netlify Drop**: go to https://app.netlify.com/drop and drag this folder onto the page. You get a live link in seconds.
- **GitHub Pages**: in the repository settings, go to Pages, set the source to this branch, and serve from the root (`/`) folder.
- **Cloudflare Pages / Vercel**: create a project from this repository and leave the output directory as the root.

To use your own domain (e.g. a `.co.tz` address), buy it from a registrar and point it at the host using that host's custom-domain instructions.
