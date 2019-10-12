from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visisted_nodes = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_node):
        print("DFS Traversal Below: ")

        self.dfs_util(start_node)

    def dfs_util(self, curr_node):
        print(curr_node, end=" ")
        self.visisted_nodes.append(curr_node)

        for adj_node in self.graph[curr_node]:
            if adj_node not in self.visisted_nodes:
                self.dfs_util(adj_node)

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

    g.dfs(1)