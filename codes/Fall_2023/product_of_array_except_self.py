# Leetcode 1029

# TC: O(nlogn), SC: O(1)
"""
Using numbers [3,2,1,4], using index 2 (1) as the current number, its product
except self will be (3*2*4) but using prefix and suffix approach, its
product will be of two parts; left(3*2) and right(4)

# the first and last for lefts and tights respectively can be filled with
1s

Numbers:    3    2    1    4
lefts:           3   3*2   3*2*1
rights    2*1*4  1*4   4    
 
 the lefts is stored in the result array and the right is calculated on it.
 Instead of creating a new array for right, a variable to hold right works 
 while multiplying the answers directly on
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        result = [1 for i in range(num_len)]

        # product flow from the right
        for idx, num in enumerate(nums):
            if idx > 0:
                result[idx] = nums[idx-1] * result[idx-1]

        # product flow from the left
        right = 1
        for idx in range(num_len-1, -1, -1):
            if idx < num_len-1:
                right = right * nums[idx+1]
            result[idx] *= right

        return result