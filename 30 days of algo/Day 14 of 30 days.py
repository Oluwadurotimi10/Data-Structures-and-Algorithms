# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:29:11 2020

@author: JADESOLA
"""

"""
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn]

"""

def shuffle_array(arr):
    n = len(arr) // 2         #number of elements in each x and y 
    x = 0                     #keeps track of the x part
    y = n                     #keeps track of the y part
    shuffled_arr = []
    while x < n:
         shuffled_arr.append(arr[x])
         shuffled_arr.append(arr[y])
         x += 1
         y += 1
        
    return shuffled_arr
arr = [2,5,1,3,4,7]
print(shuffle_array(arr))