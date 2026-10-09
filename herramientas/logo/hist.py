import sys, math
sys.path.insert(0,'.')
from stickers import *

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

def story1():
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920"><rect width="1080" height="1920" fill="{Y}"/>{lines_bg(K, .06)}'
    g, h = wm(90, 280, 300, K); s += g
    t, tw = tline("regalale", 215, 80, 640, K, -0.02, maxw=900); s += t
    t, tw = tline("luz.", 215, 80, 850, K, -0.02); s += t
    g, w, hh = place(s_lampara, 40, 930, 1.0, -6); s += g
    g, w, hh = place(lambda: burst("10 días", 78), 580, 880, 0.82, 8); s += g
    t, _ = tline("para el", 70, 580, 1325, K); s += t
    t, _ = tline("Día de la Madre", 70, 580, 1405, K, maxw=420); s += t
    g, w, hh = place(s_pedilo, 110, 1500, 0.84, -2); s += g
    return s + '</svg>'

def story2():
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920"><rect width="1080" height="1920" fill="{K}"/>{lines_bg(Y, .07)}'
    g, h = wm(90, 280, 300, Y); s += g
    for i, w_ in enumerate(("preguntame", "lo que", "quieras")):
        t, _ = tline(w_, 175, 80, 620 + i*175, Y if i != 1 else WH, -0.02, maxw=900); s += t
    for i, l in enumerate(("sobre las lámparas, los colores", "o cómo las imprimimos")):
        t, _ = tline(l, 48, 90, 1195 + i*66, WH, 0.0, maxw=900); s += t
    t, _ = tline("dejá tu pregunta acá", 62, 90, 1380, Y, maxw=700); s += t
    s += (f'<path d="M830,1330 L830,1470 M780,1420 L830,1472 L880,1420" fill="none" stroke="{Y}" stroke-width="18" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    g, w, hh = place(s_estrella, 790, 930, 0.42, 12); s += g
    g, w, hh = place(s_chispas, 40, 1500, 0.45, -8); s += g
    return s + '</svg>'

import os
os.makedirs('hist', exist_ok=True)
open('hist/h1.svg', 'w').write(story1())
open('hist/h2.svg', 'w').write(story2())
from playwright.sync_api import sync_playwright
d = os.getcwd()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg = b.new_page(viewport={'width':1080,'height':1920})
    for n in ('h1', 'h2'):
        pg.goto('file://'+d+f'/hist/{n}.svg'); pg.screenshot(path=f'hist/{n}.png')
    b.close()
print('ok')
