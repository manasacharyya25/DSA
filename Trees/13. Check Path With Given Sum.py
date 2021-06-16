class BinaryTreeNode:
    def __init__(self, key, left, right):
        self.data = key
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def check_sum(arr, index, s):
        return sum(arr[0:index]) == s

    @staticmethod
    def check_path_with_given_sum(root, arr, arr_index, sum):
        if not root:
            return

        arr[arr_index] = root.data
        arr_index += 1

        if not root.left and not root.right:
            if Solution.check_sum(arr, arr_index, sum):
                print("True")
        else:
            Solution.check_path_with_given_sum(root.left, arr, arr_index, sum)
            Solution.check_path_with_given_sum(root.right, arr, arr_index, sum)


if __name__ == "__main__":
    """
        Creating Binary Tree Structure

                     1
                   /   \
                  2     3
                /  \
               4    5
                \    \
                 7    6
                /     /
               9     8
               \
               10
    """
    _10 = BinaryTreeNode(10, None, None)
    _9 = BinaryTreeNode(9, None, _10)
    _8 = BinaryTreeNode(8, None, None)
    _7 = BinaryTreeNode(7, _9, None)
    _4 = BinaryTreeNode(4, None, _7)
    _6 = BinaryTreeNode(6, _8, None)
    _5 = BinaryTreeNode(5, None, _6)
    _2 = BinaryTreeNode(2, _4, _5)
    _3 = BinaryTreeNode(3, None, None)
    _1 = BinaryTreeNode(1, _2, _3)

    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 4)
    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 10)
    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 33)
    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 34)
    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 22)
    Solution.check_path_with_given_sum(
        _1, [0 for i in range(100)], 0, 20)
