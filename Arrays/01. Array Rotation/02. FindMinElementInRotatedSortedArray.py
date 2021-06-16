#
# Find Minimum Element ( Also the Pivot Element ) of a Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/

class Solution:
    @staticmethod
    def findMinElement(arr):
        start = 0
        end = len(arr)-1

        while end >= start:

            # if array not rotated, return first element
            if arr[end] > arr[start]:
                return arr[start]

            mid = start + (end-start)//2

            # if mid element > mid+1 element, return mid+1 element
            if arr[mid] > arr[mid+1]:
                return arr[mid+1]

            # if mid elemnt < mid-1 element, return mid element
            if arr[mid] < arr[mid-1]:
                return arr[mid]

            # if mid element > start element, implies pivot element is to right of mid
            if arr[mid] > arr[start]:
                start = mid+1
            else:
                end = mid-1


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    print(Solution.findMinElement(arr))
