import pygame
from box_cover import Box_cover
from box_empty import Box_empty

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 20)
my_font_big = pygame.font.SysFont('Verdana', 30)

# set up variables for the display
size = (1200, 600)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.jpg")


bcw1 = Box_cover(500, 250)
bew1 = Box_empty(500, 250)
bcw2 = Box_cover(575, 250)
bew2 = Box_empty(575, 250)
bcw3 = Box_cover(650, 250)
bew3 = Box_empty(650, 250)


run = True
# -------- Main Program Loop -----------
while run:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, (0, 0))
    screen.blit(bew1.image, bew1.rect)
    screen.blit(bcw1.image, bcw1.rect)
    screen.blit(bew2.image, bew2.rect)
    screen.blit(bcw2.image, bcw2.rect)
    screen.blit(bew3.image, bew3.rect)
    screen.blit(bcw3.image, bcw3.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()