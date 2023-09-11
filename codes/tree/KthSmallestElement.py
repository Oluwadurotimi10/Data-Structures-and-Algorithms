# Leetcode 230

def kthSmallest(self, root, k):
    tracker = 0
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        tracker += 1
        if tracker == k:
            return curr.val
        curr = curr.right