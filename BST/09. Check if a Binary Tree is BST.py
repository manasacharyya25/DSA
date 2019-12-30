class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def check_bst_incorrect(root):
        """ This method check only immediate children of a node satisifes bst property
            Doesnot make sure entire subtree satisfies bst property
        """
        if not root:
            return

        Solution.check_bst(root.left)
        Solution.check_bst(root.right)

        if root.left.data <= root.data and root.right.data >= root.data:
            return True
        else:
            return False

    inorder_traversal = []

    @staticmethod
    def inorder(root):
        """ Perform Inorder Traversal
            Check if resulting list is in srted order 
        """
        if not root:
            return
        
        if root.left:
            Solution.inorder(root.left)

        Solution.inorder_traversal.append(root.data)

        if root.right:
            Solution.inorder(root.right)

        @staticmethod
    def check_bst(root):
        """ Perform Inorder Traversal
            Check if resulting list is in srted order 
        """
        Solution.inorder(root)

        prev = Solution.inorder_traversal[0]
        for x in Solution.inorder_traversal[1:]:
            if x > prev:
                continue
            else:
                return False
        return True