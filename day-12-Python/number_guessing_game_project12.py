# Number Guessing Game

import random
from art import logo
from os import name,system


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def play_the_game(random_number, attempts):
    flag = True
    print(f"You have {attempts} attempts to guess the number")
    while attempts > 0 and flag:
        num = int(input("Make a Guess "))
        if num > random_number:
            print("Too High")
        elif num < random_number:
            print("Too Low")
        else:
            print(f"You've Got it , Generated number was {random_number}")
            flag = False
        attempts -= 1
    if flag:
        print(f"Sorry you've ran out of the attempts , Generated number was {random_number}")


play = True
while play:
    print(logo)
    game_level = input("Welcome to the number guessing game :)\nI'm thinking of "
                       "a number between 1 and 100\nchoose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level in ['easy', 'hard']:
        number = random.randint(1, 100)
        if game_level == 'easy':
            no_of_attempts = 10
        else:
            no_of_attempts = 5
        play_the_game(number, no_of_attempts)
        choice = input("Do you still want to continue the game 'y' or 'n' ").lower()
        if choice != 'y':
            play = False
        clear()

    else:
        print("Please select a valid level (easy / hard )")
        clear()

