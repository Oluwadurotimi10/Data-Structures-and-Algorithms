# Leetcode 128

def longestConsecutive(self, nums):
    hashset = set(nums)
    longest = 0

    for i in nums:
        if i - 1 not in hashset:
            count = 0
            while i + count in hashset:
                count += 1
            longest = max(longest, count)

    return longest