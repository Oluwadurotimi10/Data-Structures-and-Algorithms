# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:33:38 2020

@author: JADESOLA
"""

def flatten(arr):
    """
        This function accepts an array and returns a new array with all values flattened
    """
    finalArr = []
    for block in arr:
        if type(block) is list:
            finalArr.extend(flatten(block))
        else:
            finalArr.append(block)
    return finalArr 
arr =[[[1],2],3] 
print(flatten(arr))