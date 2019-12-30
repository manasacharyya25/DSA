class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def find_lca(root, k1, k2):
        """Level Order Traversal
        """
        
        queue = [root]
                
            while queue:
                curr = queue.pop(0)
                
                if curr.key in range(k1, k2+1):
                    return curr.key
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
