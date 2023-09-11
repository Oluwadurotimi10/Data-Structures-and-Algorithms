#Leetcode 323 (premium)

def countComponents(self, n: int, edges: List[List[int]]) -> int:
    graph_map = {i: [] for i in range(n)}
    visited = set()
    count = 0

    for a, b in edges:
        graph_map[a].append(b)
        graph_map[b].append(a)

    def dfs(a):
        visited.add(a)
        for i in graph_map[a]:
            if i not in visited:
                dfs(i)

    for j in graph_map:
        if j not in visited:
            dfs(j)
            count += 1
    return count

# union find
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    par = [i for i in range(n)]
    rank = [1] * n

    def find(a):

        node = a

        while node != par[node]:
            par[node] = par[par[node]]
            node = par[node]
        return node

    def union(a, b):
        p1, p2 = find(a), find(b)

        if p1 == p2:
            return 0

        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return 1

    count = n
    for a, b in edges:
        count -= union(a, b)

    return count





