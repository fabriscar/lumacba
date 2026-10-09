# Historias de la tarde (interacción) y de la noche (ambiente). Cambian por día.
# Uso: python3 tarde_noche.py tarde|noche <salida.png> [AAAA-MM-DD]
import sys, os, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from stickers import *
exec(open(os.path.join(HERE, 'helpers2.txt')).read())
Y = "#FFD60A"; K = "#0B0B0B"; WH = "#FFFFFF"; CR = "#FFF1B8"

def svg_open(bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920">'
            f'<defs><radialGradient id="glow"><stop offset="0" stop-color="{Y}" stop-opacity="0.55"/>'
            f'<stop offset="1" stop-color="{Y}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="1080" height="1920" fill="{bg}"/>')

def T(txt, size, x, y, fill, maxw=920):
    return tline(txt, size, x, y, fill, -0.03, maxw=maxw)[0]

# ---------- TARDE: preguntas para responder ----------
def t_cual(fecha):
    s = svg_open(Y) + lines_bg(K, .05)
    s += tline("luma", 34, 90, 150, K, 0.0, maxw=200)[0]
    s += T("¿cuál te llevás?", 130, 80, 560, K)
    x = 60
    for i, fn in enumerate([s_lampara, s_lamparita, s_gota, s_cubo]):
        g, w, h = place(fn, x, 800 + (i % 2) * 90, 0.36, [-4, 5, -3, 4][i]); s += g
        s += tline(str(i + 1), 90, x + 70, 1480, K, 0.0, maxw=120)[0]; x += 250
    s += tline("respondé con tu número", 62, 90, 1640, K, 0.0, maxw=900)[0]
    return s + '</svg>'

def t_color(fecha):
    s = svg_open(Y) + lines_bg(K, .05) + tline("luma", 34, 90, 150, K, 0.0, maxw=200)[0]
    s += T("¿de qué color?", 130, 80, 560, K)
    for i, (c, lbl) in enumerate([(K, "1"), (CR, "2"), ("#FFFFFF", "3")]):
        cx = 200 + i * 340
        s += f'<circle cx="{cx}" cy="950" r="130" fill="{c}" stroke="{WH}" stroke-width="16"/>'
        s += tline(lbl, 90, cx - 28, 1180, K, 0.0, maxw=120)[0]
    s += tline("respondé con tu número", 62, 90, 1640, K, 0.0, maxw=900)[0]
    return s + '</svg>'

def t_si_no(fecha):
    s = svg_open(Y) + lines_bg(K, .05) + tline("luma", 34, 90, 150, K, 0.0, maxw=200)[0]
    s += T("¿la querés?", 150, 80, 620, K)
    s += T("1 · sí", 110, 90, 900, K)
    s += T("2 · todavía no", 110, 90, 1060, K)
    s += tline("respondé con el número", 62, 90, 1640, K, 0.0, maxw=900)[0]
    return s + '</svg>'

def t_rincon(fecha):
    s = svg_open(Y) + lines_bg(K, .05) + tline("luma", 34, 90, 150, K, 0.0, maxw=200)[0]
    s += T("¿qué rincón", 130, 80, 560, K) + T("te falta?", 130, 80, 720, K)
    g, w, h = place(s_lampara, 300, 880, 0.62, -4); s += g
    s += tline("contanos cuál", 62, 90, 1640, K, 0.0, maxw=900)[0]
    return s + '</svg>'

def t_prendida(fecha):
    s = svg_open(Y) + lines_bg(K, .05) + tline("luma", 34, 90, 150, K, 0.0, maxw=200)[0]
    s += T("¿prendida o", 130, 80, 560, K) + T("apagada?", 130, 80, 720, K)
    g, w, h = place(s_lampara, 300, 880, 0.62, -4); s += g
    s += tline("1 prendida · 2 apagada", 62, 90, 1640, K, 0.0, maxw=900)[0]
    return s + '</svg>'

TARDE = [t_cual, t_color, t_rincon, t_prendida]

# ---------- NOCHE: ambiente de cierre del día ----------
def n_base(fecha, lamp=True):
    s = svg_open(K) + tline("luma", 34, 90, 150, Y, 0.0, maxw=200)[0]
    s += f'<circle cx="540" cy="1000" r="430" fill="url(#glow)"/>'
    if lamp:
        g, w, h = place(s_lampara, 260, 900, 0.85, -3); s += g
    return s

def n_prendida(fecha):
    s = n_base(fecha) + T("ya es de noche.", 118, 80, 560, Y) + T("¿la prendés?", 118, 80, 700, WH)
    return s + tline("contanos qué color te gusta", 58, 90, 1700, Y, 0.0, maxw=900)[0] + '</svg>'

def n_leer(fecha):
    s = n_base(fecha, lamp=True) + T("fin del día.", 130, 80, 560, Y)
    s += T("¿leés, mirás o", 100, 80, 1450, WH) + T("descansás?", 100, 80, 1580, WH)
    return s + '</svg>'

def n_cerrar(fecha):
    s = n_base(fecha) + T("apagá la luz", 110, 80, 560, Y) + T("grande.", 110, 80, 690, Y)
    s += tline("dejá solo la lámpara.", 58, 90, 1700, WH, 0.0, maxw=900)[0]
    return s + '</svg>'

def n_buenas(fecha):
    s = n_base(fecha) + T("buenas noches.", 120, 80, 560, Y)
    s += tline("¿cómo estuvo tu día?", 64, 90, 1640, WH, 0.0, maxw=900)[0]
    s += tline("respondé con una palabra", 58, 90, 1730, Y, 0.0, maxw=900)[0]
    return s + '</svg>'

def n_luz_calida(fecha):
    s = n_base(fecha) + T("luz cálida para", 110, 80, 560, WH) + T("cerrar el día.", 110, 80, 690, Y)
    s += tline("¿qué color le pondrías?", 58, 90, 1700, Y, 0.0, maxw=900)[0]
    return s + '</svg>'

NOCHE = [n_prendida, n_leer, n_cerrar, n_buenas, n_luz_calida]

def historia(momento, fecha):
    idx = fecha.timetuple().tm_yday
    if momento == 'tarde':
        return TARDE[idx % len(TARDE)](fecha)
    return NOCHE[(idx + 2) % len(NOCHE)](fecha)

if __name__ == "__main__":
    momento = sys.argv[1]; out = sys.argv[2]
    fecha = datetime.date.fromisoformat(sys.argv[3]) if len(sys.argv) > 3 else datetime.date.today()
    svg = os.path.splitext(out)[0] + '.svg'
    open(svg, 'w').write(historia(momento, fecha))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto('file://' + os.path.abspath(svg)); pg.wait_for_timeout(300)
        pg.screenshot(path=out); b.close()
    print('ok', out)
