
# Leetcode 33 , searching a rotated array

def search(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = left + (right - left) // 2

        if target == nums[mid]:
            return mid

        # left sorted portion
        elif nums[left] <= nums[mid]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        # right sorted portion
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1