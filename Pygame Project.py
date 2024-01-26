import pygame, sys

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

# Creating a rectangle and its parameters
rect = pygame.Rect(50, 10, 200, 100)

# Looking for the user closing the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Screen color
    screen.fill(background_color)

    # Drawing a rectangle and changing its properties
    pygame.draw.rect(screen, red, rect, 5, 20)

    # Refreshing screen
    pygame.display.flip()

    # Setting the frame rate
    clock.tick(60)
