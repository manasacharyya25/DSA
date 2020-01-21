class Solution:
    @staticmethod
    def print_root_to_leaf_paths(root, path_arr, index):
        if not root:
            return
        
        path_arr[index] = root.data
        index+=1

        if not root.left and not root.right:
            Solution.print_arr(path_arr)

        Solution.print_root_to_leaf_paths(root.left, path_arr, index)
        Solution.print_root_to_leaf_paths(root.right, path_arr, index)

    @staticmethod
    def print_arr(arr):
        for x in arr:
            print(x, end=" ")
        print()
