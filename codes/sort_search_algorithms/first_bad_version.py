# Leetcode 278

def firstBadVersion(self, n: int) -> int:
    left = 0
    right = n
    isBad = False

    while left <= right:
        mid = left + (right - left) // 2

        isBad = isBadVersion(mid)

        if not isBad:
            left = mid + 1
        else:
            right = mid - 1
            if not isBadVersion(mid - 1):
                return mid