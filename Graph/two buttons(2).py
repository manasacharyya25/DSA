from  collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs_queue = []
        self.visited = []
        self.parent = dict()

    def solve(self, initial, final):
        self.bfs_queue.append(initial)
        self.parent[initial] = "x"

        while len(self.bfs_queue) > 0:
            current = self.bfs_queue.pop(0)

            if current in self.visited:
                continue

            self.visited.append(current)

            l_child = current*2
            r_child = current-1

            if l_child == final:
                self.parent[l_child] = current
                self.count_path(final)
                return
            if r_child == final:
                self.parent[r_child] = current
                self.count_path(final)
                return

            if l_child not in self.parent:
                self.parent[l_child] = current
                self.bfs_queue.append(l_child)
            if r_child not in self.parent:
                self.parent[r_child] = current
                self.bfs_queue.append(r_child)

    def count_path(self, node):
        count = 0
        while self.parent[node] != 'x':
            count+=1
            node = self.parent[node]
        print(count)

if __name__ == "__main__":
    ab = input().strip().split(' ')
    a = int(ab[0])
    b = int(ab[1])

    g = Graph()
    g.solve(a,b)