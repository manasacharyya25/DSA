from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.dfs_stack = []
        self.visited_nodes = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node):
        self.dfs_stack.append(node)

        print("DFS Traversal Below: ")
        while len(self.dfs_stack) > 0:
            curr_node = self.dfs_stack.pop(-1)

            if curr_node in self.visited_nodes:
                continue

            print(curr_node, end=" ")
            self.visited_nodes.append(curr_node)

            for adj_node in self.graph[curr_node]:
                if adj_node not in self.visited_nodes:
                    self.dfs_stack.append(adj_node)

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
