
import re
import os
os.system("clear")
print("\n \n \n \n \n \n")

my_list = input("What is your list?").strip("[]").split(",")

# my_list = input("What is your list?")
# my_list=[int(ii) for ii in my_list[1:-1].split(',')]

def find_total(my_list) :
    total = 0
    for i,integer in enumerate(my_list):
        if i % 2 == 0:
            total += int(integer)
        if i % 2 != 0:
            total -= int(integer)
    return total

print(find_total(my_list))

#One liner

# from functools import reduce
# print(reduce(lambda total, v: total + (-v[1] if v[0]%2 else v[1]), enumerate([int(i) for i in input("What is your list?").strip('[]').split(',')]), 0))


# my_list = re.compile("\d+").findall(input("What is your list?"))
# print(my_list)