
def clear():
    import os
    os.system("clear")

clear()

import random
from game_data import data
# from art import logo, vs
import art

def randy():
    return (random.randint(0,len(data)-1))

print(art.logo)
print(art.vs)

# Add if statement for Actress to be "an actress"
# print(data[randy])



def guess():
    return input("Who has more followers? Type 'A' or 'B': \n").lower()

def compare_A():
        A = randy()
        return A
        
def compare_B():
    B = randy()
    return B

def compare_A_B():
    A = compare_A()
    B = compare_B()
    answer = []

    print (f"\nCompare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}.")
    print (f"\nAgainst B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}. \n")
    print(f"A count is {data[A]['follower_count']} , B count is {data[B]['follower_count']}")
    
    if data[A]['follower_count'] >= data[B]['follower_count']:
        print(f'A is bigger')
        answer = "A"
    else:
        print(f'B is bigger')
        answer = "B"

    if guess() == answer:
        compare_A_B()
    else:
        print("game over")



compare_A_B()