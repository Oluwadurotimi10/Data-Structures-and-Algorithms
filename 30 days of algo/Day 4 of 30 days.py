# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:00:26 2020

@author: JADESOLA
"""
"""
Given a string, find the index of the first unique character in the string.
 If it doesn't exist, return -1
Find the index of the first unique character in a string
"""
"""
def unique_cha(string):
    store = {}
    for i in range(len(string)):
        if string[i] not in store:
            store[string[i]] = 1
        else:
            store[string[i]] += 1
    for j in store:
        if store[j] == 1:
            return string.index(j)
            break
    return -1
string = 'abababa'
print(unique_cha(string))
"""

def first_unique(string):
    frequency_map = {}
    for ch in string:
        frequency_map[ch] = frequency_map.get(ch, 0) + 1
    print(frequency_map)
    for i in range(len(string)):
        if frequency_map[string[i]] == 1:
            return i
    return -1
string = 'helloworld'
print(first_unique(string))
        