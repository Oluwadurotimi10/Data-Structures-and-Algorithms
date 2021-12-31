# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:29:26 2021

@author: JADESOLA
"""

def search_sortedReverse(nums, target):
    """
    searching for an elemnt in a rotated sorted array. Return -1 if the element is 
    absent.
    """
    l, r = 0 , len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        
        #right sorted porton
        if nums[r] >= nums[mid]:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid+1
        #left sorted portion
        else:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
arr = [4,5,6,7,0,1,2,3]
target =0
print(search_sortedReverse(arr,target))
                
            