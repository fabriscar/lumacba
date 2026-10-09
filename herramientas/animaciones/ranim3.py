import os,sys
from playwright.sync_api import sync_playwright
d=os.getcwd(); FPS=30; DUR=12.5
only=[float(x) for x in sys.argv[1:]]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+d+'/anim3.html'); pg.wait_for_function('window.fontsReady===true'); pg.wait_for_timeout(800)
    if only:
        for t in only:
            pg.evaluate(f'render({t})'); pg.wait_for_timeout(50); pg.screenshot(path=f'anim3/t{t}.png')
    else:
        for i in range(int(FPS*DUR)):
            pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'anim3/f{i:04d}.png')
    b.close()
