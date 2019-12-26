class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None    

class Solution:
    @staticmethod
    def get_max_non_recursive(root: Node):
        if not root:
            return None

        while root.right:
            root = root.right
        return root.data

    @staticmethod
    def get_min_non_recursive(root: Node):
        if not root:
            return None

        while root.left:
            root = root.left
        return root.data

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(40)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.right = Node(50)
    root.right.right.left = Node(45)
    root.right.right.right = Node(60)

    print(Solution.get_max_non_recursive(root))
    print(Solution.get_min_non_recursive(root))