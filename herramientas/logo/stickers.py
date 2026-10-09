import os, sys, math
sys.path.insert(0, '.')
from geom import wordmark_path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

Y = "#FFD60A"; Y2 = "#FFE55C"; K = "#0B0B0B"; WH = "#FFFFFF"
FONT = '../fonts/bric800.ttf'
_f = TTFont(FONT); _gs = _f.getGlyphSet(); _cmap = _f.getBestCmap(); _upm = _f['head'].unitsPerEm


def text_path(txt, size, tracking_em=0.0):
    sc = size / _upm; x = 0; segs = []
    for ch in txt:
        gn = _cmap[ord(ch)]; pen = SVGPathPen(_gs)
        _gs[gn].draw(TransformPen(pen, (sc, 0, 0, -sc, x, 0))); segs.append(pen.getCommands())
        x += _gs[gn].width * sc + tracking_em * size
    return " ".join(segs), x - tracking_em * size


_id = [0]
def uid(p='c'):
    _id[0] += 1
    return f'{p}{_id[0]}'


X0, X1, Y0, Y1 = 124, 3297, 137, 764.5


def wm(x, y, w, fill, stroke=None, sw=0, layers_bg=None):
    """wordmark with left-top at (x,y), width w. returns (svg, height)"""
    k = w / (X1 - X0); h = (Y1 - Y0) * k
    paths = ""
    for p, dy in wordmark_path():
        st = f' stroke="{stroke}" stroke-width="{sw / k:.1f}" stroke-linejoin="round" paint-order="stroke"' if stroke else ''
        paths += f'<path d="{p}" transform="translate(0,{dy})" fill="{fill}" fill-rule="evenodd"{st}/>'
    g = f'<g transform="translate({x - X0 * k:.2f},{y - Y0 * k:.2f}) scale({k:.5f})">{paths}</g>'
    if layers_bg:
        cid = uid('cl')
        clip = "".join(f'<path d="{p}" transform="translate({x - X0 * k:.2f},{y - Y0 * k + k * dy:.2f}) scale({k:.5f})" fill-rule="evenodd"/>'
                       for p, dy in wordmark_path())
        n = 11; step = h / (n + 1); lines = ""
        for i in range(1, n + 1):
            lines += f'<rect x="{x}" y="{y + i * step - 1.6:.1f}" width="{w}" height="3.4" fill="{layers_bg}"/>'
        g += f'<clipPath id="{cid}">{clip}</clipPath><g clip-path="url(#{cid})" opacity=".42">{lines}</g>'
    return g, h


def pillow(x, y, w, h, r, fill, stroke=K, sw=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


# ---------------- stickers: each returns (svg_inner, W, H) ----------------
def s_badge_negro():
    W, H = 540, 200
    g, h = wm(60, (H - 80) / 2, 420, Y)
    return pillow(0, 0, W, H, 46, K, K, 0) + g, W, H


def s_letras_amarillo():
    W, H = 520, 150
    g, h = wm(40, 30, 440, Y, K, 16)
    return g, W, H + 10


def s_letras_blanco():
    W, H = 520, 150
    g, h = wm(40, 30, 440, WH, K, 16)
    return g, W, H + 10


def s_capas():
    W, H = 540, 200
    g, h = wm(60, (H - 80) / 2, 420, K, layers_bg=Y)
    return pillow(7, 7, W - 14, H - 14, 42, Y, K, 14) + g, W, H


def s_estrella():
    R = 190; c = 38; cx = cy = R + 14
    p = f'M{cx},{cy - R} Q{cx + c},{cy - c} {cx + R},{cy} Q{cx + c},{cy + c} {cx},{cy + R} Q{cx - c},{cy + c} {cx - R},{cy} Q{cx - c},{cy - c} {cx},{cy - R} Z'
    return f'<path d="{p}" fill="{Y}" stroke="{K}" stroke-width="22" stroke-linejoin="round"/>', 2 * (R + 14), 2 * (R + 14)


def s_estrella_negra():
    R = 190; c = 38; cx = cy = R + 14
    p = f'M{cx},{cy - R} Q{cx + c},{cy - c} {cx + R},{cy} Q{cx + c},{cy + c} {cx},{cy + R} Q{cx - c},{cy + c} {cx - R},{cy} Q{cx - c},{cy - c} {cx},{cy - R} Z'
    r2 = 78; c2 = 16
    q = f'M{cx},{cy - r2} Q{cx + c2},{cy - c2} {cx + r2},{cy} Q{cx + c2},{cy + c2} {cx},{cy + r2} Q{cx - c2},{cy + c2} {cx - r2},{cy} Q{cx - c2},{cy - c2} {cx},{cy - r2} Z'
    return (f'<path d="{p}" fill="{K}" stroke="{K}" stroke-width="22" stroke-linejoin="round"/>'
            f'<path d="{q}" fill="{Y}" stroke="{Y}" stroke-width="10" stroke-linejoin="round"/>'), 2 * (R + 14), 2 * (R + 14)


def s_lamparita():
    W, H = 400, 540
    ox, oy = 0, 52
    rays = ""
    for ang in (-150, -120, -90, -60, -30):
        a = math.radians(ang); x1 = 200 + 176 * math.cos(a); y1 = 190 + 176 * math.sin(a)
        x2 = 200 + 218 * math.cos(a); y2 = 190 + 218 * math.sin(a)
        rays += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{K}" stroke-width="16" stroke-linecap="round"/>'
    glass = 'M120,330 C120,300 50,262 50,190 A150,150 0 0 1 350,190 C350,262 280,300 280,330 Z'
    drop = 'M200,120 C214,152 240,172 240,206 A40,40 0 0 1 160,206 C160,172 186,152 200,120 Z'
    base = f'<rect x="128" y="332" width="144" height="108" rx="20" fill="{K}"/>'
    for yy in (362, 392, 422): base += f'<rect x="128" y="{yy}" width="144" height="7" fill="{Y}"/>'
    base += f'<rect x="162" y="440" width="76" height="40" rx="18" fill="{K}"/>'
    inner = (rays + f'<path d="{glass}" fill="{Y}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
             f'<path d="{drop}" fill="{K}"/>' + base)
    return f'<g transform="translate({ox},{oy})">{inner}</g>', W, H + 30


def s_gota():
    d = 'M180,20 C210,104 300,150 300,270 A120,120 0 0 1 60,270 C60,150 150,104 180,20 Z'
    return (f'<path d="{d}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>'
            f'<path d="M108,282 A72,72 0 0 0 152,346" fill="none" stroke="{WH}" stroke-width="18" stroke-linecap="round"/>'), 360, 420


def s_lampara():
    W, H = 470, 520
    cid = uid('cl')
    shade = 'M140,60 Q220,40 300,60 L392,240 Q220,276 48,240 Z'
    lines = "".join(f'<rect x="0" y="{y}" width="{W}" height="6" fill="{K}" opacity=".35"/>' for y in range(78, 260, 22))
    sp = 'M420,10 Q428,40 458,48 Q428,56 420,86 Q412,56 382,48 Q412,40 420,10 Z'
    return (f'<clipPath id="{cid}"><path d="{shade}"/></clipPath>'
            f'<rect x="196" y="250" width="48" height="190" fill="{K}"/>'
            f'<ellipse cx="220" cy="452" rx="100" ry="28" fill="{K}"/>'
            f'<path d="{shade}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>'
            f'<g clip-path="url(#{cid})">{lines}</g>'
            f'<path d="{sp}" fill="{K}" stroke="{K}" stroke-width="8" stroke-linejoin="round"/>'), W, H + 20


def s_extrusor():
    W, H = 420, 540
    bars = ""
    for i, (bw, yy) in enumerate(((320, 440), (276, 474), (232, 508))):
        bars += f'<rect x="{210 - bw / 2}" y="{yy - 14}" width="{bw}" height="28" rx="14" fill="{Y}" stroke="{K}" stroke-width="10"/>'
    drop = 'M210,274 C222,304 244,320 244,344 A34,34 0 0 1 176,344 C176,320 198,304 210,274 Z'
    return (f'<rect x="96" y="20" width="228" height="140" rx="30" fill="{K}"/>'
            f'<rect x="130" y="52" width="160" height="14" rx="7" fill="{Y}"/>'
            f'<rect x="130" y="84" width="110" height="14" rx="7" fill="{Y}"/>'
            f'<path d="M146,156 L274,156 L238,236 L182,236 Z" fill="{K}" stroke="{K}" stroke-width="12" stroke-linejoin="round"/>'
            f'<path d="{drop}" fill="{Y}" stroke="{K}" stroke-width="12" stroke-linejoin="round"/>' + bars), W, H + 20


def s_cubo():
    W, H = 420, 420
    top = '210,48 340,123 210,198 80,123'; left = '80,123 210,198 210,348 80,273'; right = '210,198 340,123 340,273 210,348'
    ls = ""
    for i in range(1, 5):
        ls += f'<line x1="80" y1="{123 + 30 * i}" x2="210" y2="{198 + 30 * i}" stroke="{K}" stroke-width="7" opacity=".55"/>'
        ls += f'<line x1="210" y1="{198 + 30 * i}" x2="340" y2="{123 + 30 * i}" stroke="{Y}" stroke-width="7" opacity=".6"/>'
    return (f'<polygon points="{left}" fill="{Y}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
            f'<polygon points="{right}" fill="{K}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
            f'<polygon points="{top}" fill="{Y2}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>' + ls), W, H


def s_circulo():
    W = H = 440
    g, h = wm(80, 150, 280, K)
    tp, tw = text_path("impresión 3D", 36, 0.08)
    return (f'<circle cx="220" cy="220" r="206" fill="{Y}" stroke="{K}" stroke-width="18"/>'
            f'<circle cx="220" cy="220" r="176" fill="none" stroke="{K}" stroke-width="5" stroke-dasharray="3 14" stroke-linecap="round"/>'
            + g + f'<path transform="translate({220 - tw / 2:.1f},282)" d="{tp}" fill="{K}"/>'), W, H


def s_pill_text(txt, bgc, fgc, size=92, border=None):
    tp, tw = text_path(txt, size, 0.0)
    W = tw + 120; H = size * 1.9
    base = size * 0.72
    stroke = f' stroke="{border}" stroke-width="14"' if border else ''
    return (f'<rect x="7" y="7" width="{W - 14}" height="{H - 14}" rx="{(H - 14) / 2}" fill="{bgc}"{stroke}/>'
            f'<path transform="translate(60,{H / 2 + base / 2 - 2:.1f})" d="{tp}" fill="{fgc}"/>'), W, H


def s_pill_capa():
    tp, tw = text_path("capa por capa", 92, 0.0)
    W = tw + 120; H = 92 * 1.9; cid = uid('cl')
    lines = "".join(f'<rect x="0" y="{y}" width="{W}" height="4" fill="{K}" opacity=".18"/>' for y in range(14, int(H), 20))
    return (f'<clipPath id="{cid}"><rect x="7" y="7" width="{W - 14}" height="{H - 14}" rx="{(H - 14) / 2}"/></clipPath>'
            f'<rect x="7" y="7" width="{W - 14}" height="{H - 14}" rx="{(H - 14) / 2}" fill="{Y}"/><g clip-path="url(#{cid})">{lines}</g>'
            f'<rect x="7" y="7" width="{W - 14}" height="{H - 14}" rx="{(H - 14) / 2}" fill="none" stroke="{K}" stroke-width="14"/>'
            f'<path transform="translate(60,{H / 2 + 92 * .72 / 2 - 2:.1f})" d="{tp}" fill="{K}"/>'), W, H


def s_pedilo():
    tp, tw = text_path("pedilo en la web", 80, 0.0)
    H = 168; W = tw + 120 + 140
    cx = W - 90
    arrow = (f'<circle cx="{cx}" cy="{H / 2}" r="52" fill="{Y}"/>'
             f'<path d="M{cx},{H / 2 - 24} L{cx},{H / 2 + 22} M{cx - 20},{H / 2 + 4} L{cx},{H / 2 + 24} L{cx + 20},{H / 2 + 4}" fill="none" stroke="{K}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<rect x="0" y="0" width="{W}" height="{H}" rx="{H / 2}" fill="{K}"/>'
            f'<path transform="translate(56,{H / 2 + 80 * .72 / 2 - 2:.1f})" d="{tp}" fill="{WH}"/>' + arrow), W, H


def s_nuevo():
    R1, R2, n = 212, 176, 18; cx = cy = R1 + 20
    pts = []
    for i in range(n * 2):
        r = R1 if i % 2 == 0 else R2; a = math.pi * i / n - math.pi / 2
        pts.append(f'{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}')
    tp, tw = text_path("nuevo", 92, 0.0)
    return (f'<polygon points="{" ".join(pts)}" fill="{Y}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
            f'<path transform="translate({cx - tw / 2:.1f},{cy + 92 * .72 / 2:.1f})" d="{tp}" fill="{K}"/>'), 2 * (R1 + 20), 2 * (R1 + 20)


def s_chispas():
    def star(cx, cy, R, c):
        return (f'<path d="M{cx},{cy - R} Q{cx + c},{cy - c} {cx + R},{cy} Q{cx + c},{cy + c} {cx},{cy + R} Q{cx - c},{cy + c} {cx - R},{cy} Q{cx - c},{cy - c} {cx},{cy - R} Z" '
                f'fill="{Y}" stroke="{K}" stroke-width="16" stroke-linejoin="round"/>')
    return star(190, 200, 140, 28) + star(350, 70, 62, 12) + star(88, 382, 50, 10), 420, 440


STICKERS = [
    ('luma-badge-negro', s_badge_negro), ('luma-letras-amarillo', s_letras_amarillo),
    ('luma-letras-blanco', s_letras_blanco), ('luma-capas', s_capas),
    ('estrella-luma', s_estrella), ('estrella-negra', s_estrella_negra),
    ('lamparita', s_lamparita), ('gota', s_gota),
    ('lampara', s_lampara), ('extrusor', s_extrusor),
    ('cubo-3d', s_cubo), ('sello-circular', s_circulo),
    ('prende-la-luz', lambda: s_pill_text("prendé la luz", K, Y)),
    ('capa-por-capa', s_pill_capa),
    ('pedilo-en-la-web', s_pedilo), ('nuevo', s_nuevo), ('chispas', s_chispas),
]


def cutfilter(fid, W, H, m=60):
    return (f'<filter id="{fid}" filterUnits="userSpaceOnUse" x="{-m}" y="{-m}" width="{W + 2 * m}" height="{H + 2 * m}" color-interpolation-filters="sRGB">'
            f'<feMorphology in="SourceAlpha" operator="dilate" radius="14" result="d"/>'
            f'<feGaussianBlur in="d" stdDeviation="5" result="b"/>'
            f'<feComponentTransfer in="b" result="s"><feFuncA type="linear" slope="6" intercept="-2.5"/></feComponentTransfer>'
            f'<feFlood flood-color="#fff" result="f"/><feComposite in="f" in2="s" operator="in" result="w"/>'
            f'<feMerge><feMergeNode in="w"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')


def sticker_svg(name, fn, with_bg=None):
    inner, W, H = fn()
    fid = uid('f'); m = 60
    body = f'<defs>{cutfilter(fid, W, H, m)}</defs><g filter="url(#{fid})">{inner}</g>'
    bg = f'<rect x="{-m}" y="{-m}" width="{W + 2 * m}" height="{H + 2 * m}" fill="{with_bg}"/>' if with_bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-m} {-m} {W + 2 * m} {H + 2 * m}" width="{W + 2 * m}" height="{H + 2 * m}">{bg}{body}</svg>', W, H


SPANS = {'prende-la-luz': 2, 'capa-por-capa': 2, 'pedilo-en-la-web': 2}


def sheet(cols=4, cell=500, margin=40, bg="#26262b"):
    # place stickers on a grid with column spans
    pos = []; r = 0; c = 0
    for name, fn in STICKERS:
        sp = SPANS.get(name, 1)
        if c + sp > cols: r += 1; c = 0
        pos.append((r, c, sp)); c += sp
        if c >= cols: r += 1; c = 0
    rows = max(p[0] for p in pos) + 1
    SW = cols * cell + 2 * margin; SH = rows * cell + 2 * margin
    out = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SW} {SH}" width="{SW}" height="{SH}"><rect width="{SW}" height="{SH}" fill="{bg}"/>'
    for i, (name, fn) in enumerate(STICKERS):
        inner, W, H = fn()
        fid = uid('f'); m = 60
        r, c, sp = pos[i]
        s = min((380 + (sp - 1) * cell) / W, 380 / H)
        cx = margin + c * cell + sp * cell / 2; cy = margin + r * cell + cell / 2
        out += (f'<defs>{cutfilter(fid, W, H, m)}</defs>'
                f'<g transform="translate({cx - W * s / 2:.1f},{cy - H * s / 2:.1f}) scale({s:.4f})"><g filter="url(#{fid})">{inner}</g></g>')
    out += '</svg>'
    return out, SW, SH


if __name__ == '__main__':
    os.makedirs('stk/svg', exist_ok=True)
    s, SW, SH = sheet()
    open('stk/hoja-de-stickers.svg', 'w').write(s)
    print('sheet', SW, SH)
    for name, fn in STICKERS:
        sv, W, H = sticker_svg(name, fn)
        open(f'stk/svg/{name}.svg', 'w').write(sv)
        print(name, W, H)
