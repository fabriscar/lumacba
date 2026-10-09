import os, math
os.chdir('/tmp/claude-0/-home-claude/c2e7c041-52ae-55fd-8b88-0e5e7d01572a/scratchpad/logo/lampa')
Y='#FFD60A';K='#0B0B0B';CR='#FFF1B8'
HEAD='''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url('../../fonts/bric800.ttf');}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{position:relative;font-family:B;line-height:1}
.a{position:absolute}
.im{position:absolute;display:block}
</style></head><body>'''
def burst():
    n,R1,R2=18,170,142;p=[]
    for i in range(n*2):
        r=R1 if i%2==0 else R2;a=math.pi*i/n-math.pi/2;p.append(f'{r*math.cos(a):.1f},{r*math.sin(a):.1f}')
    return f'<svg viewBox="-200 -200 400 400" width="470" height="470" style="position:absolute;filter:drop-shadow(0 0 0 #fff)"><polygon points="{" ".join(p)}" fill="{K}" stroke="{K}" stroke-width="14" stroke-linejoin="round"/><text x="0" y="-30" text-anchor="middle" font-family="B" font-size="54" fill="{Y}">Día de la</text><text x="0" y="28" text-anchor="middle" font-family="B" font-size="76" fill="{Y}">Madre</text><text x="0" y="86" text-anchor="middle" font-family="B" font-size="52" fill="#fff">18/10</text></svg>'
lines=lambda c,o:''.join(f'<div class="a" style="left:0;top:{y}px;width:1080px;height:3px;background:{c};opacity:{o}"></div>' for y in range(0,1920,14))

# S1 full-bleed
s1=HEAD+f'''<div class="a" style="inset:0;background:#7c7b78"></div><div class="a" style="left:0;top:140px;width:1080px;height:1920px;background:url(foto.png) 0 0/1080px 1920px no-repeat"></div>
<div class="a" style="inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.78) 0,rgba(0,0,0,.45) 26%,rgba(0,0,0,0) 40%,rgba(0,0,0,0) 70%,rgba(0,0,0,.65) 100%)"></div>
<img class="im" src="../stk/png/luma-badge-negro.png" style="left:60px;top:240px;height:130px">
<div class="a" style="left:80px;top:400px;font-size:92px;color:#fff;white-space:pre">tu rincón merece</div>
<div class="a" style="left:80px;top:495px;font-size:92px;color:{Y};white-space:pre">esta luz.</div>
<img class="im" src="../stk/png/chispas.png" style="right:50px;top:600px;height:150px;transform:rotate(10deg)">
<img class="im" src="../stk/png/pedilo-en-la-web.png" style="left:240px;top:1438px;height:150px;transform:rotate(-2deg)">
</body></html>'''
open('s1.html','w').write(s1)

# S2 collage
s2=HEAD+f'''<div class="a" style="inset:0;background:{Y}"></div>{lines(K,.06)}
<img class="im" src="../stk/png/luma-badge-negro.png" style="left:60px;top:240px;height:130px">
<div class="a" style="left:75px;top:400px;font-size:220px;color:{K};letter-spacing:-.02em">regalale</div>
<div class="a" style="left:75px;top:610px;font-size:220px;color:{K};letter-spacing:-.02em">luz.</div>
<div class="a" style="left:380px;top:830px;width:640px;height:720px;border-radius:56px;border:16px solid {K};box-shadow:0 0 0 14px #fff;transform:rotate(4deg);background:url(foto.png) 0 0/auto;background-size:690px auto;background-position:-15px -225px;overflow:hidden"></div>
<div class="a" style="left:-40px;top:920px;width:420px;height:420px;transform:rotate(-8deg) scale(.88);transform-origin:0 0">{burst()}</div>
<img class="im" src="../stk/png/estrella-luma.png" style="left:790px;top:660px;height:190px;transform:rotate(14deg)">
<img class="im" src="../stk/png/chispas.png" style="left:90px;top:1360px;height:170px">
<img class="im" src="../stk/png/pedilo-en-la-web.png" style="left:240px;top:1385px;height:215px;transform:rotate(-3deg)">
</body></html>'''
open('s2.html','w').write(s2)

# S3 detail circle
s3=HEAD+f'''<div class="a" style="inset:0;background:{K}"></div>{lines('#fff',.05)}
<img class="im" src="../stk/png/luma-badge-negro.png" style="left:60px;top:240px;height:130px">
<div class="a" style="left:80px;top:400px;font-size:170px;color:#fff;letter-spacing:-.02em">mirá el</div>
<div class="a" style="left:80px;top:565px;font-size:170px;color:{Y};letter-spacing:-.02em">detalle</div>
<div class="a" style="left:190px;top:800px;width:700px;height:700px;border-radius:50%;border:18px solid {Y};box-shadow:0 0 0 14px #fff;background:url(foto.png);background-size:1400px auto;background-position:-390px -730px"></div>
<img class="im" src="../stk/png/capa-por-capa.png" style="left:540px;top:1400px;height:150px;transform:rotate(-6deg)">
<img class="im" src="../stk/png/chispas.png" style="left:790px;top:760px;height:200px;transform:rotate(8deg)">
<img class="im" src="../stk/png/lamparita.png" style="left:50px;top:1300px;height:250px;transform:rotate(-10deg)">
</body></html>'''
open('s3.html','w').write(s3)

# S4 poll
s4=HEAD+f'''<div class="a" style="inset:0;background:{CR}"></div>{lines(K,.05)}
<img class="im" src="../stk/png/luma-badge-negro.png" style="left:60px;top:240px;height:130px">
<div class="a" style="left:80px;top:395px;font-size:190px;color:{K};letter-spacing:-.02em">¿dónde la</div>
<div class="a" style="left:80px;top:595px;font-size:190px;color:{K};letter-spacing:-.02em">pondrías?</div>
<div class="a" style="left:110px;top:860px;width:860px;height:520px;border-radius:56px;border:16px solid {K};box-shadow:0 0 0 14px #fff;transform:rotate(-2deg);background:url(foto.png);background-size:860px auto;background-position:0 -310px"></div>
<img class="im" src="../stk/png/estrella-luma.png" style="left:830px;top:1180px;height:190px;transform:rotate(14deg)">
<div class="a" style="left:0;top:1430px;width:1080px;text-align:center;font-size:52px;color:{K}">elegí abajo ↓</div>
</body></html>'''
open('s4.html','w').write(s4)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    for n in ('s1','s2','s3','s4'):
        pg.goto('file://'+os.getcwd()+f'/{n}.html');pg.wait_for_timeout(600);pg.screenshot(path=f'{n}.png')
    b.close()
from PIL import Image
W=Image.new('RGB',(4*405,720))
for i,n in enumerate(('s1','s2','s3','s4')): W.paste(Image.open(f'{n}.png').convert('RGB').resize((405,720)),(i*405,0))
W.save('contact.png')
