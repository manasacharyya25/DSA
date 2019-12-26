class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None    

class Solution:
    @staticmethod
    def find_key(root: Node, key: int):
        if not root:
            return False
        if root.data == key:
            return True
        
        if root.data > key:
            return Solution.find_key(root.left, key)
        else:
            return Solution.find_key(root.right, key)

    @staticmethod
    def find_key_non_recursive(root: Node, key: int):
        while root:
            if root.data == key:
                return True

            if root.data > key:
                root = root.left
            else:
                root = root.right
        return False
        
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(40)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.right = Node(50)
    root.right.right.left = Node(45)
    root.right.right.right = Node(60)

    print(Solution.find_key(root, 40))
    print(Solution.find_key(root, 47))

    print(Solution.find_key_non_recursive(root, 40))
    print(Solution.find_key_non_recursive(root, 47))