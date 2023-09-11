# Leetcode 199

def rightSideView(self, root):
    output = []
    q = collections.deque()
    q.append(root)
    if not root:
        return output

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(node.val)
    return output