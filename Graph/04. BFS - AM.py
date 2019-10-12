class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0 for i in range(vertex)] for j in range(vertex)]
        self.bfs_queue = []
        self.visited_nodes = []

    def addEdge(self, u, v):
        self.graph[u][v] = 1

    def bfs(self, start_node):
        self.bfs_queue.append(start_node)

        print("BFS Traversal Below:" )
        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            if curr_node in self.visited_nodes:
                continue

            print(curr_node)
            self.visited_nodes.append(curr_node)

            for i in range(self.vertex):
                node = i
                if self._is_adjacent(curr_node, node) and node not in self.visited_nodes:
                    self.bfs_queue.append(node)

    def _is_adjacent(self, u,v):
        return True if self.graph[u][v] == 1 else False

if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,4)
    g.addEdge(1,1)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(3,4)

    g.bfs(0)