import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options=[rock,paper,scissors]
choice=int(input("What do you choose ? 0 - Rock , 1 - Paper , 2 - scissors.\n"))
if choice >=0 and choice <=2:
  print(options[choice])
  computer_choice=random.randint(0,2)
  print(options[computer_choice])
  choice_matrix=[["It's a draw","You lose","You win"],["You win","It's a draw","You lose"],["You lose","You win","It's a draw"]]
  print(choice_matrix[choice][computer_choice])
else:
  print("Please enter a valid choice")  
