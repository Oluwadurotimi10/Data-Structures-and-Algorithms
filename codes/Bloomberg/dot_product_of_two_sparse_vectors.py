# Leetcode 1570

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero_map = {}
        for idx, n in enumerate(nums):
            if n != 0:
                self.nonzero_map[idx] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        summ = 0
        for i, j in vec.nonzero_map.items():
            if i in self.nonzero_map:
                summ += self.nonzero_map[i] * j
        return summ

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Follow up: if only one vector is sparse
