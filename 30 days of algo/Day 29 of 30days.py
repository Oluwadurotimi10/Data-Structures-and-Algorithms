# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:27:57 2020

@author: JADESOLA
"""

"""
Write a function that checks if a string has all unique characters
"""
import collections
def is_unique_characters(string):
    count_map = collections.Counter(string)
    
    for key in count_map:
        if count_map[key] > 1:
            return False
    return True
string = "jungle"
print(is_unique_characters(string))