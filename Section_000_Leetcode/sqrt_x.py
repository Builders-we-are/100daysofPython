


import os
os.system("clear")

num = int(input ("What number do you want to find the root of?"))

# num = 100
# root = ()

for i in range(int(round((num/2)))):
    if i*i == num:
        print(i)
        break

# print(1234567**2)