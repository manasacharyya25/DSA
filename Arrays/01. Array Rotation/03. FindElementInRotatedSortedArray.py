#
# Find an Element in a Sorted Array, rotated at an unknown pivot element
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/solution/
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/


class Solution:
    @staticmethod
    def find_element_in_rotated_sorted_array(arr, k):
        start = 0
        end = len(arr) - 1

        while end >= start:
            if arr[start] == k:
                return start

            if arr[end] == k:
                return end

            mid = start + (end-start)//2

            if arr[mid] == k:
                return mid

            # Check if mid element > start element. which means, Array[start:mid] is sorted. Hence break the array into two at mid and search on both sidesas per k
            if arr[mid] > arr[start]:
                if k > arr[start] and k < arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                # if mid element < start element. implies Array is rotated at some point between start:mid. Hence break the array at mid and serach for K on the two sub-arrays
                if k > arr[mid] and k < arr[end]:
                    start = mid+1
                else:
                    end = mid-1
        return "Not Found"


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 1, 2, 3, 4]

    print(Solution.find_element_in_rotated_sorted_array(arr, 0))
    print(Solution.find_element_in_rotated_sorted_array(arr, 5))
    print(Solution.find_element_in_rotated_sorted_array(arr, 6))
    print(Solution.find_element_in_rotated_sorted_array(arr, 7))
    print(Solution.find_element_in_rotated_sorted_array(arr, 8))
    print(Solution.find_element_in_rotated_sorted_array(arr, 1))
    print(Solution.find_element_in_rotated_sorted_array(arr, 2))
    print(Solution.find_element_in_rotated_sorted_array(arr, 3))
    print(Solution.find_element_in_rotated_sorted_array(arr, 4))
    print(Solution.find_element_in_rotated_sorted_array(arr, 9))
