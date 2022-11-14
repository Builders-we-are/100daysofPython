
import os
os.system("clear")

nums = [1,2,3,1]
Unique = True
# unique = [] 

# Unique = True

# for i in nums:
#     if i not in unique:
#         unique.append(i)
#     else:
#         Unique = False
#         break

# print(f"\n \n \n \n \n \n \n  This list is {Unique}")
unique = [*set(nums)]
x = len(unique)
y = len(nums)

if x < y:
    Unique = False
else:
    Unique = True

return Unique