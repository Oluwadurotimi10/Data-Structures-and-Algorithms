# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:08:44 2020

@author: JADESOLA
"""

def findPairs(arr,target):
    """
        This function takes in an array and a target, it returns the two elements
        that adds up to give the target
    """
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(arr[i],arr[j])

arr = [2,4,3,5,6,-2,4,7,8,9]
findPairs(arr,7)