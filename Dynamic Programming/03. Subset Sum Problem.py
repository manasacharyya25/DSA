class Solution:
    @staticmethod
    def if_sum_exists(arr, n):
        arr.insert(0, 0)
        dp = [[0 for j in range(n+1)] for i in range(len(arr))]
        N = [i for i in range(n+1)]

        for i in range(len(arr)):
            dp[i][0] = 1

        for i in range(1, len(arr)):
            for j in range(1, n+1):
                if arr[i] > N[j]:
                    #Since arr[i] can't be used, we check if sum: N[i] can be calculated from elements encounter till now dp[i-1][j]
                    dp[i][j] = dp[i-1][j] 
                else:
                    dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]

        return dp[len(arr)-1][n]

if __name__=="__main__":
    t = int(input())

    while t > 0:
        t-=1
        arr = list(map(int, input().strip().split()))
        n = int(input())

        print(Solution.if_sum_exists(arr, n))

