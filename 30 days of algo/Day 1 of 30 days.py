# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:49:56 2020

@author: JADESOLA
"""
""" Given an array of numbers, find the Kth smallest item. 
    This means that if k was 1, we'd find the first smallest. 
    if k was 2, we'd find the second smallest and so on. 
    Your solution should be faster than O(n log n) where n is the size of the array.
"""

import heapq
""" # Time complexity O(n log n) space complexity is O(n)
def kthsmallest(L,k):
    new = []
    heapq.heapify(L)
    print(L)
    for i in range(len(L)):
        temp = heapq.heappop(L)
        new.append(temp)
    return new[k-1]
L = [5,4,0,0,-1,7]
#L = [5,4,2,1]
print(kthsmallest(L,3))
"""
"""
# Time complexity = O(n log k) space complexity is O(k) 
def find_kth_smallest(arr,k):
    #we're using -1*arr[i] so as to get the max heapfunctionality from min heap because
    # because heapq defaultly provides min heap functionality 
    heap = []
    for i in range(k):
        heapq.heappush(heap,-1*arr[i])
    i += 1
    print(heap)
    while i < len(arr):
        heapq.heappushpop(heap, -1*arr[i])
        i += 1
    print(heap)
    return -1* heap[0]
L = [2,3,-1,6,7,1,10,2]
print(find_kth_smallest(L,4))
"""
#Quicksort (Partitioning)
def find_kth_smallest(arr,k):
    def partition(arr,l,r):
        pivot = (l+r) // 2
        i = l           # keeps track of the last postion ana element less than the pivot was placed
        arr[r],arr[pivot] = arr[pivot], arr[r]
        for j in range(l,r):
            if arr[j] <= arr[r]:
                arr[i],arr[j] = arr[j], arr[i]
                i += 1        
        arr[i] , arr[r] = arr[r], arr[i]
        return i + 1
    #return partition(arr)                    
    def helper(arr,l,r,target_index):
        while r >= l:
            pi = partition(arr,l,r)
            if pi == target_index:
                return arr[pi]
            elif pi > target_index:
                r = pi - 2
            else:
                l = pi 
        return arr[l]
    return helper(arr,0,len(arr)-1,k)
#arr = [10,80,30,90,40,50,70]
arr = [4,7,6,9,1,8]
out = find_kth_smallest(arr,2)
print(out)
