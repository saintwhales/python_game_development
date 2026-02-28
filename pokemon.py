import pgzrun
from random import randint

WIDTH =600
HEIGHT = 400
 
score = 0
game_over = False

ash = Actor("ash")
ash.pos = 100,100

pikachu = Actor("pikachu")
pikachu.pos = 200,200

def draw():
    screen.blit("background2", (0,0))
    pikachu.draw()
    ash.draw()
    screen.draw.text("Score: "+str(score),
                     color = "black",
                     topleft = (10,10)
                     )
    
    if game_over:
        screen.fill("lightblue")
        screen.draw.text("Time's up! Your Final Score: " +str(score),
                        midtop = (WIDTH/2, 20),
                        fontsize = 40,
                        color = "darkblue"
                        )
        
def place_pikachu():
    pikachu.x = randint(70, WIDTH - 70)
    pikachu.y = randint(70, HEIGHT - 70)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if game_over:
        return
    
    if keyboard.left:
        ash.x = ash.x - 3
    if keyboard.right:
        ash.x = ash.x + 3
    if keyboard.up:
        ash.y = ash.y - 3
    if keyboard.down:
        ash.y = ash.y + 3

    if ash.colliderect(pikachu):
        score += 10
        place_pikachu()

clock.schedule(time_up, 60.0)
pgzrun.go()