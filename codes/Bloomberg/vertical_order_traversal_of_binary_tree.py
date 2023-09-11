# Leetcode 987

# TC: O(n) + O(nlog(k)), where k is width of tree
# SC: o(n)
def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    order_map = defaultdict(list)
    left_col = right_col = 0
    res = []
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        if not node:
            continue

        left_col = min(left_col, col)
        right_col = max(right_col, col)

        order_map[col].append((node.val, row))

        queue.append((node.left, row + 1, col - 1))
        queue.append((node.right, row + 1, col + 1))

    for col in range(left_col, right_col + 1):
        items = order_map[col]

        items.sort(key=lambda x: (x[1], x[0]))

        items = [val for val, _ in items]

        res.append(items)

    return res