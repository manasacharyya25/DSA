"""
 HackerRank Problem :  https://www.hackerrank.com/challenges/coin-change/problem
"""


import math
import os
import random
import re
import sys

def getWays(n, c):
    N = list(range(0, n+1))
    c.insert(0, 0)

    dp = [[0 for i in range(len(N))] for j  in range(len(c))]

    for j in range(len(N)):
        dp[0][j] = 0

    for i in range(len(c)):
        dp[i][0] = 1

    for i in range(1,len(c)):
        for j in range(1, len(N)):
            if c[i] > N[j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j - c[i]] + dp[i-1][j]

    return dp[len(c)-1][n]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    ways = getWays(n, c)

    print(ways)
