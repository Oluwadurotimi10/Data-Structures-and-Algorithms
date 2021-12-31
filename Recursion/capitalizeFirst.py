# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:15:03 2020

@author: JADESOLA
"""

def capitalizeFirst(arr):
    """
        This function accepts an array of strings,whereby it capitalizes the first letter 
        of each string in the array.
    """ 
    newArr = []
    if len(arr) == 0:
        return newArr
    newArr.append(arr[0][0].upper() + arr[0][1:])
    return newArr + capitalizeFirst(arr[1:])
    
arr = ['cat', 'dog', 'monkey']
print(capitalizeFirst(arr))