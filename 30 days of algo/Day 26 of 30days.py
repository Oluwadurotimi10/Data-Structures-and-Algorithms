# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:44:46 2020

@author: JADESOLA
"""

"""
Given a string, write a function thata checks if the given string is a permutation of a palindrome
 
"""

def possible_palindrome(string):
    count_map = {}
    odd_count = 0
    for i in range(len(string)):
        count_map[string[i]] = count_map.get(string[i],0)+1
    for j in count_map:
        if count_map[j] % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
                break
    return True
string = "papa"
print(possible_palindrome(string))

#or

import collections
def is_palindrome_permutation(s):
    count_map = collections.Counter(s)
    seen_single_character = False
    
    for key in count_map:
        occurences =  count_map[key]
        if occurences % 2 == 1:
            if seen_single_character:
                return False
            seen_single_character = True
    return True