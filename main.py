import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 20)
my_font_big = pygame.font.SysFont('Verdana', 30)

# set up variables for the display
size = (1200, 600)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.jpg")

run = True
# -------- Main Program Loop -----------
while run:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, (0, 0))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()