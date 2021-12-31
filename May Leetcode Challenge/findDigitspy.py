# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:37:21 2021

@author: JADESOLA
"""

"""
Given a string s of length N, which is the english representaion of any of the digits
between 0-9 in a jumbled format. Find the digits from this representation

##################################
Notice the even numbers within that range have unique alphabet that others do not have
zero - z
two - w
four - u
six - x
eight - g

while the odd numbers all have alphabets that other digits have
one - n
three - h
five - v
seven - s
nine - i
"""

def findDigits(s):
    #array to hold the count of each digit
    arr = [0] * 10
    
    digits = ""
    
    #traversing through the string to obtain most likely digits present
    for i in range(len(s)):
        if s[i] == "z":
            arr[0] += 1
        elif s[i] == "w":
            arr[2] += 1
        elif s[i] == "u":
            arr[4] += 1
        elif s[i] == "x":
            arr[6] += 1
        elif s[i] == "g":
            arr[8] += 1
        elif s[i] == "o":
            arr[1] += 1
        elif s[i] == "h":
            arr[3] += 1
        elif s[i] == "v":
            arr[5] += 1
        elif s[i] == "s":
            arr[7] += 1
        elif s[i] == "i":
            arr[9] += 1
    
    #check to ensure the right digits were counted
    arr[3] = arr[3] - arr[8]
    arr[7] = arr[7] - arr[6]
    arr[5] = arr[5] - arr[7]
    arr[9] = arr[9] - (arr[6] + arr[8] +arr[5])
    arr[1] = arr[1] - (arr[0] + arr[2] + arr[4])
    
    #obtaining the digits
    for i in range(len(arr)):
        for j in range(arr[i]):
            digits += chr(i + ord("0"))
    return digits
s = "nnei"
print(findDigits(s))    