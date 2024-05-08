import pygame
from box import Box

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 20)
my_font_big = pygame.font.SysFont('Verdana', 30)

# set up variables for the display
size = (1000, 1000)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.jpg")

b1 = Box(300, 400, 1)


run = True
# -------- Main Program Loop -----------
while run:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            b1.uncover_box()


    screen.blit(bg, (0, 0))
    screen.blit(b1.image, b1.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()