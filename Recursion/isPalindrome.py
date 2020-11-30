# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:17:20 2020

@author: JADESOLA
"""

def isPalindrome(string):
    """
        This function retruns true if the string passed to it is a palindrome
        (reads the same forward and backward). Otherwise it returns false.
    """
    if len(string) == 0 :
        return True
    if string[0] != string[-1]:
        return False
    return isPalindrome(string[1:-1])

print(isPalindrome("amanaplanacanalpandemonium"))       