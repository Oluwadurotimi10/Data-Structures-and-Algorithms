# Leetcode 366

def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    depth_map = defaultdict(list)

    def dfs(root):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        d = max(left, right) + 1
        depth_map[d].append(root.val)
        return d

    dfs(root)
    return depth_map.values()