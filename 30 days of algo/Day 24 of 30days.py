# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:41:16 2020

@author: JADESOLA
"""

"""
Given a string, compress the string usimg counts of repeated characters
"""
def string_compression(arr):
    temp = arr[0]   #stores previous characters before moving onto the next
    new = []
    i = 0           #keeps count of the number of characters 
    for j in range(len(arr)):
        if arr[j] == temp:
            i += 1
            temp = arr[j]
        else:
            new.extend([temp,str(i)])
            temp = arr[j]
            i = 1
    new.extend([temp,str(i)])
    arr_new = ''.join(new)
    return arr_new

arr = 'abcd'
print(string_compression(arr))