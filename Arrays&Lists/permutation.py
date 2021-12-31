# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:42:17 2020

@author: JADESOLA
"""

def permutation(list1,list2):
    """
    This function takes in two arrays and returns true if their the reverse of eachother
    """
    
    i = 0
    j = len(list2)-1
    while i < len(list1):
        if list1[i] == list2[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

list1 = [1,2,3,4]
list2 = [4,3,8,1]
print(permutation(list1,list2))