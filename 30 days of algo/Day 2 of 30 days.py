# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:58:08 2020

@author: JADESOLA
"""
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid. An input string is valid if: 
     (a) Open brackets must be closed by the same type of brackets. 
     (b) Open brackets must be closed in the correct order.

"""
"""

def valid_parenthesis(arr):
    #last = len(arr)-1
    k = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] == "(" or arr[i] == "{" or arr[i] == "[":
            k += 1
        else:
            j += 1
              # arr[i] == ")" or arr[i] == "}" or arr[i] == "]"
    if k == j:
        return True
    else:
        return False
print(valid_parenthesis("((}}")) 
"""
def valid_parenthesis(arr):
    store = {"(":")","{":"}","[":"]"}
    stack = []
    for bracket in arr:
        if bracket in store:
            stack.append(bracket)
        else:
            top = stack.pop() 
            if bracket != store[top]:
                return False   
    return not stack
arr = "((((({))}{)})"
print(valid_parenthesis(arr))