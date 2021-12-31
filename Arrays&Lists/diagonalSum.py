# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:49:53 2020

@author: JADESOLA
"""

def diagonalSum(arr):
    """
        This function takes in an array and returns the sum of all the diagonal elements
        function input must be a square matrix
    """
    summ = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                continue
            else:
                summ += arr[i][j]
    return summ

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(diagonalSum(arr))