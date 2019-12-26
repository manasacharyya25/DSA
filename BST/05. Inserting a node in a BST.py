class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None    

class Solution:
    @staticmethod
    def new_node(key: int):
        return Node(key)

    @staticmethod
    def inorder(root): 
        if root: 
            Solution.inorder(root.left) 
            print(root.data) 
            Solution.inorder(root.right) 

    @staticmethod
    def insert(root: Node, key: int):
        parent = root
        while True:
            if key > root.data:
                if root.right:
                    root = root.right
                else:
                    root.right = Solution.new_node(key)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = Solution.new_node(key)
                    break
        return parent
        
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(40)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.right = Node(50)
    root.right.right.left = Node(45)
    root.right.right.right = Node(60)

    print("Before Inserting")
    Solution.inorder(root)
    root = Solution.insert(root, 6)
    print("After Inserting")
    Solution.inorder(root)
