"""
    For any nos of friends say 4:
        One way is that an element decides to stay single. So we have rest (4-1) elements tht can either pair up or stay single in f(4-1) ways

        If one element decides to pair up, we can have following scenarios:
            1,2 [3,4]
            1,3 [2,4]
            1,4 [2,3]

            ie, (4-1)*f(4-2) ways

            therefor total no of ways :     f(n-1) + (n-1)*f(n-2)
"""


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

        return dp[n] % (pow(10, 9)+7)


if __name__ == "__main__":
    t = int(input())

    while t > 0:
        t -= 1

        n = int(input())

        print(Solution.get_number_of_ways(n))
