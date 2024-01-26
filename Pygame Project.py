import pygame, sys

# Setup of pygame library
pygame.init()

clock = pygame.time.Clock()

# Window settings and name
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("My Game")

# Looking for the user closing the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Screen updating and background color
    screen.fill("white")
    pygame.display.flip()

    # Setting the frame rate
    clock.tick(60)
