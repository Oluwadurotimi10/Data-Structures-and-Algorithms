# Leetcode 105

def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
    root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])
    return root

# Leetcode 106

def buildTree(self, inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    root_idx = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
    root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx:-1])
    return root
