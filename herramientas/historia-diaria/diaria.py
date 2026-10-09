# Historia diaria de Luma: "buen <día de la semana>" + lámpara dibujada + frase corta.
# Sin lámpara de texto, sin "lámparas 3D". Solo un "luma" chiquito arriba.
# Uso: python3 diaria.py <salida.png> [AAAA-MM-DD]
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stickers import *

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
FRASES = {
    "lunes": "arrancá la semana con luz.",
    "martes": "un poquito de luz para tu rincón.",
    "miércoles": "a mitad de semana, un rato lindo.",
    "jueves": "casi viernes, ya se nota.",
    "viernes": "que tengas un finde con buena luz.",
    "sábado": "tomate el día con calma.",
    "domingo": "un domingo tranquilo y de luz.",
}
def place(fn, x, y, scale, rot=0):
    inner, W, H = fn()
    fid = uid('f')
    g = (f'<defs>{cutfilter(fid, W, H)}</defs><g transform="translate({x},{y}) rotate({rot},{W*scale/2:.1f},{H*scale/2:.1f}) scale({scale})">'
         f'<g filter="url(#{fid})">{inner}</g></g>')
    return g, W*scale, H*scale

def tline(txt, size, x, base, fill, tracking=0.0, anchor='l', maxw=None):
    tp, tw = text_path(txt, size, tracking)
    if maxw and tw > maxw:
        size = size * maxw / tw; tp, tw = text_path(txt, size, tracking)
    xx = x if anchor == 'l' else (x - tw/2 if anchor == 'c' else x - tw)
    return f'<path transform="translate({xx:.1f},{base})" d="{tp}" fill="{fill}"/>', tw

def burst(text, size):
    R1, R2, n = 212, 176, 18; cx = cy = R1 + 20
    pts = []
    for i in range(n*2):
        r = R1 if i % 2 == 0 else R2; a = math.pi*i/n - math.pi/2
        pts.append(f'{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}')
    tp, tw = text_path(text, size, 0.0)
    return (f'<polygon points="{" ".join(pts)}" fill="{K}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
            f'<path transform="translate({cx - tw/2:.1f},{cy + size*0.72/2:.1f})" d="{tp}" fill="{Y}"/>'), 2*(R1+20), 2*(R1+20)

def lines_bg(color, op, step=14, h=3):
    return "".join(f'<rect x="0" y="{y}" width="1080" height="{h}" fill="{color}" opacity="{op}"/>' for y in range(0, 1920, step))


def historia(fecha):
    dia = DIAS[fecha.weekday()]
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920">'
         f'<rect width="1080" height="1920" fill="{Y}"/>{lines_bg(K, .05)}')
    t, _ = tline("luma", 34, 90, 150, K, 0.0, maxw=200); s += t
    t, _ = tline("buen " + dia, 150, 80, 760, K, -0.03, maxw=920); s += t
    g, w, hh = place(s_lampara, 330, 960, 0.62, -4); s += g
    g, w, hh = place(s_estrella, 790, 980, 0.40, 12); s += g
    t, _ = tline(FRASES[dia], 60, 90, 1560, K, 0.0, maxw=900); s += t
    return s + '</svg>'

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "diaria.png"
    fecha = datetime.date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else datetime.date.today()
    svg = os.path.splitext(out)[0] + ".svg"
    open(svg, "w").write(historia(fecha))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto('file://' + os.path.abspath(svg)); pg.wait_for_timeout(300)
        pg.screenshot(path=out)
        b.close()
    print("ok", out)
