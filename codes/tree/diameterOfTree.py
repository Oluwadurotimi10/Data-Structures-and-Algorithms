# Leetcode 543

def diameterOfBinaryTree(self, root):
    maxDiameter = [0]

    def dfs(node):
        if node is None:
            return -1
        left = dfs(node.left)
        right = dfs(node.right)
        maxDiameter[0] = max(maxDiameter[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return maxDiameter[0]