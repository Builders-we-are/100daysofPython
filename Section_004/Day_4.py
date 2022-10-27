import random

print("What do you choose? \n Type 0 for Rock \n Type 1 for Paper \n Type 2 for Scissors. \n")

# my_choice = int(input("I chooose ..."))
my_choice = random.randint(0,2)
cpu_choice = random.randint(0,2)

choices = ["Rock","Paper","Scissors"]
print(f"{choices[my_choice]} versus {choices[cpu_choice]}")

print(my_choice , cpu_choice)

if my_choice == cpu_choice:
    print ("Draw game")

elif my_choice == 0:
    if cpu_choice == 2:
        print("You win")
    else:
        print("You lose")

elif my_choice == 1:
    if cpu_choice == 0:
        print("You win")
    else:
        print("You lose")

elif my_choice == 2:
    if cpu_choice == 1:
        print("You win")
    else:
        print("You lose")



