from calendar import c
from tkinter import *
import random

#from numpy import true_divide
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

#Izveidojam spēlētāju (bilde)
sarkG = PhotoImage(file="sjc-spele-pitons\Felikss\sarkvideja.png")
logs.create_image(250,250, image= sarkG)
player = logs.create_image(250,250, image = sarkG)
logs.delete(player)

#Fona attēla iestatīšana... (svarīgs izmērs - der PNG)
fons = PhotoImage(file="SJC-SPELE-PITONS\Felikss\mezs_sss.png")
logs.create_image(0,0, image=fons)

# SĒNES (15 elementi mapē)
sene = PhotoImage(file="SJC-SPELE-PITONS\Felikss\semene.ppm") 
# sēne 1
#sx1 = random.randrange(100, 800, 150)
#sy1 = random.randrange(100, 800, 150)
#sene1 = logs.create_image(sx1, sy1, image=sene)
#sene1status = 0

#Sēne 2
#sx2 = random.randrange(100, 800, 150)
#sy2 = random.randrange(100, 800, 150)
#sene2 = logs.create_image(sx2, sy2, image=sene)
#sene2status = 0

#Sēne 3
#sx3 = random.randrange(100, 800, 150)
#sy3 = random.randrange(100, 800, 150)
#sene3 = logs.create_image(sx3, sy3, image=sene)
#sene3status = 0

# UZTAISĪT 5- 10 sēnes!!!!
xkoordinates = []
ykoordinates = []
senes =[1,1,1,1,1,1,1,1,1,1]
print(senes)
for i in range(10):
    xkoordinates.append(random.randrange(100, 800, 150))
    ykoordinates.append(random.randrange(100, 800, 150))  

for i in range(10):
    senes[i] = logs.create_image(xkoordinates[i], ykoordinates[i], image=sene)

senesst =[0,0,0,0,0,0,0,0,0,0]
print(senesst)
print(senes)
print(xkoordinates)
print(ykoordinates)


#print(sx1, sy1, sx2, sy2)

#punktu skaitīšana....
def punkti():
    # global sx1, sy1, sx2, sy2, sx3, sy3, rezultats, sene1status, sene2status, sene3status
    global rezultats, senesst, senes, xkoordinates, ykoordinates
    
    px = logs.coords(player)
    pxx = int(px[0])
    pxy = int(px[1])
    #print(pxx, pxy, sx1, sy1 )
    # pirmā sēne noķerta... 
    # print(rezultats)
    rezultatutablo()

    for i in range(10):
        if pxx==xkoordinates[i] and pxy==ykoordinates[i] and senesst[i]==0:
            logs.delete(senes[i])
            print(i)
            rezultats = rezultats +1
            senesst[i]= senesst[i] + 1
            print(rezultats)


 #   if pxx==sx1 and pxy==sy1 and sene1status==0:
 #       logs.delete(sene1)
 #       print("seeeneee 1")
 #       rezultats = rezultats +1
 #       sene1status = sene1status + 1
        
 #   if pxx==sx2 and pxy==sy2:
 #       logs.delete(sene2)
 #       print("seeeneee 2")
 #       rezultats = rezultats +1
    
 #   if pxx==sx3 and pxy==sy3:
 #       logs.delete(sene3)
 #       print("seeeneee 3")
 #       rezultats = rezultats +1
    
    if rezultats == 5 :
        uzvarteksts = logs.create_text(450, 450,  font=(None, 50), text="SPēle uzvarēta!!!!")
        
# REZULTATU TABLO

def rezultatutablo():
    buttonBG = logs.create_rectangle(100, 0, 200, 30, fill="red", outline="grey60")
    buttonTXT = logs.create_text(150, 15,  font=(None, 25), text=rezultats)



#KUSTĪBA _ staigājam apkārt...
player = logs.create_image(250,250, image = sarkG)
def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        logs.move(player, x_vel,y_vel)
        punkti()
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
    koordinates = logs.coords(player)
    #print(koordinates)

def on_keyrelease(event):
    global direction
    direction = None







#Master mainloops - izmaiņas un notikumi
master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()