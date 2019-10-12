from collections import defaultdict

class Graph:
    def __init__(self):
        self.count = 0
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def count_paths(self, s, d):
        self.count_paths_util(s, d)
        return self.count

    def count_paths_util(self, s, d):
        self.visited.append(s)

        if s == d:
            self.count+=1
            self.print_path()
        else:
            for node in self.graph[s]:
                if node not in self.visited:
                    self.count_paths_util(node, d)
        self.visited.remove(s)

    def print_path(self):
        for x in self.visited:
            print(x,end='->')
        print()

if __name__ == "__main__":
    t = int(input())

    while t>0:
        t-=1

        ve = input().strip().split(' ')
        v = int(ve[0])
        e = int(ve[1])

        edges = input().strip().split(' ')

        g = Graph()

        for i in range(e):
            g.addEdge(int(edges[2*i]), int(edges[2*i+1]))

        sd = input().strip().split(' ')
        s = int(sd[0])
        d = int(sd[1])

        print(g.count_paths(s, d))

