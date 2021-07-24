#This is a capstone project it can be improved with using functions (TODO :- add functions and modularize code )

import random
from art import logo
from os import system,name
import time

'''
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
'''


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


play = True

while play:
    print(logo)
    choice = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ").lower()
    keep_on_playing = True
    if choice == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_cards = []
        opponent_cards = []
        player_score = 0
        opponent_score = 0
        player_cards.extend(random.sample(cards, 2))
        opponent_cards.extend(random.sample(cards, 2))
        while keep_on_playing:
            if 11 in player_cards:
                if player_score > 10:
                    index = player_cards.index(11)
                    player_cards[index] = 1
            if 11 in opponent_cards:
                if opponent_score > 10:
                    index = opponent_cards.index(11)
                    opponent_cards[index] = 1
            player_score = sum(player_cards)
            opponent_score = sum(opponent_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's First Card: {opponent_cards[0]}")
            if opponent_score < 17:
                opponent_cards.extend(random.sample(cards, 1))
                
            if opponent_score > 21 or player_score == 21:
                print("You Win :)")
                time.sleep(5)
                clear()
                break
            elif player_score > 21 or opponent_score == 21:
                print("You lost :/")
                time.sleep(5)
                clear()
                break
            else:
                option = input("Type 'y' to get another card , type 'n' to pass: ").lower()
                if option == 'y':
                    player_cards.extend(random.sample(cards, 1))
                    opponent_cards.extend(random.sample(cards, 1))
                else:
                    keep_on_playing = False
                    if opponent_score > player_score:
                        print("You lost :/")
                    elif opponent_score == player_score:
                        print("Game has draw")
                    else:
                        print("You Win :)")
                    time.sleep(5)
                    clear()

    else:
        play = False

