
import random
"""
random.randint(0,1)

random_side == random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Texas", "ohio", "North_Dakota", "South_Dakota", "California", "oregon", "Louissiana", "Hawaii", "Utah", "Iowa", "Tennesse"]
states_of_america[1]="ohios"
print(states_of_america)
states_of_america.append("Alaska")
print(states_of_america)

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
print(names)
"""

states_of_america = ["Texas", "ohio", "North_Dakota", "South_Dakota", "California", "oregon", "Louissiana", "Hawaii", "Utah", "Iowa", "Tennesse"]
print(len(states_of_america))
State_to_move = random.choice(states_of_america)
print(State_to_move)
 