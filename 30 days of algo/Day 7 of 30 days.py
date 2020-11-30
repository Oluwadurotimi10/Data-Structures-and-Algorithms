# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:22:27 2020

@author: JADESOLA
"""
"""
Given a non-empty array of integers. Reverse the array. Solve it in constant space
"""

def reverse_array(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        arr[r], arr[l] = arr[l], arr[r]
        l += 1
        r -= 1
    return arr
arr = [5,5,4,2]
print(reverse_array(arr))
        