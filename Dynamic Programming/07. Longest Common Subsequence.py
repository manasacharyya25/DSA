"""
    Geeksforgeeks Practice Problem:
    https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
"""
class Solution:
    @staticmethod
    def get_length_of_lcs(n1, n2, str1, str2):
        dp = [[0 for j in range(n1+1)] for i in range(n2+1)]

        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if str2[i-1] == str1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print( dp[-1][-1])

if __name__=="__main__":
    t = int(input())

    while t>0:
        t-=1

        n1, n2 = tuple(map(int, input().strip().split(' ')))
        str1 = input()
        str2 = input()
        
        Solution.get_length_of_lcs(n1, n2, str1, str2)
