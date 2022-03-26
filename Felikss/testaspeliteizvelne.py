from calendar import c
from tkinter import *
import random


canvas_width = 900
canvas_height = 900
master = Tk()

#mainīgie - kas svarīgi

direction = None

rezultats = 0

#Izveidojam spelēs laukumu!!! neaizmirstam komandu .pack()
logs = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
master.title("Līnijas spēle")
logs.pack()

#Fona attēla iestatīšana... (svarīgs izmērs - der PNG) (FONS ir globāls mainīgais)
fons = PhotoImage(file="Felikss\mezs_sss.png")


#Izveidojam spēlētāju (bilde (globāls mainīgais))
sarkG = PhotoImage(file="Felikss\sarkvideja.ppm")

# SĒNES (Globāls mainīgais)
sene = PhotoImage(file="Felikss\semene.ppm") 

# UZTAISĪT sēnes (mainot masīva izmēru var veidot vairāk sēnes (arī globāls mainīgais))!!!!
xkoordinates = []
ykoordinates = []
senesst = []
senes = []

#tukšie mainīgie (kas vēlāk tiek "apdzīvoti" (tie vēlāk vajadzīgi, lai izsauktu metodēs))
uzvarteksts = None
uzvarteksts1 = None

#atsevišķa funkcija - kas "rada spēlētāju" 
# 1.funkcija
def speletajs():
    global player
    player = logs.create_image(random.randrange(100, 800, 150),random.randrange(100, 800, 150), image = sarkG) 

#STARTA MENU - sākuma izvēlne (vēl nav uz loga nekas izveidots - tagad izveido "menu, kuru nospiežot tiek izsaukta funkcija (nākamā) nospiests")
# 2.funkcija
def SakumaIzvelne():
    print("Starta menu")
    global menu1, menu
    menu1 = logs.create_rectangle(150, 400, 750, 500, fill="white", outline="blue")
    menu = logs.create_text(450, 450,  font=(None, 50), text="SĀKT SPĒLI")
    logs.tag_bind(menu1, "<Button-1>", nospiests)
    logs.tag_bind(menu, "<Button-1>", nospiests)

# funkcija nospiests (pa lielam uzāk spēli - pirmā lieta - nodzēš "izvēlnes pogas" (arī "uzvarastekstu)") un uzliek fona attēlu,
# iztīra sēņu masīvus un uzģenēr jaunus, tad izsauc 1.funkciju "spēlētājs" )
# 3.funkcija (ietvars spēlei...)

def Grutibasmenu():
    print("Grutibas menu")
    global menu1, menu
    menu1 = logs.create_rectangle(250, 500, 450, 500, fill="white", outline="blue")
    menu = logs.create_text(350, 350,  font=(None, 50), text="Grutibas menu")
    logs.tag_bind(menu1, "<Button-1>", nospiests)
    logs.tag_bind(menu, "<Button-1>", nospiests)
 
def nospiests(none):
    print("nospiests")
    logs.delete(menu1)
    logs.delete(menu)
    logs.delete(uzvarteksts1)
    logs.delete(uzvarteksts)
    global xkoordinates, ykoordinates, senes, senesst,sene, fons, sarkG
    logs.create_image(0,0, image=fons)
    xkoordinates.clear()
    ykoordinates.clear()
    senes.clear()
    senesst.clear()
    for i in range(10):
        xkoordinates.append(random.randrange(100, 800, 150))
        ykoordinates.append(random.randrange(100, 800, 150))
        senesst.append(0)  
        senes.append(i)

    for i in range(10):
        senes[i] = logs.create_image(xkoordinates[i], ykoordinates[i], image=sene)
    speletajs()
    print(senesst)
    print(senes)
    print(xkoordinates)
    print(ykoordinates)    

SakumaIzvelne()

# punktu skaitīšana (kas notiek kad apēd sēni), sev iekša izsauc funkciju "rezultatutablo - katru reizi kad izpildās", iekšā funkcijā punkti
# ir definēts "spēles rezultāts - kas notiek, kad spēlētājs salasa uzvaras punktus")
def punkti():
    global rezultats, senesst, senes, xkoordinates, ykoordinates
    px = logs.coords(player)
    pxx = int(px[0])
    pxy = int(px[1])
    rezultatutablo()

    for i in range(10):
        if (xkoordinates[i]-30)<pxx<(xkoordinates[i]+30) and (ykoordinates[i]-30)<pxy<(ykoordinates[i]+30) and senesst[i]==0:
            logs.delete(senes[i])
            rezultats = rezultats +1
            senesst[i]= senesst[i] + 1
                    
    if rezultats == 10 :
        # šis notiek kad "tiek savākti 10 punkti" - parādās "Spēle uzvarēta", kuru nospiežot tiek izsaukta funkcija "nospiests" - principā spēle resetojas!!!
        global uzvarteksts, uzvarteksts1
        uzvarteksts1 = logs.create_rectangle(150, 400, 750, 500, fill="white", outline="blue")
        uzvarteksts = logs.create_text(450, 450,  font=(None, 50), text="Spēle uzvarēta!!!!")
        logs.tag_bind(uzvarteksts, "<Button-1>", nospiests)
        logs.tag_bind(uzvarteksts1, "<Button-1>", nospiests)
        rezultats = 0

# REZULTATU TABLO (lauks, kurā mainās rezultāts (globālie punkti))
def rezultatutablo():
    buttonBG = logs.create_rectangle(100, 0, 200, 30, fill="red", outline="grey60")
    buttonTXT = logs.create_text(150, 15,  font=(None, 25), text=rezultats)



#KUSTĪBA _ staigājam apkārt... (Šīs 3 tālākas funkcijas vislaik ir aktīvas :) bet faktiski izpildās, tad gad mums ir "globālais player" - funkcija spēlētājs, 
# funkcija spēlētājs tiek izsaukta "funkcijā nospiests"

def move():
    global player
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        logs.move(player, x_vel,y_vel)
        punkti()
        #kustināt vilku... 
        #after(33,move)

def on_keypress(event):
    global direction
    global x_vel
    global y_vel
    if event.keysym == "Left":
        direction = "left"
        x_vel = -5
        y_vel = 0
    if event.keysym == "Right":
        direction = "right"
        x_vel = 5
        y_vel = 0
    if event.keysym == "Down":
        direction = "down"
        x_vel = 0
        y_vel = 5
    if event.keysym == "Up":
        direction = "up"
        x_vel = 0
        y_vel = -5
    
    move()
    

def on_keyrelease(event):
    global direction
    direction = None







#Master mainloops - izmaiņas un notikumi
master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()