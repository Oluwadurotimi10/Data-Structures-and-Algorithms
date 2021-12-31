# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 05:51:22 2021

@author: JADESOLA
"""

def maxSum(arr):
    last =len(arr)-2
    maxSum = 0
    for i in range(last):
        summ1 = 0
        summ2 = arr[i]
        j = i + 2
        k = i + 2
        while j <= last+1:
            summ1 = arr[i] + arr[j]
            if k <= last+1:
                summ2 = summ2 + arr[k]
                k += 2
            maxSum = max(summ1,summ2, maxSum)
            summ1 = 0
            j += 1
    if maxSum < 0:
        return 0         
    return maxSum
arr = [3,5,-7,8,10]
print(maxSum(arr))