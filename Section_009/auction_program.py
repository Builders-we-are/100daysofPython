


import os
import math
from time import sleep

def clear():
    os.system("clear")

# sleep(0)

print("Welcome to the secret auction program")
auction = { }
maxx = int(0)
others = "yes"

while others == "yes" or others =="y":
    name = input("What is your name? ")
    bid = int(input('What is your bid? $ '))
    others = input('Are there any other bidders? Yes or No? ').lower()

    auction[name] = bid
    clear()

else:
    for names in auction:
        if auction[names] > maxx:
            winner = names
            maxx = auction[names]

print(f"The winner is {winner} with a bid of ${maxx}")

