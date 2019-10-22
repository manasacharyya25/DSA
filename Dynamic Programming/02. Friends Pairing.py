class Solution:
    @staticmethod
    def get_number_of_ways(n: int) -> int:
        dp = [0]*(n+1)
        
        if n > 0:
            dp[1] = 1

        if n > 1:
            dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + (i-1)*dp[i-2]

        return dp[n]%(pow(10,9)+7)

if __name__=="__main__":
    t = int(input())

    while t > 0:
        t-=1

        n = int(input())

        print(Solution.get_number_of_ways(n))

