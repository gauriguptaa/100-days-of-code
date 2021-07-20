#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
person_paying_bill=names[random.randint(0,len(names)-1)]
print(f"{person_paying_bill} is going to buy the meal today!")
