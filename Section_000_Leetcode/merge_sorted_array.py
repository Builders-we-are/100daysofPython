

import os
os.system("clear")
print("\n \n \n \n \n \n")


nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

index = 0

for x in range(m,len(nums1)):
    if index != n:
        nums1[x] = nums2[index]
        index += 1
    # else:
    #     break
nums1.sort()
print((nums1))





# nums1 = [1,2,3,0,0,0]
# m = 3

# nums2 = [2,5,6]
# n = 3

# nums3 = []

# for i in range(0,m):
#     nums3.append(nums1[i])
# for i in range(0,n):
#     nums3.append(nums2[i])

# nums1 = sorted(nums3)

# print(nums1)