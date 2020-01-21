"""
    To Check if two trees are Structurally Same.

->  Check if both trees are Null, return True.
    If one is Null and other is not, return False.
    Check if data is same and recursively check for left and right subtrees.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def are_structurally_same(root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        return ((root1.data == root2.data)\
            and (Solution.are_structurally_same(root1.left, root2.left)\
            and (Solution.are_structurally_same(root1.right, root2.right))
