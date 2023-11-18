import random

import art

import hangman_words

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# now, to clear the screen


# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

word_list = ["aardvark", "baboon", "camel"]

print(art.logo)

chosen_word = random.choice(hangman_words.word_list)

print(chosen_word)

user_progress = []

# user_display = ""

for char in chosen_word:
    user_progress.append("-")

is_game_over = False
no_lives = 7


print(f"No lives remaining: {no_lives}")

user_guess_list = []

# for x in range(len(chosen_word)):
#     if user_guess == chosen_word[x]:
#         user_progress[x] = chosen_word[x]


def check_and_replace(char):
    for x in range(len(chosen_word)):
        if char == chosen_word[x]:
            user_progress[x] = chosen_word[x]


def update_display():
    user_display = ""
    for char in user_progress:
        user_display += char
        user_display += " "
    print(user_display)


# print(user_progress)
while not is_game_over:
    print(user_progress)
    update_display()
    user_guess = input("Please guess a letter:\n").lower()
    cls()
    if user_guess in user_guess_list:

        print(f"You have guessed {user_guess} before")

    elif user_guess in chosen_word:

        user_guess_list.append(user_guess)
        check_and_replace(user_guess)
        print("Correct")
        if "-" not in user_progress:
            is_game_over = True
            game_mode = "win"
    else:

        user_guess_list.append(user_guess)
        print("Your guess is incorrect. Guess again")
        no_lives -= 1
        print(art.stages[no_lives])
        print(f"You have {no_lives} lives left")

        if no_lives == 0:
            is_game_over = True
            game_mode = "lose"


if game_mode == "win":
    print("Completed the word")
    print(f"The word was: {chosen_word}")
elif game_mode == "lose":
    print("You ran out of lives")
    print(f"The word was: {chosen_word}")
