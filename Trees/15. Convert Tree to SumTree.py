class BinaryTreeNode:
    def __init__(self, k, left, right):
        self.data = k
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_tree(root):
        if not root:
            return 0

        # Trick is to store curr value in temp var
        curr_val = root.data

        left_sum = Solution.sum_tree(root.left)
        right_sum = Solution.sum_tree(root.right)

        # Udate Curr Node Data with sum of its Child
        root.data = left_sum+right_sum

        # Return TEMP_VAR + Left_sum + Right_sum
        return curr_val+left_sum+right_sum
