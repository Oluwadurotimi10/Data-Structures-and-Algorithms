# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:40:34 2021

@author: JADESOLA
"""

"""
Finding the median of two sorted arrays using O(log n) time complexity
"""
def median(nums1,nums2):       
    i = 0
    j = 0
    joined_arr = []
    if nums1[-1] < nums2[0]:
        joined_arr = nums1+nums2
    while i<len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            joined_arr.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            joined_arr.append(nums2[j]) 
            j += 1
    if len(nums1) > len(nums2):
        joined_arr = joined_arr + nums1[i:len(nums1)]
    else:
        joined_arr = joined_arr + nums2[j:len(nums2)]
    print(joined_arr)
    if len(joined_arr) % 2 == 0:
        mid1 = len(joined_arr)//2
        mid2 = mid1-1
        median = (joined_arr[mid1] + joined_arr[mid2])/2
    else:
        mid = len(joined_arr)//2
        median = joined_arr[mid]
    return median    
        
        
nums1=[1,3,7]
nums2=[2,5]
print(median(nums1,nums2))        
        
        

        
        
        
        
        
        
arr1 = [1,3]
arr2 = [2,4]