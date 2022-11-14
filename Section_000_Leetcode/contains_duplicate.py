
import os
os.system("clear")

nums = [1,2,3,1]
unique = [] 

Unique = True

for i in nums:
    if i not in unique:
        unique.append(i)
    else:
        Unique = False
        break

print(f"\n \n \n \n \n \n \n  This list is {Unique}")