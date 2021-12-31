# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:49:37 2021

@author: JADESOLA
"""

#Binary Search implementation
#for a sorted list in ascending order
def check(array, num, mid):
    if array[mid] == num:
        if mid-1 >= 0 and array[mid-1] == num:
            return "left"
        else:
            return "found"
    if num < array[mid]:
        return "left"
    else:
        return "right"

def binary_search(array, num, check):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (right + left)//2
        move = checkDescend(array,num, mid)
        if move == "found":
            return "The number is", array[mid], "and it's index is", mid
        elif move == "left":
            right = mid - 1
        elif move == "right":
            left = mid + 1
    return -1

#for a sorted list in descending order
    
def checkDescend(array, num, mid):
    if array[mid] == num:
        if mid -1 >= 0 and array[mid-1] == num:
            return "left"
        else:
            return "found"
    if num < array[mid]:
        return "right"
    else:
        return "left"
    
        
#array = [1,2,3,4,5,6,7,8,9]
array = [9,8,7,6,5,4,3,2,1]
print(binary_search(array, 9, check))


#searching a rotated list
def count_rotations_search(nums, target):
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and nums[mid-1] > mid_number:
            # The middle position is the answer
            if target > nums[len(nums)-1]:
                return [nums[0:mid], "left"]
            else:
                return [nums[mid:], "right"]
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return [nums, "None"]

def find_element(nums, target,count_rotations_search):
    lists = count_rotations_search(nums,target)
    found_list = lists[0]
    lo = 0
    hi = len(found_list)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = found_list[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == target:
            # The middle position is the answer
            if lists[1] == "right":
                position = len(nums) - len(found_list) + 1
                return position + mid
            else:
                return mid + 1
        
        elif mid_number > target:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return -1