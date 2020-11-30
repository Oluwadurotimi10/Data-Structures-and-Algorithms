# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:49:32 2020

@author: JADESOLA
"""

def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True

def someRecursive(arr,cb):
    """
        This function accepts an array and a call back, it returns true if a 
        single value in the array returns true when passed in the callback.
        Otherwise it returns false.
    """
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    return someRecursive(arr[1:], cb)
arr = [4,6,8,10,20,44]
print(someRecursive(arr, isOdd))