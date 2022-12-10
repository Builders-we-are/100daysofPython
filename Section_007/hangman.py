
# Step 3
import random
import os
os.system("clear")

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word = "aardvark"
word_length = len(chosen_word)
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
    print(display)

# TODO-1: - Use a while loop to let the user guess again. The loop
# should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

guess = input("Guess a letter: ").lower()
# Check guessed letter
while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    for position in range(word_length):
        if guess != chosen_word[position]:
            lives -= 1
            if lives == 0:
                print(f"You have {lives} live(s) left")
                break


print('You won')