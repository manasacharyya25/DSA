from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs_queue = []
        self.visisted_nodes = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_index):
        self.bfs_queue.append(start_index)

        print("BFS Traversal Below: ")

        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            if curr_node in self.visisted_nodes:
                continue

            print(curr_node, end=" ")
            self.visisted_nodes.append(curr_node)

            for adj_node in self.graph[curr_node]:
                if adj_node not in self.visisted_nodes:
                    self.bfs_queue.append(adj_node)

    def print_adjacency_list(self):
        for vertex in self.graph:
            print(vertex," : ", self.graph[vertex])

if __name__=="__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(1,6)
    g.addEdge(2,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    g.addEdge(4,5)

    g.bfs(1)