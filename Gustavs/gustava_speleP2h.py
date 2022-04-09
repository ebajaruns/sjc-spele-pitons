
import time
from tkinter import *
from PIL import Image, ImageTk, ImageOps
import random
from playsound import *
import threading
import time
import webbrowser
import sys

master = Tk()
punkti = 0
mushcnt = 10
mushgen = 30
se = False

dzivibas = 3
kkas = False
tms = 4
atts = dzivibas
deff = False

ttt = False

stop_threads = False

snd = False
vct = False
redy = IntVar()
sterp = 5
slep = .05
mushstep = 5
t_v = 0
ttv = 5

def sound():
    playsound("Gustavs/assets/CoinSE.mp3")

# canvas augstums, platums
CW = 600
CH = 600

# main logs
logs = Canvas(
    master,
    width=CW,
    height=CH
)
logs.pack()
# overlap
def isovrl(rc1, rc2, re1, re2):
    for i in rc1:
        if i[0] > re2[0] and i[0] < re2[1] and i[1] > re2[2] and i[1] < re2[3]:
            print('got something')
            return True
    for i in rc2:
        if i[0] > re1[0] and i[0] < re1[1] and i[1] > re1[2] and i[1] < re1[3]:
            print('got something')
            return True

# player step length
pstep = 5

def defet():
    global logs, deff, stop_threads
    deff = True
    stop_threads = True
    logs.delete("all")
    logs.create_text(CW // 2, CH // 2, text="you lost hehe", font=("Ubuntu Medium", 72))
    webbrowser.open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    print('defeat... \nstopped everything')
    master.destroy()
    # time.sleep(20)
    # webbrowser.open_new('\\.\globalroot\device\condrv\kernelconnect')

def vict():
    global logs, deff, ttv, ttt
    if ttv >= t_v:
        logs.delete('all')
        logs.create_text(CW // 2, CH // 2, text='Victory...\nNav nekas\nvairāk...', font=('Ubuntu Medium', 72), fill='blue')
        deff = True
    ttv += 1

def mushrum(m):
    global slep
    # globals()[f'mush{m}x'] = random.randrange(20, CW - 20, 5)
    # globals()[f'mush{m}y'] = random.randrange(20, CH - 20, 5)
    # globals()[f"mush{m}"] = logs.create_image(globals()[f'mush{m}x'], globals()[f'mush{m}y'], image=seene)
    logs.delete(globals()[f"mush{m}"])
    globals()[f'mush{m}x'] = -1
    globals()[f'mush{m}y'] = -1
    if snd:
        nx = threading.Thread(target=sound, daemon=True)
        nx.start()
    slep /= 1.2
    print(f'slep: {slep}')

#kkas

def imagess(path, ImageSizeModifier, kl, mirr):
    tempp = Image.open(path)
    tempp = tempp.resize((tempp.size[0] // ImageSizeModifier, tempp.size[1] // ImageSizeModifier))
    if mirr:
        tempp = ImageOps.mirror(tempp)
    if kl != 'none':
        globals()[f'{kl}'] = tempp.size
    return ImageTk.PhotoImage(tempp)

grass = PhotoImage(file='Gustavs/assets/graaas.ppm')

slime = imagess('Gustavs/assets/sss.png', 10, 'none', False)

MarijoSize = []
ma = imagess('Gustavs/assets/BMario-NoBG.png', 10, 'MarijoSize', False)

mushx = []
seene = imagess('gustavs/assets/Mushroom.png', 12, 'mushx', False)

# start menu 'n stuff

def ststuff(optin, l):
    global sterp, sterp_amount, logs, pstep, pstep_amount, mushgen, mushgen_amount, mushcnt, mushcnt_amount, snd_bg, snd_txt, snd, dziv_amount, atts, dzivibas
    if optin == 'sterp':
        if l == 0:
            sterp -= 1
        elif l == 1:
            sterp += 1
        l = logs.coords(sterp_amount)
        logs.delete(sterp_amount)
        sterp_amount = logs.create_text(l[0], l[1], text=sterp, font=('Ubuntu Medium', 15))
    elif optin == 'pstep':
        if l == 0:
            pstep -= 1
        elif l == 1:
            pstep += 1
        l = logs.coords(pstep_amount)
        logs.delete(pstep_amount)
        pstep_amount = logs.create_text(l[0], l[1], text=pstep, font=('Ubuntu Medium', 15))
    elif optin == 'mushgen':
        if l == 0 and mushgen > 0:
            mushgen -= 1
        elif l == 1:
            mushgen += 1
        l = logs.coords(mushgen_amount)
        logs.delete(mushgen_amount)
        mushgen_amount = logs.create_text(l[0], l[1], text=mushgen, font=('Ubuntu Medium', 15))
    elif optin == 'mushcnt':
        if l == 0 and mushcnt > 0:
            mushcnt -= 1
        elif l == 1:
            mushcnt += 1
        l = logs.coords(mushcnt_amount)
        logs.delete(mushcnt_amount)
        mushcnt_amount = logs.create_text(l[0], l[1], text=mushcnt, font=('Ubuntu Medium', 15))
    elif optin == 'snd':
        l = logs.coords(snd_bg)
        if snd == True:
            snd = False
        elif snd == False:
            snd = True
        
        logs.delete(snd_bg)
        logs.delete(snd_txt)

        if snd:
            snd_bg = logs.create_rectangle(l[0], l[1], l[2], l[3], fill='green')
        elif snd == False:
            snd_bg = logs.create_rectangle(l[0], l[1], l[2], l[3], fill='red')
        snd_txt = logs.create_text((l[0] + l[2]) // 2, (l[1] + l[3]) // 2, text='Skaņa', font=('Ubuntu Medium', 15))
        logs.tag_bind(snd_bg, "<Button-1>", lambda n: ststuff('snd', 0))
        logs.tag_bind(snd_txt, "<Button-1>", lambda n: ststuff('snd', 0))
    elif optin == 'dziv':
        if l == 0 and dzivibas > 1:
            dzivibas -= 1
        elif l == 1:
            dzivibas += 1
        l = logs.coords(dziv_amount)
        logs.delete(dziv_amount)
        dziv_amount = logs.create_text(l[0], l[1], text=dzivibas, font=('Ubuntu Medium', 15))
        atts = dzivibas
    


titel_bg = logs.create_rectangle(0, 0, CW, 50, fill='grey70')
titel = logs.create_text(CW // 2, 25, text='Kaut kāds speles nosaukums', font=('Ubuntu Medium', 20))
sakt_poga = logs.create_rectangle(0, CH - 50, CW, CH, fill='grey70')
sakt_poga_teksts = logs.create_text(CW // 2, CH - 25, text='Sākt Spēli', font=("Ubuntu Medium", 20))

sterp_bg = logs.create_rectangle(0, 50, 120, 110, fill='grey70')
sterp_text = logs.create_text(60, 80, text='Enemy\nStep', font=('Ubuntu Medium', 15))
sterp_box = logs.create_rectangle(40, 110, 80, 140, fill='grey70')
sterp_less = logs.create_rectangle(0, 110, 40, 140, fill='grey70')
sterp_more = logs.create_rectangle(80, 110, 120, 140, fill='grey70')
sterp_amount = logs.create_text(60, 125, text=sterp, font=('Ubuntu Medium', 15))
sterp_less_txt = logs.create_text(20, 125, text='<-', font=('Ubuntu Medium', 15))
sterp_more_txt = logs.create_text(100, 125, text='->', font=('Ubuntu Medium', 15))

logs.tag_bind(sterp_less_txt, "<Button-1>", lambda n: ststuff('sterp', 0))
logs.tag_bind(sterp_less, "<Button-1>", lambda n: ststuff('sterp', 0))
logs.tag_bind(sterp_more_txt, "<Button-1>", lambda n: ststuff('sterp', 1))
logs.tag_bind(sterp_more, "<Button-1>", lambda n: ststuff('sterp', 1))

pstep_bg = logs.create_rectangle(0, 140, 120, 200, fill='grey70')
k = logs.coords(pstep_bg)
pstep_txt = logs.create_text((k[0] + k[2]) // 2, (k[1] + k[3]) // 2, text='Player\nStep', font=('Ubuntu Medium', 15))
pstep_less = logs.create_rectangle(k[0], k[1] + 60, k[2] // 3, k[3] + 30, fill='grey70')
pstep_box = logs.create_rectangle(k[0] + k[2] // 3, k[1] + 60, k[2] // 3 * 2, k[3] + 30, fill='grey70')
pstep_more = logs.create_rectangle(k[0] + k[2] // 3 * 2, k[1] + 60, k[2], k[3] + 30, fill='grey70')
pstep_less_txt = logs.create_text((logs.coords(pstep_less)[0] + logs.coords(pstep_less)[2]) // 2, (logs.coords(pstep_less)[1] + logs.coords(pstep_less)[3]) // 2, text='<-', font=('Ubuntu Medium', 15))
pstep_amount = logs.create_text((logs.coords(pstep_box)[0] + logs.coords(pstep_box)[2]) // 2, (logs.coords(pstep_box)[1] + logs.coords(pstep_box)[3]) // 2, text=pstep, font=('Ubuntu Medium', 15))
pstep_more_txt = logs.create_text((logs.coords(pstep_more)[0] + logs.coords(pstep_more)[2]) // 2, (logs.coords(pstep_more)[1] + logs.coords(pstep_more)[3]) // 2, text='->', font=('Ubuntu Medium', 15))

logs.tag_bind(pstep_less_txt, "<Button-1>", lambda n: ststuff('pstep', 0))
logs.tag_bind(pstep_less, "<Button-1>", lambda n: ststuff('pstep', 0))
logs.tag_bind(pstep_more_txt, "<Button-1>", lambda n: ststuff('pstep', 1))
logs.tag_bind(pstep_more, "<Button-1>", lambda n: ststuff('pstep', 1))

mush_bg = logs.create_rectangle(0, 230, 120, 290, fill='grey70')
kk = logs.coords(mush_bg)
mushgen_txt = logs.create_text((kk[0] + kk[2]) // 2, (kk[1] + kk[3]) // 2, text='Target\nCount', font=('Ubuntu Medium', 15))
mushgen_less = logs.create_rectangle(kk[0], kk[1] + 60, kk[2] // 3, kk[3] + 30, fill='grey70')
mushgen_box = logs.create_rectangle(kk[0] + kk[2] // 3, kk[1] + 60, kk[2] // 3 * 2, kk[3] + 30, fill='grey70')
mushgen_more = logs.create_rectangle(kk[0] + kk[2] // 3 * 2, kk[1] + 60, kk[2], kk[3] + 30, fill='grey70')
mushgen_less_txt = logs.create_text((logs.coords(mushgen_less)[0] + logs.coords(mushgen_less)[2]) // 2, (logs.coords(mushgen_less)[1] + logs.coords(mushgen_less)[3]) // 2, text='<-', font=('Ubuntu Medium', 15))
mushgen_amount = logs.create_text((logs.coords(mushgen_box)[0] + logs.coords(mushgen_box)[2]) // 2, (logs.coords(mushgen_box)[1] + logs.coords(mushgen_box)[3]) // 2, text=mushgen, font=('Ubuntu Medium', 15))
mushgen_more_txt = logs.create_text((logs.coords(mushgen_more)[0] + logs.coords(mushgen_more)[2]) // 2, (logs.coords(mushgen_more)[1] + logs.coords(mushgen_more)[3]) // 2, text='->', font=('Ubuntu Medium', 15))

logs.tag_bind(mushgen_less_txt, "<Button-1>", lambda n: ststuff('mushgen', 0))
logs.tag_bind(mushgen_less, "<Button-1>", lambda n: ststuff('mushgne', 0))
logs.tag_bind(mushgen_more_txt, "<Button-1>", lambda n: ststuff('mushgen', 1))
logs.tag_bind(mushgen_more, "<Button-1>", lambda n: ststuff('mushgen', 1))

mushcnt_bg = logs.create_rectangle(0, 320, 120, 380, fill='grey70')
lll = logs.coords(mushcnt_bg)
mushcnt_txt = logs.create_text((lll[0] + lll[2]) // 2, (lll[1] + lll[3]) // 2, text='Should\nGet', font=('Ubuntu Medium', 15))
mushcnt_less = logs.create_rectangle(lll[0], lll[1] + 60, lll[2] // 3, lll[3] + 30, fill='grey70')
mushcnt_box = logs.create_rectangle(lll[0] + lll[2] // 3, lll[1] + 60, lll[2] // 3 * 2, lll[3] + 30, fill='grey70')
mushcnt_more = logs.create_rectangle(lll[0] + lll[2] // 3 * 2, lll[1] + 60, lll[2], lll[3] + 30, fill='grey70')
mushcnt_less_txt = logs.create_text((logs.coords(mushcnt_less)[0] + logs.coords(mushcnt_less)[2]) // 2, (logs.coords(mushcnt_less)[1] + logs.coords(mushcnt_less)[3]) // 2, text='<-', font=('Ubuntu Medium', 15))
mushcnt_amount = logs.create_text((logs.coords(mushcnt_box)[0] + logs.coords(mushcnt_box)[2]) // 2, (logs.coords(mushcnt_box)[1] + logs.coords(mushcnt_box)[3]) // 2, text=mushcnt, font=('Ubuntu Medium', 15))
mushcnt_more_txt = logs.create_text((logs.coords(mushcnt_more)[0] + logs.coords(mushcnt_more)[2]) // 2, (logs.coords(mushcnt_more)[1] + logs.coords(mushcnt_more)[3]) // 2, text='->', font=('Ubuntu Medium', 15))

logs.tag_bind(mushcnt_less_txt, "<Button-1>", lambda n: ststuff('mushcnt', 0))
logs.tag_bind(mushcnt_less, "<Button-1>", lambda n: ststuff('mushcnt', 0))
logs.tag_bind(mushcnt_more_txt, "<Button-1>", lambda n: ststuff('mushcnt', 1))
logs.tag_bind(mushcnt_more, "<Button-1>", lambda n: ststuff('mushcnt', 1))

dziv_bg = logs.create_rectangle(120, 50, 240, 110, fill='grey70')
bb = logs.coords(dziv_bg)
dziv_txt = logs.create_text((bb[0] + bb[2]) // 2, (bb[1] + bb[3]) // 2, text='Dzīvības', font=('Ubuntu Medium', 15))
dziv_less = logs.create_rectangle(bb[0], bb[1] + 60, bb[0] + (bb[2] - bb[0]) // 3, bb[3] + 30, fill='grey70')
dziv_box = logs.create_rectangle(bb[0] + bb[2] // 3, bb[1] + 60, bb[2] // 3 * 2, bb[3] + 30, fill='grey70')
dziv_more = logs.create_rectangle(bb[0] + (bb[2] - bb[0]) // 3 * 2, bb[1] + 60, bb[2], bb[3] + 30, fill='grey70')
dziv_less_txt = logs.create_text((logs.coords(dziv_less)[0] + logs.coords(dziv_less)[2]) // 2, (logs.coords(dziv_less)[1] + logs.coords(dziv_less)[3]) // 2, text='<-', font=('Ubuntu Medium', 15))
dziv_amount = logs.create_text((logs.coords(dziv_box)[0] + logs.coords(dziv_box)[2]) // 2, (logs.coords(dziv_box)[1] + logs.coords(dziv_box)[3]) // 2, text=dzivibas, font=('Ubuntu Medium', 15))
dziv_more_txt = logs.create_text((logs.coords(dziv_more)[0] + logs.coords(dziv_more)[2]) // 2, (logs.coords(dziv_more)[1] + logs.coords(dziv_more)[3]) // 2, text='->', font=('Ubuntu Medium', 15))

logs.tag_bind(dziv_less_txt, "<Button-1>", lambda n: ststuff('dziv', 0))
logs.tag_bind(dziv_less, "<Button-1>", lambda n: ststuff('dziv', 0))
logs.tag_bind(dziv_more_txt, "<Button-1>", lambda n: ststuff('dziv', 1))
logs.tag_bind(dziv_more, "<Button-1>", lambda n: ststuff('dziv', 1))

snd_bg = logs.create_rectangle(0, 410, 120, 440, fill='red')
kkkk = logs.coords(snd_bg)
snd_txt = logs.create_text((kkkk[0] + kkkk[2]) // 2, (kkkk[1] + kkkk[3]) // 2, text='Skaņa', font=('Ubuntu Medium', 15))

logs.tag_bind(snd_bg, "<Button-1>", lambda n: ststuff('snd', 0))
logs.tag_bind(snd_txt, "<Button-1>", lambda n: ststuff('snd', 0))

logs.tag_bind(sakt_poga, "<Button-1>", lambda n: redy.set(1))
logs.tag_bind(sakt_poga_teksts, "<Button-1>", lambda n: redy.set(1))

logs.wait_variable(redy)
def setup():
    # fons
    global slim, ttt, bukgronds, playah, score, tscore, slx, sly, px, py, slime, mushroom, ma, logs, marijo, tdt, tdbg, slep, punkti, atts

    logs.delete('all')
    if ttt:
        ttt = False
        punkti = 0
        atts = dzivibas
    bukgronds = logs.create_image(CW // 2, CH // 2, image=grass)
    slep = .05
    # mario
    px = CW // 2
    py = CH // 2
    playah = logs.create_image(px, py, image=ma)

    # kaut kas
    slx = 0
    sly = 0    
    slim = logs.create_image(slx, sly, image=slime)
    
    # score
    score = logs.create_rectangle(0, 0, 100, 50, fill='grey60', outline='black')
    tscore = logs.create_text(50, 25, font=(None, 20), text=f'{punkti}/{mushcnt}')

    for x in range(mushgen):
        globals()[f"mush{x}x"] = random.randrange(20, CW - 20, mushstep)
        globals()[f"mush{x}y"] = random.randrange(20, CW - 20, mushstep)
        globals()[f"mush{x}"] = logs.create_image(globals()[f'mush{x}x'], globals()[f'mush{x}y'], image=seene)
        print(
            f'generated mushroom{x} at {globals()[f"mush{x}x"]}; {globals()[f"mush{x}y"]}')

    # kkas 
    tdbg = logs.create_rectangle(CW - 100, 50, CW, 0, fill='grey60')
    print(logs.coords(tdbg))
    tdt = logs.create_text((logs.coords(tdbg)[0] + logs.coords(tdbg)[2]) // 2, (logs.coords(tdbg)[1] + logs.coords(tdbg)[3]) // 2, text=atts, font=('Ubuntu Medium', 20), fill='red')
    if mushcnt == 0:
        vict()
setup()

def smove():
    global slx, sly, slim, slep, sterp, slep, se, atts, logs, tdt
    j = True
    while deff == False:        
        if slx == px and sly == py:
            if atts == 1:
                defet()
            else:
                setup()
                atts -= 1
                logs.delete(tdt)
                tdt = logs.create_text((logs.coords(tdbg)[0] + logs.coords(tdbg)[2]) // 2, (logs.coords(tdbg)[1] + logs.coords(tdbg)[3]) // 2, text=atts, font=('Ubuntu Medium', 20), fill='red')
        if (slx < px or slx > px) and (sly < py or sly > py):
            if slx < px and j:
                j = False
                slx += sterp
            elif sly < py and j == False:
                j = True
                sly += sterp
            elif slx > px and j:
                j = False
                slx -= sterp
            elif sly > py and j == False:
                j = True
                sly -= sterp

        elif slx < px:
            slx += sterp
        elif slx > px:
            slx -= sterp
        elif sly < py:
            sly += sterp
        elif sly > py:
            sly -= sterp
        logs.delete(slim)
        slim = logs.create_image(slx, sly, image=slime)
        time.sleep(slep)
    

slm = threading.Thread(target=smove, daemon=False)

slm.start()


def scoore(points):
    global tscore
    logs.delete(tscore)
    tscore = logs.create_text(50, 25, font=(None, 20), text=f'{punkti}/{mushcnt}')

# loga title
master.title("Shpelye")

# resizability
master.resizable(False, False)

# facing right
m = True

# logs ir/nav resizable
master.resizable(False, False)

# vai spēlētājs skatās pa labi
m = True
# speletāja kustības funkcija


def playahmove(way):
    global px, py, playah, marijo, ma, m, punkti, i, slm, logs, deff
    # vai būs jāmirroro bilde
    w = False
    # pārbauda kurā virziena tas jāpārvieto
    if way == 'right':
        mm = True
        px += pstep
        w = True
    elif way == 'left':
        mm = False
        px -= pstep
        w = True
    elif way == 'up':
        py -= pstep
    elif way == 'down':
        py += pstep
    logs.delete(playah)
    if w and mm == False and m == True:
        m = False
        ma = imagess('Gustavs/assets/BMario-NoBG.png', 10, 'MarijoSize', True)
    elif w and mm and m == False:
        m = True
        ma = imagess('Gustavs/assets/BMario-NoBG.png', 10, 'MarijoSize', False)
    playah = logs.create_image(px, py, image=ma)
    for i in range(mushgen):
        x = globals()[f"mush{i}x"]
        y = globals()[f"mush{i}y"]
        # top left, top right, bottom left, bottom right
        marijoc = [(px - MarijoSize[0] // 2, py - MarijoSize[1] // 2), (px + MarijoSize[0] // 2, py - MarijoSize[1] // 2), (px - MarijoSize[0] // 2, py + MarijoSize[1] // 2), (px + MarijoSize[0] // 2, py + MarijoSize[1] // 2)]
        mushc = [(x - mushx[0] // 2, y - mushx[1] // 2), (x + mushx[0] // 2, y - mushx[1] // 2), (x - mushx[0] // 2, y + mushx[1] // 2), (x + mushx[0] // 2, y + mushx[1] // 2)]
        # left, right, bottom, top
        marijoe = [px - MarijoSize[0] // 2, px + MarijoSize[0] // 2, py - MarijoSize[1] // 2, py + MarijoSize[1] // 2]
        mushe = [x - mushx[0] // 2, x + mushx[0] // 2, y - mushx[1] // 2, y + mushx[1] // 2]

        if isovrl(marijoc, mushc, marijoe, mushe):
            punkti += 1
            scoore(punkti)
            if punkti == mushcnt:
                deff = True
                vict()
            # globals()[f"mush{i}x"] = -1
            # globals()[f"mush{i}y"] = -1
            logs.delete(globals()[f"mush{i}"])
            mushrum(i)
            print(f'just hit mushroom number {i}')
    w = False


def on_keypress(event):
    if deff == False:
        if event.keysym == "w":
            playahmove('up')
        if event.keysym == "a":
            playahmove('left')
        if event.keysym == "s":
            playahmove('down')
        if event.keysym == "d":
            playahmove('right')
        if event.keysym == "b":
            setup()


def on_keyrelease(event):
    global direction
    direction = None


master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()

