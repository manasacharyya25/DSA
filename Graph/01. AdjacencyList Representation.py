from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print_adjacency_list(self):
        for vertex in self.graph:
            print(vertex," : ", self.graph[vertex])

if __name__=="__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(2,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    g.addEdge(4,5)

    g.print_adjacency_list()