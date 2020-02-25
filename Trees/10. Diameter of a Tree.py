"""
    Diameter of a Tree  =  Max(1 + LeftHeight + RightHeight, Max(LeftDiameter, RightDiameter))'

    Calculating Height of tree at each recursion increases time complexity to O(n^2)

    To reduuce this, we memoise height of each node
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    height_map = dict()

    @staticmethod
    def height(root):
        if not root:
            return 0

        if root.data in Solution.height_map:
            return Solution.height_map[root.data]

        Solution.height_map[root.data] = 1 + max(Solution.height(root.left), Solution.height(root.right))

    @staticmethod
    def diameter_util(root):
        if not root:
            return 0

        if root.left:
            lheight = Solution.height_map[root.left.data]
        else:
            lheight = 0
        
        if root.right:
            rheight = Solution.height_map[root.right.data]
        else:
            rheight = 0

        ldiameter = Solution.diameter_util(root.left)
        rdiameter = Solution.diameter_util(root.right)

        return max(1+lheight+rheight, max(ldiameter, rdiameter))

    @staticmethod
    def diameter(root):
        Solution.height(root)

        Solution.diameter_util(root)




