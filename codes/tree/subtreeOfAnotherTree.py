# Leetcode 572

def isSubtree(self, root, subRoot):
    if not root and subRoot:
        return False
    if self.sameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def sameTree(self, p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)