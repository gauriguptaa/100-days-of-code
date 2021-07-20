#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

'''
password=''
for num in range(nr_letters):
  password+=random.choice(letters)
for num in range(nr_symbols):
  password+=random.choice(symbols)
for num in range(nr_numbers):
  password+=random.choice(numbers)

random_password=''
for i in range(len(password)):
  random_password+=random.choice(password)

print(f"This is your generated password: {random_password}")  


'''
#Random.choice doesn't include unique values where

password = []
password.extend(random.sample(letters,nr_letters))
password.extend(random.sample(symbols,nr_symbols))
password.extend(random.sample(numbers,nr_numbers))

random_password = []
random_password.extend(random.sample(password,len(password)))

print(f"This is your generated password: {''.join(str(e) for e in random_password)}")
