# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:25:02 2020

@author: JADESOLA
"""
"""
Given an array containing n distinct numbers taken from 0,1,2,...,n, find the one that is missing 
from the array
"""
"""
class missing():
    #sorting the array
    def selection(self,L):
        for i in range(len(L)-1):
            minpos = i
            for j in range(i,len(L)):
                if L[j] < L[minpos]:
                    minpos = j
            temp = L[i]
            L[i] = L[minpos]
            L[minpos] = temp
        return L
    
    def missing_number(self,L):
        length = len(L)
        for i in range(length+1):
            if i not in L:
                return i
         
L = [0]
one = missing() 
L = one.selection(L)
print(one.missing_number(L))   

def find_missing_number(nums):
    nums.sort()
    # since the numbers lie between 0 and n, the first number must be 0
    if nums[0] != 0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]+1:
            return nums[i-1]+1
    #if at the end nonumber that isn't equal to number on the left, the missing number is just
    #the last number plus 1, e.g nums = [0,1,2,3]
    #4 is the missing number
    return nums[-1]+1
"""
#Using XOR property
def find_missing_number_2(nums):
    res = 0 
    n = len(nums)+1
    for i in range (0,n):
        res ^= i
    for n in nums:
        res ^= n
    return res
print(find_missing_number_2([0,1,2]))

def find_missing_number_3(nums):
    arr_sum = sum(nums)
    sum_to_n = len(nums)*(len(nums)+1) /2
    return sum_to_n - arr_sum
