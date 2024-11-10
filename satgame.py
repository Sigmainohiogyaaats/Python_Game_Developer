import pgzrun
from time import time  
from random import randint

WIDTH = 600 
HEIGHT = 500  

satellites = [] 
lines = [] 

start_time = 0
total_time = 0
end_time = 0 
total_sats = 8  
next_satellite = 0
def create_satellite(): 
    global start_time
    for count in range(0,total_sats): 
        satellite = Actor('sat') 
        satellite.pos = randint(20,WIDTH - 20) ,randint(20,HEIGHT - 20)  
        satellites.append(satellite) 
    start_time = time() 

def draw():  
    global total_time
    screen.blit('bg',(0,0)) 
    number = 1 
    for satellite in satellites: 
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1] + 15)) 
        satellite.draw()
        number += 1  

    for line in lines: 
        screen.draw.line(line[0], line[1], 'orange')  

    if next_satellite < total_sats: 
        total_time = time() - start_time   
        screen.draw.text(str(round(total_time,1)), (40,10), fontsize = 40)
    else: 
        screen.draw.text(str(round(total_time,1)), (40,10), fontsize = 40) 

def update(): 
    pass 

def on_mouse_down(pos):  
    global next_satellite, lines
    if next_satellite < total_sats: 
        if satellites[next_satellite].collidepoint(pos): 
            if next_satellite : 
                lines.append((satellites[next_satellite-1].pos , satellites[next_satellite].pos) )
            next_satellite += 1 
        else:  
            lines = []
            next_satellite = 0




create_satellite() 
pgzrun.go()


        



