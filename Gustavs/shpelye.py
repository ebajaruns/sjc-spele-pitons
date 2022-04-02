from tkinter import *

from PIL import Image, ImageTk, ImageOps

import random
from playsound import *
import threading
import time

master = Tk()
punkti = 0
mushcnt = 10

def sound():
    playsound("Gustavs/assets/CoinSE.mp3")


# canvas augstums, platums
CW = 600
CH = 600

#main logs
logs = Canvas (
    master,
    width=CW,
    height=CH
)
logs.pack()

# logs.create_rectangle(0, 500, 500, 600, fill='green')
# logs.create_text(0, 500, 500, 600, text='Sākt')

# player step length
pstep = 5

#fons
grass = PhotoImage(file='Gustavs/assets/graaas.ppm')
bukgronds = logs.create_image(CW // 2, CH // 2, image= grass)

# pa cik pikseļiem playeris pārvietojas
pstep = 5

#sēne bildes izmēri, pa cik bilde tiks uztaisīta mazāka, tās uzlikšana
mushM = 12
mushroom = Image.open('gustavs/assets/Mushroom.png')
MushSiz = mushroom.size
mushroom = mushroom.resize((MushSiz[0] // mushM, MushSiz[1] // mushM))
seene = ImageTk.PhotoImage(mushroom)

for x in range(mushcnt):
    globals()[f"mush{x}x"] = random.randrange(20, CW - 20, 5)
    globals()[f"mush{x}y"] = random.randrange(20, CW - 20, 5)
    globals()[f"mush{x}"] = logs.create_image(globals()[f'mush{x}x'], globals()[f'mush{x}y'], image= seene)
    print(f'generated mushroom{x} at {globals()[f"mush{x}x"]}; {globals()[f"mush{x}y"]}')

def mushrum(m):
    global slep
    globals()[f'mush{m}x'] = random.randrange(20, CW - 20, 5)
    globals()[f'mush{m}y'] = random.randrange(20, CH - 20, 5)
    globals()[f"mush{m}"] = logs.create_image(globals()[f'mush{m}x'], globals()[f'mush{m}y'], image=seene)
    nx = threading.Thread(target=sound, daemon=True)
    nx.start()
    slep /= 1.5
    print(f'slep: {slep}')


#mario
px = CW // 2
py = CH // 2
ImgM = 10
marijo = Image.open('Gustavs/assets/BMario-NoBG.png')
MarioSiz = marijo.size
marijo = marijo.resize((MarioSiz[0] // ImgM, MarioSiz[1] // ImgM))
ma = ImageTk.PhotoImage(marijo)
playah = logs.create_image(px, py, image = ma)
print(f'px: {px}; py: {py}')

# kaut kas
slx = 0
sly = 0
slimeeM = 10
slimee = Image.open('Gustavs/assets/sss.png')
slimee = slimee.resize((slimee.size[0] // slimeeM, slimee.size[1] // slimeeM))
slime = ImageTk.PhotoImage(slimee)
slim = logs.create_image(slx, sly, image = slime)

def smove():
    global slx, sly, slim, slep
    sterp = 1
    slep = .025
    while 1:
        if slx == px and sly == py:
            print('hehe')
        if slx < px:
            slx += sterp
        else:
            slx -= sterp
        if sly < py:
            sly += sterp
        else:
            sly -= sterp
        logs.delete(slim)
        slim = logs.create_image(slx, sly, image = slime)
        time.sleep(slep)

slm =  threading.Thread(target=smove, daemon=False)

slm.start()

#score
score = logs.create_rectangle(0, 0, 100, 50, fill='grey60', outline='black')
tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)
def scoore(points):
    global tscore
    logs.delete(tscore)
    tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)

#loga title
master.title("Maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarioo")

#resizability
master.resizable(False, False)

#facing right
m = True

#player move
def playahmove(way):
    global px, py, playah, marijo, ma, m
    w = False
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

#logs ir/nav resizable
master.resizable(False, False)

#vai spēlētājs skatās pa labi
m = True
#speletāja kustības funkcija
def playahmove(way):
    global px, py, playah, marijo, ma, m, punkti, i
    #vai būs jāmirroro bilde
    w = False
    #pārbauda kurā virziena tas jāpārvieto
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
        marijo = ImageOps.mirror(marijo)
        ma = ImageTk.PhotoImage(marijo)
    elif w and mm and m == False:
        m = True
        marijo = ImageOps.mirror(marijo)
        ma = ImageTk.PhotoImage(marijo)
    playah = logs.create_image(px, py, image = ma)
    for i in range(mushcnt):
        if px <= globals()[f"mush{i}x"] and px + marijo.size[0] >= globals()[f"mush{i}x"] + mushroom.size[1] and py <= globals()[f"mush{i}y"] and py + marijo.size[1] >= globals()[f"mush{i}y"] + mushroom.size[1]:
            punkti += 1
            scoore(punkti)
            # globals()[f"mush{i}x"] = -1
            # globals()[f"mush{i}y"] = -1
            logs.delete(globals()[f"mush{i}"])
            mushrum(i)
            print(f'just hit mushroom number {i}')
    w = False


def on_keypress(event):
    if event.keysym == "w":
        playahmove('up')
    if event.keysym == "a":
        playahmove('left')
    if event.keysym == "s":
        playahmove('down')
    if event.keysym == "d":
        playahmove('right')

def on_keyrelease(event):
    global direction
    direction = None

master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()