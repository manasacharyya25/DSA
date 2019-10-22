""" Geeksforgeeks Practice Problem:
    https://practice.geeksforgeeks.org/problems/cutted-segments/0
"""

class Solution:
    @staticmethod
    def get_max_cut_segments(n, arr):
        N = [i for i in range(n+1)]
        arr.insert(0,0)

        dp = [[0 for j in range(len(N))] for i in range(len(arr))]

        for i in range(1, len(arr)):
            for j in range(1, n+1):
                if arr[i] > N[j]:
                    dp[i][j] = dp[i-1][j]
                else:
                    if ( j-arr[i] == 0 ) or (dp[i][j-arr[i]] != 0):
                        dp[i][j] = max(1 + dp[i][j-arr[i]], dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]

        print(dp[-1][-1])

if __name__=="__main__":
    t = int(input())

    while t > 0:
        t-=1

        n = int(input())

        arr = list(map(int, input().strip().split()))

        Solution.get_max_cut_segments(n, arr)

