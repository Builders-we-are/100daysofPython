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

#Write your code below this line 👇
r_p_s = [rock, paper, scissors]
import random

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
computer = random.randint(0, 2)

if computer == 0 and you == 2:
  you = -1
if computer > you:
  print (f"{r_p_s[you]}\nComputer chose:\n{r_p_s[computer]}\nYou lose")
elif computer < you:
  print (f"{r_p_s[you]}\nComputer chose:\n{r_p_s[computer]}\nYou win")
else:
  print (f"{r_p_s[you]}\nComputer chose:\n{r_p_s[computer]}\nTie")
