# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:07:43 2020

@author: JADESOLA
"""
"""
Given an integer array nums, find the sum of the elements between indices i and j (i <=j) ,inclusive
"""

def range_sum(nums,i,j):
    summ = 0
    for k in range(i,j+1):
        summ += nums[k]
    return summ
nums = [-2,0,3,-5,2,-1]
print(range_sum(nums,5,5))
        
    