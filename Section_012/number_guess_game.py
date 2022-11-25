
import random
import math
import os
os.system("clear")

print("\n \n \n \n \n \n \n")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

value = random.randint(0, 100)
print(f"\nPssst, the correct answer is {value} \n")

mode = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
mode_dict = {
    'easy': 10,
    'hard': 5,
}

attempts = mode_dict[mode]
print(f"You have {attempts} remaining to guess the number.")

while attempts != 0:
    guess = int(input("\nMake a guess: "))
    if guess == value:
        print(f"You got it! The answer was {value} \n")
        break
    elif guess > value:
        print("Too high. \nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < value:
        print("Too low. \nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")


if attempts == 0:
    print("You've run out of guesses, you lose. \n")
