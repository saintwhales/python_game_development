import pgzrun

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.pos = (100,250)
ball = Actor('ball')
ball.pos = (400,250)

def draw():
    screen.fill((128,0,0))
    
    alien.draw()
    ball.draw()

def update():

    #1st charactor
    if keyboard.left:
        alien.x = alien.x - 2

    if keyboard.right:
        alien.x = alien.x + 2

    if keyboard.up:
        alien.y = alien.y - 2

    if keyboard.down:
        alien.y = alien.y + 2

    #2nd charactor
    if keyboard.a:
        ball.x = ball.x - 2

    if keyboard.d:
        ball.x = ball.x + 2

    if keyboard.w:
        ball.y = ball.y - 2

    if keyboard.s:
        ball.y = ball.y + 2

pgzrun.go()