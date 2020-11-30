# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:39:07 2020

@author: JADESOLA
"""
"""
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array.
 The functions should put all 0s first, then all 1s and all 2s in last.
 """
#Dutch National Flag problem
#using quicksort partition

def partition(arr):
    l = 0 
    r = len(arr) - 1
    i = 0
    while i < r:
        if arr[i] == 2:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        elif arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        else:
            i += 1
    return arr
arr = [1,1,2,1,1,2]
print(partition(arr))

"""
def part(arr):
    i = 0
    j = 0
    k = len(arr)
    mid = k//2
    while j < k:
        if arr[j] < arr[mid]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > arr[mid]:
            k -= 1
            arr[j], arr[k] = arr[k], arr[j]
        else:
            j += 1
    return arr
arr = [2,2,2,2,1,0,2,1,1]
print(part(arr))
"""