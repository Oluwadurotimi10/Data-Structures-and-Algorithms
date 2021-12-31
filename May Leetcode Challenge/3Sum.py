# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:03:14 2021

@author: JADESOLA
"""

"""
Finding the three numbers in a list that add up to give 0, none of the numbers
 must be of the same index but can of the same value
""" 
def threeSum(nums, target):
   nums.sort()
   print(nums)
   final = []
   for i in range(len(nums)-2):
       l = i + 1
       r = len(nums) - 1
       if nums[i] == nums[i-1] and i > 0 :
           continue
       while l != r:
           hold = nums[i] + nums[l] + nums[r]
           #print(nums[i] + nums[l] + nums[r], nums[i], nums[l], nums[r])
           if hold < target:
               l += 1
           elif hold > target:
               r -= 1
           else:
               #print(i,l,r)
               if [nums[i], nums[l],nums[r]] not in final:
                   final.append([nums[i], nums[l],nums[r]])                  
   return final
               
               
         
     
#nums = [-4, -1, -1, 0, 1, 2]
nums = [0,0,0,0]
target = 0
print(threeSum(nums, target))
"""
a=[]
a.extend([1,2,3])
b = []
b.append(a)
print(b) """