# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:18:02 2020

@author: JADESOLA
"""
import numpy as np

def inArray(arr,val):
    """
        This function takes in ana array and a value, returns true if val is present in the array
        else return false.
    """
    for i in range(len(arr)):
        if arr[i] == val:
            print(i)
            return True
    return False
myarr = np.array([1,2,3,4,55,6,7,34,23,16,44,69,0])
print(inArray(myarr,55))