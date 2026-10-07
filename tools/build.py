"""Builds the Tax & Accounting Solutions website.

Every page shares the same header and footer, so the pages are generated
from this one file. Edit the content below, then run:

    python3 tools/art.py      # only if you change the illustrations
    python3 tools/build.py

and commit the regenerated .html files in the repository root.

To use a real photograph for a page, save it in assets/img/ and change
that page's "image" value below (e.g. "assets/img/tax.jpg").
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIRM = "Tax &amp; Accounting Solutions"
TAGLINE = "Precision. Compliance. Growth."
PRINCIPAL = "Obren Allan Kitilya"
PRINCIPAL_ROLE = "Principal Consultant"
PHONE = "+255 755 656 369"
PHONE_TEL = "+255755656369"
EMAIL = "obrenkitilya@gmail.com"   # change to md@tas.co.tz once the domain email is live
LOCATION = "Dar es Salaam, Tanzania"
WHATSAPP = "255755656369"
WA_LINK = f"https://wa.me/{WHATSAPP}?text=Hello%20Tax%20%26%20Accounting%20Solutions%2C%20I%20would%20like%20help%20with%3A%20"

# ------------------------------------------------------------------ content
# "deliver": cards under "What we deliver" — (anchor, title, text, [bullets])
# "approach": four steps — (title, text)
SERVICES = [
    {
        "file": "tax.html", "name": "Tax", "image": "assets/img/tax.svg",
        "tags": "Compliance · Advisory · TRA audits &amp; objections",
        "summary": "Tax compliance, advice and support with TRA across income tax, VAT, PAYE, SDL and withholding tax, for businesses and individuals.",
        "detail": "Tanzania's tax rules are detailed and change every year, and penalties and interest start the day after a deadline is missed. We file accurately and on time, explain your position plainly, and stand with you when TRA raises questions.",
        "card": "Returns and registrations, tax advice, and TRA audits and objections.",
        "deliver": [
            ("tax-compliance", "Tax Compliance",
             "Preparation and filing of returns, accurately and on time, with proper supporting records.",
             ["TIN and VAT registration", "Income tax: provisional instalments and final returns", "Monthly PAYE, SDL, withholding tax and VAT returns", "EFD/VFD registration and tax clearance certificates"]),
            ("tax-advisory", "Tax Advice &amp; Health Checks",
             "Advice on the tax consequences of decisions before you make them, and a review of your returns and records to find errors and exposures before TRA does.",
             []),
            ("tra-audits-and-objections", "TRA Audits, Examinations &amp; Objections",
             "Structured support from TRA's first letter to resolution: review of the findings, reconciliation of TRA's computations, written responses within the prescribed timelines, meetings with TRA, and objections where an assessment is wrong.",
             []),
            ("second-opinion", "Second Opinion",
             "Already have an adviser? Send us a TRA notice, an assessment or your recent returns and we will tell you plainly whether anything is wrong, what it could cost and what to do next.",
             []),
        ],
        "approach": [
            ("Diagnose", "We review your obligations, returns and records to find gaps before they become assessments."),
            ("Comply", "A filing calendar for every monthly, quarterly and annual return, managed so deadlines are not missed."),
            ("Advise", "Clear advice on your tax position and on decisions with tax consequences, in English or Kiswahili."),
            ("Defend", "Responses, meetings and objections with TRA, handled promptly and properly documented."),
        ],
    },
    {
        "file": "accounting.html", "name": "Accounting", "image": "assets/img/accounting.svg",
        "tags": "Bookkeeping · Financial statements · Payroll",
        "summary": "Bookkeeping, financial statements and payroll for small and growing businesses and non-profits, kept accurate and ready for tax.",
        "detail": "Reliable records are the foundation of good decisions and of every tax return. We keep your books up to date, prepare your financial statements and run your payroll, so you always know where your business stands.",
        "card": "Bookkeeping, financial statements, payroll and management reports.",
        "deliver": [
            ("bookkeeping", "Bookkeeping &amp; Reconciliations",
             "Recording of transactions, bank and cash reconciliations, and follow-up of unexplained differences.",
             []),
            ("financial-statements", "Financial Statements",
             "Annual financial statements prepared in accordance with the applicable framework, ready for tax filing, banks and investors, and for audit where required.",
             []),
            ("payroll", "Payroll",
             "Monthly payroll processed confidentially, with payslips and reports, and PAYE, SDL, NSSF and WCF computed and filed on time.",
             []),
            ("management-reporting", "Management Reports",
             "Simple monthly or quarterly reports showing income, expenses, cash and tax due, so you can plan ahead.",
             []),
        ],
        "approach": [
            ("Set up", "We agree what you need, collect opening balances and set up your records and payroll data."),
            ("Monthly", "Bookkeeping, reconciliations, payroll and statutory payments, with a short monthly summary."),
            ("Quarterly", "A review of results and tax position, and any adjustments to your filing calendar."),
            ("Year end", "Financial statements and final tax returns prepared and filed on time."),
        ],
    },
    {
        "file": "business-registration.html", "name": "Business Registration", "image": "assets/img/registration.svg",
        "tags": "BRELA · TRA · Licences",
        "summary": "Registering your business correctly with BRELA and TRA, obtaining licences, and keeping your statutory filings up to date.",
        "detail": "Getting registration right at the start avoids problems later with banks, tenders and TRA. We handle the paperwork from your first TIN to annual returns, so your business stays in good standing.",
        "card": "BRELA registration, TIN and VAT, licences and annual returns.",
        "deliver": [
            ("brela-registration", "Company &amp; Business Name Registration",
             "Registration of companies and business names with BRELA, including preparation of the required documents.",
             []),
            ("tra-registration", "TIN, VAT &amp; EFD/VFD",
             "TIN registration for businesses and individuals, VAT registration where required, and EFD/VFD registration.",
             []),
            ("business-licences", "Business Licences",
             "Applications for new business licences and renewals before they expire.",
             []),
            ("annual-returns", "Annual Returns &amp; Statutory Changes",
             "BRELA annual returns, and changes of directors, shareholding and address filed correctly and on time.",
             []),
        ],
        "approach": [
            ("Consult", "We confirm the right structure and registrations for your business."),
            ("Prepare", "We prepare the documents and tell you exactly what we need from you."),
            ("File", "We submit to BRELA, TRA and the licensing authority and follow up."),
            ("Maintain", "Reminders and filing for annual returns, renewals and changes."),
        ],
    },
    {
        "file": "advisory.html", "name": "Advisory", "image": "assets/img/advisory.svg",
        "tags": "Consultancy · Decisions · Compliance reviews",
        "summary": "Practical tax and business advice before you sign, buy, hire or expand, and reviews that keep a growing business compliant.",
        "detail": "The best time to get tax advice is before a decision is made. We help owners and managers understand the tax and financial consequences of their plans and choose the right way forward.",
        "card": "Tax and business consultancy, and advice before key decisions.",
        "deliver": [
            ("consultancy", "Tax &amp; Business Consultancy",
             "Advice on structuring your business, managing your tax position and meeting your obligations as you grow.",
             []),
            ("decisions", "Advice Before Key Decisions",
             "Review of the tax implications of contracts, asset purchases, new premises, hiring and expansion before you commit.",
             []),
            ("compliance-reviews", "Compliance Reviews",
             "A review of your tax, payroll and registration compliance with a clear list of what to fix and in what order.",
             []),
        ],
        "approach": [
            ("Understand", "We learn your business and the decision you are facing."),
            ("Analyse", "We work through the tax and financial consequences of each option."),
            ("Recommend", "A clear recommendation in plain language, in writing."),
            ("Support", "Help putting the decision into practice, and follow-up where needed."),
        ],
    },
]

SEGMENTS = [
    {
        "file": "small-businesses-and-startups.html", "name": "Small Businesses &amp; Startups", "image": "assets/img/small-business.svg",
        "tags": "Sole proprietors · Partnerships · New companies",
        "summary": "Getting registered, staying compliant and keeping simple, reliable records from the first day of trading.",
        "card": "Registration, compliance and bookkeeping from day one.",
        "help": [
            ("Start correctly", "BRELA registration, TIN, licences and VAT registration where needed."),
            ("Stay compliant", "Monthly and annual returns filed on time, with a reminder before every deadline."),
            ("Keep records", "Simple bookkeeping and payroll so you always know your position."),
            ("Grow", "Advice before you hire, buy equipment or open new premises."),
        ],
        "related": [("business-registration.html", "Business Registration"), ("tax.html#tax-compliance", "Tax Compliance"), ("accounting.html#bookkeeping", "Bookkeeping")],
    },
    {
        "file": "established-companies.html", "name": "Established Companies", "image": "assets/img/companies.svg",
        "tags": "Companies · Branches · Family businesses",
        "summary": "Dependable tax compliance, financial statements and support through TRA audits for companies with growing obligations.",
        "card": "Tax compliance, financial statements and TRA audit support.",
        "help": [
            ("Tax compliance", "Corporate income tax, VAT, PAYE, SDL and withholding tax managed on a filing calendar."),
            ("TRA audits", "Support through audits, examinations and objections, from first letter to resolution."),
            ("Financial statements", "Annual financial statements ready for tax filing and for the auditors."),
            ("Health checks", "Periodic reviews to find and fix exposures before TRA does."),
        ],
        "related": [("tax.html#tra-audits-and-objections", "TRA Audits &amp; Objections"), ("accounting.html#financial-statements", "Financial Statements"), ("tax.html#tax-advisory", "Tax Health Checks")],
    },
    {
        "file": "ngos-and-non-profits.html", "name": "NGOs &amp; Non-Profits", "image": "assets/img/ngos.svg",
        "tags": "NGOs · Foundations · Community organisations",
        "summary": "Accounting, payroll and employment tax compliance for organisations accountable to donors and regulators.",
        "card": "Accounting, payroll and employment tax compliance.",
        "help": [
            ("Accounting", "Bookkeeping and financial statements prepared for donors, boards and auditors."),
            ("Payroll", "Payroll with PAYE, SDL, NSSF and WCF computed and filed on time."),
            ("Tax compliance", "Withholding tax and employment tax obligations met and documented."),
            ("Registration", "Support with registrations and statutory filings."),
        ],
        "related": [("accounting.html", "Accounting"), ("accounting.html#payroll", "Payroll"), ("tax.html#tax-compliance", "Tax Compliance")],
    },
]

ICONS = {
    "down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "send": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.6.13-.14.3-.35.44-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35zM12.04 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88a9.82 9.82 0 0 1 6.99 2.9 9.82 9.82 0 0 1 2.9 6.99c0 5.45-4.44 9.88-9.89 9.88zm8.41-18.3A11.81 11.81 0 0 0 12.04 0C5.5 0 .16 5.34.16 11.890c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.49-8.41z"/></svg>',
}
ICONS["wa"] = ICONS["wa"].replace("11.890c", "11.89c")
ARROW = '<span class="arrow">&rarr;</span>'


def img(src, alt=""):
    return f'<div class="img"><img src="{src}" alt="{alt}" loading="lazy"></div>'


def logo():
    return f'<span class="seal">TAS</span><span class="wordmark"><b>{FIRM}</b><small>{TAGLINE.upper()}</small></span>'


def tone(n):
    return "navy" if n % 4 in (0, 3) else "gold"


# ------------------------------------------------------------------ layout

def header(active):
    def cls(key, extra=""):
        c = " ".join(x for x in [extra, "active" if key == active else ""] if x)
        return f' class="{c}"' if c else ""

    mega = "".join(
        f'<div class="mega-col"><a class="mega-head" href="{s["file"]}">{s["name"]}</a><ul>'
        + "".join(f'<li><a href="{s["file"]}#{a}">{t}</a></li>' for a, t, *_ in s["deliver"])
        + "</ul></div>"
        for s in SERVICES)
    segments = "".join(f'<li><a href="{x["file"]}">{x["name"]}</a></li>' for x in SEGMENTS)
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="{FIRM}, home">{logo()}</a>
    <ul class="menu" id="menu">
      <li{cls("about")}><a href="about.html">About</a></li>
      <li{cls("services", "has-mega")}><a href="services.html">Services{ICONS["down"]}</a><div class="dropdown mega">{mega}</div></li>
      <li{cls("clients")}><a href="who-we-help.html">Who we help{ICONS["down"]}</a><ul class="dropdown">{segments}</ul></li>
      <li{cls("insights")}><a href="compliance-calendar.html">Insights</a></li>
      <li{cls("contact")}><a href="contact.html">Contact</a></li>
    </ul>
    <div class="nav-tools">
      <a class="nav-link email" href="tel:{PHONE_TEL}">{ICONS["phone"]}{PHONE}</a>
      <a class="btn-partner" href="contact.html"><span>Book<span class="long"> a</span> consultation</span> {ARROW}</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>"""


def footer():
    svc = "".join(f'<li><a href="{s["file"]}">{s["name"]}</a></li>' for s in SERVICES)
    seg = "".join(f'<li><a href="{x["file"]}">{x["name"]}</a></li>' for x in SEGMENTS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="index.html">{logo()}</a>
        <p>Tax, accounting and business registration services for businesses and individuals in Tanzania.</p>
        <p>{LOCATION}<br><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Who we help</h4><ul>{seg}</ul></div>
      <div><h4>The practice</h4><ul>
        <li><a href="about.html">About us</a></li>
        <li><a href="compliance-calendar.html">Compliance calendar</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul></div>
    </div>
    <div class="legal">
      <span>&copy; <span id="year">2026</span> {FIRM}. All rights reserved.</span>
      <span>Information on this website is general guidance and does not constitute professional advice.</span>
    </div>
  </div>
</footer>"""


def cta(title="Need help with tax, accounts or registration?"):
    return f"""<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="cta">
      <div><h2>{title}</h2><p>Tell us what you need. A photo of the document is enough to start, and the fee is agreed before any work begins.</p></div>
      <div class="btn-row">
        <a class="btn btn-gold" href="contact.html">Book a consultation {ARROW}</a>
        <a class="btn btn-ghost" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["wa"]}WhatsApp</a>
      </div>
    </div>
  </div>
</section>"""


def page(filename, title, description, body, active=None):
    full_title = (f"{title} | {FIRM}" if title != FIRM
                  else f"{FIRM} | Tax, Accounting &amp; Business Registration, Tanzania")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#131a2c">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='32' fill='%23131a2c'/%3E%3Ccircle cx='32' cy='32' r='28' fill='none' stroke='%23d9aa4e' stroke-width='3'/%3E%3Ctext x='32' y='40' text-anchor='middle' font-family='Georgia,serif' font-size='20' fill='%23d9aa4e'%3ETAS%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
<script>
  var t = document.querySelector('.menu-toggle'), m = document.getElementById('menu');
  t.addEventListener('click', function () {{ var o = m.classList.toggle('open'); t.setAttribute('aria-expanded', o); }});
  m.addEventListener('click', function (e) {{ if (e.target.closest('a[href*="#"]')) {{ m.classList.remove('open'); t.setAttribute('aria-expanded', false); }} }});
  document.getElementById('year').textContent = new Date().getFullYear();
</script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def cards(items):
    return "".join(f"""
      <a class="card" href="{x["file"]}">{img(x["image"])}<div class="card-body"><span class="card-title">{x["name"]}{ARROW}</span><p>{x["card"]}</p></div></a>"""
                   for x in items)


def calendar_table():
    return """<table class="cal">
      <thead><tr><th>Due date</th><th>Obligation</th><th>Applies to</th></tr></thead>
      <tbody>
        <tr><td>7th of each month</td><td>PAYE, SDL and withholding tax</td><td>Returns and payment for the previous month</td></tr>
        <tr><td>20th of each month</td><td>VAT return and payment</td><td>For the previous month</td></tr>
        <tr><td>Quarterly</td><td>Provisional income tax instalments</td><td>Based on the estimated tax for the year of income</td></tr>
        <tr><td>Within 6 months</td><td>Final income tax return</td><td>After the end of the year of income</td></tr>
      </tbody>
    </table>"""


def detail_hero(back_href, back_label, tags, title, summary, detail, image):
    return f"""<section class="svc-hero">
  <div class="wrap">
    <a class="back" href="{back_href}">&larr; {back_label}</a>
    <div class="svc-hero-grid">
      <div>
        <span class="eyebrow">{tags}</span>
        <h1>{title}</h1>
        <p class="summary">{summary}</p>
        {f'<p class="detail">{detail}</p>' if detail else ''}
      </div>
      {img(image, title)}
    </div>
  </div>
</section>"""


def deliver_cards(items):
    out = ""
    for n, item in enumerate(items):
        anchor, title, text, bullets = (item + ([],))[:4] if len(item) == 3 else item
        ul = f'<ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul>' if bullets else ""
        idattr = f' id="{anchor}"' if anchor else ""
        out += f'<div class="dcard {tone(n)}"{idattr}><h3>{title}</h3><p>{text}</p>{ul}</div>'
    return out


# ------------------------------------------------------------------ pages

def build_home():
    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Tunarahisisha kodi na usajili wa biashara yako</span>
      <h1>Your taxes and accounts, <em>handled properly.</em></h1>
      <p class="lead">{FIRM} helps businesses and individuals in Tanzania register, file and stay on the right side of TRA and BRELA, with clear advice and a fee agreed before any work starts.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">Book a consultation {ARROW}</a>
        <a class="btn btn-outline" href="services.html">Explore our services</a>
      </div>
    </div>
    <div class="hero-media">
      {img("assets/img/hero.svg", "Dar es Salaam skyline")}
      <div class="hero-badge"><strong>Fixed fee, agreed upfront</strong><span>You know the price and the timeline before any work starts.</span></div>
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Huduma zetu · Services</span><h2>What we do</h2></div>
      <p>From your first TIN to a full TRA audit. If you don't see what you need, ask: most business paperwork with TRA and BRELA, we can take on.</p>
    </div>
    <div class="cards">{cards(SERVICES)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Who we help</span><h2>Built for Tanzanian businesses</h2></div>
      <p>From sole proprietors in their first year to established companies and non-profits. We also help individuals with their own tax affairs.</p>
    </div>
    <div class="cards three">{cards(SEGMENTS)}
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Why {FIRM}</span>
      <h2>Real tax experience, straight answers.</h2>
      <p>You work directly with a tax professional with hands-on experience of TRA audits and examinations, VAT refund claims, corporate income tax and financial reporting.</p>
      <p>Every engagement starts with a clear scope and a fixed fee, and you receive copies of everything filed on your behalf.</p>
      <a class="btn btn-outline" href="about.html" style="margin-top:14px">About us {ARROW}</a>
    </div>
    <ul class="facts">
      <li>{ICONS["check"]}<span>Fixed fee, agreed upfront<small>Price and timeline confirmed before work starts</small></span></li>
      <li>{ICONS["check"]}<span>Straight answers<small>Plain explanations in English or Kiswahili, including when tax is due</small></span></li>
      <li>{ICONS["check"]}<span>On time, every time<small>A reminder before each deadline, and returns filed on time</small></span></li>
      <li>{ICONS["check"]}<span>Confidential<small>Your documents and figures are used only for the work you asked for</small></span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Insights</span><h2>TRA dates we track for you</h2></div>
      <p>Miss one and penalties and interest start the next day. We remind you before each date and file on time.</p>
    </div>
    {calendar_table()}
    <p class="note">General guidance only. <a href="compliance-calendar.html" style="color:#a87a22">View the compliance calendar</a>.</p>
  </div>
</section>

{cta()}"""
    page("index.html", FIRM,
         f"{FIRM} helps businesses and individuals in Tanzania with tax compliance, TRA audits, accounting, payroll and BRELA business registration, for a fee agreed upfront.",
         body)


def build_listing(filename, title, eyebrow, intro, items, active, three=False):
    body = f"""<section class="svc-hero" style="padding-bottom:40px">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="summary" style="max-width:720px">{intro}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><div class="cards{' three' if three else ''}">{cards(items)}</div></div>
</section>
{cta()}"""
    page(filename, title, intro, body, active=active)


def build_service(s):
    steps = "".join(f"<div><h3>{t}</h3><p>{p}</p></div>" for t, p in s["approach"])
    others = "".join(f'<a class="chip" href="{x["file"]}">{x["name"]} {ARROW}</a>' for x in SERVICES if x is not s)
    body = detail_hero("services.html", "All services", s["tags"], s["name"], s["summary"], s["detail"], s["image"]) + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">What we deliver</span>
    <hr class="rule">
    <div class="deliver">{deliver_cards(s["deliver"])}</div>
    <div class="approach">
      <span class="eyebrow">How we work</span>
      <div class="approach-grid">{steps}</div>
    </div>
    <div style="margin-top:48px"><span class="eyebrow">Other services</span><div class="related">{others}</div></div>
  </div>
</section>
{cta()}"""
    page(s["file"], s["name"], s["summary"], body, active="services")


def build_segment(x):
    related = "".join(f'<a class="chip" href="{h}">{l} {ARROW}</a>' for h, l in x["related"])
    others = "".join(f'<a class="chip" href="{o["file"]}">{o["name"]}</a>' for o in SEGMENTS if o is not x)
    body = detail_hero("who-we-help.html", "Who we help", x["tags"], x["name"], x["summary"], "", x["image"]) + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">How we help</span>
    <hr class="rule">
    <div class="deliver">{deliver_cards([(None, t, p) for t, p in x["help"]])}</div>
    <div style="margin-top:48px"><span class="eyebrow">Related services</span><div class="related">{related}</div></div>
    <div style="margin-top:32px"><span class="eyebrow">Also see</span><div class="related">{others}</div></div>
  </div>
</section>
{cta()}"""
    page(x["file"], x["name"], x["summary"], body, active="clients")


def build_about():
    values = [("Fixed fee", "The price and timeline are agreed before any work starts. No surprises on the invoice."),
              ("Straight answers", "Plain explanations in English or Kiswahili, including when the honest answer is that you owe the tax."),
              ("On time", "A reminder before each deadline, and returns filed on time with copies sent to you."),
              ("Confidential", "Your documents and figures stay between us and are used only for the work you asked for.")]
    steps = "".join(f"<div><h3>{t}</h3><p>{p}</p></div>" for t, p in [
        ("Tell us what you need", "WhatsApp, call or email. A photo of the document is enough to start."),
        ("Get a fixed fee", "You know the price and the timeline before any work starts."),
        ("We do the work", "We prepare, file and follow up with TRA or BRELA, and keep you updated."),
        ("Stay ahead", "Copies of everything filed, and a reminder before your next deadline."),
    ])
    body = detail_hero("index.html", "Home", "About the practice", "About us",
                       f"{FIRM} is a Dar es Salaam tax and accounting practice led by {PRINCIPAL}, {PRINCIPAL_ROLE}.",
                       "We help businesses and individuals register, file and stay on the right side of TRA and BRELA. Our experience includes TRA audits and tax examinations, VAT refund claims, corporate income tax and financial reporting for established companies.",
                       "assets/img/hero.svg") + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">What you can expect</span>
    <hr class="rule">
    <div class="deliver">{deliver_cards([(None, t, p) for t, p in values])}</div>
    <div class="approach" id="approach">
      <span class="eyebrow">How it works</span>
      <div class="approach-grid">{steps}</div>
    </div>
  </div>
</section>
{cta()}"""
    page("about.html", "About us",
         f"About {FIRM}, a tax and accounting practice in Dar es Salaam led by {PRINCIPAL}.",
         body, active="about")


def build_calendar():
    body = f"""<section class="svc-hero" style="padding-bottom:40px">
  <div class="wrap">
    <a class="back" href="index.html">&larr; Home</a>
    <span class="eyebrow">Insights · Compliance</span>
    <h1>Compliance calendar</h1>
    <p class="summary" style="max-width:760px">Missing a filing or payment deadline attracts penalties and interest from the day after the due date. These are the main recurring obligations for most businesses in Tanzania.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {calendar_table()}
    <p class="note">If a due date falls on a weekend or public holiday, confirm the applicable date with TRA or your adviser.</p>
    <div class="longform">
      <h2>Other recurring obligations</h2>
      <h3>BRELA annual returns</h3>
      <p>Companies must file annual returns with BRELA each year; the due date depends on the date of incorporation.</p>
      <h3>Business licences</h3>
      <p>Business licences must be renewed before they expire.</p>
      <p class="note">General guidance only. <a href="contact.html">Contact us</a> for advice on your position, or to have us manage your filings.</p>
    </div>
  </div>
</section>
{cta()}"""
    page("compliance-calendar.html", "Compliance calendar",
         "Key Tanzania Revenue Authority filing and payment deadlines and other recurring compliance obligations.",
         body, active="insights")


def build_contact():
    body = f"""<section class="svc-hero">
  <div class="wrap">
    <a class="back" href="index.html">&larr; Home</a>
    <div class="svc-hero-grid" style="align-items:start">
      <div>
        <span class="eyebrow">Wasiliana nasi · Contact</span>
        <h1>Book a consultation</h1>
        <p class="summary">Tell us what you need. A photo of the TRA letter or document is enough to start, and we reply the same day.</p>
        <div class="btn-row" style="margin-top:28px">
          <a class="btn btn-primary" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["wa"]}Chat on WhatsApp</a>
          <a class="btn btn-outline" href="tel:{PHONE_TEL}">{ICONS["phone"]}Call {PHONE}</a>
        </div>
      </div>
      <div class="contact-grid">
        <a class="c-card" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span class="c-label">Phone &amp; WhatsApp</span><span class="c-value">{PHONE}</span></a>
        <a class="c-card" href="mailto:{EMAIL}?subject=Enquiry">{ICONS["mail"]}<span class="c-label">Email</span><span class="c-value">{EMAIL.replace("@", "<wbr>@")}</span></a>
        <div class="c-card">{ICONS["pin"]}<span class="c-label">Location</span><span class="c-value">{LOCATION}</span></div>
        <div class="c-card">{ICONS["user"]}<span class="c-label">{PRINCIPAL_ROLE}</span><span class="c-value">{PRINCIPAL}</span></div>
      </div>
    </div>
  </div>
</section>"""
    page("contact.html", "Contact us",
         f"Contact {FIRM} in Dar es Salaam by phone, WhatsApp or email.",
         body, active="contact")


if __name__ == "__main__":
    for old in ROOT.glob("*.html"):
        old.unlink()
    build_home()
    build_listing("services.html", "Our services", "Huduma zetu · Services",
                  "Tax, accounting, business registration and advisory services for businesses and individuals in Tanzania.",
                  SERVICES, "services")
    build_listing("who-we-help.html", "Who we help", "Clients",
                  "Sole proprietors, startups, established companies and non-profits, plus individuals with their own tax affairs.",
                  SEGMENTS, "clients", three=True)
    for s in SERVICES:
        build_service(s)
    for x in SEGMENTS:
        build_segment(x)
    build_about()
    build_calendar()
    build_contact()
