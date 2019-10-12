from collections import defaultdict
import queue

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.bfs_queue = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_index):
        self.visited.clear()
        self.bfs_queue.append(start_index)
        self.visited.append(start_index)

        while len(self.bfs_queue) != 0:
            current_node = self.bfs_queue.pop(0)

            if current_node in self.visited:        # if same node is in bfs_queue, skip it
                continue

            print("Current Node: ", current_node)
            self.visited.append(current_node)
            
            for adj_node in self.graph[current_node]:
                if adj_node not in self.visited:
                    self.bfs_queue.append(adj_node)
                    # self.visited.append(adj_node)     # appending to visited list here, prevents duplicate entry to bfs_queue, due to check above

            print("BFS Queue: ", end = " ")
            print(*self.bfs_queue)
            print()
            print("Visited Nodes: ", end = " ")
            print(*self.visited)
            print("---"*5)
            print()

    def dfs(self, start_index):
        self.visited.clear()
        self.visited.append(start_index)
        
        print("DFS Traversal")
        self.dfs_util(start_index)

    def dfs_util(self, node):
        print(node, end=" ")
        for adj_node in self.graph[node]:
            if adj_node not in self.visited:
                self.visited.append(adj_node)
                self.dfs_util(adj_node)
        

if __name__ == "__main__":
    g = Graph()

    g.addEdge(1,5)
    g.addEdge(1,2)
    g.addEdge(2,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(5,4)

    g.bfs(1)
    g.dfs(1)


