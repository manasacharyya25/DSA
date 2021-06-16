#
# Rearrange positive and negative numbers alternatively in O(n) time and O(1) extra space
#
# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/


class Solution:
    @staticmethod
    def rearrange_positive_and_negative(arr):
        """ Uses Partition Method of Quick Sort to Rearrange elements in O(n) Time. 
        """
        pivot_element = 0
        start = 0
        end = len(arr) - 1

        while start < end:
            # If element is Positive, Place it at end. Decrement End. Continue looping wihout changing start
            if arr[start] > pivot_element:
                arr[start], arr[end] = arr[end], arr[start]
                end -= 1
            else:
                start += 1
        return arr


if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    print(Solution.rearrange_positive_and_negative(arr))
