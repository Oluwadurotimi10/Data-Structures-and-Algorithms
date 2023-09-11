# Leetcode 797


# TC: O(E + K*V)  where k is the number of possible path
# SC: O(V)

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    # edge case
    if not graph:
        return []

    # creating dictionary to store node and its neighbors
    n_map = {}
    for i in range(len(graph)):
        n_map[i] = graph[i]

    # applying DFS
    n = len(graph)

    stack = [(0, [0])]
    res = []
    while stack:
        node, path = stack.pop()

        if node == n - 1:
            res.append(path)
        for nei in n_map[node]:
            stack.append((nei, path + [nei]))
            print(stack)

    return res
