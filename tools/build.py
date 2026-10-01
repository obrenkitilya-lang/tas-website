"""Builds the Danis Associates website.

Every page shares the same header, footer and side panels, so they are
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
WA_LINK = f"https://wa.me/{WHATSAPP}?text=Hello%20Danis%20Associates%2C%20I%20would%20like%20to%20request%20a%20consultation%20regarding%3A%20"

# ------------------------------------------------------------------ content
# Each service line is one page; each area is a section on that page.
SERVICES = [
    {
        "file": "audit-and-assurance.html",
        "name": "Audit &amp; Assurance",
        "summary": "Statutory audits, donor and project audits, internal audit and special investigations that give stakeholders confidence in your financial information.",
        "intro": "Independent, high-quality assurance gives shareholders, boards, lenders, donors and regulators confidence in the information you report. Our audit approach is risk-based and grounded in a practical understanding of your organisation, so that our work adds value beyond the audit opinion.",
        "areas": [
            ("statutory-audit", "Statutory Audit",
             """<p>We audit financial statements in accordance with International Standards on Auditing (ISAs) and the requirements of the Companies Act and other applicable legislation. Our engagements cover companies, partnerships, cooperatives and other entities that require an independent audit opinion.</p>
      <ol>
        <li>Planning based on an understanding of the entity, its environment and its key risks;</li>
        <li>Evaluation of internal controls relevant to financial reporting;</li>
        <li>Substantive testing of balances, transactions and disclosures;</li>
        <li>Review of compliance with the applicable financial reporting framework, such as IFRS or IFRS for SMEs;</li>
        <li>An audit report and a management letter setting out control weaknesses and recommendations.</li>
      </ol>"""),
            ("donor-and-project-audits", "Donor &amp; Project Audits",
             """<p>Non-governmental organisations and donor-funded projects must account for funds in line with the terms of their grant agreements and the reporting requirements of their development partners. We carry out:</p>
      <ul class="list">
        <li>Audits of NGO and project financial statements;</li>
        <li>Grant and project audits to donor-specific terms of reference;</li>
        <li>Expenditure verification and agreed-upon procedures engagements;</li>
        <li>Reviews of compliance with grant conditions and procurement requirements.</li>
      </ul>"""),
            ("internal-audit", "Internal Audit",
             """<p>We provide outsourced and co-sourced internal audit services to organisations that need an effective internal audit function without the cost of a full in-house team. Our work includes risk-based internal audit plans, reviews of internal controls and processes, follow-up of management actions, and reporting to the board or audit committee.</p>"""),
            ("special-audits-and-investigations", "Special Audits &amp; Forensic Investigations",
             """<p>Where there are concerns about fraud, misappropriation or irregularities, or where a specific matter requires independent examination, we carry out special audits and investigations. Our work includes fact-finding, analysis of transactions and records, and a clear written report of findings suitable for management, boards and, where required, legal proceedings.</p>
      <p>We also perform agreed-upon procedures engagements, reporting factual findings on specific matters agreed with the client.</p>"""),
        ],
    },
    {
        "file": "tax.html",
        "name": "Tax",
        "summary": "Tax compliance, tax advisory and support through TRA audits, examinations, objections and disputes.",
        "intro": "Tanzania's tax environment is complex and changes frequently. We help organisations meet their obligations to the Tanzania Revenue Authority accurately and on time, plan transactions with the tax consequences understood, and resolve disputes when they arise.",
        "areas": [
            ("tax-compliance", "Tax Compliance",
             """<p>We prepare and file returns accurately and on time, supported by proper records.</p>
      <ol>
        <li>TIN registration and registration for the taxes that apply to your business, including VAT;</li>
        <li>Income tax computations, statements of estimated tax, provisional instalments and final returns of income;</li>
        <li>Monthly PAYE, Skills and Development Levy (SDL) and withholding tax returns;</li>
        <li>Monthly VAT returns, review of input tax and preparation of VAT refund claims;</li>
        <li>EFD and VFD registration and guidance;</li>
        <li>Tax clearance certificates for licensing, tenders and other purposes.</li>
      </ol>"""),
            ("tax-advisory", "Tax Advisory",
             """<p>We advise on the tax implications of significant decisions before you commit, including new investments, contracts, restructuring, the acquisition of assets and cross-border transactions. We also carry out tax health checks to identify errors and exposures across the main taxes before TRA does.</p>"""),
            ("tax-audits-and-disputes", "Tax Audits, Examinations &amp; Disputes",
             """<p>A TRA audit or examination requires a structured, well-documented response within the prescribed timelines. We manage the process from the first review of TRA's findings through to resolution:</p>
      <ol>
        <li>Review of TRA's findings for each year of income and a work plan for resolution;</li>
        <li>Collection and review of financial records, filings and supporting documents;</li>
        <li>Reconciliation of TRA's computations with your records to establish the correct tax position;</li>
        <li>Preparation and submission of a written response within the prescribed timelines;</li>
        <li>Representation at meetings and in correspondence, and follow-up until matters are resolved;</li>
        <li>Advice to management on tax exposures and corrective action.</li>
      </ol>
      <p>Where an assessment is incorrect, we advise whether an objection is justified and prepare and lodge it within the statutory time limits.</p>"""),
        ],
    },
    {
        "file": "advisory.html",
        "name": "Advisory",
        "summary": "Risk and governance, financial due diligence, valuations, feasibility studies and professional training.",
        "intro": "Our advisory services help boards and management make informed decisions, strengthen governance and controls, and build the capability of their finance teams.",
        "areas": [
            ("risk-and-governance", "Risk &amp; Governance",
             """<p>We help organisations identify, assess and manage the risks that matter to them. Our work includes enterprise risk management frameworks, internal control design and reviews, governance reviews, and the development of policies and procedures manuals.</p>"""),
            ("due-diligence-and-valuations", "Due Diligence, Valuations &amp; Feasibility Studies",
             """<p>Before an acquisition, investment or financing decision, we provide independent analysis of the financial position and prospects of a business:</p>
      <ul class="list">
        <li>Financial and tax due diligence for buyers, investors and lenders;</li>
        <li>Business and share valuations;</li>
        <li>Feasibility studies and business plans for new projects and financing applications.</li>
      </ul>"""),
            ("training", "Training",
             """<p>We design and deliver practical training for finance teams, management and boards, including International Financial Reporting Standards (IFRS), Tanzanian tax updates, internal controls and financial management for non-finance managers. Training can be delivered in-house and tailored to your organisation.</p>"""),
        ],
    },
    {
        "file": "outsourcing.html",
        "name": "Outsourcing",
        "summary": "Accounting and financial reporting, payroll, and company secretarial and business registration services.",
        "intro": "Many organisations prefer to outsource routine finance and administrative functions so that management can focus on running the business. We provide reliable outsourced services across accounting, payroll and company secretarial work.",
        "areas": [
            ("accounting", "Accounting &amp; Financial Reporting",
             """<p>We maintain accounting records, prepare bank reconciliations and monthly management accounts, and prepare annual financial statements in accordance with the applicable framework, including IFRS, IFRS for SMEs and IPSAS.</p>"""),
            ("payroll", "Payroll",
             """<p>We process payroll accurately and confidentially, including the computation of PAYE, the Skills and Development Levy, NSSF and WCF contributions, preparation of payslips and payroll reports, and filing of the related statutory returns.</p>"""),
            ("company-secretarial", "Company Secretarial &amp; Business Registration",
             """<p>We assist local and foreign investors to establish businesses in Tanzania and keep their statutory records up to date with the Business Registrations and Licensing Agency (BRELA):</p>
      <ul class="list">
        <li>Company and business name registration, TIN and business licences;</li>
        <li>Annual returns and statutory filings under the Companies Act;</li>
        <li>Changes of directors, shareholding, share capital and registered office;</li>
        <li>Notices, resolutions and minutes of board and shareholder meetings.</li>
      </ul>"""),
        ],
    },
]

INDUSTRIES = [
    {
        "file": "ngos-and-donor-funded-projects.html",
        "name": "NGOs &amp; Donor-Funded Projects",
        "summary": "Audits, financial management and compliance support for non-profits and development projects.",
        "body": """<p class="intro">Non-governmental organisations and donor-funded projects operate under close scrutiny from development partners, regulators and the communities they serve. Accurate financial reporting and compliance with grant conditions are essential to maintaining funding.</p>
      <h2>How we help</h2>
      <ul class="list">
        <li>Annual audits of NGO financial statements;</li>
        <li>Project and grant audits to donor terms of reference, expenditure verification and agreed-upon procedures;</li>
        <li>Financial management and internal control reviews;</li>
        <li>Policies and procedures manuals for finance, procurement and grants management;</li>
        <li>Outsourced accounting, payroll and tax compliance, including employment taxes;</li>
        <li>Training for finance and programme staff.</li>
      </ul>""",
        "links": [("audit-and-assurance.html#donor-and-project-audits", "Donor &amp; Project Audits"),
                  ("advisory.html#risk-and-governance", "Risk &amp; Governance"),
                  ("outsourcing.html#accounting", "Accounting &amp; Financial Reporting")],
    },
    {
        "file": "financial-services.html",
        "name": "Financial Services",
        "summary": "Assurance and advisory for SACCOs, microfinance institutions, insurers and other financial institutions.",
        "body": """<p class="intro">Financial institutions, including savings and credit cooperative societies (SACCOs), microfinance institutions and insurers, face demanding regulatory, reporting and governance requirements.</p>
      <h2>How we help</h2>
      <ul class="list">
        <li>Statutory audits and audits required by the relevant regulator;</li>
        <li>Internal audit and internal control reviews, including credit and loan portfolio processes;</li>
        <li>Risk management and governance frameworks;</li>
        <li>Financial reporting under IFRS and regulatory reporting support;</li>
        <li>Tax compliance and advisory;</li>
        <li>Training for boards, management and finance staff.</li>
      </ul>""",
        "links": [("audit-and-assurance.html#statutory-audit", "Statutory Audit"),
                  ("audit-and-assurance.html#internal-audit", "Internal Audit"),
                  ("advisory.html#risk-and-governance", "Risk &amp; Governance")],
    },
    {
        "file": "trade-and-manufacturing.html",
        "name": "Trade &amp; Manufacturing",
        "summary": "Audit, tax and advisory for manufacturers, distributors, retailers and logistics businesses.",
        "body": """<p class="intro">Manufacturers, wholesalers, retailers and logistics businesses deal with inventory, high transaction volumes, VAT and customs exposure, and pressure on margins and working capital.</p>
      <h2>How we help</h2>
      <ul class="list">
        <li>Statutory audits, including inventory and cost accounting;</li>
        <li>VAT compliance, refund claims and tax health checks;</li>
        <li>Support through TRA audits and examinations;</li>
        <li>Internal controls over purchasing, inventory and sales;</li>
        <li>Due diligence, valuations and feasibility studies for expansion and investment;</li>
        <li>Outsourced accounting and payroll.</li>
      </ul>""",
        "links": [("audit-and-assurance.html#statutory-audit", "Statutory Audit"),
                  ("tax.html#tax-compliance", "Tax Compliance"),
                  ("advisory.html#due-diligence-and-valuations", "Due Diligence &amp; Valuations")],
    },
    {
        "file": "public-sector.html",
        "name": "Public Sector",
        "summary": "Support for government agencies, parastatals and local government authorities.",
        "body": """<p class="intro">Public sector entities are accountable for the use of public resources and must meet strict standards of financial reporting, internal control and governance.</p>
      <h2>How we help</h2>
      <ul class="list">
        <li>Financial reporting under International Public Sector Accounting Standards (IPSAS);</li>
        <li>Internal audit and internal control reviews;</li>
        <li>Audits, reviews and special assignments where the firm is appointed;</li>
        <li>Risk management and governance advisory;</li>
        <li>Training for finance, audit and management staff.</li>
      </ul>""",
        "links": [("audit-and-assurance.html#internal-audit", "Internal Audit"),
                  ("outsourcing.html#accounting", "Accounting &amp; Financial Reporting"),
                  ("advisory.html#training", "Training")],
    },
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


# ------------------------------------------------------------------ layout

def header(active):
    def cls(key):
        return ' class="active"' if key == active else ""

    mega = "".join(
        f'<div class="mega-col"><a class="mega-head" href="{s["file"]}">{s["name"]}{ICONS["chev"]}</a><ul>'
        + "".join(f'<li><a href="{s["file"]}#{a}">{n}</a></li>' for a, n, _ in s["areas"])
        + "</ul></div>"
        for s in SERVICES)
    industries = "".join(f'<li><a href="{i["file"]}">{i["name"]}{ICONS["chev"]}</a></li>' for i in INDUSTRIES)
    about = (f'<li><a href="about.html">The firm{ICONS["chev"]}</a></li>'
             f'<li><a href="about.html#approach">Our approach{ICONS["chev"]}</a></li>'
             f'<li><a href="compliance-calendar.html">Compliance calendar{ICONS["chev"]}</a></li>')
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="{FIRM}, home">
      <img src="assets/logo-maroon.png" alt="{FIRM}" width="133" height="52">
      <span class="region">Tanzania</span>
    </a>
    <ul class="menu" id="menu">
      <li{cls("services")}><a href="index.html#services">Services{ICONS["down"]}</a><div class="dropdown mega">{mega}</div></li>
      <li{cls("industries")}><a href="index.html#industries">Industries{ICONS["down"]}</a><ul class="dropdown">{industries}</ul></li>
      <li{cls("about")}><a href="about.html">About us{ICONS["down"]}</a><ul class="dropdown">{about}</ul></li>
      <li{cls("contact")}><a href="contact.html">Contact</a></li>
    </ul>
    <a class="header-contact" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span>Call <strong>{PHONE}</strong></span></a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>"""


def footer():
    svc = "".join(f'<li><a href="{s["file"]}">{s["name"]}</a></li>' for s in SERVICES)
    ind = "".join(f'<li><a href="{i["file"]}">{i["name"]}</a></li>' for i in INDUSTRIES)
    others = " · ".join(f'<a href="tel:{t}">{d}</a>' for d, t in PHONES_OTHER)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="assets/logo-white.png" alt="{FIRM}" width="123" height="48">
        <p>{TAGLINE}.</p>
        <p>{POSTAL}.</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE}</a> · {others}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Industries</h4><ul>{ind}</ul></div>
      <div>
        <h4>The firm</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="about.html#approach">Our approach</a></li>
          <li><a href="compliance-calendar.html">Compliance calendar</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; <span id="year">2026</span> {FIRM}. All rights reserved.</span>
      <span>Information on this website is general guidance and does not constitute professional advice.</span>
    </div>
  </div>
</footer>"""


def panel(title, links, current=None):
    items = "".join(
        f'<li{" class=" + chr(34) + "current" + chr(34) if href == current else ""}><a href="{href}">{label}{ICONS["chev"]}</a></li>'
        for href, label in links)
    return f'<div class="panel"><h2>{title}</h2><ul>{items}</ul></div>'


def mini_panel(title, links):
    items = "".join(f'<li><a href="{h}">{l}{ICONS["chev"]}</a></li>' for h, l in links)
    return f'<div class="mini-panel"><h3>{title}</h3><ul>{items}</ul></div>'


def cta_box():
    return """<div class="panel-cta">
      <h3>Speak to our team</h3>
      <p>Tell us about your requirements and we will arrange an initial meeting.</p>
      <a class="btn btn-light" href="contact.html">Contact us</a>
    </div>"""


def service_links():
    return [(s["file"], s["name"]) for s in SERVICES]


def industry_links():
    return [(i["file"], i["name"]) for i in INDUSTRIES]


def page(filename, title, description, body, active=None):
    full_title = (f"{title} | {FIRM}" if title != FIRM
                  else f"{FIRM} | Audit, Tax &amp; Advisory, Tanzania")
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
  m.addEventListener('click', function (e) {{ if (e.target.closest('a[href*="#"]')) {{ m.classList.remove('open'); t.setAttribute('aria-expanded', false); }} }});
  document.getElementById('year').textContent = new Date().getFullYear();
</script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def two_col(main_html, side_html):
    return f"""<div class="page">
  <div class="wrap page-grid">
    <article class="page-main">
{main_html}
    </article>
    <aside class="side">
    {side_html}
    </aside>
  </div>
</div>"""


def cta_band():
    return f"""<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>Looking for an audit, tax or advisory partner?</h2>
      <p>Contact the firm to discuss your requirements.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-light" href="contact.html">Contact us</a>
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ICONS["phone"]}{PHONE}</a>
    </div>
  </div>
</section>"""


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


# ------------------------------------------------------------------ pages

def build_home():
    svc_tiles = "".join(f"""
      <a class="tile" href="{s["file"]}"><span class="tile-no">0{n}</span><h3>{s["name"]}</h3><p>{s["summary"]}</p><span class="more">Learn more {ICONS["chev"]}</span></a>"""
                        for n, s in enumerate(SERVICES, 1))
    ind_tiles = "".join(f"""
      <a class="tile" href="{i["file"]}"><h3>{i["name"]}</h3><p>{i["summary"]}</p><span class="more">Learn more {ICONS["chev"]}</span></a>"""
                        for i in INDUSTRIES)
    body = f"""<section class="hero">
  <div class="wrap page-grid">
    <div class="hero-text">
      <h1>Audit, tax and advisory services <strong>you can rely on</strong></h1>
      <p class="lead">{FIRM} is a firm of Certified Public Accountants in public practice and tax consultants in Tanzania. We provide audit and assurance, tax, advisory and outsourcing services to companies, NGOs and donor-funded projects, financial institutions and public sector entities.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">Contact us</a>
        <a class="btn btn-outline" href="#services">Our services</a>
      </div>
    </div>
    <aside class="side">{panel("Our services", service_links())}</aside>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Services</span><h2>What we do</h2></div>
      <p>Four service lines, delivered by qualified professionals and backed by a practical understanding of the Tanzanian regulatory environment.</p>
    </div>
    <div class="tiles">{svc_tiles}
    </div>
  </div>
</section>

<section class="section grey" id="industries">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Industries</span><h2>Sectors we serve</h2></div>
      <p>Each sector has its own reporting, regulatory and governance requirements. We bring relevant experience to every engagement.</p>
    </div>
    <div class="tiles">{ind_tiles}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="eyebrow">About the firm</span>
      <h2>Independent. Qualified. Committed to quality.</h2>
      <p style="margin-top:28px">We work with owner-managed businesses, growing companies, established organisations, NGOs and public sector entities across Tanzania. Every engagement is planned and performed in accordance with applicable professional standards and laws, and led by experienced professionals.</p>
      <p>Each engagement begins with a written proposal that sets out the scope of work, deliverables, timeline and fee, followed by a signed engagement letter.</p>
      <a class="btn btn-outline" href="about.html" style="margin-top:12px">About us</a>
    </div>
    <ul class="facts">
      <li>{ICONS["check"]}<span>Certified Public Accountants in public practice<small>Audit and assurance in accordance with International Standards on Auditing</small></span></li>
      <li>{ICONS["check"]}<span>Tax consultants<small>Compliance, advisory and representation before the Tanzania Revenue Authority</small></span></li>
      <li>{ICONS["check"]}<span>Advisory and outsourcing<small>Risk and governance, due diligence, valuations, accounting, payroll and company secretarial</small></span></li>
      <li>{ICONS["check"]}<span>Independent and confidential<small>Client information is used only for the engagement instructed</small></span></li>
    </ul>
  </div>
</section>

<section class="section grey">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Compliance calendar</span><h2>Key TRA deadlines</h2></div>
      <p>Late filing and payment attract penalties and interest. These are the principal recurring deadlines for most businesses.</p>
    </div>
    {calendar_table()}
    <p class="note">General guidance only. <a href="compliance-calendar.html" style="color:var(--brand)">See the compliance calendar</a>.</p>
  </div>
</section>

{cta_band()}"""
    page("index.html", FIRM,
         f"{FIRM}: Certified Public Accountants in public practice and tax consultants in Tanzania, providing audit and assurance, tax, advisory and outsourcing services.",
         body)


def build_service(s):
    nav = "".join(f'<a href="#{a}">{n}</a>' for a, n, _ in s["areas"])
    sections = "".join(f"""
      <section class="area" id="{a}">
        <h2>{n}</h2>
      {html}
      </section>""" for a, n, html in s["areas"])
    main = f"""      <h1>{s["name"]}</h1>
      <p class="intro">{s["intro"]}</p>
      <nav class="jump" aria-label="On this page">{nav}</nav>{sections}"""
    side = (panel("Our areas", [(f'#{a}', n) for a, n, _ in s["areas"]])
            + mini_panel("Other services", [(x["file"], x["name"]) for x in SERVICES if x is not s])
            + cta_box())
    page(s["file"], s["name"], s["summary"], two_col(main, side) + cta_band(), active="services")


def build_industry(i):
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in i["links"])
    main = f"""      <h1>{i["name"]}</h1>
      {i["body"]}
      <div class="callout"><p><strong>Related services:</strong></p><ul class="inline-links">{links}</ul></div>"""
    side = panel("Industries", industry_links(), current=i["file"]) + cta_box()
    page(i["file"], i["name"], i["summary"], two_col(main, side), active="industries")


def build_about():
    main = f"""      <h1>About us</h1>
      <p class="intro">{FIRM} is a firm of Certified Public Accountants in public practice and tax consultants based in Dar es Salaam. We provide audit and assurance, tax, advisory and outsourcing services to organisations across Tanzania.</p>
      <p>Our clients include owner-managed businesses, growing and established companies, NGOs and donor-funded projects, financial institutions and public sector entities. All services are performed in accordance with applicable professional standards and laws.</p>

      <h2>Our values</h2>
      <h3>Independence and integrity</h3>
      <p>We act objectively and with professional scepticism, and we say what we find.</p>
      <h3>Quality</h3>
      <p>Every engagement is planned, performed and reviewed in accordance with professional standards, and led by experienced professionals.</p>
      <h3>Clarity</h3>
      <p>We agree the scope, deliverables, timeline and fee in writing before work begins, and communicate our findings plainly, in English or Kiswahili.</p>
      <h3>Confidentiality</h3>
      <p>Client records and information are used only for the engagement we have been instructed on.</p>

      <h2 id="approach">Our approach</h2>
      <h3>1. Initial meeting</h3>
      <p>We discuss your requirements and review the relevant information.</p>
      <h3>2. Proposal and engagement letter</h3>
      <p>We issue a written proposal setting out the scope of work, deliverables, timeline and professional fee. Work begins once the engagement letter is signed.</p>
      <h3>3. Execution</h3>
      <p>Our team performs the work, keeping management informed and liaising with regulators and authorities as required.</p>
      <h3>4. Reporting</h3>
      <p>We deliver our reports and recommendations and, where relevant, agree follow-up actions.</p>"""
    side = panel("Our services", service_links()) + mini_panel("Industries", industry_links()) + cta_box()
    page("about.html", "About us",
         f"About {FIRM}, Certified Public Accountants in public practice and tax consultants in Dar es Salaam.",
         two_col(main, side) + cta_band(), active="about")


def build_calendar():
    main = f"""      <h1>Compliance calendar</h1>
      <p class="intro">Missing a filing or payment deadline attracts penalties and interest from the day after the due date. The table below summarises the principal recurring Tanzania Revenue Authority deadlines for most businesses.</p>
      {calendar_table()}
      <p class="note">If a due date falls on a weekend or public holiday, confirm the applicable date with TRA or your adviser.</p>
      <h2>Other recurring obligations</h2>
      <h3>Audited financial statements</h3>
      <p>Companies must prepare financial statements each year, and those required to be audited should plan the audit early enough to meet their filing and reporting deadlines.</p>
      <h3>BRELA annual returns</h3>
      <p>Companies must file annual returns with BRELA each year. The due date depends on the company's date of incorporation.</p>
      <h3>Business licences</h3>
      <p>Business licences must be renewed before they expire.</p>
      <div class="callout"><p><strong>General guidance only.</strong> Specific obligations depend on the nature of your organisation. <a href="contact.html">Contact us</a> for advice on your position.</p></div>"""
    side = panel("Our services", service_links()) + cta_box()
    page("compliance-calendar.html", "Compliance calendar",
         "Key Tanzania Revenue Authority filing and payment deadlines and other recurring compliance obligations.",
         two_col(main, side), active="about")


def build_contact():
    others = " · ".join(d for d, _ in PHONES_OTHER)
    main = f"""      <h1>Contact us</h1>
      <p class="intro">To discuss an audit, tax, advisory or outsourcing requirement, contact the firm by telephone or email and we will arrange an initial meeting.</p>
      <div class="contact-cards">
        <a class="c-card" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span class="c-label">Telephone</span><span class="c-value">{PHONE}</span><span class="c-sub">{others}</span></a>
        <a class="c-card" href="mailto:{EMAIL}?subject=Enquiry">{ICONS["mail"]}<span class="c-label">Email</span><span class="c-value">{EMAIL.replace("@", "<wbr>@")}</span></a>
        <div class="c-card">{ICONS["pin"]}<span class="c-label">Postal address</span><span class="c-value">{POSTAL}</span></div>
        <a class="c-card" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["user"]}<span class="c-label">Tax &amp; Legal</span><span class="c-value">{CONTACT_NAME}</span><span class="c-sub">{CONTACT_ROLE} · {WHATSAPP_DISPLAY} · WhatsApp</span></a>
      </div>
      <div class="btn-row">
        <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Enquiry">{ICONS["mail"]}Email the firm</a>
        <a class="btn btn-outline" href="tel:{PHONE_TEL}">{ICONS["phone"]}Call {PHONE}</a>
      </div>"""
    side = panel("Our services", service_links())
    page("contact.html", "Contact us",
         f"Contact {FIRM} in Dar es Salaam: telephone, email and postal address.",
         two_col(main, side), active="contact")


if __name__ == "__main__":
    for old in ["tax-compliance.html", "tax-audits-and-disputes.html",
                "business-registration.html", "accounting-and-advisory.html"]:
        (ROOT / old).unlink(missing_ok=True)
    build_home()
    for s in SERVICES:
        build_service(s)
    for i in INDUSTRIES:
        build_industry(i)
    build_about()
    build_calendar()
    build_contact()
