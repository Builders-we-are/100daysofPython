
import art
from game_data import data
import random


def clear():
    import os
    os.system("clear")


clear()

# from art import logo, vs


score = 0
game_should_continue = True
account_b = random.choice(data)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}. from {account_country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """Take the user guess and follower counts and returns if they got it right. """
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


# Make the game repeatable
while game_should_continue:
    print(art.logo)
    # Making account at position B become the next account at position A.
    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear scren between rounds
    clear()
    # print(art.logo)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score:{score} . \n ")
    else:
        print(f"\n Sorry, that's wrong. Final score: {score} .\n")
        game_should_continue = False

    # Keep track of score
