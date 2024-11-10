import pgzrun 

HEIGHT = 500 
WIDTH = 500 
from random import randint
def draw(): 
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255) 
    width = WIDTH - 200 
    height = HEIGHT - 400
    for i in range(10):
        rect = Rect((0,0),(width,height)) 
        rect.center = 250,250 
        screen.draw.rect(rect,(r,g,b))  

        width -= 10 
        height += 10

pgzrun.go()