from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_nodes = []
        self.bfs_queue = []
        self.parent = dict()
        self.path = []
        self.is_solved = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def shortest_path(self, u, v):
        self.bfs_queue.append(u)
        self.visited_nodes.append(u)
        self.parent[u] = -1

        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            for adj_node in self.graph[curr_node]:
                if adj_node not in self.visited_nodes:
                    self.bfs_queue.append(adj_node)
                    self.visited_nodes.append(adj_node)
                    self.parent[adj_node] = curr_node
                if adj_node ==  v:
                    self.is_solved = True
                    break
            
            if self.is_solved:
                break

        self.print_shortest_path(u, v)

    def print_shortest_path(self, u, v):
        while v != -1:
            self.path.insert(0, v)
            v = self.parent[v]

        print(self.path)

if __name__ == "__main__":
    g = Graph()

    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)

    g.shortest_path(1, 5)