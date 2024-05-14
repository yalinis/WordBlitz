import pygame
from box import Box

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 20)
answer_font = pygame.font.SysFont('Comic Sans', 35)
save_message = my_font.render("Click to type: ", True, (0, 0, 0))
my_font_big = pygame.font.SysFont('Verdana', 30)

# set up variables for the display
width = 1200
length = 670
size = (width, length)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.png")

# text box
guess_box = pygame.Rect(0, 0, 1, 1)
guess_box_color = (255, 255, 255, 0)
guess_box_active = False

message_x = (width/2)

# user guess
guessed_word = ""
guessed_word = guessed_word.upper()
guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))

if len(guessed_word) == 1:
    message_x = (width / 2)
if len(guessed_word) == 2:
    message_x -= 15
if len(guessed_word) == 3:
    message_x -= 15
if len(guessed_word) == 4:
    message_x -= 15
if len(guessed_word) == 5:
    message_x -= 15
if len(guessed_word) == 6:
    message_x -= 15

# word 1: 3 letters
w1l1 = Box(500, 275, 1)
w1l2 = Box(575, 275, 1)
w1l3 = Box(650, 275, 1)

# word 2: 4 letters
w2l1 = Box(463, 375, 1)
w2l2 = Box(538, 375, 1)
w2l3 = Box(613, 375, 1)
w2l4 = Box(688, 375, 1)

# word 3: 5 letters
w3l1 = Box(500, 475, 1)
w3l2 = Box(575, 475, 1)
w3l3 = Box(650, 475, 1)
w3l4 = Box(725, 475, 1)
w3l5 = Box(425, 475, 1)

# word 4: 6 letters
w4l1 = Box(388, 575, 1)
w4l2 = Box(463, 575, 1)
w4l3 = Box(538, 575, 1)
w4l4 = Box(613, 575, 1)
w4l5 = Box(688, 575, 1)
w4l6 = Box(763, 575, 1)


run = True
# -------- Main Program Loop -----------
while run:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYUP and guess_box_active:
            # if the user presses backspace, remove the last letter from the text
            if event.key == 8:
                guessed_word = guessed_word[0:len(guessed_word) - 1]
                guessed_word = guessed_word.upper()
                guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))
                message_x += 15

            # otherwise, add the typed letter to the text field
            else:
                guessed_word += event.unicode
                guessed_word = guessed_word.upper()
                guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))
                if len(guessed_word) == 1:
                    message_x = (width / 2)
                if len(guessed_word) == 2:
                    message_x -= 15
                if len(guessed_word) == 3:
                    message_x -= 15
                if len(guessed_word) == 4:
                    message_x -= 15
                if len(guessed_word) == 5:
                    message_x -= 15
                if len(guessed_word) == 6:
                    message_x -= 15

        if event.type == pygame.MOUSEBUTTONUP:
            # activate text box
            #if guess_box.collidepoint(event.pos):
            guess_box_color = (255, 255, 255, 0)
            guess_box_active = True
            # de-activate the text box
            # else:
             #   guess_box_color = (0, 0, 0)
              #  guess_box_active = False

            # word 1
            w1l1.uncover_box()
            w1l2.uncover_box()
            w1l3.uncover_box()

            # word 2
            w2l1.uncover_box()
            w2l2.uncover_box()
            w2l3.uncover_box()
            w2l4.uncover_box()

            # word 3
            w3l1.uncover_box()
            w3l2.uncover_box()
            w3l3.uncover_box()
            w3l4.uncover_box()
            w3l5.uncover_box()

            # word 4
            w4l1.uncover_box()
            w4l2.uncover_box()
            w4l3.uncover_box()
            w4l4.uncover_box()
            w4l5.uncover_box()
            w4l6.uncover_box()


    screen.blit(bg, (0, 0))

    # typing
    screen.blit(save_message, (520, 150))
    pygame.draw.rect(screen, guess_box_color, guess_box, 3)
    screen.blit(guessed_word_display, (message_x, 195))

    # word 1
    screen.blit(w1l1.image, w1l1.rect)
    screen.blit(w1l2.image, w1l2.rect)
    screen.blit(w1l3.image, w1l3.rect)

    # word 2
    screen.blit(w2l1.image, w2l1.rect)
    screen.blit(w2l2.image, w2l2.rect)
    screen.blit(w2l3.image, w2l3.rect)
    screen.blit(w2l4.image, w2l4.rect)

    # word 3
    screen.blit(w3l1.image, w3l1.rect)
    screen.blit(w3l2.image, w3l2.rect)
    screen.blit(w3l3.image, w3l3.rect)
    screen.blit(w3l4.image, w3l4.rect)
    screen.blit(w3l5.image, w3l5.rect)

    # word 4
    screen.blit(w4l1.image, w4l1.rect)
    screen.blit(w4l2.image, w4l2.rect)
    screen.blit(w4l3.image, w4l3.rect)
    screen.blit(w4l4.image, w4l4.rect)
    screen.blit(w4l5.image, w4l5.rect)
    screen.blit(w4l6.image, w4l6.rect)

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()