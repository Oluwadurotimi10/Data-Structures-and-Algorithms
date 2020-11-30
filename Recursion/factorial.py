# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:40:14 2020

@author: JADESOLA
"""

def fact(num):
    assert num >= 0 and int(num) == num; "Ensure the num is a whole number and positive"
    if num == 0:
        return 1
    return num*fact(num-1)

print(fact(5))