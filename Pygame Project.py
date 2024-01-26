import pygame, sys, math

# Setup of pygame library
pygame.init()

clock = pygame.time.Clock()

# Window settings and name (pygame y is backwards, but not x)
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Defining colors
white = pygame.Color(255, 255, 255, 1)
red = pygame.Color(255, 0, 0, 1)
green = pygame.Color(0, 255, 0, 1)
blue = pygame.Color(0, 0, 255, 1)
purple = pygame.Color(255, 0, 255, 1)

# Defined colors for specific uses
background_color = white

# Defining the plumber image
apple = pygame.image.load("apple.png")
apple_rect = apple.get_rect()
apple_rect = apple_rect.move(10, 10)
# apple = pygame.transform.scale(apple, (200, 200))
# apple = pygame.transform.rotate(apple, 180)

# Have the dimensions of the screen for tracking purposes
screen_rect = screen.get_rect()

point = (150, 15)

obstacle = pygame.Rect(0, 200, 100, 10)


# Defining how the collision detection works
def check_for_collision():
    if apple_rect.x <= 0 or apple_rect.x + apple_rect.width >= screen_rect.width or apple_rect.y <= 0 or apple_rect.y + apple_rect.height >= screen_rect.height:
        return True
    if apple_rect.colliderect(obstacle):
        return True
    if apple_rect.collidepoint(point[0], point[1]):
        return True
    return False


# Creating shapes and their parameters (the rect transformations are unique to rects)
rect = pygame.Rect(100, 50, 100, 100)
# rect = rect.move(-50, 50)
# rect = rect.inflate(100, 100)
# rect = rect.inflate(-75, -75)
rect.update(50, 100, 200, 150)
triangle_coordinates = [(100, 50), (125, 100), (75, 100)]
circle_x = 50
circle_y = 50

# Looking for the user closing the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Screen color
    screen.fill(background_color)

    # Drawing a rectangle and changing its properties (coordinates are for top right corner)
    # pygame.draw.rect(screen, red, rect, 5, 20)

    # Drawing a circle (coordinates are for center)
    # pygame.draw.circle(screen, "blue", (100, 100), 50)

    # Drawing a polygon, specifically a triangle
    # pygame.draw.polygon(screen, "green", triangle_coordinates)

    # Border for image if there was no background, and image created
    # pygame.draw.rect(screen, "black", apple_rect, 1)

    # Checking for collision between image and screen edge
    if not check_for_collision():
        apple_rect = apple_rect.move(1, 0)

    pygame.draw.rect(screen, "red", obstacle)
    screen.blit(apple, apple_rect)


    # Moving a circle
    # circle_x += 1
    # circle_y += 1
    # pygame.draw.circle(screen, "red", (circle_x, circle_y), 50)

    # Drawing lines
    # pygame.draw.line(screen, "black", (50, 50), (200, 100), 5)
    # pygame.draw.lines(screen, "blue", False, [(50, 250), (50, 50), (250, 250), (250, 50)], 5)

    # Drawing ellipses and arc
    # pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 100, 200), 1)
    # pygame.draw.ellipse(screen, "green", pygame.Rect(50, 50, 100, 200)
    # pygame.draw.arc(screen, "purple", pygame.Rect(50, 50, 100, 100), 0, math.pi, 5)

    # pygame.draw.rect(screen, "blue", rect)

    # Refreshing screen
    pygame.display.flip()

    # Setting the frame rate
    clock.tick(60)
