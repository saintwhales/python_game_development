import pgzrun

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
ball = Actor('ball')

def draw():
    screen.fill(color = (128,0,0))
    
    alien.draw()
    ball.draw()

def on_mouse_down(pos):
    alien.pos = pos

def on_key_pressed():
    ball.pos = 

pgzrun.go()