# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:46:00 2020

@author: JADESOLA
"""

def fib(n):
    """
        This function accepts a number and returns the nth number in the fibonacci sequence.
        Recall, the fibonacci sequence is the sequence of whole numbers 0,1,1,2,3,5,8,... which
        starts with 0 and 1, where the number thereafter is equal to the sum of the previous two 
        numbers.
    """
    if n <= 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(3))