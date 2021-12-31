# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:46:56 2021

@author: JADESOLA
"""

def tripletSubsequence(nums):
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] < nums[i+2]:
            return True
    return False

nums=[6,8,9]
print(tripletSubsequence(nums))