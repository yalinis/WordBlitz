import pygame
from box import Box
from bird import Bird
import random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 20)
answer_font = pygame.font.SysFont('Comic Sans', 35)
won_font = pygame.font.SysFont('Comic Sans', 50)
save_message = my_font.render("Click to type: ", True, (0, 0, 0))
game_over_message = won_font.render("Game Over", True, (0, 0, 0))
won_message2 = won_font.render("You won!!", True, (0, 0, 0))
my_font_big = pygame.font.SysFont('Verdana', 30)

# set up variables for the display
width = 1200
length = 670
size = (width, length)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.png")
bird_start_y = 200
bird_start_x = 100
bird = Bird(bird_start_x, bird_start_y)

# text box
guess_box = pygame.Rect(0, 0, 1, 1)
guess_box_color = (255, 255, 255, 0)
guess_box_active = False

message_x = (width/2)

# user guess
guessed_word = ""
guessed_word = guessed_word.upper()
guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))

round = 1
word_guessed = False
guessed_word_checker = [ False, False, False, False ]
words_displayed = [ False, False, False, False]
round_over = False
game_won = False
game_over = False
touched = False
words_done = 0

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

# scrambling word:
def pick_secret_word(round):
    let_3 = []
    let_4 = []
    let_5 = []
    let_6 = []
    f = open("Words", "r") # opens a file called Words
    for w in f: # for the words in the file
        w = w.rstrip()
        if len(w) == 3:
            let_3.append(w)
        if len(w) == 4:
            let_4.append(w)
        if len(w) == 5:
            let_5.append(w)
        if len(w) == 6:
            let_6.append(w)
    if round == 1:
        r = random.randint(0, len(let_3) - 1)
        random_word = let_3[r]
    if round == 2:
        r = random.randint(0, len(let_4) - 1)
        random_word = let_4[r]
    if round == 3:
        r = random.randint(0, len(let_5) - 1)
        random_word = let_5[r]
    if round == 4:
        r = random.randint(0, len(let_6) - 1)
        random_word = let_6[r]


    f.close() # closes file

    return random_word.upper() # returns chosen word in uppercase


def create_secret_word_list(secret_word):
    secret_word_list = []
    for letter in secret_word:
        secret_word_list.append(letter)
    return secret_word_list

def scramble_word(secret_word_list):
    shuffled_list = secret_word_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

def check_word(secret_word_list, guessed_word_list):
    if len(secret_word_list) != len(guessed_word_list):
        return False

    for i in range(len(secret_word_list)):
        if secret_word_list[i] != guessed_word_list[i]:
            return False

    return True

def unscramble_word(round):
    if check_word:
        guessed_word_checker[round - 1] = True
        if round == 1:
            # word 1
            w1l1.uncover_box()
            w1l2.uncover_box()
            w1l3.uncover_box()

        if round == 2:
            # word 2
            w2l1.uncover_box()
            w2l2.uncover_box()
            w2l3.uncover_box()
            w2l4.uncover_box()

        if round == 3:
            # word 3
            w3l1.uncover_box()
            w3l2.uncover_box()
            w3l3.uncover_box()
            w3l4.uncover_box()
            w3l5.uncover_box()

        if round == 4:
            # word 4
            w4l1.uncover_box()
            w4l2.uncover_box()
            w4l3.uncover_box()
            w4l4.uncover_box()
            w4l5.uncover_box()
            w4l6.uncover_box()


secret_word = pick_secret_word(round)
secret_word_list = create_secret_word_list(secret_word)
scrambled_word = scramble_word(secret_word_list)

round1_word = secret_word
round2_word = ""
round3_word = ""
round4_word = ""

run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop

    clock.tick(60)
    if frame % 25 == 0:
        bird.switch_image()

    if guessed_word_checker[0] == True:
        bird.move_bird()
        if bird.move_bird() == True:
            guessed_word_checker[0] = False
            words_done += 1

    if guessed_word_checker[1] == True:
        bird.y = 350
        bird.move_bird()
        if bird.x == 1200:
            guessed_word_checker[1] = False
            words_done += 1


    if guessed_word_checker[2] == True:
        bird.y = 450
        bird.move_bird()
        if bird.x == 1200:
            guessed_word_checker[2] = False
            words_done += 1

    if guessed_word_checker[3] == True:
        bird.y = 550
        bird.move_bird()
        if bird.x == 1200:
            guessed_word_checker[3] = False
            words_done += 1


    if bird.rect.colliderect(w1l1.rect):
        touched = True
        print(touched)


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYUP and guess_box_active:
            # if the user presses backspace, remove the last letter from the text
            if event.key == 8:
                guessed_word = guessed_word[0:len(guessed_word) - 1]
                guessed_word = guessed_word.upper()
                guessed_word_list = create_secret_word_list(guessed_word)
                guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))
                message_x += 15

            # otherwise, add the typed letter to the text field
            elif event.key != 13:
                guessed_word += event.unicode
                guessed_word = guessed_word.upper()
                guessed_word_list = create_secret_word_list(guessed_word)
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
                if len(guessed_word) == 7:
                    message_x -= 15

        if event.type == pygame.MOUSEBUTTONUP:
            # activate text box
            guess_box_color = (255, 255, 255, 0)
            guess_box_active = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            checking = check_word(secret_word_list, guessed_word_list)
            if checking:
                word_guessed = True


        if keys[pygame.K_RETURN] and word_guessed == True:
            bird.move_bird()
            if round == 1:
                unscramble1 = unscramble_word(1)
            if round == 2:
                unscramble1 = unscramble_word(2)
            if round == 3:
                unscramble1 = unscramble_word(3)
            if round == 4:
                unscramble1 = unscramble_word(4)

            if round < 5:
                round += 1
            elif round == 5:
                game_won = True
            round_over = True

        if keys[pygame.K_RETURN] and word_guessed == True and round_over == True and game_won == False and round < 5:
            word_guessed = False
            round_over = False
            secret_word = pick_secret_word(round)
            secret_word_list = create_secret_word_list(secret_word)
            scrambled_word = scramble_word(secret_word_list)
            print(secret_word_list)

            if round == 2:
                round2_word = secret_word_list
            if round == 3:
                round3_word = secret_word_list
            if round == 4:
                round4_word = secret_word_list

            guessed_word = guessed_word[0:len(guessed_word) - len(guessed_word)]
            guessed_word = guessed_word.upper()
            guessed_word_list = create_secret_word_list(guessed_word)
            guessed_word_display = answer_font.render(guessed_word, True, (0, 0, 0))


    screen.blit(bg, (0, 0))

    # won game
    if words_done == 4:
        screen.blit(game_over_message, (475, 250))
        screen.blit(won_message2, (500, 315))


    else:
        # typing
        screen.blit(save_message, (540, 160))
        pygame.draw.rect(screen, guess_box_color, guess_box, 3)
        screen.blit(guessed_word_display, (message_x, 200))
        screen.blit(bird.image, bird.rect)
        if round == 1:
            blit_position = 550
        if round == 2:
            blit_position = 530
        if round == 3:
            blit_position = 510
        if round == 4:
            blit_position = 480
        for letter in scrambled_word:
            letter_blit = answer_font.render(letter, True, (0, 0, 0))
            screen.blit(letter_blit, (blit_position, 75))
            blit_position += 50

       # print(round, words_displayed)

        if round == 1:
            words_displayed[0] = True


        if round == 1 or words_displayed[0] == True:
            blit_position_y = 285
            blit_position_x = 515
            for letter in round1_word:
                word_blit = answer_font.render(letter, True, (0, 0, 0))
                screen.blit(word_blit, (blit_position_x, blit_position_y))
                blit_position_x += 75

        if round == 2:
            words_displayed[1] = True


        elif round == 2 or words_displayed[1] == True:
            blit_position_y = 385
            blit_position_x = 478
            for letter in round2_word:
                word_blit = answer_font.render(letter, True, (0, 0, 0))
                screen.blit(word_blit, (blit_position_x, blit_position_y))
                blit_position_x += 75

        if round == 3:
            words_displayed[2] = True

        elif round == 3 or words_displayed[2] == True:
            blit_position_y = 485
            blit_position_x = 440
            for letter in round3_word:
                word_blit = answer_font.render(letter, True, (0, 0, 0))
                screen.blit(word_blit, (blit_position_x, blit_position_y))
                blit_position_x += 75

        if round == 4:
            words_displayed[3] = True

        elif round == 4 or words_displayed[3] == True:
            blit_position_y = 585
            blit_position_x = 403
            for letter in round4_word:
                word_blit = answer_font.render(letter, True, (0, 0, 0))
                screen.blit(word_blit, (blit_position_x, blit_position_y))
                blit_position_x += 75


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

    frame += 1

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()