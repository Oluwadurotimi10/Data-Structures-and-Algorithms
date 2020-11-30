# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:18:45 2020

@author: JADESOLA
"""
"""
#Brute force method
def length_of_smallest_array_gt_k(arr,k):
    ans = len(arr)+1
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            curr_subarray_sum = sum(arr[i:j+1])
            if curr_subarray_sum > k:
                ans = min(ans,j-i+1)
    return ans if ans != len(arr)+1 else 0

arr = [1,2,3,4,5,6,7,8]
print(length_of_smallest_array_gt_k(arr,20))   

"""
def length_of_smallest_array_gt_k(arr,k):
    i = 0
    j = 0
    curr_window_sum = 0
    ans = len(arr)+1
    while j < len(arr):
        curr_window_sum += arr[j]
        while i < len(arr) and curr_window_sum > k:
            ans = min(ans,j-i+1)
            curr_window_sum -= arr[i]
            i += 1
        j += 1
    return ans if ans != len(arr)+1 else 0            
arr = [1,2,3,4,5,6,7,8]
print(length_of_smallest_array_gt_k(arr,20))            
        
    
         
        
    