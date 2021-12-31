# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:29:59 2020

@author: JADESOLA
"""

import numpy as np

def maxProduct(arr):
    """
        This function takes in ana array and returns the index of the elements with the 
        largest product.
    """
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
          if arr[i] == arr[j]:
              continue
          elif arr[i] * arr[j] > max_product:
              max_product = arr[i] * arr[j]
              pairs = str(arr[i]) + "," + str(arr[j])
          
    print(pairs)
    print(max_product)

myarr = np.array([1,2,3,4,55,6,7,34,23,16,44,69,0])
maxProduct(myarr)