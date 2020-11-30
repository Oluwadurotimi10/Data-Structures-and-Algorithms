# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:17:54 2020

@author: JADESOLA
"""
"""
Given a string s1 and string s2, write a function to check whether s1 and s2 are anagrams
"""
"""
def isAnagram(s1,s2):
    count = 0
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] in s2:
            count += 1
    if count == len(s1):
        return True
    return False
s1 = "meteor"
s2 = "remote"
print(isAnagram(s1,s2))
"""
"""
 #using sorting
def isAnagram(s1,s2):
     if len(s1) != len(s2):
         return False
     s1 = sorted(list(s1))
     s2 = sorted(list(s2))
     
     s1 = ''.join(s1)
     s2 = ''.join(s2)
     
     return s1 == s2
s1 = "fired"
s2 = "fired"
print(isAnagram(s1,s2))     
"""

#using hashtable
def isAnagram(s1,s2):
    count_map = {}
    for char in s1:
        count_map[char] = count_map.get(char,0) + 1
    print(count_map)     
    for char in s2:
        count_map[char] = count_map.get(char,0) - 1
        if count_map[char] < 0:
            return False
    print(count_map) 
    return True
s1 = "dessert"
s2 = "stressed"
print(isAnagram(s1,s2))        
    
     