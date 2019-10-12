from collections import defaultdict
import queue

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.bfs_queue = []
        self.path = dict()
        self.isSolved = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_shortest_path(self, start_index, final_index):
        self.visited.clear()
        self.bfs_queue.append(start_index)
        self.visited.append(start_index)
        self.path[start_index]=-1

        while len(self.bfs_queue) != 0:
            current_node = self.bfs_queue.pop(0)
            
            if self.isSolved:
                self.print_path(final_index)
                break

            for adj_node in self.graph[current_node]:
                if adj_node not in self.visited:
                    if adj_node == final_index:
                        self.path[adj_node] = current_node
                        self.isSolved = True
                        break
                    self.bfs_queue.append(adj_node)
                    self.path[adj_node] = current_node
                    self.visited.append(adj_node)       # Must Append to Visited List, when pushing into bfs_queue, else same element may exist in bfs_queue more than once

    def print_path(self, dest_node):
        if self.path[dest_node] == -1:
            print(dest_node)
            return  
        print(dest_node)
        self.print_path(self.path[dest_node])
                
if __name__ == "__main__":
    g = Graph()

    g.addEdge(1,5)
    g.addEdge(1,2)
    g.addEdge(2,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(5,4)
    g.addEdge(4,6)
    g.addEdge(5,6)

    g.find_shortest_path(1, 6)


