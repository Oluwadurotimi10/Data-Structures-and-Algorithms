# Leetcode 11

def maxArea(self, height) -> int:
    maximum = 0
    left_ptr = 0
    right_ptr = len(height) - 1

    while left_ptr < right_ptr:
        width = right_ptr - left_ptr
        maximum = max(maximum, min(height[left_ptr], height[right_ptr]) * width)
        if height[right_ptr] >= height[left_ptr]:
            left_ptr += 1
        elif height[left_ptr] > height[right_ptr]:
            right_ptr -= 1
    return maximum
