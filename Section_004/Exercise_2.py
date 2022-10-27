
import random
# # # 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# # Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# # 🚨 Don't change the code above 👆

# states = ["",""]
# states.extend(["Delaware","NY"]) 
# # states.append()="Penn"

# print(states)

# #Write your code below this line 👇

# flip = random.randint(0,len(names)-1)

print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")
