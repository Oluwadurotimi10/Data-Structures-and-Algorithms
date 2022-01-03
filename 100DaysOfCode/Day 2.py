"""
Leetcode 2Sum question
Returning indices of the two numbers that add up to the target. Each input has exactly
one solution and aan element may not be used twice
"""
def twoSum(nums,target):
        count_dict = {i:nums.count(i) for i in nums}
        pair_count = 0
        out = []
        print(count_dict)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                #ensuring the same element is not used twice
                if diff == nums[i] and count_dict[diff] > 1 and pair_count < 2 :
                    pair_count += 1
                    out.append(i)
                elif diff != nums[i]:
                    out.append(i)
                    out.append(nums.index(diff))
                    #print(out)
                    #print(pair_count)
                    break
                
        return out
   
    
nums = [7,2,12,11,15]
target = 14
print(twoSum(nums,target))