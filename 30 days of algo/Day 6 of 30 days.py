# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:42:58 2020

@author: JADESOLA
"""
"""
Given a non-empty array of integers,every element appears twice except for one. Find that single one.
Solve it in constant space
"""
"""
def single(arr):
    frequency_map ={}
    for i in arr:
        frequency_map[i] = frequency_map.get(i,0)+ 1
    for j in arr:
        if frequency_map[j] == 1:
            return j
arr = [2,5,2,8,1,1,8]
print(single(arr))
"""

def single(arr):
    num_check = 0
    for num in arr:
        num_check ^= num
    return num_check
arr = [2,5,2,8,1,1,8]
print(single(arr))