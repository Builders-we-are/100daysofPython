
import math
from datetime import datetime
import os
os.system("clear")

# for n in range(1, 11):
#     print(f"The value is {n:04}")

# for n in range(1, 11):
#     print(f"The value is {n:04}")

# pi = 3.14159265
# pi = 365646464

print(f"{math.pi:04.8f}")


birthday = datetime(1990, 1, 1)

print(f"I was born on {birthday:%B %d, %Y}")  # Check in python documentation


# TODO: Add example with import time it to see how tuples are faster to use compared to lists


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

a = 13.949999999999999
a = format(a, '.3f')
print(a)
