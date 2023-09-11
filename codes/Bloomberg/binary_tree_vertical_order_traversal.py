# Leetcode 314
# TC: O(n)
# sc: O(n)


def verticalOrder(root):
    order_map = defaultdict(list)
    min_pos = float('inf')
    max_pos = float('-inf')

    if not root:
        return []

    queue = deque([(0, root)])

    while queue:
        pos, node = queue.popleft()

        if not node:
            continue

        min_pos = min(pos, min_pos)
        max_pos = max(pos, max_pos)

        order_map[pos].append(node.val)

        queue.append((pos - 1, node.left))
        queue.append((pos + 1, node.right))

    return [order_map[key] for key in range(min_pos, max_pos + 1)]