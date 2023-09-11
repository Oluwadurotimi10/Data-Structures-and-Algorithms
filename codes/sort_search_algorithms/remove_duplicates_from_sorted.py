# Leetcode  26. Removing duplicates from sorted array


def removeDuplicates(nums):
    ptr = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[ptr]:
            ptr += 1
            nums[ptr] = nums[i]
    return ptr + 1
