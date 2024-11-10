import pgzrun 
import random 
import pygame 

#screen dimension 
WIDTH = 1000
HEIGHT = 500

#game variable 
score = 0 
game_over = False 
enemies = []  
fireballM = True 
enemydead = 0 


#images 
naruto = Actor('naruto') 
naruto.pos = 340,300
fireball= Actor('rasengan') 
fireball.pos = -100,-100 

def enemy(): 
    num = 0 
    enemy_images = ['itachi', 'kisame', 'kushimaru', 'raiga', 'zabuza'] 
    for i in range (6): 
        print (i)
        temp = Actor(random.choice(enemy_images)) 
        enemies.append(temp ) 
        enemies[i].pos = ( 125*num + 40,50 )
        num += 1 
enemy() 

def fire(): 
    global fireballM  
    fireball.pos = (naruto.x,naruto.y) 
    fireballM = True 
    

        
def draw(): 
    screen.blit('bg', (0,0)) 
    naruto.draw() 
    fireball.draw()

    for i in enemies: 
        i.draw() 
        i.y = i.y+1
    # movement of fireball  
    if fireballM == True: 
        fireball.y = fireball.y - 7
    if game_over : 
        screen.clear() 
        screen.fill('red') 
        screen.draw.text('you lose fucking nigger go to the fied black ass', center = (500,250), fontsize = 180) 
    if enemydead == 6: 
            screen.clear() 
            screen.fill('green') 
            screen.draw.text('you win', center = (500,250), fontsize = 180) 
    

def update():  
    global enemies,enemydead
    global game_over
    if keyboard.a: 
        if naruto.x > 10: 
            naruto.x = naruto.x-10 
    elif keyboard.d: 
        if naruto.x < 670: 
            naruto.x = naruto.x + 10
    elif keyboard[keys.SPACE]: 
        fire() 
    for k in enemies:  
        if k.y > 450: 
            game_over = True 
    for l in enemies: 
        if fireball.colliderect(l) :
            print('hit') 
            enemies.remove (l) 
            enemydead += 1
            fire.pos = (2000,2000)



        

pgzrun.go() 
pygame.quit()


