# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:59:10 2020

@author: JADESOLA
"""

"""
Given ana array of integers and another integer between 0-9. Add the value to the array without 
converting the entire array into an integer
"""
def add_to_array(arr,k):
    i = len(arr)-1
    carry = k
    while i >= 0:
        summ = arr[i] + carry
        if summ < 10:
            arr[i] = summ
            break
        left = summ % 10
        carry = summ // 10
        arr[i] = left
        i -= 1

    if carry:
        return [1] + arr
    return arr
arr = [9]
print(add_to_array(arr,1))
            