
# print("\n".join(map(str, range(10, 0, -1))))
# print(*range(10, 0, -1))
# print(sorted(range(first, last+1, 1), reverse=False))
# print(list(range(first, last+1, 1)))

import os
os.system("clear")

# nums = [247645, 695157, 1735965, 4220736, 4322043, 9465544, 9543270, 9900210]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
k = 5

first = nums[0]
last = nums[-1]

missing = []

while k != 0:
    first += 1
    if first not in nums:
        k -= 1
        missing.append(first)
print(missing[k-1])
