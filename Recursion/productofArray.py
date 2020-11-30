# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:24:23 2020

@author: JADESOLA
"""

def productofArray(arr):
    """
        This function takes in an array and returns the product of the numbers 
        in the array.
    """
    if len(arr) == 0:
        return 1
    return arr[0] * productofArray(arr[1:])

print(productofArray([1,-2,3,4]))