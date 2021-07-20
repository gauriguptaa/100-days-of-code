#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

toss=random.randint(0,1)
print("Heads") if toss == 1 else print("Tails")
