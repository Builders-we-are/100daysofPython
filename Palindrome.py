import random
word_list = ["racecar", "baboon", "camel","kayak","rotator"]
chosen_word = random.choice(word_list)
print(f'Pssst, the random word chosen is {chosen_word}.')

# For the main word
display = []
for n in range(len(chosen_word)):
    display.append(chosen_word[n])

real_word = ""
for n in range(len(display)):
    real_word += display[n]

# For the flipped version
display.reverse()
flipped_word = ""
for n in range(len(display)):
    flipped_word += display[n]

# If test for equal
if real_word == flipped_word:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
 
