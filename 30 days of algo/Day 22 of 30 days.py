# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:10:15 2020

@author: JADESOLA
"""
"""
def reverse_sentence(sentence):
    temp = []
    final = []
    for i in range(len(sentence)-1,0):
        if sentence[i] != ' ':
            temp.append(sentence[i])
        if sentence[i] == ' ':
            final  = final
        
sentence = "hi there"
print(reverse_sentence(sentence))
"""
#using negative indexing
def reverse_arr(arr,start,stop):
    arr = arr[start:stop:-1]
    start += 2
    stop = start + 1
    print(arr)
    print(start)
    print(stop)
    
    
def reverse_words(arr):
    start = -(len(arr)+1)
    stop = -(len(arr)+1)
    arr = arr[::-1]
    #print(arr)
    for i in range(0,len(arr)):
        if arr[i] == ' ':
            reverse_arr(arr,start,stop)
            #print(arr)
        else:
            start += 1
        print(start)
        #print(stop)
    if start == 0:
        reverse_arr(arr,start,0)
    #return arr

arr = ['h','i',' ','t','h','e','r','e']
print(reverse_words(arr))  