class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def increasingBST(root: TreeNode) -> TreeNode:
        stack = []
        res_tree_node = None
        next_ptr = None

        while True:
            while root:
                stack.append(root)
                root = root.left

            if len(stack) <= 0:
                break

            top = stack.pop(-1)

            if not res_tree_node:
                res_tree_node = TreeNode(top.val)
                next_ptr = res_tree_node
            else:
                next_ptr.right = TreeNode(top.val)
                next_ptr = next_ptr.right

            root = top.right

        return res_tree_node


if __name__ == "__main__":
    pass
