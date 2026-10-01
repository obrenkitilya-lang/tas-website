"""Generates the brand illustrations in assets/img/.

These are placeholders in the firm's colours. To use a real photograph
instead, save it in assets/img/ and change the "image" value for that
page in tools/build.py (e.g. "assets/img/audit.jpg").
"""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "img"

THEMES = {
    "maroon": dict(sky=("#8c0909", "#3d0202"), far="#5a0303", near="#2a0101", accent="#d6a447", light="#f3e3c3"),
    "gold":   dict(sky=("#f3e3c3", "#d6a447"), far="#a2650f", near="#5a0303", accent="#7e0505", light="#fff7e8"),
    "dark":   dict(sky=("#3a3232", "#1f1b1b"), far="#4a3d3a", near="#120f0f", accent="#d6a447", light="#f3e3c3"),
    "cream":  dict(sky=("#faf7f2", "#ecdcc0"), far="#c9a77a", near="#7e0505", accent="#d6a447", light="#ffffff"),
}
W, H = 800, 600


def frame(theme, inner):
    t = THEMES[theme]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" role="img">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t['sky'][0]}"/><stop offset="1" stop-color="{t['sky'][1]}"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
{inner}
</svg>
"""


def windows(x, y, w, h, color, rng, density=.55, op=.55):
    out = []
    for yy in range(int(y) + 14, int(y + h) - 10, 18):
        for xx in range(int(x) + 8, int(x + w) - 10, 14):
            if rng.random() < density:
                out.append(f'<rect x="{xx}" y="{yy}" width="6" height="9" fill="{color}" opacity="{op}"/>')
    return "".join(out)


def skyline(theme, seed=3):
    t, rng = THEMES[theme], random.Random(seed)
    parts = [f'<circle cx="590" cy="190" r="70" fill="{t["accent"]}" opacity=".9"/>']
    x = -20
    while x < W:  # far row
        w = rng.randint(50, 90); h = rng.randint(140, 300)
        parts.append(f'<rect x="{x}" y="{460-h}" width="{w}" height="{h}" fill="{t["far"]}"/>')
        x += w + rng.randint(4, 14)
    x = -10
    while x < W:  # near row with windows
        w = rng.randint(60, 120); h = rng.randint(90, 330)
        parts.append(f'<rect x="{x}" y="{470-h}" width="{w}" height="{h}" fill="{t["near"]}"/>')
        parts.append(windows(x, 470 - h, w, h, t["accent"], rng, .45, .5))
        x += w + rng.randint(10, 30)
    parts.append(f'<rect y="470" width="{W}" height="130" fill="{t["near"]}"/>')
    for i in range(6):  # water shimmer
        y = 492 + i * 17
        parts.append(f'<rect x="{rng.randint(40, 500)}" y="{y}" width="{rng.randint(60, 240)}" height="3" fill="{t["accent"]}" opacity=".35"/>')
    return frame(theme, "".join(parts))


def documents(theme):
    t = THEMES[theme]
    parts = [f'<circle cx="650" cy="110" r="150" fill="{t["light"]}" opacity=".12"/>']
    for i, (dx, dy, rot) in enumerate([(-40, 30, -10), (10, 0, -3), (60, -20, 6)]):
        g = [f'<rect x="250" y="120" width="300" height="380" rx="8" fill="{t["light"]}" stroke="{t["near"]}" stroke-opacity=".15"/>']
        for k in range(9):
            w = 220 if k % 3 else 150
            g.append(f'<rect x="290" y="{180 + k * 30}" width="{w}" height="8" rx="4" fill="{t["near"]}" opacity="{.18 if i < 2 else .3}"/>')
        parts.append(f'<g transform="translate({dx},{dy}) rotate({rot} 400 310)">{"".join(g)}</g>')
    parts.append(f'<circle cx="560" cy="420" r="58" fill="{t["accent"]}"/><circle cx="560" cy="420" r="44" fill="none" stroke="{t["light"]}" stroke-width="3" stroke-dasharray="6 6"/>')
    parts.append(f'<path d="m538 420 16 16 30-34" fill="none" stroke="{t["light"]}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append(f'<g transform="rotate(38 200 470)"><rect x="120" y="455" width="190" height="22" rx="11" fill="{t["near"]}"/><path d="M310 455 l34 11 -34 11z" fill="{t["accent"]}"/></g>')
    return frame(theme, "".join(parts))


def chart(theme):
    t = THEMES[theme]
    parts = []
    for y in range(140, 520, 60):
        parts.append(f'<rect x="90" y="{y}" width="620" height="1.5" fill="{t["light"]}" opacity=".15"/>')
    heights = [90, 130, 120, 180, 230, 290]
    for i, h in enumerate(heights):
        x = 120 + i * 98
        parts.append(f'<rect x="{x}" y="{500-h}" width="56" height="{h}" rx="4" fill="{t["light"] if i < 5 else t["accent"]}" opacity="{.22 if i < 5 else 1}"/>')
    pts = [(148, 360), (246, 330), (344, 340), (442, 270), (540, 220), (638, 150)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    parts.append(f'<path d="{d}" fill="none" stroke="{t["light"]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    for x, y in pts:
        parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{t["light"]}"/><circle cx="{x}" cy="{y}" r="4" fill="{t["near"]}"/>')
    parts.append(f'<path d="M638 150 l-34 4 m34 -4 l-8 33" stroke="{t["light"]}" stroke-width="5" stroke-linecap="round"/>')
    parts.append(f'<rect x="90" y="500" width="620" height="3" fill="{t["light"]}" opacity=".5"/>')
    return frame(theme, "".join(parts))


def facade(theme, seed=7):
    t, rng = THEMES[theme], random.Random(seed)
    parts = [f'<polygon points="140,600 220,40 660,0 700,600" fill="{t["near"]}"/>']
    rows, cols = 14, 9
    for r in range(rows):
        for c in range(cols):
            fx0 = c / cols; fx1 = (c + .8) / cols
            fy = r / rows; fy1 = (r + .72) / rows
            def pt(fx, fy):
                top_l, top_r, bot_l, bot_r = (220, 40), (660, 0), (140, 600), (700, 600)
                lx = top_l[0] + (bot_l[0] - top_l[0]) * fy; ly = top_l[1] + (bot_l[1] - top_l[1]) * fy
                rx = top_r[0] + (bot_r[0] - top_r[0]) * fy; ry = top_r[1] + (bot_r[1] - top_r[1]) * fy
                return lx + (rx - lx) * fx, ly + (ry - ly) * fx
            p = [pt(fx0, fy), pt(fx1, fy), pt(fx1, fy1), pt(fx0, fy1)]
            lit = rng.random() < .35
            parts.append(f'<polygon points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in p)}" fill="{t["accent"] if lit else t["far"]}" opacity="{.85 if lit else .55}"/>')
    parts.append(f'<circle cx="90" cy="120" r="60" fill="{t["accent"]}" opacity=".85"/>')
    return frame(theme, "".join(parts))


def network(theme, seed=11):
    t, rng = THEMES[theme], random.Random(seed)
    nodes = [(rng.randint(80, 720), rng.randint(80, 520)) for _ in range(16)]
    nodes += [(400, 300)]
    parts = []
    for i, (x, y) in enumerate(nodes):
        for (x2, y2) in nodes[i + 1:]:
            if (x - x2) ** 2 + (y - y2) ** 2 < 210 ** 2:
                parts.append(f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{t["light"]}" stroke-opacity=".25" stroke-width="2"/>')
    for i, (x, y) in enumerate(nodes):
        r = 46 if i == len(nodes) - 1 else rng.choice([14, 18, 24, 30])
        fill = t["accent"] if i == len(nodes) - 1 or i % 4 == 0 else t["light"]
        parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" opacity="{1 if fill == t["accent"] else .85}"/>')
        parts.append(f'<circle cx="{x}" cy="{y - r * .25:.0f}" r="{r * .3:.0f}" fill="{t["near"]}" opacity=".7"/><path d="M{x - r * .5:.0f} {y + r * .5:.0f} q{r * .5:.0f} {-r * .7:.0f} {r:.0f} 0" fill="{t["near"]}" opacity=".7"/>')
    return frame(theme, "".join(parts))


def columns(theme):
    t = THEMES[theme]
    parts = [f'<circle cx="640" cy="120" r="70" fill="{t["accent"]}" opacity=".9"/>',
             f'<polygon points="130,230 400,110 670,230" fill="{t["near"]}"/>',
             f'<polygon points="200,214 400,140 600,214" fill="{t["far"]}" opacity=".6"/>',
             f'<rect x="120" y="230" width="560" height="30" fill="{t["near"]}"/>']
    for i in range(6):
        x = 160 + i * 92
        parts.append(f'<rect x="{x}" y="268" width="40" height="232" fill="{t["light"]}" opacity=".92"/>')
        parts.append(f'<rect x="{x - 8}" y="260" width="56" height="12" fill="{t["light"]}"/>')
        for k in range(3):
            parts.append(f'<rect x="{x + 8 + k * 10}" y="280" width="3" height="210" fill="{t["near"]}" opacity=".12"/>')
    parts += [f'<rect x="100" y="500" width="600" height="24" fill="{t["near"]}"/>',
              f'<rect x="70" y="524" width="660" height="24" fill="{t["near"]}" opacity=".85"/>',
              f'<rect y="548" width="{W}" height="52" fill="{t["near"]}" opacity=".7"/>']
    return frame(theme, "".join(parts))


def factory(theme):
    t = THEMES[theme]
    parts = [f'<circle cx="160" cy="140" r="60" fill="{t["accent"]}" opacity=".9"/>',
             f'<rect x="560" y="120" width="44" height="260" fill="{t["far"]}"/>',
             f'<rect x="630" y="170" width="36" height="210" fill="{t["far"]}"/>']
    for i, x in enumerate(range(80, 720, 128)):
        parts.append(f'<polygon points="{x},380 {x},270 {x + 128},330 {x + 128},380" fill="{t["near"]}"/>')
        parts.append(f'<polygon points="{x + 6},300 {x + 6},282 {x + 60},310 {x + 60},328" fill="{t["accent"]}" opacity=".6"/>')
    parts.append(f'<rect x="80" y="378" width="640" height="130" fill="{t["near"]}"/>')
    for i in range(5):
        parts.append(f'<rect x="{110 + i * 120}" y="410" width="80" height="60" fill="{t["accent"]}" opacity=".55"/>')
    cols = [t["accent"], t["far"], t["light"]]
    for i in range(6):
        parts.append(f'<rect x="{60 + i * 118}" y="520" width="108" height="46" fill="{cols[i % 3]}" opacity=".9"/>')
        for k in range(5):
            parts.append(f'<rect x="{68 + i * 118 + k * 20}" y="526" width="4" height="34" fill="{t["near"]}" opacity=".25"/>')
    return frame(theme, "".join(parts))


def dome(theme):
    t = THEMES[theme]
    parts = [f'<rect x="398" y="60" width="4" height="70" fill="{t["near"]}"/>',
             f'<rect x="402" y="62" width="46" height="28" fill="{t["accent"]}"/>',
             f'<path d="M290 260 a110 120 0 0 1 220 0z" fill="{t["near"]}"/>',
             f'<rect x="300" y="250" width="200" height="30" fill="{t["far"]}"/>',
             f'<rect x="90" y="300" width="620" height="200" fill="{t["near"]}"/>',
             f'<polygon points="300,300 400,240 500,300" fill="{t["far"]}"/>',
             f'<rect x="80" y="280" width="640" height="22" fill="{t["far"]}"/>']
    for i in range(8):
        x = 128 + i * 76
        parts.append(f'<rect x="{x}" y="320" width="22" height="150" fill="{t["light"]}" opacity=".85"/>')
        parts.append(f'<rect x="{x + 30}" y="340" width="30" height="50" rx="15" fill="{t["accent"]}" opacity=".5"/>')
    for k in range(4):
        parts.append(f'<rect x="{60 - k * 20}" y="{500 + k * 22}" width="{680 + k * 40}" height="22" fill="{t["near"]}" opacity="{.9 - k * .15}"/>')
    parts.append(f'<circle cx="640" cy="150" r="50" fill="{t["accent"]}" opacity=".5"/>')
    return frame(theme, "".join(parts))


ART = {
    "hero.svg": lambda: skyline("maroon", 5),
    "audit.svg": lambda: skyline("dark", 9),
    "tax.svg": lambda: documents("gold"),
    "advisory.svg": lambda: chart("maroon"),
    "outsourcing.svg": lambda: facade("cream"),
    "ngos.svg": lambda: network("maroon"),
    "financial.svg": lambda: columns("cream"),
    "trade.svg": lambda: factory("gold"),
    "public.svg": lambda: dome("dark"),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in ART.items():
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)
