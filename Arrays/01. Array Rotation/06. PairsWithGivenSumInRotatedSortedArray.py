#
# Given a sorted and rotated array, find if there is a pair with a given sum
#
# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

class Solution:
    def find_pair_with_sum_1(arr, k):
        """ Meet In The Middle Algorithm
        """
        n = len(arr)

        def find_pivot(arr):
            start = 0
            end = len(arr) - 1

            if arr[end] > arr[start]:
                return 0

            while end >= start:
                mid = start + (end-start)//2

                if arr[mid] > arr[mid+1]:
                    return mid+1
                if arr[mid] < arr[mid-1]:
                    return mid

                if arr[mid] > arr[start]:
                    start = mid+1
                else:
                    end = mid-1

        smallest_index = find_pivot(arr)
        print("Pivot is at ", smallest_index)
        largest_index = smallest_index-1

        while smallest_index != largest_index:
            curr_sum = arr[smallest_index] + arr[largest_index]

            if curr_sum == k:
                return (arr[smallest_index], arr[largest_index])

            if curr_sum > k:
                largest_index = (largest_index - 1) % n
            else:
                smallest_index = (smallest_index + 1) % n

        return "Not Found"

    def find_pair_with_sum_2(arr, k):
        """ HashMap Method
        """
        pass


if __name__ == '__main__':
    arr = [11, 15, 6, 8, 9, 10]

    print(Solution.find_pair_with_sum_1(arr, 26))
