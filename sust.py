# introduce the libraries 
#set the background with images 
#set the images for the game 
#make the movement of the images 
#make the paper bag if you click correct and the others wrong
# set a winner and loser screen 


import pgzrun 
import random 

WIDTH = 650
HEIGHT = 400
finallevel = 5 
startspeed = 10
ITEMS = ['bottle','bat','plastic bag'] 
game_over = False 
currentlevel = 1 
items = [] 
animations = []  
game_complete = False

# Create an Actor with your background image
background = Actor("reduce")  # without the file extension

# Resize the background to fit the screen
background.width = WIDTH
background.height = HEIGHT


def draw(): 
    screen.clear()  
    background.draw()   


   
    if game_over : 
        display_message('game over','try again') 
    elif game_complete: 
        display_message('wow you beat it','well done') 
    else:
        for item in items:
            item.draw()
    
def update():  
    global items
    if len(items) == 0:
        items = make_items(currentlevel)
def make_items(num_of_extra_items):  
    items_to_create = get_option_to_create(num_of_extra_items) 
    new_items = create_items(items_to_create) 
    layout_items(new_items) 
    animate_items(new_items) 
    return new_items 

def get_option_to_create(num_of_extra_items): 
    items_to_create = ['paper'] 
    for i in range (0,num_of_extra_items):  
        random_option = random.choice(ITEMS) 
        items_to_create.append(random_option)
    return items_to_create 

def create_items(items_to_create) :
    new_items = [] 
    for i in items_to_create: 
        item = Actor(i)
        new_items.append(item) 
    return new_items  

def layout_items(items_to_layout): 
    number_of_gaps = len(items_to_layout) + 1 
    gap_size = WIDTH /number_of_gaps  
    random.shuffle(items_to_layout)
    for i, item in enumerate(items_to_layout): 
        new_x_pos = (i + 1) * gap_size 
        item.x = new_x_pos 

def animate_items(items_to_animate):  
    global animations 
    for item in items_to_animate: 
        duration = startspeed - currentlevel 
        item.anchor = ('center', 'bottom') 
        animation = animate(item, duration=duration, on_finished=handle_game_over, y = HEIGHT) 
        animations.append(animation) 

def handle_game_over():
    global game_over 
    game_over = True   


def on_mouse_down(pos):   
    for item in items: 
        if item.collidepoint(pos):  
            if 'paper' in item.image: 
                move_to_nextlevel() 
            else: 
                handle_game_over()

def move_to_nextlevel():  
    global game_complete,animations,items,currentlevel
    stop_animation(animations) 
    if currentlevel == finallevel: 
        game_complete = True 
    else: 
        currentlevel += 1 
        items = []
        animations = []
         
def stop_animation(animation_to_stop):  
    global items
    for animation in animation_to_stop: 
        if animation.running: 
            animation.stop()  

def display_message(heading_text, subheading):
    screen.draw.text(heading_text, fontsize = 60, center = (WIDTH/2,HEIGHT/2),color = 'black')
    screen.draw.text(subheading, fontsize = 30, center = (WIDTH/2,HEIGHT/2+30),color = 'black')      








pgzrun.go()



