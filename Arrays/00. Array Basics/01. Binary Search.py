#
# Find an element in Sorted Array in O(log n) Time Complexity
#

class Solution:
    @staticmethod
    def binary_search_iterative(arr, k):
        start = 0
        end = len(arr) - 1

        if arr[start] == k:
            return start
        if arr[end] == k:
            return end

        while end >= start:
            mid = start + (end-start)//2

            if arr[mid] == k:
                return mid

            if k < arr[mid]:
                end = mid-1
            else:
                start = mid+1

        return "Not Found"

    @staticmethod
    def binary_search_recursive(arr, start, end, k):
        if end >= start:
            if arr[start] == k:
                return start

            if arr[end] == k:
                return end

            mid = start+(end-start)//2

            if arr[mid] == k:
                return mid

            if k < arr[mid]:
                return Solution.binary_search_recursive(arr, start, mid-1, k)
            else:
                return Solution.binary_search_recursive(arr, mid+1, end, k)
        return "Not Found"


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Iterative Binary Search\n")
    print("0: ", Solution.binary_search_iterative(arr, 0))
    print("1: ", Solution.binary_search_iterative(arr, 1))
    print("3: ", Solution.binary_search_iterative(arr, 3))
    print("5: ", Solution.binary_search_iterative(arr, 5))
    print("8: ", Solution.binary_search_iterative(arr, 8))
    print("10: ", Solution.binary_search_iterative(arr, 10))
    print("11: ", Solution.binary_search_iterative(arr, 11))

    print("\nRecursive Binary Search\n")
    print("0: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 0))
    print("1: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 1))
    print("3: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 3))
    print("5: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 5))
    print("8: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 8))
    print("10: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 10))
    print("11: ", Solution.binary_search_recursive(arr, 0, len(arr)-1, 11))
