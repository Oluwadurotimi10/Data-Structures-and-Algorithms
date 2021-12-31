# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:40:14 2020

@author: JADESOLA
"""
"""
def fact(num):
    assert num >= 0 and int(num) == num; "Ensure the num is a whole number and positive"
    if num == 0:
        return 1
    return num*fact(num-1)

print(fact(5))
"""

#importing the array module
from array import *

#declaring an array with typecode 'i'
arr = array('i', [9,8,7,6,5,4])

#inserting an element '3' into the sixth index
arr.insert(6,3)
print(arr)

#inserting an element '2' into the first index
arr.insert(0,2)
print(arr)