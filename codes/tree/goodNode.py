# Leetcode 1448

def goodNodes(self, root: TreeNode) -> int:
    def check(node, maxVal):
        if not node:
            return 0

        count = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        count += check(node.left, maxVal)
        count += check(node.right, maxVal)

        return count

    return check(root, root.val)