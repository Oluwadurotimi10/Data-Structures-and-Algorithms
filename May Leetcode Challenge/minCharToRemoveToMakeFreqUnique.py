# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:47:06 2021

@author: JADESOLA
"""
"""
Given a string, return minimum number of letters that must be deleted to obtain a
word in which every letter occurs a unique number of times.
"""

def minUniqueCharCount(s):
    store = {}
    maxFrequency = []
    no0fCharRemoved = 0
    
    for i in range(len(s)):
        store[s[i]] = store.get(s[i], 0) + 1
    
    for val in store.values():
        maxFrequency.append(val)
    
    maxFrequency.sort()
    print(maxFrequency)
    print(store)
    while (len(maxFrequency) > 0):
        top =  maxFrequency[-1]
    
        del maxFrequency[-1]
        
        if len(maxFrequency) == 0:
            return no0fCharRemoved
        
        if (top == maxFrequency[-1]):
            if top > 1:
                maxFrequency.append(top-1)
            no0fCharRemoved += 1
        maxFrequency.sort()
        
    return no0fCharRemoved
 
s="eecccffffee"
print(minUniqueCharCount(s))       