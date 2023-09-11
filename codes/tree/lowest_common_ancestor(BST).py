# Leetcode 235  ( LCA of a binary search tree)

# TC -> O(log n) , since we are visiting one node for every level of the tree, the TC is the height of the tree.
# Since we are using where the split of p and q occur to determine the LCA
# SC -> O(1)


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr