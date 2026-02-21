import pgzrun

WIDTH = 500
HEIGHT = 500

count = 0

alien = Actor('alien')

def draw():
    screen.fill(color = (128,0,0))
    
    alien.draw()
    screen.draw.text(f"Score: {count}", center = (400,10), fontsize = 30)

def on_mouse_down(pos):
    global count
    
    alien.pos = pos
    count += 1

pgzrun.go()