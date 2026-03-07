import pgzrun

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
ball = Actor('ball')

def draw():
    screen.fill(color = (128,0,0))
    
    alien.draw()
    ball.draw()

def alien_move():
    if keyboard.left:
        alien.x = alien.x - 2

    if keyboard.right:
        alien.x = alien.x + 2

    if keyboard.up:
        alien.y = alien.y - 2

    if keyboard.down:
        alien.y = alien.y + 2

def ball_move():
    if keyboard.a:
        ball.x = ball.x - 2

    if keyboard.d:
        ball.x = ball.x + 2

    if keyboard.w:
        ball.y = ball.y - 2

    if keyboard.s:
        ball.y = ball.y + 2

alien_move()
ball_move()
draw()

pgzrun.go()