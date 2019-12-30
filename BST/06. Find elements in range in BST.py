class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def find_in_range(root, k1, k2):
        """Perform Inorder Traversal, to print numbers in Sorted Order
        """
        if k1 < root.data:
            Solution.find_in_range(root.left, k1, k2)
        
        if root.data in range(k1, k2+1):
            print(root.data, end=" ")

        if k2 > root.data:
            Solution.find_in_range(root.right, k1, k2)


