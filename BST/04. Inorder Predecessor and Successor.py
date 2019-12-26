class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None    

class Solution:
    @staticmethod
    def find(root: Node, key: int):
        if not root:
            return None
        if root.data == key:
            return root
        if root.data > key:
            return Solution.find(root.left, key)
        else:
            return Solution.find(root.right, key)

    @staticmethod
    def get_max(root: Node):
        if not root:
            return None

        while root.right:
            root = root.right
        return root.data

    @staticmethod
    def get_min(root: Node):
        if not root:
            return None

        while root.left:
            root = root.left
        return root.data

    @staticmethod
    def get_predecessor(root: Node, key: int):
        if not root:
            return None
        
        curr = Solution.find(root, key)

        if curr.left:
            return Solution.get_max(curr.left)
        else:
            anc = root
            pre = None

            while(anc.data != curr.data):
                if anc.data > curr.data: 
                    anc = anc.left
                else:
                    pre = anc
                    anc = anc.right        
            return pre.data

    @staticmethod
    def get_successor(root: Node, key: int):
        if not root:
            return None

        curr = Solution.find(root, key)

        if curr.right:
            return Solution.get_min(root.right)
        else:
            anc = root
            succ = None

            while anc != curr:
                if anc.data < curr.data:
                    anc = anc.right
                else:
                    succ = anc
                    anc = anc.left
            return succ.data

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(40)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right.right = Node(50)
    root.right.right.left = Node(45)
    root.right.right.right = Node(60)

    print(Solution.get_predecessor(root, 10))
    print(Solution.get_successor(root, 10))

    print(Solution.get_predecessor(root, 6))
    print(Solution.get_successor(root, 7))