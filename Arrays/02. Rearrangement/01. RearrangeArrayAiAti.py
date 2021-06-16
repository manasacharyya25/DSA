#
# Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.
#
# https://www.geeksforgeeks.org/rearrange-array-arri/


class Solution:
    @staticmethod
    def rearrange_using_hashmap(arr):
        """ Time Complexity: O(n)
            Space Complexity: O(max(arr))
        """
        M = max(arr)
        result = [-1 for i in range(M+1)]

        for x in arr:
            if x >= 0:
                result[x] = x
        return result

    @staticmethod
    def rearrange_inplace(arr):
        """ Time Complexity: O(n)
            Space Complexity: O(1)
        """
        start = 0
        end = len(arr)

        while start < end:
            # Ignore Negative Values, Continue to next element
            if arr[start] < 0:
                start += 1
                continue

            # If element already at correct place, Continue to next element
            if arr[start] == start:
                start += 1
                continue

            # If element not at correct place, Swap with corret position and continue from same location
            arr[arr[start]], arr[start] = arr[start], arr[arr[start]]

        return arr


if __name__ == '__main__':
    arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
           11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

    arr2 = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

    print(Solution.rearrange_inplace(arr))
    print(Solution.rearrange_inplace(arr2))
