# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:59:40 2020

@author: JADESOLA
"""

def missing(arr):
    """
        This function takes in an array and returns the missing value in the array range
    """
    sum1 = 0
    sum2 = 0
    n = len(arr)+1
    #using sum of n series equation
    sum1 = (n*(n+1))/2
    sum2 = sum(arr)
    return sum1-sum2

arr = [1,2,3,4,5,6,7,8,9,10,12,13,14,15]
print(missing(arr))