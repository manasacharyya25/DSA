class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    inorder_traversal_of_bt = []
    
    @staticmethod
    def convert_bt_to_bst(root):
        Solution.store_inorder(root)

        Solution.inorder_traversal_of_bt.sort()

        Solution.copy_arr_to_tree(root)

    @staticmethod
    def store_inorder(root):
        if not root:
            return

        Solution.store_inorder(root.left)
        Solution.inorder_traversal_of_bt.append(root.data)
        Solution.store_inorder(root.right)

    @staticmethod
    def copy_array_to_tree(root):
        if not root:
            return

        Solution.copy_array_to_tree(root.left)
        
        root.data = Solution.inorder_traversal_of_bt[0]
        Soluton.inorder_traversal_of_bt.pop(0)

        Solution.copy_array_to_tree(root.right)

        

