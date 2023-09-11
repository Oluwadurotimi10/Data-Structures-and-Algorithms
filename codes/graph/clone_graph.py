# Leetcode 133

def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None

    old_to_new = {}

    def clone(node):
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(clone(nei))
        return copy

    return clone(node)
