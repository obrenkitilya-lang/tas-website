"""Builds the Danis Associates website.

Every page shares the same header and footer, so the pages are generated
from this one file. Edit the content below, then run:

    python3 tools/art.py      # only if you change the illustrations
    python3 tools/build.py

and commit the regenerated .html files in the repository root.

To use a real photograph for a page, save it in assets/img/ and change
that page's "image" value below (e.g. "assets/img/audit.jpg").
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
WA_LINK = f"https://wa.me/{WHATSAPP}?text=Hello%20Danis%20Associates%2C%20I%20would%20like%20to%20discuss%3A%20"

# ------------------------------------------------------------------ content
# "deliver": cards under "What we deliver" — (anchor, title, text, [bullets])
# "approach": four steps — (title, text)
SERVICES = [
    {
        "file": "audit-and-assurance.html", "name": "Audit &amp; Assurance", "image": "assets/img/audit.svg",
        "tags": "Statutory · Donor · Internal · Special purpose",
        "summary": "Independent audits for companies, NGOs, donor-funded projects, financial institutions and public entities, performed in accordance with International Standards on Auditing.",
        "detail": "Reliable, independently verified financial information gives shareholders, boards, lenders, donors and regulators the confidence to make decisions. Our risk-based approach focuses audit effort where it matters most, and our findings help management strengthen controls.",
        "card": "Statutory, donor and project, internal and special purpose audits.",
        "deliver": [
            ("statutory-audit", "Statutory Audit",
             "Audits of financial statements in accordance with ISAs and the Companies Act, giving an independent opinion on whether they present a true and fair view under IFRS or IFRS for SMEs.",
             ["Risk assessment and audit planning", "Evaluation of internal controls", "Audit report and management letter"]),
            ("donor-and-project-audits", "Donor &amp; Project Audits",
             "Audits of NGOs, projects and grants to the reporting requirements and terms of reference of development partners.",
             ["Project and grant audits", "Expenditure verification", "Compliance with grant conditions"]),
            ("internal-audit", "Internal Audit",
             "Outsourced and co-sourced internal audit that evaluates risk management, internal controls and governance, with practical recommendations for the board and audit committee.",
             []),
            ("special-audits-and-investigations", "Special Audits &amp; Investigations",
             "Special purpose audits, agreed-upon procedures and forensic investigations into suspected fraud or irregularities, with clear written reports of findings.",
             []),
        ],
        "approach": [
            ("Understand &amp; plan", "We learn the organisation, its systems and key risks, and agree the audit plan and timetable with management."),
            ("Test &amp; evaluate", "We evaluate controls and test balances, transactions and disclosures, raising issues as they arise."),
            ("Review &amp; report", "Senior review of the work and conclusions, followed by the audit report on the financial statements."),
            ("Management letter", "Findings on control weaknesses with prioritised recommendations, discussed with management."),
        ],
    },
    {
        "file": "tax.html", "name": "Tax", "image": "assets/img/tax.svg",
        "tags": "Compliance · Advisory · TRA disputes",
        "summary": "Tax compliance, advisory and dispute support across corporate income tax, VAT, PAYE, SDL and withholding tax, including representation in TRA audits and examinations.",
        "detail": "Tanzania's tax rules are complex and change every year. We help organisations file accurately and on time, understand the tax consequences of decisions before they make them, and defend their position when TRA raises questions.",
        "card": "Compliance, tax advisory, and TRA audits, examinations and disputes.",
        "deliver": [
            ("tax-compliance", "Tax Compliance",
             "Preparation and filing of returns, accurately and on time, with proper supporting records.",
             ["TIN and VAT registration", "Income tax, provisional and final returns", "PAYE, SDL, withholding tax and VAT returns", "EFD/VFD and tax clearance certificates"]),
            ("tax-advisory", "Tax Advisory",
             "Advice on the tax implications of investments, contracts, restructuring and cross-border transactions, and tax health checks that find exposures before TRA does.",
             []),
            ("tax-audits-and-disputes", "TRA Audits, Examinations &amp; Disputes",
             "Structured support from TRA's first findings to resolution: reconciliation of TRA's computations, written responses within the prescribed timelines, representation at meetings, and objections where assessments are incorrect.",
             []),
        ],
        "approach": [
            ("Diagnose", "A review of every tax obligation to identify gaps and exposures before they become assessments."),
            ("Comply", "A filing calendar for monthly, quarterly and annual returns, managed so deadlines are not missed."),
            ("Advise", "Tax positions and transactions planned and documented so that they can be supported."),
            ("Defend", "Engagement with TRA through responses, meetings and objections where the facts warrant it."),
        ],
    },
    {
        "file": "advisory.html", "name": "Advisory", "image": "assets/img/advisory.svg",
        "tags": "Risk · Transactions · Capacity building",
        "summary": "Risk and governance, financial due diligence, valuations, feasibility studies and professional training for boards, management and finance teams.",
        "detail": "Our advisory work helps leaders make informed decisions, strengthen governance and controls, and build the capability of the people who run their finance function.",
        "card": "Risk and governance, due diligence and valuations, and training.",
        "deliver": [
            ("risk-and-governance", "Risk &amp; Governance",
             "Enterprise risk management frameworks, internal control design and reviews, governance reviews, and finance and procurement policies and procedures manuals.",
             []),
            ("due-diligence-and-valuations", "Due Diligence, Valuations &amp; Feasibility",
             "Independent analysis before you buy, invest or lend.",
             ["Financial and tax due diligence", "Business and share valuations", "Feasibility studies and business plans"]),
            ("training", "Training &amp; Capacity Building",
             "Practical in-house training for finance teams, management and boards on IFRS, Tanzanian tax updates, internal controls and financial management for non-finance managers.",
             []),
        ],
        "approach": [
            ("Understand", "We agree the questions to be answered, the scope and the decision the work will support."),
            ("Analyse", "We gather and test the information, and identify the issues that matter."),
            ("Recommend", "Clear findings and practical recommendations, presented to management and the board."),
            ("Implement", "Support to put recommendations into practice, and follow-up where agreed."),
        ],
    },
    {
        "file": "outsourcing.html", "name": "Outsourcing", "image": "assets/img/outsourcing.svg",
        "tags": "Accounting · Payroll · Company secretarial",
        "summary": "Accounting, payroll and company secretarial services for growing businesses, NGOs and branches of foreign companies.",
        "detail": "Outsourcing routine finance and statutory work lets management focus on running the organisation, while qualified professionals keep the records, payroll and filings accurate and on time.",
        "card": "Accounting and reporting, payroll, and company secretarial.",
        "deliver": [
            ("accounting", "Accounting &amp; Financial Reporting",
             "Bookkeeping, bank reconciliations, monthly management accounts, and annual financial statements under IFRS, IFRS for SMEs or IPSAS, ready for audit.",
             []),
            ("payroll", "Payroll",
             "Confidential payroll processing, payslips and reports, with PAYE, SDL, NSSF and WCF computed and filed on time.",
             []),
            ("company-secretarial", "Company Secretarial &amp; Registration",
             "Setting up and maintaining companies with BRELA.",
             ["Company and business name registration, TIN and licences", "Annual returns and statutory filings", "Changes of directors, shares and registered office", "Board and shareholder minutes and resolutions"]),
        ],
        "approach": [
            ("Onboard", "Chart of accounts, opening balances, payroll data and statutory calendar set up."),
            ("Monthly close", "Bookkeeping, reconciliations, payroll and statutory remittances, with a management accounts pack."),
            ("Quarterly review", "Results reviewed with management, and the compliance calendar checked."),
            ("Year end", "Financial statements ready for audit, statutory filings and tax returns."),
        ],
    },
]

INDUSTRIES = [
    {
        "file": "ngos-and-donor-funded-projects.html", "name": "NGOs &amp; Donor-Funded Projects", "image": "assets/img/ngos.svg",
        "tags": "Non-profits · Development partners · Grants",
        "summary": "Audit, financial management and compliance support for organisations accountable to donors, regulators and the communities they serve.",
        "card": "Audits and financial management for non-profits and projects.",
        "help": [
            ("Audits", "Annual NGO audits, and project and grant audits to donor terms of reference, including expenditure verification."),
            ("Financial management", "Internal control reviews and policies and procedures manuals for finance, procurement and grants."),
            ("Outsourcing", "Accounting, payroll and employment tax compliance for organisations without a large finance team."),
            ("Capacity building", "Training for finance and programme staff on donor reporting and financial management."),
        ],
        "related": [("audit-and-assurance.html#donor-and-project-audits", "Donor &amp; Project Audits"),
                    ("advisory.html#risk-and-governance", "Risk &amp; Governance"),
                    ("outsourcing.html#accounting", "Accounting")],
    },
    {
        "file": "financial-services.html", "name": "Financial Services", "image": "assets/img/financial.svg",
        "tags": "SACCOs · Microfinance · Insurance",
        "summary": "Assurance and advisory for SACCOs, microfinance institutions, insurers and other financial institutions operating under close regulatory oversight.",
        "card": "Assurance and advisory for SACCOs, microfinance and insurers.",
        "help": [
            ("Audit", "Statutory audits and audits required by the relevant regulator."),
            ("Internal audit", "Reviews of credit, loan portfolio and operational controls."),
            ("Risk &amp; governance", "Risk management frameworks and board governance reviews."),
            ("Reporting &amp; tax", "IFRS reporting support, tax compliance and training for boards and staff."),
        ],
        "related": [("audit-and-assurance.html#statutory-audit", "Statutory Audit"),
                    ("audit-and-assurance.html#internal-audit", "Internal Audit"),
                    ("advisory.html#risk-and-governance", "Risk &amp; Governance")],
    },
    {
        "file": "trade-and-manufacturing.html", "name": "Trade &amp; Manufacturing", "image": "assets/img/trade.svg",
        "tags": "Manufacturing · Distribution · Retail · Logistics",
        "summary": "Audit, tax and advisory for businesses managing inventory, high transaction volumes, VAT exposure and pressure on working capital.",
        "card": "Audit, tax and advisory for manufacturers and traders.",
        "help": [
            ("Audit", "Statutory audits with a focus on inventory, costing and revenue."),
            ("Tax", "VAT compliance and refund claims, tax health checks and TRA examination support."),
            ("Controls", "Internal controls over purchasing, inventory and sales."),
            ("Growth", "Due diligence, valuations and feasibility studies for expansion and investment."),
        ],
        "related": [("audit-and-assurance.html#statutory-audit", "Statutory Audit"),
                    ("tax.html#tax-compliance", "Tax Compliance"),
                    ("advisory.html#due-diligence-and-valuations", "Due Diligence")],
    },
    {
        "file": "public-sector.html", "name": "Public Sector", "image": "assets/img/public.svg",
        "tags": "Agencies · Parastatals · Local government",
        "summary": "Support for government agencies, parastatals and local government authorities accountable for the use of public resources.",
        "card": "IPSAS reporting, internal audit and governance support.",
        "help": [
            ("Financial reporting", "Preparation and review of financial statements under IPSAS."),
            ("Internal audit", "Internal audit support and internal control reviews."),
            ("Special assignments", "Audits, reviews and special assignments where the firm is appointed."),
            ("Capacity building", "Training for finance, audit and management staff."),
        ],
        "related": [("audit-and-assurance.html#internal-audit", "Internal Audit"),
                    ("outsourcing.html#accounting", "Financial Reporting"),
                    ("advisory.html#training", "Training")],
    },
]

ICONS = {
    "down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6-6 6" transform="rotate(90 12 12)"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "send": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
}
ARROW = '<span class="arrow">&rarr;</span>'


def img(src, alt=""):
    return f'<div class="img"><img src="{src}" alt="{alt}" loading="lazy"></div>'


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
    industries = "".join(f'<li><a href="{i["file"]}">{i["name"]}</a></li>' for i in INDUSTRIES)
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="{FIRM}, home"><img src="assets/logo-maroon.png" alt="{FIRM}" width="123" height="48"></a>
    <ul class="menu" id="menu">
      <li{cls("about")}><a href="about.html">About</a></li>
      <li{cls("services", "has-mega")}><a href="services.html">Services{ICONS["down"]}</a><div class="dropdown mega">{mega}</div></li>
      <li{cls("industries")}><a href="industries.html">Industries{ICONS["down"]}</a><ul class="dropdown">{industries}</ul></li>
      <li{cls("insights")}><a href="compliance-calendar.html">Insights</a></li>
      <li{cls("contact")}><a href="contact.html">Contact</a></li>
    </ul>
    <div class="nav-tools">
      <a class="nav-link email" href="mailto:{EMAIL}">{ICONS["send"]}{EMAIL}</a>
      <a class="nav-link" href="tel:{PHONE_TEL}" aria-label="Call {PHONE}">{ICONS["phone"]}</a>
      <a class="btn-partner" href="contact.html"><span>Speak to<span class="long"> a</span> Partner</span> {ARROW}</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
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
        <img src="assets/logo-white.png" alt="{FIRM}" width="118" height="46">
        <p>{TAGLINE}.</p>
        <p>{POSTAL}<br><a href="tel:{PHONE_TEL}">{PHONE}</a> · {others}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Industries</h4><ul>{ind}</ul></div>
      <div><h4>The firm</h4><ul>
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


def cta(title="Ready to discuss your audit, tax or advisory needs?"):
    return f"""<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="cta">
      <div><h2>{title}</h2><p>Speak to a partner about your requirements. We respond to every enquiry.</p></div>
      <div class="btn-row">
        <a class="btn btn-gold" href="contact.html">Speak to a Partner {ARROW}</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ICONS["phone"]}{PHONE}</a>
      </div>
    </div>
  </div>
</section>"""


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


def service_cards(items):
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


# ------------------------------------------------------------------ pages

def build_home():
    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Audit · Tax · Advisory · Outsourcing</span>
      <h1>Assurance and advice <em>you can build on.</em></h1>
      <p class="lead">{FIRM} is a Tanzanian firm of Certified Public Accountants in public practice and tax consultants, serving companies, NGOs and donor-funded projects, financial institutions and public sector entities.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">Speak to a Partner {ARROW}</a>
        <a class="btn btn-outline" href="services.html">Explore our services</a>
      </div>
    </div>
    <div class="hero-media">
      {img("assets/img/hero.svg", "Dar es Salaam skyline")}
      <div class="hero-badge"><strong>Clear from day one</strong><span>Scope, deliverables and fees agreed in writing before work begins.</span></div>
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Services</span><h2>What we do</h2></div>
      <p>Four service lines delivered by qualified professionals with a practical understanding of Tanzania's regulatory environment.</p>
    </div>
    <div class="cards">{service_cards(SERVICES)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Industries</span><h2>Sectors we serve</h2></div>
      <p>Every sector has its own reporting, regulatory and governance requirements. We bring relevant experience to each engagement.</p>
    </div>
    <div class="cards">{service_cards(INDUSTRIES)}
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Why {FIRM}</span>
      <h2>Independent, qualified and committed to quality.</h2>
      <p>Every engagement is planned and performed in accordance with applicable professional standards and laws, and led by experienced professionals.</p>
      <p>Each engagement begins with a written proposal setting out the scope, deliverables, timeline and fee, followed by a signed engagement letter.</p>
      <a class="btn btn-outline" href="about.html" style="margin-top:14px">About the firm {ARROW}</a>
    </div>
    <ul class="facts">
      <li>{ICONS["check"]}<span>Certified Public Accountants in public practice<small>Audits performed in accordance with International Standards on Auditing</small></span></li>
      <li>{ICONS["check"]}<span>Tax consultants<small>Compliance, advisory and representation before the Tanzania Revenue Authority</small></span></li>
      <li>{ICONS["check"]}<span>Breadth of services<small>Audit, tax, advisory and outsourcing under one roof</small></span></li>
      <li>{ICONS["check"]}<span>Independent and confidential<small>Client information is used only for the engagement instructed</small></span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Insights</span><h2>Key TRA deadlines</h2></div>
      <p>Late filing and payment attract penalties and interest. These are the principal recurring deadlines for most businesses.</p>
    </div>
    {calendar_table()}
    <p class="note">General guidance only. <a href="compliance-calendar.html" style="color:var(--brand)">View the compliance calendar</a>.</p>
  </div>
</section>

{cta()}"""
    page("index.html", FIRM,
         f"{FIRM}: Certified Public Accountants in public practice and tax consultants in Tanzania, providing audit and assurance, tax, advisory and outsourcing services.",
         body)


def build_listing(filename, title, eyebrow, intro, items, active):
    body = f"""<section class="svc-hero" style="padding-bottom:40px">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1 class="serif" style="font-size:clamp(42px,5vw,64px);margin-bottom:20px">{title}</h1>
    <p class="summary" style="max-width:720px;font-size:19px">{intro}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><div class="cards">{service_cards(items)}</div></div>
</section>
{cta()}"""
    page(filename, title, intro, body, active=active)


def build_service(s):
    cards = ""
    for n, (a, title, text, bullets) in enumerate(s["deliver"]):
        tone = "maroon" if n % 4 in (0, 3) else "gold"
        ul = f'<ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul>' if bullets else ""
        cards += f'<div class="dcard {tone}" id="{a}"><h3>{title}</h3><p>{text}</p>{ul}</div>'
    steps = "".join(f"<div><h3>{t}</h3><p>{p}</p></div>" for t, p in s["approach"])
    others = "".join(f'<a class="chip" href="{x["file"]}">{x["name"]} {ARROW}</a>' for x in SERVICES if x is not s)
    body = detail_hero("services.html", "All services", s["tags"], s["name"], s["summary"], s["detail"], s["image"]) + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">What we deliver</span>
    <hr class="rule">
    <div class="deliver">{cards}</div>
    <div class="approach">
      <span class="eyebrow">Our approach</span>
      <div class="approach-grid">{steps}</div>
    </div>
    <div style="margin-top:48px"><span class="eyebrow">Other services</span><div class="related">{others}</div></div>
  </div>
</section>
{cta()}"""
    page(s["file"], s["name"], s["summary"], body, active="services")


def build_industry(i):
    cards = "".join(f'<div class="dcard {"maroon" if n % 4 in (0, 3) else "gold"}"><h3>{t}</h3><p>{p}</p></div>'
                    for n, (t, p) in enumerate(i["help"]))
    related = "".join(f'<a class="chip" href="{h}">{l} {ARROW}</a>' for h, l in i["related"])
    others = "".join(f'<a class="chip" href="{x["file"]}">{x["name"]}</a>' for x in INDUSTRIES if x is not i)
    body = detail_hero("industries.html", "All industries", i["tags"], i["name"], i["summary"], "", i["image"]) + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">How we help</span>
    <hr class="rule">
    <div class="deliver">{cards}</div>
    <div style="margin-top:48px"><span class="eyebrow">Related services</span><div class="related">{related}</div></div>
    <div style="margin-top:32px"><span class="eyebrow">Other industries</span><div class="related">{others}</div></div>
  </div>
</section>
{cta()}"""
    page(i["file"], i["name"], i["summary"], body, active="industries")


def build_about():
    values = [("Independence &amp; integrity", "We act objectively, apply professional scepticism and report what we find."),
              ("Quality", "Every engagement is planned, performed and reviewed in accordance with professional standards."),
              ("Clarity", "Scope, deliverables, timelines and fees agreed in writing; findings explained plainly, in English or Kiswahili."),
              ("Confidentiality", "Client information is used only for the engagement we have been instructed on.")]
    cards = "".join(f'<div class="dcard {"maroon" if n % 4 in (0, 3) else "gold"}"><h3>{t}</h3><p>{p}</p></div>'
                    for n, (t, p) in enumerate(values))
    steps = "".join(f"<div><h3>{t}</h3><p>{p}</p></div>" for t, p in [
        ("Initial meeting", "We discuss your requirements and review the relevant information."),
        ("Proposal", "A written proposal with scope, deliverables, timeline and fee, then a signed engagement letter."),
        ("Execution", "Our team performs the work and keeps management informed throughout."),
        ("Reporting", "Reports and recommendations delivered and, where relevant, follow-up agreed."),
    ])
    body = detail_hero("index.html", "Home", "About the firm", "About us",
                       f"{FIRM} is a firm of Certified Public Accountants in public practice and tax consultants based in Dar es Salaam.",
                       "We provide audit and assurance, tax, advisory and outsourcing services to owner-managed businesses, growing and established companies, NGOs and donor-funded projects, financial institutions and public sector entities across Tanzania.",
                       "assets/img/hero.svg") + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">Our values</span>
    <hr class="rule">
    <div class="deliver">{cards}</div>
    <div class="approach" id="approach">
      <span class="eyebrow">How we work</span>
      <div class="approach-grid">{steps}</div>
    </div>
  </div>
</section>
{cta()}"""
    page("about.html", "About us",
         f"About {FIRM}, Certified Public Accountants in public practice and tax consultants in Dar es Salaam.",
         body, active="about")


def build_calendar():
    body = f"""<section class="svc-hero" style="padding-bottom:40px">
  <div class="wrap">
    <a class="back" href="index.html">&larr; Home</a>
    <span class="eyebrow">Insights · Compliance</span>
    <h1>Compliance calendar</h1>
    <p class="summary" style="max-width:760px">Missing a filing or payment deadline attracts penalties and interest from the day after the due date. These are the principal recurring obligations for most businesses in Tanzania.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {calendar_table()}
    <p class="note">If a due date falls on a weekend or public holiday, confirm the applicable date with TRA or your adviser.</p>
    <div class="longform">
      <h2>Other recurring obligations</h2>
      <h3>Audited financial statements</h3>
      <p>Organisations required to have an audit should plan it early enough to meet their filing and reporting deadlines.</p>
      <h3>BRELA annual returns</h3>
      <p>Companies must file annual returns with BRELA each year; the due date depends on the date of incorporation.</p>
      <h3>Business licences</h3>
      <p>Business licences must be renewed before they expire.</p>
      <p class="note">General guidance only. <a href="contact.html">Contact us</a> for advice on your position.</p>
    </div>
  </div>
</section>
{cta()}"""
    page("compliance-calendar.html", "Compliance calendar",
         "Key Tanzania Revenue Authority filing and payment deadlines and other recurring compliance obligations.",
         body, active="insights")


def build_contact():
    others = " · ".join(d for d, _ in PHONES_OTHER)
    body = f"""<section class="svc-hero">
  <div class="wrap">
    <a class="back" href="index.html">&larr; Home</a>
    <div class="svc-hero-grid" style="align-items:start">
      <div>
        <span class="eyebrow">Contact</span>
        <h1>Speak to a Partner</h1>
        <p class="summary">Tell us about your audit, tax, advisory or outsourcing requirements and we will arrange an initial meeting.</p>
        <div class="btn-row" style="margin-top:28px">
          <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Enquiry">{ICONS["mail"]}Email the firm</a>
          <a class="btn btn-outline" href="tel:{PHONE_TEL}">{ICONS["phone"]}Call {PHONE}</a>
        </div>
      </div>
      <div class="contact-grid">
        <a class="c-card" href="tel:{PHONE_TEL}">{ICONS["phone"]}<span class="c-label">Telephone</span><span class="c-value">{PHONE}</span><span class="c-sub">{others}</span></a>
        <a class="c-card" href="mailto:{EMAIL}?subject=Enquiry">{ICONS["mail"]}<span class="c-label">Email</span><span class="c-value">{EMAIL.replace("@", "<wbr>@")}</span></a>
        <div class="c-card">{ICONS["pin"]}<span class="c-label">Postal address</span><span class="c-value">{POSTAL}</span></div>
        <a class="c-card" href="{WA_LINK}" target="_blank" rel="noopener">{ICONS["user"]}<span class="c-label">Tax &amp; Legal</span><span class="c-value">{CONTACT_NAME}</span><span class="c-sub">{CONTACT_ROLE} · {WHATSAPP_DISPLAY} · WhatsApp</span></a>
      </div>
    </div>
  </div>
</section>"""
    page("contact.html", "Contact us",
         f"Contact {FIRM} in Dar es Salaam: telephone, email and postal address.",
         body, active="contact")


if __name__ == "__main__":
    build_home()
    build_listing("services.html", "Our services", "Services",
                  "Audit and assurance, tax, advisory and outsourcing services for organisations across Tanzania.",
                  SERVICES, "services")
    build_listing("industries.html", "Industries", "Sectors we serve",
                  "Experience across the sectors that drive Tanzania's economy, and the reporting and regulatory requirements that come with them.",
                  INDUSTRIES, "industries")
    for s in SERVICES:
        build_service(s)
    for i in INDUSTRIES:
        build_industry(i)
    build_about()
    build_calendar()
    build_contact()
