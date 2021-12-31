# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:28:41 2021

@author: JADESOLA
"""

"""
Container with most water. Check LeetCode
"""
def containerWithMostWater(arr):
    left = 0
    right = len(arr)-1
    x = 0
    y = 0
    area = 0
    max_area = 0
    while left < right:
        x = right - left
        y = min(arr[right], arr[left])
        area = x * y
        max_area = max(area, max_area)
        if arr[left] < arr[right]:
            left += 1
        elif arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_area
arr = [1,8,6,2,5,4,8,3,7]
ans = containerWithMostWater(arr) 
print(ans)    