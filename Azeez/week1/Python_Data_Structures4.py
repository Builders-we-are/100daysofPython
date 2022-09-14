# List comprehension
#get values within a range
under_10 = [x for x in range(10)]
print(under_10)

#get squared values
squares = [x**2 for x in under_10]
print(squares)

#delete an item from a list
import random
letters = [x for x in "ABCDEF"]
random.shuffle(letters)
letrs = [a for a in letters if a != "C"]
print(letters, letrs)

#Append and pop from a stack
my_stack = list()
my_stack.append(12)
my_stack.append(8)
my_stack.append(6)
my_stack.append(7)
print(my_stack)

print(my_stack.pop())
print(my_stack)