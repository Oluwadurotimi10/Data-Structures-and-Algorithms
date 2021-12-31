# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:10:05 2021

@author: JADESOLA
"""

def jump(nums):
    """
    Given an array of non-negative integers nums, you are initially positioned at the 
    first index of the array.

    Each element in the array represents your maximum jump length at that position.
    
    Your goal is to reach the last index in the minimum number of jumps.
    
    You can assume that you can always reach the last index.
    """
    end = 0
    farthest = 0
    move = 0
    for i in range(len(nums)-1):
        farthest = max(farthest, nums[i]+i)
        if i == end:
            move += 1
            end = farthest   
    return move
    
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
#nums = [2,3,1,1,4]
#nums = [3,1,1,1,1]
print(jump(nums))