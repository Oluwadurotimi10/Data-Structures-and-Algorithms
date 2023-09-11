# Leetcode 238

def productExceptSelf(self, nums):
    output = []
    prefix = 1
    postfix = 1

    # for prefix
    for i in range(len(nums)):
        output.append(prefix)
        prefix *= nums[i]

    # for postfix
    for j in range(len(nums) - 1, -1, -1):
        output[j] *= postfix
        postfix *= nums[j]
    return output