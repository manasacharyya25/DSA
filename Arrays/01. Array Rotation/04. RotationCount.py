#
# Find Rotation Count for a given Rotated Sorted Array. (Clockwise and Anti-Clockwise)
#
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
#


class Solution:
    @staticmethod
    def rotation_count(arr, direction):
        start = 0
        end = len(arr)-1

        # If Array already Sorted, No rotation. Return 0 Rotation Count
        if arr[end] > arr[start]:
            return 0

        while end >= start:
            mid = start + (end-start)//2

            if arr[mid] > arr[mid+1]:
                inf_point = mid+1
                break

            if arr[mid] < arr[mid-1]:
                inf_point = mid
                break

            if arr[mid] > arr[start]:
                start = mid+1
            else:
                end = mid-1

        if direction == 'clockwise':
            return inf_point

        if direction == 'anti-clockwise':
            return len(arr) - inf_point


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 0, 1, 2, 3, 4]
    print("Clockwise Roation Count : ",
          Solution.rotation_count(arr, 'clockwise'))
    print("Anti-Clockwise Roation Count : ",
          Solution.rotation_count(arr, 'anti-clockwise'))
