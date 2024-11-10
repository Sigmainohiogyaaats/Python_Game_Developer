import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 300

WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skibidi Touch Game")

toilet_image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game dev 1\lesson 5\images\kanke.png')
camera_man_image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game dev 1\lesson 5\images\skibdidi.png')
background_image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game dev 1\lesson 5\images\field.jpg')


toilet_image = pygame.transform.scale(toilet_image, (50, 50))  # Adjust size as necessary
camera_man_image = pygame.transform.scale(camera_man_image, (50, 50))  # Adjust size as necessary


toilet_rect = toilet_image.get_rect()
camera_man_rect = camera_man_image.get_rect()


toilet_rect.topleft = (100, 200)
camera_man_rect.topleft = (200, 200)


score = 0
speed = 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        toilet_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        toilet_rect.x += speed
    if keys[pygame.K_UP]:
        toilet_rect.y -= speed
    if keys[pygame.K_DOWN]:
        toilet_rect.y += speed

   
    if toilet_rect.left < 0:
        toilet_rect.left = 0
    if toilet_rect.right > WIDTH:
        toilet_rect.right = WIDTH
    if toilet_rect.top < 0:
        toilet_rect.top = 0
    if toilet_rect.bottom > HEIGHT:
        toilet_rect.bottom = HEIGHT

    # Check
    if toilet_rect.colliderect(camera_man_rect):
        score += 1
        camera_man_rect.x = random.randint(0, WIDTH - camera_man_rect.width)
        camera_man_rect.y = random.randint(0, HEIGHT - camera_man_rect.height)

   
    screen.blit(background_image, (0, 0))
    screen.blit(toilet_image, toilet_rect)
    screen.blit(camera_man_image, camera_man_rect)

    
    pygame.display.flip()


pygame.quit()




