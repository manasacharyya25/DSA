class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0 for i in range(vertex)] for j in range(vertex)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1

    def print_adjacency_matrix(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.graph[i][j], end=" ")
            print()

if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,4)
    g.addEdge(1,1)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(3,4)

    g.print_adjacency_matrix()