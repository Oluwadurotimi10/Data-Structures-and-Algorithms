# Leetcode 1

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i, j in enumerate(nums):
        if target - j not in hashmap:
            hashmap[j] = i
        else:
            return [i, hashmap[target - j]]