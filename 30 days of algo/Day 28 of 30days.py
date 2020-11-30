# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:14:42 2020

@author: JADESOLA
"""

"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of nums[i]*nums[j]
"""

def maximum_product(arr):
    i = 0
    j = 1
    max_mul = 0
    while i < len(arr)-1:
        mul = arr[i] * arr[j]
        j += 1
        max_mul = max(mul,max_mul)
        if j == len(arr):
            i += 1
            j = i + 1
    return max_mul
arr = [1,7,6,5]
print( maximum_product(arr))    

#or
def maxProduct(nums):
    max1 = max(nums[0],nums[1])
    max2 = min(nums[0],nums[1])
    
    for n in nums[2:]:
        if n >= max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    return(max1-1)*(max2-1)