"""
    Geeksforgeeks Practice
    https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
"""


class Solution:
    @staticmethod
    def get_lis(n, arr):
        lis = [1 for i in range(n)]

        for j in range(1, n):
            for i in range(0, j):
                if arr[i] < arr[j]:
                    lis[j] = max(lis[j], lis[i] + 1)

        return lis[-1]

if __name__ == "__main__":
    t = int(input())

    while t > 0:
        t-=1

        n = int(input())

        arr = list(map(int, input().strip().split(' ')))

        print(Solution.get_lis(n, arr))
