import pgzrun
from random import randint

TITLE = "Circle"

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((0,0,0))#background colour of screen (black)

    r = 255
    g = 0
    b = randint(120,255)
 
    center = (150,150)

    radius = 20

    for i in range(15):
        screen.draw.circle(center, radius, (r, g, b))

        radius += 10

        r -= 10
        g += 10

pgzrun.go()