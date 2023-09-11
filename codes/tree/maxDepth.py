# Leetcode 104

#recursion
def maxDepth(self, root):
    if not root:
        return 0
    else:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#DFS
def maxDepth(self, root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    ans = 0

    while stack:
        node, depth = stack.pop()

        if node:
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            ans = max(ans, depth)
    return ans

#BFS
def maxDepth(self, root):
    if not root:
        return 0

    level = 0
    q = deque([root])
    while q:

        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

    #OR


def maxDepth(self, root):
    ans = 0
    queue = collections.deque()
    queue.append([root, 1])

    while queue:
        node, depth = queue.popleft()

        if node:
            ans = max(ans, depth)
            queue.append([node.left, depth + 1])
            queue.append([node.right, depth + 1])
    return ans