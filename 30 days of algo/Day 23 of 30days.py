 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:48:53 2020

@author: JADESOLA
"""

def longest_valid_parenthesis(string):
    #converts the string input to list
    stack = list(string) 
    #keeps count of valid parenthesis    
    count = 0 
    # keeps count of previous valid parenthesis
    temp = 0
    #the both store value from the top of the stack
    top1 = stack.pop() if stack else -1
    top2 = stack.pop() if stack else -1
    for i in range(len(string)):
        #checking if valid
        if top1 == ')' and top2 == '(':
            count += 2
            top1 = stack.pop() if stack else -1
            top2 = stack.pop() if stack else -1
        else:
            #stores the maximum count
            temp =max(count,temp)
            count = 0
            top1 = top2
            top2 = stack.pop() if stack else -1
    return temp    
string = ")()())"
print(longest_valid_parenthesis(string))
        
        