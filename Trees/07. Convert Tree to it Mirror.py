"""
    To Convert Tree to its Mirror.

->  Perform Post Order Traversal and Swap Left and Right Nodes 
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def convert_to_mirror(root):
        if not root:
            return None
        
        Solution.convert_to_mirror(root.left)
        Solution.convert_to_mirror(root.right)

        temp = root.left.data
        root.left.data = root.right.data
        root.right.data = temp

        