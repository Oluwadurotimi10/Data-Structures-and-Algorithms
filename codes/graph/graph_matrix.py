# Using adjacency matrix

class GraphMatrix:
    def __init__(self):
        self.vertices = []
        self.graph = []
        self.vertices_no = 0

    def add_vertex(self, v):
        if v in self.vertices:
            print(f'vertex {v} already in graph.')
        else:
            self.vertices_no += 1
            self.vertices.append(v)

            if self.vertices_no > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.vertices_no):
                temp.append(0)
            self.graph.append(temp)
            print(self.graph)

    def add_edge(self, v1, v2, e):
        if v1 not in self.vertices:
            print(f'{v1} is not a vertex in the graph')
        elif v2 not in self.vertices:
            print(f'{v2} is not a vertex in the graph')
        else:
            #idx1 = self.vertices.index(v1)
            #idx2 = self.vertices.index(v2)
            self.graph[idx1][idx2] = e

    def print_graph(self):
        for i in self.vertices_no:
            for j in self.vertices_no:
                if self.graph[i][j] != 0:
                    print(f'There is a vertex from {self.vertices[i]} to {self.vertices[j]} with weight {self.graph[i][j]}.')


if __name__ == '__main__':
    graph = GraphMatrix()
    graph.add_vertex(1)
    graph.add_vertex(1)
    graph.add_vertex(3)
    graph.add_vertex(9)
    graph.add_vertex(2)
    graph.add_edge(1,3,6)
    graph.add_vertex(4)
