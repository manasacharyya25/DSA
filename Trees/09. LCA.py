class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def LCA(root, key1, key2):
        if not root:
            return None

        if root.data == key1 or root.data == key2:
            return root
            

        left = Solution.LCA(root.left, key1, key2)
        right = Solution.LCA(root.right, key1, key2)

        if left and right:
            return root
        
        return left if left else right
