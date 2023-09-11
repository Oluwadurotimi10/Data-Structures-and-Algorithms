def isBST(node, minVal, maxVal):
    def isBST(node, minKey, maxKey):
        if not node:
            return True
        if node.val <= minKey or node.val >= maxKey:
            return False

        return (isBST(node.left, minKey, node.val)) and (isBST(node.right, node.val, maxKey))


isBST(root, float('-inf'), float('inf'))


 """
    3
  1   5
     4  6
 """

