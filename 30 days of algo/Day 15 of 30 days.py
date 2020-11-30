# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:41:10 2020

@author: JADESOLA
"""
"""
    Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

"""
def reduce_to_zero(num):
    count = 0
    n = num//2
    for i in range(n):
        if num % 2 == 0:
            num = num//2
        else:
            num = num - 1
        count += 1
        if num == 0:
            return count
print(reduce_to_zero(44))