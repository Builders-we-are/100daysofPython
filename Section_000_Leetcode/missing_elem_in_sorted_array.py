
# print("\n".join(map(str, range(10, 0, -1))))
# print(*range(10, 0, -1))
# print(sorted(range(first, last+1, 1), reverse=False))
# print(list(range(first, last+1, 1)))

import os
os.system("clear")

nums = [1, 2, 4]
k = 3

first = nums[0]
last = nums[-1]

check = range(first, last + k)

print(list(check))

missing = []

for i, j in enumerate(check):
    if j not in nums:
        missing.append(j)

print(missing)

print(missing[k-1])
