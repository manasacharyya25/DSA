from collections import defaultdict


class Array:
    @staticmethod
    def rotate_array(arr, k):
        # Copy First K Elements
        tmp_arr = arr[0:k]

        # Shift last n-k elements to left
        arr = arr[k:]

        # Append first K elements at the end
        for x in tmp_arr:
            arr.append(x)

        return arr


class BinaryTree:
    class Node:
        def __init__(self, val, left, right):
            self.value = val
            self.left = left
            self.right = right

    def __init__(self, parent: Node):
        self.parent = parent

    def preorder_traveral(self, node):
        if node == None:
            return

        self.preorder_traveral(node.left)
        print(node.value, end=' ')
        self.preorder_traveral(node.right)


class Graph:
    def __init__(self):
        self.adjList: defaultdict = defaultdict(list)
        self.bfsQueue: list = list()
        self.bfsVisitedNodes: list = list()

    def addEdge(self, a, b):
        self.adjList[a].append(b)

    def printAdjList(self):
        for node in self.adjList:
            print(node, " ", self.adjList[node], end='\n')

    def bfs(self, startNode):
        self.bfsQueue.append(startNode)
        self.bfsVisitedNodes.append(startNode)

        while (len(self.bfsQueue) != 0):
            top = self.bfsQueue.pop(0)
            print(top, end=" ")

            for node in self.adjList[top]:
                if node not in self.bfsVisitedNodes:
                    self.bfsQueue.append(node)
                    self.bfsVisitedNodes.append(node)

    def dfs(self, startNode):
        def dfsUtil(node):
            self.bfsQueue.append(node)
            for adjNode in self.adjList[node]:
                if adjNode not in self.bfsVisitedNodes:
                    dfsUtil(adjNode)
            top = self.bfsQueue.pop()
            print(top, end=" ")
            self.bfsVisitedNodes.append(top)

        self.bfsQueue.append(startNode)
        dfsUtil(startNode)


class BST:
    class Node:
        def __init__(self, k, l, r):
            self.data = k

    def find(self, root, k):
        if not root:
            return

        if k == root.data:
            return root

        if k < root.data:
            find(root.left)

        if k > root.data:
            find(root.right)

    def find_iterative(self, root, k):
        while root:
            if root.data == k:
                return root
            if k < root.data:
                root = root.left
            else:
                root = root.right
        return False

    def find_kth_min(self, root, k):
        min_arr = []

        while root:
            min_arr.append(root.data)
            root = root.left

        return min_arr[k-1]

    def find_inbetween(self, root, k1, k2):
        res = []

        while root:
            if root.data > k1 and root.data < k2:
                res.append(root.data)

            if root.data < k1:
                root = root.right
            if root.data > k2:
                root = root.left
        return res


class MajorityElement:
    @staticmethod
    def majorityElement(nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


class Leetcode:


if __name__ == '__main__':
    # graph = Graph()
    # graph.addEdge(1, 3)
    # graph.addEdge(1, 6)
    # graph.addEdge(1, 2)
    # graph.addEdge(2, 4)
    # graph.addEdge(2, 5)
    # graph.addEdge(3, 5)
    # graph.addEdge(6, 7)
    # graph.addEdge(5, 7)

    # graph.dfs(1)

    # print(Array.rotate_array([1, 2, 3, 4, 5, 6, 7], 3))

    # n1 = BinaryTree.Node(1, None, None)
    # n2 = BinaryTree.Node(2, None, None)
    # n3 = BinaryTree.Node(3, None, None)
    # n1.left = n2
    # n1.right = n3

    # n0 = BinaryTree.Node(0, n1, None)

    # binaryTree = BinaryTree(n0)

    # binaryTree.preorder_traveral(n0)

    print(MajorityElement.majorityElement([7, 7, 5, 7, 6, 1, 1]))
