# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:36:51 2020

@author: JADESOLA
"""
"""
def reverse_num(num):
    
    num = str(num)          #converts the integer to a string
    num_list = list(num)    #converts the string to a list
    i = 0                   #keeps track of the numbers at the beginning
    j = len(num_list) - 1   #keeps track of the numbers at the end
    while i < j:
        num_list[i], num_list[j] =  num_list[j], num_list[i]
        i += 1
        j -= 1
    string = [str(number) for number in num_list]       
    num_string = "".join(string)                         #converts the list to a string
    num = int(num_string)                                #converts the string to an integer
    return num
print(reverse_num(1024))
"""        

def reverse_num(num):
    if num == 0:
        return 0
    reversed_num = []
    while num != 0:
        rev_num = num % 10
        reversed_num.append(rev_num)
        num = num // 10
    string = [str(number) for number in reversed_num]       
    num_string = "".join(string)                         #converts the list to a string
    #num = int(num_string)                                #converts the string to an integer
    return num_string

print(reverse_num(98713321909122))        

"""
This function reverses an integer
    
    args : num -> the number to be reversed
    
    return the reversed form of the input number
"""        