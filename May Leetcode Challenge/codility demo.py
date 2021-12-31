# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:39:37 2021

@author: JADESOLA
"""
"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
"""
def sol(A):
    A.sort()
    max_val = max(A)
    if max_val < 0:
        return 1
    val_list = [ i if i > 0 else 0 for i in A]
    print(val_list)
    for i in range(len(val_list)-1):
        diff = val_list[i+1]-val_list[i]
        if diff != 0 and diff != 1 and val_list[i] != 0:
            return val_list[i]+1
    return max_val+1
    
    

A = [-1,-2,-3,2,3]
print(sol(A))


#returning the sentence with the largest number of word in a text 
def solution(S):
    max_len = 0
    word_end = False
    word = 0
    for i in range(len(S)): 
        if S[i] != '' and S[i] != '?' and S[i] != '.' and S[i] != '!' and word_end == False:
            word += 1
            word_end = True
            print(S[i])
            #flag = False
        else:
           if S[i] == ' ':
               word_end = False
           elif S[i] == '?' or S[i] == '.' or S[i] == '!' :    
               max_len = max(max_len, word)
               #print(words)
               word_end = True
               word = 0
               #flag = False
    return max_len
    
S = "We test coders. Give us a try? "
#S = " A." 
print(solution(S))
"""
def solution(S):
    # write your code in Python 3.6
    store = {}
    key = ['B','A','L','O','N']
    count = 0
    if len(S) < 7:
        return 0
    for i in range(len(S)):
        if S[i] in key:
            store[S[i]] = store.get(S[i], 0)+1
    print(store)
    while store['L'] > 1 and store['O'] > 1:
        store['L'] -= 2 
        store['O'] -= 2 
        count += 1
        print(store)
    return count

#S= "ONLABLABLOON"
S="BAOOLLLNNOLOLGBAX"
print(solution(S))
