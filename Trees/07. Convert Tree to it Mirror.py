"""
    To Convert Tree to its Mirror.

->  Perform Post Order Traversal and Swap Left and Right Nodes 
"""


class BinaryTreeNode:
    def __init__(self, key, left, right):
        self.data = key
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def convert_to_mirror(root):
        if not root:
            return None

        Solution.convert_to_mirror(root.left)
        Solution.convert_to_mirror(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root

    @staticmethod
    def levelorder(root):
        queue = []
        queue.append(root)
        queue.append(None)

        while len(queue) > 0:
            curr = queue.pop(0)

            if curr == None:
                if len(queue) > 0:
                    queue.append(None)
            else:
                print(curr.data, end=" ")

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)


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

    _1 = Solution.convert_to_mirror(_1)

    Solution.levelorder(_1)
