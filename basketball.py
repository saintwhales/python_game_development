import pgzrun

TITLE = "Basketball Shooter"
WIDTH = 600
HEIGHT = 500

ball = Actor('ball')
hoop = Actor('hoop')

ball.pos = (80, HEIGHT - 60)
hoop.pos = (WIDTH - 80, 150)

vx = 0
vy = 0
gravity = 0.5
shooting = False
score = 0 

def draw():
    screen.clear()
    screen.fill((30,120,30))

    ball.draw()
    hoop.draw()

    screen.draw.text(f"Score: {score}", (10,10), fontsize = 30)

def update():
    global vx, vy, shooting, score

    if shooting:
        ball.x += vx
        ball.y += vy
        vy += gravity

    if hoop.left < ball.x < hoop.right and hoop.top < ball.y < hoop.bottom:
        score += 1
        reset_ball()

    if ball.y > HEIGHT or ball.x >WIDTH:
        reset_ball()

def on_mouse_down(pos):
    global vx, vy, shooting

    if not shooting:
        dx = pos[0] - ball.x
        dy = pos[1] - ball.y

        vx = dx / 20
        vy = dy / 20

        shooting = True
    
def reset_ball():
    global vx, vy, shooting
    ball.pos = (80,HEIGHT-60)
    vx = 0
    vy = 0
    shooting = False

pgzrun.go()
    