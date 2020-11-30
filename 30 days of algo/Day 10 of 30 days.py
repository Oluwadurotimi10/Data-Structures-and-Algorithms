# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:12:53 2020

@author: JADESOLA
"""
"""
    Given an array of integers nums, write a method that returns the 'pivot' index of this array.
 We define the pivot index as the index where the sum of all the numbers to the left of the index is
 equal to the sum of all the numbers to the right of the index. If no such index exists, we should
 return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
 
"""
"""
#using prefix sums
def pivot_index(nums):
    prefix_sum1 = {}
    sum1 = 0
    prefix_sum2 = {}
    sum2 = 0
    last = len(nums)-1

    for i in range(len(nums)):    #indexes are keys and numbers are values
        sum1 = sum1+nums[i]
        prefix_sum1[i] = sum1
        
    for j in range(last,-1,-1):     #indexes are values and numbers are keys
        sum2 = sum2+nums[j]
        prefix_sum2[j] = sum2
        
    for k in range(len(prefix_sum1)-1):
        if prefix_sum1[k] in prefix_sum2.values():
            temp_key = list(prefix_sum2.keys())[list(prefix_sum2.values()).index(prefix_sum1[k])]
            #print(temp_key)
            #print(prefix_sum1[k-1])
            #print(prefix_sum2[temp_key+1])
            if prefix_sum1[k-1] == prefix_sum2[temp_key+1]:
                return nums[k]
    #return prefix_sum1, prefix_sum2
nums = [1,2,3,6,4,3,-1]
print(pivot_index(nums))
"""
def pivot_index(nums):
    right_sum = sum(nums)
    left_sum = 0  #this variable computes the sum to the left on the fly
    
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
nums = [1,2,3,6,4,3,-1]
print(pivot_index(nums))