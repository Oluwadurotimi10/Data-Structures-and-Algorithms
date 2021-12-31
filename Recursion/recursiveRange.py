# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:33:04 2020

@author: JADESOLA
"""

def recursiveRange(num):
    """
        This function accepts a number and adds up all the numbers from 0 to the
        number passed to the function.
    """
    if num <= 0:
        return 0
    return num + recursiveRange(num-1)

print(recursiveRange(3))