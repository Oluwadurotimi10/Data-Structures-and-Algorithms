# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:47:46 2020

@author: JADESOLA
"""
"""
        Given an arrayrepresenting heights of buildings.
        The array has buildings from left to right and also has it's  sun at the far left,
        count number pf buildings that have a sunset view. It is assumed that heights of all buildings
        are distinct
"""

def isSunsetBuilding(arr):
    i = 0
    j = 1
    building_count = 1          #because the first buiding will always see the sunset
    tallest = 0                 #keeps track of the tallest building
    while j <= len(arr)-1:
        if arr[i] < arr[j]:
            tallest = max(tallest,arr[j])
            if arr[j] >= tallest:
                building_count += 1
        i += 1
        j += 1
        #print('i',i,'j',j)
    return building_count
arr = [2,3,4,5]
print(isSunsetBuilding(arr))

#or
"""
def isSunsetBuilding(arr):
     building_count = 0
     temp = arr[-1]
     for i in range(len(arr)-2,0,-1):
         if arr[i] < temp:
             building_count += 1
         temp = arr[i]
     if arr[0] >= temp:
         building_count += 1
     return building_count
arr = [4,2,1,5]
print(isSunsetBuilding(arr))  """