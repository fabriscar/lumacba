import sys, math
sys.path.insert(0,'.')
from stickers import *

def ridges(cid, y0, y1, W, step=22, op=.28):
    return f'<g clip-path="url(#{cid})">' + "".join(f'<rect x="0" y="{y}" width="{W}" height="6" fill="{K}" opacity="{op}"/>' for y in range(y0, y1, step)) + '</g>'

def flower(cx, cy, r, rot=0):
    p = ""
    for i in range(8):
        a = i * 45
        p += f'<ellipse cx="0" cy="{-r*0.62}" rx="{r*0.26}" ry="{r*0.42}" transform="rotate({a})" fill="{WH}" stroke="{K}" stroke-width="9"/>'
    return f'<g transform="translate({cx},{cy}) rotate({rot})">{p}<circle r="{r*0.3}" fill="{Y}" stroke="{K}" stroke-width="9"/></g>'

def leaf(rot, L=190, w=62, ox=230, oy=330):
    d = f'M0,0 C-{w},-{L*0.3} -{w*0.9},-{L*0.75} 0,-{L} C{w*0.9},-{L*0.75} {w},-{L*0.3} 0,0 Z'
    return (f'<g transform="translate({ox},{oy}) rotate({rot})"><path d="{d}" fill="{K}" stroke="{K}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="M0,-18 L0,-{L*0.78}" stroke="{Y}" stroke-width="9" stroke-linecap="round"/></g>')

def o_maceta():
    W, H = 460, 640; cid = uid('c')
    pot = 'M84,340 L376,340 L346,570 Q342,600 312,600 L148,600 Q118,600 114,570 Z'
    inner = (leaf(-62, 170) + leaf(62, 170) + leaf(-30, 220) + leaf(30, 220) + leaf(0, 250)
             + f'<clipPath id="{cid}"><path d="{pot}"/></clipPath>'
             + f'<path d="{pot}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>' + ridges(cid, 372, 600, W)
             + f'<rect x="60" y="306" width="340" height="64" rx="18" fill="{K}"/>')
    return inner, W, H

def o_florero():
    W, H = 460, 680; cid = uid('c')
    body = 'M180,300 C180,350 92,392 92,500 C92,590 146,640 230,640 C314,640 368,590 368,500 C368,392 280,350 280,300 Z'
    stems = "".join(f'<path d="M230,310 Q{x1},{y1} {x},{y}" fill="none" stroke="{K}" stroke-width="13" stroke-linecap="round"/>' for x1, y1, x, y in ((200, 250, 120, 140), (230, 200, 232, 90), (262, 250, 340, 150)))
    inner = (stems + flower(120, 140, 78, -12) + flower(232, 86, 84, 8) + flower(340, 150, 74, 14)
             + f'<clipPath id="{cid}"><path d="{body}"/></clipPath>'
             + f'<path d="{body}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>' + ridges(cid, 330, 640, W)
             + f'<rect x="160" y="290" width="140" height="30" rx="14" fill="{K}"/>')
    return inner, W, H

def o_colgante():
    W, H = 480, 640; cid = uid('c')
    dome = 'M60,400 C60,290 134,214 240,214 C346,214 420,290 420,400 Z'
    rays = "".join(f'<line x1="{240+ r1*math.cos(math.radians(a)):.1f}" y1="{430+ r1*math.sin(math.radians(a)):.1f}" x2="{240+ r2*math.cos(math.radians(a)):.1f}" y2="{430+ r2*math.sin(math.radians(a)):.1f}" stroke="{K}" stroke-width="14" stroke-linecap="round"/>' for a, r1, r2 in ((60, 100, 150), (90, 100, 160), (120, 100, 150), (30, 190, 225), (150, 190, 225)))
    inner = (f'<rect x="232" y="0" width="16" height="190" fill="{K}"/>'
             + f'<rect x="206" y="170" width="68" height="56" rx="10" fill="{K}"/>'
             + rays + f'<ellipse cx="240" cy="418" rx="70" ry="34" fill="{WH}" stroke="{K}" stroke-width="14"/>'
             + f'<clipPath id="{cid}"><path d="{dome}"/></clipPath>'
             + f'<path d="{dome}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>' + ridges(cid, 240, 400, W, 20)
             + f'<rect x="46" y="388" width="388" height="34" rx="17" fill="{K}"/>')
    return inner, W, H

def o_portavelas():
    W, H = 440, 620; cid = uid('c')
    holder = 'M100,380 L340,380 L318,570 Q315,596 290,596 L150,596 Q125,596 122,570 Z'
    flame = 'M220,40 C250,90 272,118 272,160 A52,52 0 0 1 168,160 C168,118 190,90 220,40 Z'
    inner = (f'<path d="{flame}" fill="{Y}" stroke="{K}" stroke-width="18" stroke-linejoin="round"/>'
             + f'<path d="M220,110 C234,134 240,146 240,162 A20,20 0 0 1 200,162 C200,146 206,134 220,110 Z" fill="{K}"/>'
             + f'<rect x="190" y="206" width="60" height="190" fill="{WH}" stroke="{K}" stroke-width="16" stroke-linejoin="round"/>'
             + f'<path d="M220,196 L220,214" stroke="{K}" stroke-width="12" stroke-linecap="round"/>'
             + f'<clipPath id="{cid}"><path d="{holder}"/></clipPath>'
             + f'<path d="{holder}" fill="{Y}" stroke="{K}" stroke-width="20" stroke-linejoin="round"/>' + ridges(cid, 410, 596, W, 20)
             + f'<rect x="80" y="364" width="280" height="44" rx="18" fill="{K}"/>')
    return inner, W, H

def o_esfera():
    W, H = 480, 600; cid = uid('c')
    arcs = "".join(f'<ellipse cx="240" cy="{240+dy}" rx="{ (200**2 - dy**2)**.5:.1f}" ry="14" fill="none" stroke="{K}" stroke-width="7" opacity=".35"/>' for dy in range(-150, 170, 38))
    inner = (f'<rect x="206" y="420" width="68" height="120" fill="{K}"/>'
             + f'<rect x="130" y="520" width="220" height="48" rx="22" fill="{K}"/>'
             + f'<clipPath id="{cid}"><circle cx="240" cy="240" r="200"/></clipPath>'
             + f'<circle cx="240" cy="240" r="200" fill="{Y}" stroke="{K}" stroke-width="20"/>' + f'<g clip-path="url(#{cid})">{arcs}</g>'
             + f'<path d="M110,200 A140,140 0 0 1 200,110" fill="none" stroke="{WH}" stroke-width="20" stroke-linecap="round"/>')
    return inner, W, H

OBJS = {'maceta': o_maceta, 'florero': o_florero, 'lampara': s_lampara, 'colgante': o_colgante, 'portavelas': o_portavelas, 'esfera': o_esfera}
if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    import os, re
    d = os.getcwd()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for n, fn in OBJS.items():
            svg, W, H = sticker_svg(n, fn)
            open(f'anim2/svg/{n}.svg', 'w').write(svg)
            w = W + 120; h = H + 120; sc = 900 / max(w, h)
            pg = b.new_page(viewport={'width': int(w) + 1, 'height': int(h) + 1}, device_scale_factor=sc)
            pg.goto('file://' + d + f'/anim2/svg/{n}.svg')
            pg.screenshot(path=f'anim2/obj/{n}.png', omit_background=True, clip={'x': 0, 'y': 0, 'width': w, 'height': h}); pg.close()
        b.close()
    from PIL import Image
    S = Image.new('RGB', (6 * 360, 420), (255, 214, 10))
    for i, n in enumerate(OBJS):
        im = Image.open(f'anim2/obj/{n}.png'); im.thumbnail((350, 400)); S.paste(im, (i * 360 + 5, 10), im)
    S.save('anim2/objs.png'); print('ok')
