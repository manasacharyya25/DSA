class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def reverse_level_order(root):
        queue = [root]
        stack = []

        while queue:
            top = queue.pop(0)

            stack.append(top)
            
            if top.right:
                queue.append(top.right)

            if top.left:
                queue.append(top.left)

        while stack:
            top = stack.pop(-1)
            print(top)