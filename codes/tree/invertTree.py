def invertTree(self, root):
    if root is None:
        return None
    else:
        self.invertTree(root.right)
        self.invertTree(root.left)

        temp = root.right
        root.right = root.left
        root.left = temp
    return root