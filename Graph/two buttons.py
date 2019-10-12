from  collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs_queue = []
        self.visited = []
        self.parent = dict()
        self.path = []
        self.isSolvable = False

    def solve(self, initial, final):
        count = 0
        self.bfs_queue.append(initial)
        self.bfs_queue.append('x')

        while len(self.bfs_queue) > 0:
            current = self.bfs_queue.pop(0)

            if current == 'x':
                self.bfs_queue.append('x')
                count+=1
                continue

            if current in self.visited:
                continue

            self.visited.append(current)

            if current == final:
                print(count)
                return

            l_child = current*2
            r_child = current-1

            self.graph[current].append(l_child)
            self.graph[current].append(r_child)            
            
            for adj_node in self.graph[current]:
                if adj_node not in self.visited:
                    self.bfs_queue.append(adj_node)

if __name__ == "__main__":
    ab = input().strip().split(' ')
    a = int(ab[0])
    b = int(ab[1])

    g = Graph()
    g.solve(a,b)