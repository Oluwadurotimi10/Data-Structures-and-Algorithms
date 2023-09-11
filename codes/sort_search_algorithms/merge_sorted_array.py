# Leetcode 88: Merge sorted array

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums_temp = nums1[:m]

    length = len(nums1)

    k = 0
    i = 0
    j = 0

    while i < len(nums_temp) and j < len(nums2):
        if nums_temp[i] <= nums2[j]:
            nums1[k] = nums_temp[i]
            k += 1
            i += 1
        else:
            nums1[k] = nums2[j]
            k += 1
            j += 1

    while i < m:
        nums1[k] = nums_temp[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1