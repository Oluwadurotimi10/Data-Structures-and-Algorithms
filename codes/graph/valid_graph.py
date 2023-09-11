# Leetcode 261

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    graph_map = {i: [] for i in range(n)}
    visited = set()
    prev = -1

    for a, b in edges:
        graph_map[a].append(b)
        graph_map[b].append(a)
    print(graph_map)

    def dfs(s, prev):
        if s in visited:
            return False

        visited.add(s)
        for i in graph_map[s]:
            if prev == i:
                continue
            if not dfs(i, s):
                return False
        return True

    return dfs(0, prev) and n == len(visited)


