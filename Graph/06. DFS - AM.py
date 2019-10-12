class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0 for i in range(vertex)] for j in range(vertex)]
        self.visited_nodes = []

    def addEdge(self, u, v):
        self.graph[u][v] = 1

    def dfs(self, start_node):
        print(" DFS Traversal Below: ")
        self.dfs_util(start_node)

    def dfs_util(self, curr_node):
        print(curr_node, end=" ")
        self.visited_nodes.append(curr_node)

        for i in range(self.vertex):
            node = i
            if self.is_adjacent(curr_node, node) and node not in self.visited_nodes:
                self.dfs_util(node)

    def is_adjacent(self, u, v):
        return True if self.graph[u][v] == 1 else False

if __name__=="__main__":
    g = Graph(6)
    g.addEdge(0,1)
    g.addEdge(0,4)
    g.addEdge(0,5)
    g.addEdge(1,1)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(3,4)

    g.dfs(0)