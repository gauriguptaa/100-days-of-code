import random
from hangman_words import word_list
from hangman_art import stages,logo
from replit import clear


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
guessed_letters=[]
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in guessed_letters:
      print(f"You've already guessed {guess}")
    else:
      guessed_letters.append(guess)
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
            display[position] = letter
      if guess not in chosen_word:
         print(f"{guess} is not in the word, You've lost a life :/") 
         lives -= 1
    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True    
        print("You lose.")
        print(f"Correct Word was {chosen_word} ")    
