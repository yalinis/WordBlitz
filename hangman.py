import random
from termcolor import colored
import os

os.environ['FORCE_COLOR'] = '1'


def pick_secret_word():
    words = []
    f = open("Words", "r")
    for w in f:
        words.append(w.rstrip())
    r = random.randint(0, len(words) - 1)
    f.close()
    random_word = words[r]
    return random_word.upper()


def create_secret_word_list(secret_word):
    secret_word_list = []
    for letter in secret_word:
        secret_word_list.append(letter)
    return secret_word_list


def scramble_word(secret_word_list):
    shuffled_list = secret_word_list.copy()
    random.shuffle(shuffled_list)
    for letter in shuffled_list:
        print(colored(letter, "blue"), end=" ")
    print()


def check_word(secret_word_list, guessed_word_list):
    if len(secret_word_list) != len(guessed_word_list):
        return False

    for i in range(len(secret_word_list)):
        if secret_word_list[i] != guessed_word_list[i]:
            return False

    return True


game_over = False

print(colored("Welcome to Unscramble!", "blue"))

while game_over == False:
    secret_word = pick_secret_word()
    secret_word_list = create_secret_word_list(secret_word)
    print()
    print(colored("Here are your letters: ", "white"))
    scramble_word(secret_word_list)
    print()

    guessed_word = input("Guess the word (x to end): ")
    guessed_word = guessed_word.upper()
    guessed_word_list = create_secret_word_list(guessed_word)

    if check_word(secret_word_list, guessed_word_list) == True:
        print(colored("You got it right!", "blue"))

    else:
        print(colored("The word was: " + str(secret_word), "red"))

    if guessed_word == "X":
        game_over = True