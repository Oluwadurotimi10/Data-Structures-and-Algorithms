# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:14:42 2020

@author: JADESOLA
"""
"""
Given an array of integers, move all zeros present in the array to the end. 
The solution should maintain the relative order of items of the array
"""

"""
def end_with_zeros(arr):
    new = []
    num_of_zeros = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            new.append(arr[i])
        elif arr[i] == 0:
            num_of_zeros += 1
    for j in range(num_of_zeros):
        new.append(0)
    return new
arr = [4,5,7,9]
print(end_with_zeros(arr))
"""
            
def end_with_zeros(arr):
    #instatiate the count
    count = 0
    #traversing through the array
    for j in arr:
        #Checking if it is a non zero value
        if j>0:
            arr[count] = j
            count += 1
            
    while count < len(arr):
        arr[count] = 0
        count += 1
        
    return arr
arr = [4,0,5,0,7,9]
print(end_with_zeros(arr))
            