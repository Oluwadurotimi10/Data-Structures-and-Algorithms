# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:58:38 2021

@author: JADESOLA
"""

"""
Find the longest substring without repeating characters

def longest_substring(s):
    #optimized solution
    i = 0
    j = 0
    max_len = 0
    count = 0 
    store ={}
    while j < len(s):
        if s[j] not in store:
            store[s[j]] = 1
            count += 1
            j += 1
            print(store)
            print('c1',count)
        else:
            del store[s[i]]
            count -= 1
            i += 1
            print('c',count)
        #print('j',j)
        max_len = max(count, max_len)        
    return max_len
s = "jdvdff"
ans = longest_substring(s)
print(ans)
"""

#longest palindromic substring
def longest_palindromic_substring(s):
    palin = ""
    palinLength = 0
    for i in range(len(s)):
        #odd length
        l, r = i, i
        while i >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > palinLength:
                palin = s[l:r+1]
                palinLength = r-l+1
            l -= 1
            r += 1
            
        #even length
        l,r = i, i+1
        while i >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > palinLength:
                palin = s[l:r+1]
                palinLength = r-l+1
            l -= 1
            r += 1
            
    return palin

s= "daad"
print(longest_palindromic_substring(s))
        