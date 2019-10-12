from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.bfs_queue = []
        self.parent = dict()
        self.path = []

    def count_min_button_press(self, u, v):
        self.bfs_queue.append(u)
        self.visited.append(u)
        self.parent[u] = -1

        while len(self.bfs_queue) > 0:
            curr_node = self.bfs_queue.pop(0)

            if curr_node ==  v:
                self.is_solved = True
                break
            else:
                mul_child = curr_node*2
                sub_child = curr_node-1

                if mul_child ==  v:
                    self.parent[mul_child] = curr_node
                    self.print_path(v)
                    break
                elif sub_child == v:
                    self.parent[sub_child] = curr_node
                    self.print_path(v)
                    break
                
                if mul_child not in self.visited:
                    self.bfs_queue.append(mul_child)
                    self.visited.append(mul_child)
                    self.parent[mul_child] = curr_node

                
                if sub_child not in self.visited:
                    self.bfs_queue.append(sub_child)
                    self.visited.append(sub_child)
                    self.parent[sub_child] = curr_node

    def print_path(self, v):
        while v != -1:
            self.path.insert(0, v)
            v = self.parent[v]
        print(self.path)
        print("Min. Button Presses Required", len(self.path)-1)

if __name__=="__main__":
    g = Graph()

    #g.count_min_button_press(4, 6)
    print()
    #g.count_min_button_press(10, 1)
    print()
    g.count_min_button_press(8, 28)
    