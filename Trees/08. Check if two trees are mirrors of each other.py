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
        if not root1 or not root2:          # Since Both Null is already checked, Checking For OR Condition implies 1 of them is Null,
            return False
        if root1.data != root2.data:
            return False
        return (Solution.are_mirrors(root1.left, root2.right)
                and Solution.are_mirrors(root1.right, root2.left))

    @staticmethod
    def are_mirrors_iterative(root1, root2):
        def inorder(root):
            pass

        inorder1 = inorder(root1)
        inorder2 = inorder(root2)

        if inorder1 == inorder2.reverse():
            return True
        else:
            return False
