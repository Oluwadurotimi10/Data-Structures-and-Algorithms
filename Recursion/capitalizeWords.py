# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:28:26 2020

@author: JADESOLA
"""

def capitalizeWords(arr):
    """
        This function accepts an array of words and returns a new array 
        containing each words capitalized.
    """
    newArr = []
    if len(arr) == 0:
        return newArr
    newArr.append(arr[0][:].upper())
    return newArr + capitalizeWords(arr[1:])
arr = ['cat', 'dog', 'monkey']
print(capitalizeWords(arr))
    