import pgzrun
import random
WIDTH = 600
HEIGHT = 600
alien = Actor("alien")
alien.x = 300
alien.y = 300
text = "Click on alien"
def draw():
    screen.fill((193, 245, 236))
    alien.draw()
    screen.draw.text(text, (20, 20), color =(245, 193, 227))
def on_mouse_down(pos):
    global text
    print (alien.collidepoint(pos))
    if alien.collidepoint(pos) == True:
        alien.x = random.randint(50, 550) 
        alien.y = random.randint(50, 550)
        text = "Good shot!"
    else:
        text = "Bad shot!"
def update():
    pass
pgzrun.go()