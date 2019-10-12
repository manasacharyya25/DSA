from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs_queue = []
        self.visisted_nodes = []
        self.is_reachable = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def path_exist(self, t):
        self.bfs_queue.append(1)

        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            self.visisted_nodes.append(curr_node)

            for adj_node in self.graph[curr_node]:
                if adj_node == t:
                    return True
                if adj_node > t:
                    return False
                if adj_node not in self.visisted_nodes:
                    self.bfs_queue.append(adj_node)
                    self.visisted_nodes.append(adj_node)
        
        return self.is_reachable

if __name__=="__main__":
    nt = input().strip().split(' ')
    
    n = int(nt[0])
    t = int(nt[1])

    _arr= input().strip().split(' ')

    portal_arr = ['x']
    for x in _arr:
        portal_arr.append(int(x))

    g = Graph()

    for i in range(1, len(portal_arr)):
        g.addEdge(i, i + portal_arr[i])

    if g.path_exist(t):
        print("YES")
    else:
        print("NO")
