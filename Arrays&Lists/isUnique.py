# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:37:41 2020

@author: JADESOLA
"""

arr = [1,2,3,4,2,44,67,90,34,77]

def isUnique(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] in temp:
            print(arr[i])
            return False
        else:
            temp.append(arr[i])
    return True

print(isUnique(arr))