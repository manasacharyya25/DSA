"""
    LeetCode
    https://leetcode.com/problems/counting-bits/
"""
from typing import List

class Solution:
    @staticmethod
    def countBits(num: int) -> List[int]:
        dp = [i for i in range(num+1)]
        
        dp[0] = 0
        
        if num > 0:
            dp[1] = 1
    
        if num > 1:
            dp[2] = 1
        
        if num > 2:
            for i in range(3, num+1):
                if i%2 == 1:
                    dp[i] = dp[int(i/2)] + 1
                else:
                    dp[i] = dp[int(i/2)]
                
        return dp

if __name__ == "__main__":
    num = int(input())

    print(Solution.countBits(num))