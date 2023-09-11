# Using adjacency list
import collections


class GraphList:
    def __init__(self):
        self.graph = {}
        self.vertices_no = 0

    def add_vertex(self, v):
        if v in self.graph:
            print(f'vertex {v} already in graph.')
        else:
            self.vertices_no += 1
            self.graph[v] = []

    def add_edge(self, v1, v2, e):
        if v1 not in self.graph:
            print(f'{v1} is not a vertex in the graph')
        elif v2 not in self.graph:
            print(f'{v2} is not a vertex in the graph')
        else:
            temp = [v2, e]
            self.graph[v1].append(temp)

    def print_graph(self):
        print(self.graph)
        print("  ")
        for vertex in self.graph:
            res = []
            for edge in self.graph[vertex]:
                #print(f'There is a vertex from {vertex} to {edge[0]} with weight {edge[1]}.')
                res.append([edge[0], edge[1]])
            print(f"{vertex} -> {res}")

    def dfs(self, start):

        # iterative
        stack = [start]

        while stack:
            curr = stack.pop()
            print(curr)
            for i in self.graph[curr]:
                stack.append(i[0])
        """
        # recursive
        print(start)
        for i in self.graph[start]:
            self.dfs(i[0])
        """

    def bfs(self, start):
        queue = collections.deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()
            print(curr)
            for i in self.graph[curr]:
                queue.append(i[0])


if __name__ == '__main__':
    graph = GraphList()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)

    graph.add_edge(1, 3, 0)
    graph.add_edge(1, 2, 0)
    graph.add_edge(2, 4, 0)
    #graph.add_edge(4, 3, 0)
    graph.add_edge(3, 5, 0)
    graph.add_edge(5, 6, 0)

    #graph.print_graph()

    graph.dfs(2)
    print("   ")
    graph.bfs(2)




