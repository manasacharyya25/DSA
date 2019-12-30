class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class TreeTraversal:
    @staticmethod
    def Preorder(root):
        """ For Non Recursive Preorder Traversal:
            -   Create Empty Stack and Push root to stack
            -   Append root.right first to stack and then root.left
            -   As a result, left nodes will be processed before right, which is the desired behaviour
        """
        stack = [root]

        while stack:
            curr = stack.pop(-1)
            print(curr.data, end = " ")
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.push(curr.left)

    @staticmethod
    def Inorder(root):
        stack = []
        curr = root

        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            if not stack:
                break

            temp = stack.pop(-1)
            print(temp.data)

            if temp.right:
                curr = temp.right

    @staticmethod
    def Postorder(root):
        while(True):
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            if not stack:
                break

            root = stack.pop(-1)
            if root.right and root.right == stack[-1]:
                stack.pop(-1)
                stack.append(root)
                root = root.right
            else:
                print(root.data)
                root = None     #Set to NULL else while loop will run again

    @staticmethod
    def Postorder_Simpler(root):
        while(True):
            while root:
                stack.push(root)
                stack.push(root)
                if root.left:
                    root = root.left

            if not stack:
                break

            root = stack.pop(-1)
            if root == stack[-1] and root.right:
                root = root.right
            else:
                print(root.data)
                root = None     #Set to NULL else while loop will run again

        