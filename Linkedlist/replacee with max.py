# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:00:17 2021

@author: JADESOLA
"""

class Solution:
    def replace_element(self, arr: list[int]) -> list[int]:
    
        """
        Replacing elemnts with the greatest on the right side. The last element
        is replaced with -1.
        
        #solution 1
        last = len(arr)-1
        for i in range(last):
            max_num = max(arr[i+1:])
            arr[i]=max_num
        arr[last] =-1
        return arr """
        #solution 2
        #initial max =-1
        #reverse iteration
        #new_max = max(oldmax, arr[i])
        rightMax = -1
        last = len(arr)-1
        for i in range(last,-1, -1):
            max_num = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax=max_num
        return arr
arr=[1,2,3,4,5]
