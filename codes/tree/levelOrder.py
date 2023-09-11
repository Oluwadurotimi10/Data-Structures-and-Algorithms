# Leetcode 102
import collections


def levelOrder(self, root):
    output = []
    queue = collections.deque()
    queue.append(root)

    if not root:
        return output

    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)
        output.append(level)
    return output