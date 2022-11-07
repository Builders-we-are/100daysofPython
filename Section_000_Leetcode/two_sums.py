


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

nums = [3,3]
target = 6
output = [ ]

for i in nums:
    for j in nums:
        if nums.index(i) != nums.index(j) and i + j  == target :
                print(i)
                output.append(nums.index(i))
                break
              

print(output)
            


# twoSum(nums = [3,4,5], target = 9 )
