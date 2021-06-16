class BinaryTreeNode:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def construct(inorder, preorder, p_ind):
        if not preorder or not inorder:
            return None

        if len(inorder) < 2:
            return BinaryTreeNode(inorder[0])

        root = BinaryTreeNode(preorder[p_ind])

        i_ind = inorder.index(preorder[p_ind])
        root.left = construct(inorder[0: i_ind], preorder[p_ind+1:], p_ind+1)
        root.right = construct(inorder[i_ind+1:], preorder[p_ind+1:], p_ind+1)
