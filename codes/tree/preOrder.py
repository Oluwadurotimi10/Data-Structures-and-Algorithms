def preorderTraversal(self, root):
    node = root
    stack = []
    output = []
    while stack or node:
        if node is not None:
            output.append(node.val)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right

    return output

"""
if root is None:
    return []
else:
    return [root.val]+ self.preorderTraversal(root.left) +  self.preorderTraversal(root.right)
    """