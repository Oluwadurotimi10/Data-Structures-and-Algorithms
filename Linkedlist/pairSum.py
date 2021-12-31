# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:35:24 2021

@author: JADESOLA
"""

def pairSum(myList, sum):
    """
     This function return pairs whose sum is the the same with the sum given..
    """
"""   
    # TODO
    new=[]
    others = []
    for i in range(len(myList)):
        pair = ""
        other = sum - myList[i]
        if other in myList:
            print(other)
            others.append(other)
            pair = str(myList[i]) + "+" + str(other)
            if pair not in new:
                new.append(pair)
                print(new)
            
    return new
print(pairSum([2,4,3,5,6,-2,4,7,8,9], 7))
"""
def twoSum(nums, target):
        count_dict = {i:nums.count(i) for i in nums}
        pair_count = 0
        out = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                if diff == nums[i] and count_dict[diff] > 1 and pair_count < 2 :
                    pair_count += 1
                    out.append(i)
                elif diff != nums[i]:
                    out.append(i)
                    out.append(nums.index(diff))
                    break
        return out
   
print(twoSum([3,3,2], 6))