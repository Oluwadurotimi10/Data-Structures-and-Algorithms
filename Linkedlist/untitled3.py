# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:35:24 2021

@author: JADESOLA
"""

def pairSum(myList, sum):
    # TODO
    new=[]
    others = []
    for i in range(len(myList)):
        pair = ""
        other = sum - myList[i]
        
        if other in myList:
            print(other)
            others.append(other)
            pair = str(myList[i]) + "+" + str(other)
            if pair not in new:
                new.append(pair)
                print(new)
            
    return new
print(pairSum([2,4,3,5,6,-2,4,7,8,9], 7))