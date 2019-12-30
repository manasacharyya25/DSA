class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def construct_bst_from_prrorder(arr):
        root = Node(arr[0])
        
        if len(arr) == 1:
            return root

        next_biggest_index = Solution.find_index_of_next_biggest_element(arr)

        if next_biggest_index == 0:
            root.left =  Solution.construct_bst_from_prrorder(arr[next_biggest_index:])
            root.right = None
            return root
        if next_biggest_index == 1:
            root.left = None
            root.right = Solution.construct_bst_from_prrorder(arr[next_biggest_index:])
            return root
        
        root.left = Solution.construct_bst_from_prrorder(arr[1:next_biggest_index])
        root.right = Solution.construct_bst_from_prrorder(arr[next_biggest_index:])

        return root

    @staticmethod
    def find_index_of_next_biggest_element(arr):
        max_index = 0

        for i in range(1, len(arr)):
            if arr[i]>arr[max_index]:
                max_index = i

        return max_index

    @staticmethod
    def inorder(root):
        if not root:
            return 
        if root.left:
            Solution.inorder(root.left)
        print(root.data)
        if root.right:
            Solution.inorder(root.right)

if __name__ == "__main__":
    # root = Solution.construct_bst_from_prrorder([10, 5, 4, 8, 7, 6, 9, 15])
    root = Solution.construct_bst_from_prrorder([12, 9, 10, 15])
    Solution.inorder(root)