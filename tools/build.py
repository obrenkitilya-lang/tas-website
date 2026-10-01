"""Builds the Danis Associates website.

Every page shares the same header, footer and side panel, so they are
generated from this one file. Edit the content below, then run:

    python3 tools/build.py

and commit the regenerated .html files in the repository root.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIRM = "Danis Associates"
TAGLINE = "Certified Public Accountants in Public Practice &amp; Tax Consultants"
PHONE = "+255 767 889 960"
PHONE_TEL = "+255767889960"
PHONES_OTHER = [("0628 304 441", "+255628304441"), ("0755 738 183", "+255755738183")]
EMAIL = "infodanisassociates@gmail.com"
POSTAL = "P.O. Box 2786, Dar es Salaam, Tanzania"
CONTACT_NAME = "Obren Allan Kitilya"
CONTACT_ROLE = "Manager, Tax &amp; Legal"
WHATSAPP = "255755656369"
WHATSAPP_DISPLAY = "+255 755 656 369"

# (file, menu label, short summary) for each service page
SERVICES = [
    ("tax-compliance.html", "Tax Compliance",
     "Registration, returns and payments for income tax, PAYE, SDL, VAT and withholding tax."),
    ("tax-audits-and-disputes.html", "Tax Audits, Examinations &amp; Disputes",
     "Support through TRA audits and examinations, objections and the resolution of tax disputes."),
    ("business-registration.html", "Business Registration &amp; Company Secretarial",
     "Company and business name registration, BRELA filings, statutory changes and licences."),
    ("accounting-and-advisory.html", "Accounting &amp; Advisory",
     "Bookkeeping, financial statements, tax health checks and advice before key decisions."),
]

ICONS = {
    "chev": '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>',
    "down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.6.13-.14.3-.35.44-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35zM12.04 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88a9.82 9.82 0 0 1 6.99 2.9 9.82 9.82 0 0 1 2.9 6.99c0 5.45-4.44 9.88-9.89 9.88zm8.41-18.3A11.81 11.81 0 0 0 12.04 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.49-8.41z"/></svg>',
}

WA_LINK = f"https://wa.me/{WHATSAPP}?text=Hello%20Danis%20Associates%2C%20I%20would%20like%20to%20request%20a%20consultation%20regarding%3A%20"


def header(active):
    def item(key, href, label, dropdown=None):
        cls = ' class="active"' if key == active else ""
        if not dropdown:
            return f'<li{cls}><a href="{href}">{label}</a></li>'
        return (f'<li{cls}><a href="{href}">{label}{ICONS["down"]}</a>'
                f'<ul class="dropdown">{dropdown}</ul></li>')

    services_dd = "".join(f'<li><a href="{f}">{label}{ICONS["chev"]}</a></li>' for f, label, _ in SERVICES)
    about_dd = (f'<li><a href="about.html">The firm{ICONS["chev"]}</a></li>'
                f'<li><a href="about.html#approach">Our approach{ICONS["chev"]}</a></li>')
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="{FIRM}, home">
      <img src="assets/logo-maroon.png" alt="{FIRM}" width="133" height="52">
      <span class="region">Tanzania</span>
    </a>
    <ul class="menu" id="menu">
      {item("services", "index.html#services", "Services", services_dd)}
      {item("insights", "compliance-calendar.html", "Compliance Calendar")}
      {item("about", "about.html", "About us", about_dd)}
      {item("contact", "contact.html", "Contact")}
    </ul>
    <a class="header-contact" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span>Call <strong>{PHONE}</strong></span></a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>"""


def footer():
    svc = "".join(f'<li><a href="{f}">{label}</a></li>' for f, label, _ in SERVICES)
    others = " · ".join(f'<a href="tel:{t}">{d}</a>' for d, t in PHONES_OTHER)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="assets/logo-white.png" alt="{FIRM}" width="123" height="48">
        <p>{TAGLINE}.</p>
        <p>{POSTAL}.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc}</ul>
      </div>
      <div>
        <h4>The firm</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="about.html#approach">Our approach</a></li>
          <li><a href="compliance-calendar.html">Compliance calendar</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li>{others}</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; <span id="year">2026</span> {FIRM}. All rights reserved.</span>
      <span>Information on this website is general guidance and does not constitute professional advice.</span>
    </div>
  </div>
</footer>"""


def side_panel(current=None, title="Our areas", cta=True):
    current_cls = ' class="current"'
    items = "".join(
        f'<li{current_cls if f == current else ""}><a href="{f}">{label}{ICONS["chev"]}</a></li>'
        for f, label, _ in SERVICES)
    cta_html = f"""
    <div class="panel-cta">
      <h3>Speak to an adviser</h3>
      <p>Tell us about your matter and we will arrange an initial consultation.</p>
      <a class="btn btn-light" href="contact.html">Contact us</a>
    </div>""" if cta else ""
    return f"""<aside class="side">
    <div class="panel">
      <h2>{title}</h2>
      <ul>{items}</ul>
    </div>{cta_html}
  </aside>"""


def page(filename, title, description, body, active=None):
    full_title = f"{title} | {FIRM}" if title != FIRM else f"{FIRM} | Certified Public Accountants &amp; Tax Consultants, Tanzania"
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
<meta name="theme-color" content="#7e0505">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%237e0505'/%3E%3Ctext x='32' y='46' text-anchor='middle' font-family='Georgia,serif' font-style='italic' font-weight='700' font-size='40' fill='%23fff'%3ED%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
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
  document.getElementById('year').textContent = new Date().getFullYear();
</script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def service_page(filename, title, description, content):
    body = f"""<div class="page">
  <div class="wrap page-grid">
    <article class="page-main">
      <h1>{title}</h1>
{content}
    </article>
    {side_panel(filename)}
  </div>
</div>"""
    page(filename, title, description, body, active="services")


# ---------------------------------------------------------------- pages

def build_home():
    tiles = "".join(f"""
      <a class="tile" href="{f}"><h3>{label}</h3><p>{summary}</p><span class="more">Learn more {ICONS["chev"]}</span></a>"""
                    for f, label, summary in SERVICES)
    body = f"""<section class="hero">
  <div class="wrap page-grid">
    <div class="hero-text">
      <h1>Tax, accounting and compliance advice for <strong>Tanzanian businesses</strong></h1>
      <p class="lead">{FIRM} is a firm of Certified Public Accountants in public practice and tax consultants. We help businesses meet their obligations to the Tanzania Revenue Authority and BRELA, respond to tax audits and examinations, and maintain reliable financial records.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">Request a consultation</a>
        <a class="btn btn-outline" href="#services">Our services</a>
      </div>
    </div>
    {side_panel(title="Our services", cta=False)}
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Services</span><h2>How we can help</h2></div>
      <p>From registration and routine monthly compliance to TRA examinations and advisory work. If your matter is not listed, contact us to discuss it.</p>
    </div>
    <div class="tiles">{tiles}
    </div>
  </div>
</section>

<section class="section grey">
  <div class="wrap split">
    <div>
      <span class="eyebrow">About the firm</span>
      <h2>Qualified advisers, a clear scope and an agreed fee</h2>
      <p style="margin-top:28px">We work with owner-managed businesses, growing companies and established organisations across Tanzania. Every engagement begins with a written proposal that sets out the scope of work, deliverables, timeline and fee, followed by a signed engagement letter.</p>
      <p>Our advice is given in plain English or Kiswahili, including where the honest answer is that tax is due.</p>
      <a class="btn btn-outline" href="about.html" style="margin-top:12px">About us</a>
    </div>
    <ul class="facts">
      <li>{ICONS["check"]}<span>Certified Public Accountants in public practice</span></li>
      <li>{ICONS["check"]}<span>Tax consultants<small>Representation before the Tanzania Revenue Authority</small></span></li>
      <li>{ICONS["check"]}<span>Tax examination and audit support<small>From TRA findings through to resolution</small></span></li>
      <li>{ICONS["check"]}<span>Confidential<small>Client information is used only for the engagement instructed</small></span></li>
      <li>{ICONS["check"]}<span>Engagements in English and Kiswahili</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Compliance calendar</span><h2>Key TRA deadlines</h2></div>
      <p>Late filing and payment attract penalties and interest. These are the principal recurring deadlines for most businesses.</p>
    </div>
    {calendar_table()}
    <p class="note">General guidance only. <a href="compliance-calendar.html" style="color:var(--brand)">See the full compliance calendar</a>.</p>
  </div>
</section>

{cta_band()}"""
    page("index.html", FIRM,
         f"{FIRM}: Certified Public Accountants in public practice and tax consultants in Dar es Salaam, advising Tanzanian businesses on tax compliance, TRA audits and examinations, BRELA registration and accounting.",
         body)


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


def cta_band():
    return f"""<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>Need advice on a tax, compliance or registration matter?</h2>
      <p>Contact the firm to arrange an initial consultation.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-light" href="contact.html">Contact us</a>
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ICONS["phone"]}{PHONE}</a>
    </div>
  </div>
</section>"""


def build_services():
    service_page("tax-compliance.html", "Tax Compliance",
        "Tax registration, returns and payments for Tanzanian businesses: income tax, PAYE, SDL, VAT and withholding tax.",
        """      <p class="intro">Every company, partnership and individual carrying on business in Tanzania must register with the Tanzania Revenue Authority and meet a regular cycle of filing and payment deadlines. Late returns and late payments attract penalties and interest, and can affect your ability to obtain a tax clearance certificate.</p>
      <p>We take responsibility for preparing and filing your returns accurately and on time, supported by proper records, so that you can concentrate on running your business.</p>

      <h2>What we do</h2>
      <h3>Registration</h3>
      <p>We obtain Taxpayer Identification Numbers (TIN) for new businesses and individuals, and register businesses for the taxes that apply to them, including VAT where turnover reaches the registration threshold.</p>

      <h3>Income tax</h3>
      <ol>
        <li>Preparation of income tax computations in accordance with the applicable tax legislation;</li>
        <li>Preparation and filing of statements of estimated tax and quarterly provisional instalments;</li>
        <li>Preparation and filing of the final return of income after the end of the year of income;</li>
        <li>Advice on allowable deductions, capital allowances and the tax treatment of specific transactions.</li>
      </ol>

      <h3>Employment taxes</h3>
      <p>Monthly computation and filing of Pay As You Earn (PAYE) and the Skills and Development Levy (SDL), and reconciliation of employee records against amounts declared.</p>

      <h3>Value Added Tax</h3>
      <p>Preparation and filing of monthly VAT returns, review of input tax claims and supporting documentation, and preparation of VAT refund claims.</p>

      <h3>Withholding tax</h3>
      <p>Identification of payments subject to withholding tax, monthly returns and payment, and issue of withholding tax certificates.</p>

      <h3>EFD and VFD</h3>
      <p>Guidance on Electronic Fiscal Device and Virtual Fiscal Device obligations, and support with registration.</p>

      <h3>Tax clearance</h3>
      <p>Preparation of the documentation required to obtain tax clearance certificates for licensing, tenders and other purposes.</p>

      <div class="callout"><p><strong>Monthly compliance.</strong> We can manage your recurring returns on an ongoing basis, with a reminder before each deadline and copies of every return filed.</p></div>""")

    service_page("tax-audits-and-disputes.html", "Tax Audits, Examinations &amp; Disputes",
        "Support through TRA tax audits and examinations, review of findings, objections and resolution of tax disputes in Tanzania.",
        """      <p class="intro">A tax audit or examination by the Tanzania Revenue Authority requires a structured, well-documented response within the prescribed timelines. Errors at this stage can lead to assessments, penalties and interest that are difficult to reverse later.</p>
      <p>We manage the process from the first review of TRA's findings through to resolution, establishing the correct tax position and keeping management informed throughout.</p>

      <h2>Our approach to a tax examination</h2>
      <h3>Review of TRA findings</h3>
      <p>We analyse TRA's findings for each year of income under review, identify the issues raised and prepare a work plan for resolution.</p>
      <h3>Collection and review of information</h3>
      <p>We gather and review the relevant financial records, tax filings and supporting documents against TRA's findings.</p>
      <h3>Reconciliation of TRA computations</h3>
      <p>We compare TRA's computations with your records to establish the correct tax position for each year.</p>
      <h3>Response to TRA</h3>
      <p>We prepare and submit a comprehensive written response to TRA's findings within the prescribed timelines.</p>
      <h3>Representation and follow-up</h3>
      <p>We address queries raised by TRA, attend meetings and handle correspondence, and follow up regularly until outstanding matters are resolved.</p>
      <h3>Advisory on tax exposures</h3>
      <p>We advise management on potential tax exposures identified during the process and recommend corrective action.</p>

      <div class="callout"><p><strong>Deliverables.</strong> A detailed reconciliation report, the official response letter to TRA, an advisory report on identified exposures and recommendations, and progress updates throughout the engagement.</p></div>

      <h2>Assessments and objections</h2>
      <p>Where TRA issues an assessment that you believe is incorrect, strict time limits and procedural requirements apply to lodging an objection. We review the assessment, advise whether an objection is justified, and prepare and lodge the objection with supporting evidence.</p>

      <h2>Second opinions</h2>
      <p>If you already have an adviser, we can review a TRA notice, assessment or recent returns and give an independent view on whether anything is wrong, the likely exposure, and the options available.</p>""")

    service_page("business-registration.html", "Business Registration &amp; Company Secretarial",
        "Company and business name registration with BRELA, annual returns, statutory changes, business licences and company secretarial support in Tanzania.",
        """      <p class="intro">We assist local and foreign investors to establish businesses in Tanzania, and help existing companies keep their statutory records and filings up to date with the Business Registrations and Licensing Agency (BRELA).</p>

      <h2>What we do</h2>
      <h3>Registration</h3>
      <p>We register companies and business names with BRELA. As part of our post-registration services, we obtain the company's Taxpayer Identification Number (TIN) and assist with business licences from the relevant licensing authority.</p>

      <h3>Annual returns and statutory filings</h3>
      <p>We prepare and file annual returns and ensure that the statutory filings required under the Companies Act are made on time with BRELA.</p>

      <h3>Statutory changes</h3>
      <p>We handle changes to directors, shareholding, share capital and registered office address, and file the required notifications with BRELA.</p>

      <h3>Meetings and minutes</h3>
      <p>We prepare notices, resolutions and minutes of board and shareholder meetings as required by the company.</p>

      <h3>Business licences</h3>
      <p>We prepare applications for new business licences and manage renewals before expiry.</p>

      <h3>Advice</h3>
      <p>We advise on company secretarial matters, including restructuring and changes in ownership, and keep clients informed of relevant changes in the law.</p>""")

    service_page("accounting-and-advisory.html", "Accounting &amp; Advisory",
        "Bookkeeping, bank reconciliations, financial statements, tax health checks and business advisory for Tanzanian businesses.",
        """      <p class="intro">Accurate accounting records are the foundation of tax compliance and good management decisions. We provide accounting support to businesses that do not have, or do not need, a full in-house finance function, and advise management on the tax implications of key decisions.</p>

      <h2>What we do</h2>
      <h3>Bookkeeping</h3>
      <p>We maintain your accounting records, process transactions and prepare monthly management information.</p>

      <h3>Bank reconciliations</h3>
      <p>We reconcile bank and cash accounts regularly and follow up on unexplained differences.</p>

      <h3>Financial statements</h3>
      <p>We prepare annual financial statements in accordance with the applicable financial reporting framework, ready for tax filing and other statutory purposes.</p>

      <h3>Tax health checks</h3>
      <p>We review your returns, records and processes across the main taxes to identify errors and exposures before TRA does, and recommend how to correct them.</p>

      <h3>Tax and business advisory</h3>
      <p>We advise on the tax implications of significant transactions and decisions, such as entering contracts, acquiring assets, restructuring or expanding, before you commit.</p>

      <div class="callout"><p><strong>Outsourced finance support.</strong> Combining accounting with our tax compliance service means one adviser is responsible for both your records and your returns.</p></div>""")


def build_about():
    body = f"""<div class="page">
  <div class="wrap page-grid">
    <article class="page-main">
      <h1>About us</h1>
      <p class="intro">{FIRM} is a firm of Certified Public Accountants in public practice and tax consultants based in Dar es Salaam. We advise owner-managed businesses, growing companies and established organisations on tax, compliance, business registration and accounting.</p>
      <p>Our work ranges from routine monthly filings to complex matters such as TRA tax examinations, objections and tax advisory. All services are performed in accordance with applicable tax laws and professional standards.</p>

      <h2>Our values</h2>
      <h3>Qualified</h3>
      <p>Our advisers are Certified Public Accountants and tax consultants with practical experience of TRA audits and examinations, VAT refund claims, corporate income tax and financial reporting.</p>
      <h3>Clear</h3>
      <p>We agree the scope, deliverables, timeline and fee in writing before work begins, and explain your position plainly, in English or Kiswahili.</p>
      <h3>Confidential</h3>
      <p>Client records and information are used only for the engagement we have been instructed on.</p>

      <h2 id="approach">Our approach</h2>
      <h3>1. Initial consultation</h3>
      <p>We discuss your requirements and review the relevant documents.</p>
      <h3>2. Proposal and engagement letter</h3>
      <p>We issue a written proposal setting out the scope of work, deliverables, timeline and professional fee. Work begins once the engagement letter is signed.</p>
      <h3>3. Execution</h3>
      <p>We carry out the work and liaise with TRA, BRELA or other authorities as required.</p>
      <h3>4. Reporting</h3>
      <p>We provide progress updates, copies of everything filed, and notice of upcoming obligations.</p>

      <h2>Key contact</h2>
      <p><strong style="color:var(--ink)">{CONTACT_NAME}</strong>, {CONTACT_ROLE}<br>
      <a href="tel:+{WHATSAPP}">{WHATSAPP_DISPLAY}</a> · <a href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp</a></p>
    </article>
    {side_panel()}
  </div>
</div>
{cta_band()}"""
    page("about.html", "About us",
         f"About {FIRM}, Certified Public Accountants in public practice and tax consultants in Dar es Salaam.",
         body, active="about")


def build_calendar():
    body = f"""<div class="page">
  <div class="wrap page-grid">
    <article class="page-main">
      <h1>Compliance calendar</h1>
      <p class="intro">Missing a filing or payment deadline attracts penalties and interest from the day after the due date. The table below summarises the principal recurring TRA deadlines for most businesses.</p>
      {calendar_table()}
      <p class="note">If a due date falls on a weekend or public holiday, confirm the applicable date with TRA or your adviser.</p>

      <h2>Other recurring obligations</h2>
      <h3>BRELA annual returns</h3>
      <p>Companies must file annual returns with BRELA each year. The due date depends on the company's date of incorporation.</p>
      <h3>Business licences</h3>
      <p>Business licences must be renewed before they expire. Check the expiry date on your current licence.</p>

      <div class="callout"><p><strong>General guidance only.</strong> Specific obligations depend on the nature of your business. <a href="contact.html">Contact us</a> for advice on your position, or to have us manage your filings.</p></div>
    </article>
    {side_panel()}
  </div>
</div>"""
    page("compliance-calendar.html", "Compliance calendar",
         "Key Tanzania Revenue Authority filing and payment deadlines: PAYE, SDL, withholding tax, VAT, provisional tax and final returns.",
         body, active="insights")


def build_contact():
    others = " · ".join(d for d, _ in PHONES_OTHER)
    body = f"""<div class="page">
  <div class="wrap page-grid">
    <article class="page-main">
      <h1>Contact us</h1>
      <p class="intro">Tell us about your matter and we will arrange an initial consultation. Copies of any TRA notices, assessments or correspondence help us respond quickly.</p>
      <div class="contact-cards">
        <a class="c-card" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span class="c-label">Telephone</span><span class="c-value">{PHONE}</span><span class="c-sub">{others}</span></a>
        <a class="c-card" href="mailto:{EMAIL}?subject=Consultation%20request">{ICONS["mail"]}<span class="c-label">Email</span><span class="c-value">{EMAIL.replace("@", "<wbr>@")}</span></a>
        <div class="c-card">{ICONS["pin"]}<span class="c-label">Postal address</span><span class="c-value">{POSTAL}</span></div>
        <a class="c-card" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["user"]}<span class="c-label">Tax &amp; Legal</span><span class="c-value">{CONTACT_NAME}</span><span class="c-sub">{CONTACT_ROLE} · {WHATSAPP_DISPLAY} · WhatsApp</span></a>
      </div>
      <div class="btn-row">
        <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Consultation%20request">{ICONS["mail"]}Email the firm</a>
        <a class="btn btn-outline" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["wa"]}Message on WhatsApp</a>
      </div>
    </article>
    {side_panel(cta=False)}
  </div>
</div>"""
    page("contact.html", "Contact us",
         f"Contact {FIRM} in Dar es Salaam: telephone, email and WhatsApp.",
         body, active="contact")


if __name__ == "__main__":
    build_home()
    build_services()
    build_about()
    build_calendar()
    build_contact()
