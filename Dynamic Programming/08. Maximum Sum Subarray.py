"""
    Geeksforgeeks
    https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
"""


class Solution:
    @staticmethod
    def get_max_sum_subarray(n, arr):
        if n == 1:
            print(arr[0])
            return

        max_sum = arr

        for i in range(1, n):
            max_sum[i] = max(arr[i], arr[i] + max_sum[i - 1])

        print(max(max_sum))
        return


if __name__ == "__main__":
    t = int(input())

    while t > 0:
        t -= 1

        n = int(input())

        arr = list(map(int, input().strip().split(' ')))

        Solution.get_max_sum_subarray(n, arr)
