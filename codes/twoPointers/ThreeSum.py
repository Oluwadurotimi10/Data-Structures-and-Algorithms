# Leetcode 15


# runs faster TC: O(nlogn)+O(n^2)  -> O(n^2)     SC:O(1) or O(n) bcos of the sorting
def threeSum(self, nums):
    output = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        a = nums[i]
        while l < r:
            curr_sum = a + nums[l] + nums[r]
            if curr_sum > 0:
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                ans = [a, nums[l], nums[r]]
                output.append(ans)
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return output

# runs slowly
def threeSum(self, nums):
    nums.sort()
    output = []

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        a = nums[i]
        while l < r:
            curr_sum = a + nums[l] + nums[r]
            if curr_sum > 0:
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                ans = [a, nums[l], nums[r]]
                if ans not in output:
                    output.append(ans)
                l += 1
                r -= 1
    return output