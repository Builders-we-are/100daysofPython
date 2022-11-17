class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
     
nums = [ 1, 3, 5, 6]
nums.sort()
target = int(input("What number are you looking for?"))
x=0

if target < min(nums)-2 or target > max(nums)+2 :
    print("target is out of range")

elif target < min(nums):
    print(f"I can be inserted here at position number: 0")

elif target > max(nums):
    print(f"I can be inserted here at position number: {len(nums)}")

elif target in nums:
        while x < len(nums):
            if nums[x] != target:
                x += 1
            else:
                print(f"I am here at position number: {x}")
                break

else:            
        while x < len(nums):
            if (nums[x]+nums[x+1])/2 == target:    
                # No need to convert above to int, tested with bool(int(4.0)=float(4.0)) gave out True
                print(f"I can be inserted here at position number: {x+1}")
                break
            else:
                x += 1
        


