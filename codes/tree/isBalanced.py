# Leetcode 110

def isBalanced(self, root) -> bool:
    def dfs(root):
        if not root:
            return [True, 0]
        else:
            left = dfs(root.left)
            right = dfs(root.right)
            height_diff = abs(left[1] - right[1])
            balanced = left[0] and right[0] and height_diff <= 1

            return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]