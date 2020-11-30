# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:54:11 2020

@author: JADESOLA
"""
"""
Given a string s1 and s2, write a function to check whether s2 is a rotation of s1
"""
"""
def check_rotation(s1,s2):
    s1_list = list(s1)
    s2_list = list(s2)
    check = []
    for i in range(len(s2)):
        check.append(s2_list[-1])
        for j in range(len(s2)-1):
            check.append(s2_list[j])
        if check == s1_list:
            return True
            break
        else:
            s2_list = check
            check = []     
    return False
s1 = "abcde"
s2 = "deabc"
print(check_rotation(s1,s2))        
"""
def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    #s2 will be a rotation of s1 if it is a substring of s1+s1
    #concatenate s1 to s1
    concat_s1 = s1+s1
    print(concat_s1)
    #checking if s2 can be found in concat_s1
    if s2 in concat_s1:
        return True
    return False
s1 = "WATERBOTTLE"
s2 = "ERBOTTLEWAT"
print(isRotation(s1,s2))

    
    
    