"""
Idea here is to perform a DFS on the Graph and look for back-edge. 
If a back-edge exist, that confirms a cycle exists in the graph.

How to look for a back edge:
    - Perform DFS Recusively. 
    - Maintain a separate Stack, to keep track of nodes currently in the recursive call stack
    - At each recursive call to "DfsUtil", push the node into the Stack
    - While looking into the adj_nodes, if we find such a node that is still in the recursive call stack, Cycle exists
    - Once DfsUtil has been recursively called for al adj_nodes, remove curr_node from recursive call stack
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.recusrive_call_stack = []
        self.visited_nodes = []
        self.cycles_count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_node):
        self.visited_nodes.append(start_node)
        
        self.dfs_util(start_node)

    def dfs_util(self, curr_node):
        self.recusrive_call_stack.append(curr_node)

        for adj_node in self.graph[curr_node]:
            if adj_node in self.recusrive_call_stack:
                self.cycles_count += 1
                continue                    # donot call DfsUtil for the cycle forming node again, as it is already in recursive call stack
            
            if adj_node not in self.visited_nodes:
                self.visited_nodes.append(adj_node)
                self.dfs_util(adj_node)

        self.recusrive_call_stack.pop(-1)

    def check_if_cycle_exists(self):
        if self.cycles_count == 0:
            print("Cycle Doesnot Exist")
        else:
            print(self.cycles_count, "Cycles Exist")

if __name__=="__main__":
    g = Graph()

    g.addEdge(1, 2)
    g.addEdge(1, 6)
    g.addEdge(2, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 2)
    g.addEdge(4, 5)
    g.addEdge(5, 1)
    g.addEdge(6,6)
    g.addEdge(7,8)
    g.addEdge(8,7)

    for vertex in g.graph:
        if vertex not in g.visited_nodes:
            g.dfs(vertex)

    g.check_if_cycle_exists()



