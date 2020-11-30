# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:37:14 2020

@author: JADESOLA
"""
"""
    Given a string, that contains special character together with alphabets 
    (‘a’ to ‘z’ and ‘A’ to ‘Z’),reverse the string in a way that special characters are not affected.
"""
"""
def reverse_string_only(string):
    string_list = list(string)
    print(string_list)
    l = 0
    r = len(string_list)-1
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQUSTUVWXYZ"
    while l<r:
        
        if ((string_list[l] in lower) or (string_list[l] in upper)) and\
        ((string_list[r] in lower) or (string_list[r] in upper)):
                string_list[l],string_list[r] = string_list[r],string_list[l]
                l += 1
                r -= 1
        elif ((string_list[r] not in lower) or (string_list[r] not in upper)) and\
        ((string_list[l] in lower) or (string_list[l] in upper)):
            print(r)
            r -= 1
        elif ((string_list[l] not in lower) or (string_list[l] not in upper)) and\
        ((string_list[r] in lower) or (string_list[r] in upper)) :
            l += 1
        else:
            l += 1
            r-=1
            
    return ''.join(string_list)
string = "j$a&d)e"
print(reverse_string_only(string))
        
"""
def reverse_string_only(string):
    string_list = list(string)
    l = 0
    r = len(string_list)-1
    while l<r:
        if not string_list[l].isalpha():
            l+=1
        elif not string_list[r].isalpha():
            r-=1
        else:
            string_list[l],string_list[r] = string_list[r],string_list[l]
            l += 1
            r -= 1
    return ''.join(string_list)
string = "j$a&d)e"
print(reverse_string_only(string))
