class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def are_mirrors(root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        return ((root1.left.data == root2.right.data)\
            and (Solution.are_mirrors(root1.left, root2.right)\
            and (Solution.are_mirrors(root1.right, root2.left))
