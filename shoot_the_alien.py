import pgzrun 
from random import randint 
#capitals because it is a constant vaiable
TITLE = 'good shot' 
WIDTH = 600
HEIGHT = 700 

dog = Actor('doggo') 
dog.pos = 150,150
message = ''

def draw(): 
    screen.clear 
    screen.fill('blue') 
    dog.draw() 
    screen.draw.text(message,center = (100,100), fontsize = 27)

def changeplace(): 
    dog.x = randint(50,WIDTH - 50) 
    dog.y = randint(50,HEIGHT - 50) 
def on_mouse_down(pos):  
    global message
    if dog.collidepoint(pos): 
        message = 'good shot'   
        changeplace() 
    else: 
        message = 'you missed'




changeplace()
pgzrun.go()