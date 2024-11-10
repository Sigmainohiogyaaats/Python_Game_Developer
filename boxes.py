import pgzrun
import random

WIDTH = 500
HEIGHT = 600

rectangles = []

# Generate random RGB values for the rectangles
def generate_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Generate 10 rectangles with decreasing width and increasing height
for i in range(10):
    r, g, b = generate_random_color()
    width = WIDTH - i * 10
    height = HEIGHT - 500 + i * 10
    corner1 = (250 - width // 2, 300 - height // 2)
    corner2 = (corner1[0] + width, corner1[1] + height)
    rectangles.append(Rect(corner1, corner2, (r, g, b)))

# Main drawing function
def draw():
    screen.fill('teal')
    for rect in rectangles:
        screen.draw.rect(rect, rect.color)

pgzrun.go()
