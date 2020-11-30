# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 07:55:51 2020

@author: JADESOLA
"""

def reverseString(string):
    """
        This function accepts a string and returns a new string in reverse
    """
    if len(string) == 0:
        return string;
    return reverseString(string[1:]) + string[0]
    

print(reverseString("hit"))