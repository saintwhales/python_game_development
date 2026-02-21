import pgzrun

WIDTH = 500
HEIGHT = 500

count = 0

alien = Actor('alien')

def draw():
    screen.fill(color = (128,0,0))

    screen.draw.text(f"Score: {count}", center = (400,10), fontsize = 30)

def place_alien():
    alien.x = (mouseX)
    alien.y = (mouseY)

def on_mouse_down(pos):
    global count

    place_alien()
    count += 1

pgzrun.go()