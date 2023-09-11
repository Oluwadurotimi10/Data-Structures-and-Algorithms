# Leetcode 977

# brute force
def sortedSquaredArray(array):
    # Write your code here.
    result = []

    for num in array:
        result.append(num ** 2)
    result.sort()
    return result

# TC: O(nlogn), O(n)


# optimized , TC: O(n), SC: O(n)
def sortedSquares(self, nums: List[int]) -> List[int]:
    left_ptr, right_ptr = 0, len(nums) - 1
    ans = []

    while left_ptr <= right_ptr:
        if abs(nums[left_ptr]) > abs(nums[right_ptr]):
            ans.append(nums[left_ptr] ** 2)
            left_ptr += 1
        else:
            ans.append(nums[right_ptr] ** 2)
            right_ptr -= 1

    return ans[::-1]


# using list without reversing
def sortedSquares(self, nums: List[int]) -> List[int]:
    left_ptr, right_ptr = 0, len(nums) - 1
    ans = [0] * len(nums)

    while left_ptr <= right_ptr:
        l_num = abs(nums[left_ptr])
        r_num = abs(nums[right_ptr])

        if l_num > r_num:
            ans[right_ptr - left_ptr] = nums[left_ptr] ** 2
            left_ptr += 1
        else:
            ans[right_ptr - left_ptr] = nums[right_ptr] ** 2
            right_ptr -= 1

    return ans


# using queue
def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)