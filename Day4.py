# Exercise2 Banker Rouleete- Who will pay the bill?
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Using the split function allows you to separate a string components based on some sort of divider
# Split function on a string in the output, will divide the components into a list, separating all the words by a comma and a space

# print(names)
# print(names[0]) #this will print the first item in the list which is Angela
# now how do we get a random number to replace 0, first import random module then
# print(len(names)) just to check the total nunmber of items in the list
num_items = len(names)
# generate random numbers between 0 and the last index
# random_choice = random.randint(0, num_items - 1)   # this bcos the number start with 0 & end with total num - 1
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today.")