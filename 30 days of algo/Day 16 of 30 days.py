# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:42:17 2020

@author: JADESOLA
"""
"""
def lucky_num(nums):
    frequency_map = {}
    lucky = 0 
    for i in range(len(nums)):
        frequency_map[nums[i]] = frequency_map.get(nums[i],0)+1
    print(frequency_map)
    for j in frequency_map:
        if j == frequency_map[j]:
            if lucky > j:
                continue
            else:
                lucky = j 
    if lucky == 0:
        return -1
    return lucky
nums = [5]
print(lucky_num(nums))
"""

def find_lucky(arr):
    count_map = {}
    ans = -1
    for v in arr:
        count_map[v] = count_map.get(v,0)+1
        
    for v in arr:
        if count_map[v] == v and v > ans:
            ans = v
    return ans
nums = [5]
print(find_lucky(nums))