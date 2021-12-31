# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:19:20 2021

@author: JADESOLA
"""
"""
Find the sum of three numbers in the array closest to the target given
"""

def three_sum(nums, target):
    if len(nums) == 3:
        return sum(nums)
    nums = sorted(nums)
    length = len(nums)
    closest = None
    
    min_diff = min(abs(target- (nums[0] + nums[1] + nums[2])), abs(target-(nums[-3] + nums[-2] + nums[-1])))
    for i in range(length):
        l = i+1
        r = length-1
        
        while l < r:
            temp_sum = nums[i] + nums[l] + nums[r]
            diff = abs(target-temp_sum)
            if diff <= min_diff:
                min_diff = diff
                closest = temp_sum
            if temp_sum < target:
                l += 1
            elif temp_sum > target:
                r -= 1
            else:
                return target
    return closest
       
          
#arr = [1,2,4,8,16,32,64,128]
nums = [1,1,1,1]
print(three_sum(nums,1))                                                                                                                  