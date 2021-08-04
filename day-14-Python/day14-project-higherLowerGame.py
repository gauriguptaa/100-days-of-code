from art import logo, vs
from game_data import data
import random
import os


def gen_game_data():
    games_data = random.choice(data)
    return games_data


def print_game_data(game_data, choice):
    print(f"Compare {choice}: {game_data['name']},{game_data['description']}, from {game_data['country']} ")


keep_on_playing = True
first_play = True
while keep_on_playing:

    first = "A"
    second = "B"
    correct_choice = "A"
    score = 0
    game_data1 = gen_game_data()
    while first_play:
        print(logo)
        print_game_data(game_data1, first)
        print(vs)
        game_data2 = gen_game_data()
        print_game_data(game_data2, second)
        option = input("Who has more follower type (A/B):").upper()
        if option not in ["A", "B"]:
            print("Invalid option")
        else:
            if game_data1['follower_count'] < game_data2['follower_count']:
                correct_choice = "B"
            if option == correct_choice:
                score += 1
                game_data1 = game_data2
                keep_on_playing = False
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"Sorry that's wrong , your final score is {score}")
                keep_on_playing = False
                first_play = False

