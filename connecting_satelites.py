import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satelites = []

lines = []

next_satelite = []

start_time = 0
total_time = 0

total_satelites= 7

def createSatelites():
    global start_time, satelites, lines, next_satelite

    satelites = []
    lines = []
    next_satelite = 0

    for i in range(total_satelites):
        satelite = Actor("satelite")
        satelite.pos = randint(60, WIDTH-60), randint(60, HEIGHT-60)
        satelites.append(satelite)

    start_time = time()

def draw():
    global total_time

    screen.blit("background", (0,0))
    number = 1
    for satelite in satelites:
        satelite.draw()
        screen.draw.text(
            str(number),
            center = (satelite.x, satelite.y + 40),
            fontsize = 35,
            color = "white",
            owidth =1.5,
            ocolor = "black"
        )

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,150))
    
    if next_satelite < total_satelites:
        total_time = time() - start_time

    screen.draw.text(
        "Time: "+str(round(total_time, 1)),
        (10,10),
        fontsize = 40,
        color = "cyan",
        owidth = 1.5,
        ocolor = "black"
    )

    if next_satelite == total_satelites:
        screen.draw.text(
            "Constellation Completed!",
            center = (WIDTH/2, 50),
            fontsize = 50,
            color = "yellow",
            owidth = 1.5,
            ocolor = "black"
        )

def on_mouse_down(pos):
    global next_satelite

    if next_satelite < total_satelites:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite > 0:
                lines.append((satelites[next_satelite -1].pos, satelites[next_satelite].pos))
            next_satelite += 1
    
    else:
        createSatelites()

createSatelites()
pgzrun.go