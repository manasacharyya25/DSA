from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs_queue = []
        self.visisted_nodes = []

        # DATA STRUCTURE TO STORE LEVEL INFORMATION
        self.level_of_node = defaultdict(int)
        self.number_of_nodes_in_level = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_index):
        self.bfs_queue.append(start_index)
        self.level_of_node[start_index] = 0
        self.number_of_nodes_in_level[0] = 1

        print("BFS Traversal Below: ")

        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            # REMOVE VISITED CHECK FROM HERE

            print(curr_node, end=" ")
            self.visisted_nodes.append(curr_node)

            for adj_node in self.graph[curr_node]:
                if adj_node not in self.visisted_nodes:
                    self.bfs_queue.append(adj_node)
                    # APPEND TO VISITED AT THIS LEVEL 
                    self.visisted_nodes.append(adj_node)
                    self.level_of_node[adj_node] = self.level_of_node[curr_node] + 1
                    self.number_of_nodes_in_level[self.level_of_node[adj_node]] += 1

    def print_adjacency_list(self):
        print("\n\nAdjacency List: ")
        for vertex in self.graph:
            print(vertex," : ", self.graph[vertex])

    def print_level_of_each_node(self):
        print("\nNode : Level")
        for node in self.level_of_node:
            print(node, " : ", self.level_of_node[node])

    def print_number_of_nodes_in_each_level(self):
        print("\nLevel: Number of Nodes")
        for level in self.number_of_nodes_in_level:
            print(level, " : ", self.number_of_nodes_in_level[level])

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

    g.print_adjacency_list()
    g.print_level_of_each_node()
    g.print_number_of_nodes_in_each_level()