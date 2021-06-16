class BinaryTreeNode:
    def __init__(self, key, left_child, right_child):
        self.data = key
        self.left = left_child
        self.right = right_child


class Traversal:
    @staticmethod
    def Preorder(root):
        stack = []
        curr = root

        while True:             # While True Loop, with Break Condition Checking Stack is empty inside the loop
            while(curr):
                print(curr.data, end=" ")
                stack.append(curr)
                curr = curr.left

            if len(stack) <= 0:     # While True Loop Break Condition. Check before Stack.Pop()
                return

            top = stack.pop(-1)

            """ Set Current to Top.Right , without checking for Null.  """
            curr = top.right

    @staticmethod
    def Inorder(root):
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            if len(stack) <= 0:
                return

            top = stack.pop(-1)
            print(top.data, end=" ")

            curr = top.right

    @staticmethod
    def Postorder(root):
        def peek(stack):
            """ Utility Method Required for checking last element of Stack Against Stack.Top()
            """
            return stack[-1] if len(stack) > 0 else None

        stack = []
        curr = root

        while True:                                                             # While True Loop as usual
            while curr:                                                         # While Curr Loop as Usual
                if curr.right:                                       # If Curr.Right Exist, Push before Pushing Curr to Stack
                    stack.append(curr.right)
                # Push Curr As Usual
                stack.append(curr)
                # Move Curr to Curr.Left as usual
                curr = curr.left

            # Check Stack Not Empty as Usual
            if len(stack) <= 0:
                return

            # Pop Stack Top Element as usual
            top = stack.pop(-1)

            # Check if Top Element has a Right Element and It is the Current Top of Stack.
            if top.right and top.right == peek(stack):
                # Implies top needs to be pushed Back to Stack, and Process Right Child Before that.
                curr = stack.pop(-1)
                stack.append(top)
            else:
                # Print Top Element as Usual
                print(top.data, end=" ")
                # Set Curr to Null. This happens automatically in Preorder and Inorder.
                curr = None

    @staticmethod
    def Postorder_simpler(root):
        def peek(stack):
            """ Utility Method Required for checking last element of Stack Against Stack.Top()
            """
            return stack[-1] if len(stack) > 0 else None

        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                stack.append(curr)
                curr = curr.left

            if len(stack) <= 0:
                return

            top = stack.pop(-1)

            if top == peek(stack):
                curr = top.right
            else:
                print(top.data, end=" ")
                curr = None

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
                /  \     \
               4    5     6
                \        /
                 7      8
    """
    _8 = BinaryTreeNode(8, None, None)
    _7 = BinaryTreeNode(7, None, None)
    _4 = BinaryTreeNode(4, None, _7)
    _5 = BinaryTreeNode(5, None, None)
    _6 = BinaryTreeNode(6, _8, None)
    _2 = BinaryTreeNode(2, _4, _5)
    _3 = BinaryTreeNode(3, None, _6)
    _1 = BinaryTreeNode(1, _2, _3)

    Traversal.levelorder(_1)
