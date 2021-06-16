class BinaryTreeNode:
    def __init__(self, key, left, right):
        self.data = key
        self.left = left
        self.right = right


class Solution:
    """
        Calculate Height of Each Node
        Calculate Diameter of Each Node  ( 1 + height of left subtree + height of right subtree) in Postorder Manner
        Return Max of Diameter across all nodes
    """
    height_dict = dict()
    height_dict[None] = 0
    diameter_arr = []

    @ staticmethod
    def height(node):
        if not node:
            return 0
        else:
            Solution.height_dict[node] = 1 + \
                max(Solution.height(node.left), Solution.height(node.right))
            return Solution.height_dict[node]

    @ staticmethod
    def diameter(node):
        if not node:
            return 0
        else:
            # Recursively calculate diameter of each node in Postorder Manner
            Solution.diameter(node.left)
            Solution.diameter(node.right)

            # Current Diameter is 1 + Height(Node.Left) + Height(Node.Right)

            curr_diameter = 1 + \
                Solution.height_dict[node.left] + \
                Solution.height_dict[node.right]

            Solution.diameter_arr.append(curr_diameter)


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

    Solution.height(_1)
    Solution.diameter(_1)
    print(max(Solution.diameter_arr))
