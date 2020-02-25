class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None    

class Solution:
    number_of_nodes_visited = 0

    @staticmethod
    def get_kth_min(root: Node, k:int):
        """ 
           Maintain an array of size k
            When root.left is None, i+1 element is the kth min
        """
        arr = [0 for i in range(k)]
        index = 0

        while root:
            arr[index] = root.data
            index = (index + 1) % k

            root = root.left

        return arr[index] #since index is already incremented in loop

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(40)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.right = Node(50)
    root.right.right.left = Node(45)
    root.right.right.right = Node(60)

    Solution.get_kth_min(root, 3)