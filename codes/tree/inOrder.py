def inorderTraversal(self, root):
    node = root
    stack = []
    output = []
    while stack or node:
        if node is not None:
            stack.append(node)
            node = node.left

        else:
            node = stack.pop()
            output.append(node.val)
            node = node.right
    return output

    """ 
    if not root:
        return []
    else:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        """