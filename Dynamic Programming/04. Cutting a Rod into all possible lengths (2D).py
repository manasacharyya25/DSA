"""NOT SOLVED
"""

class Solution:
    @staticmethod
    def max_selling_price(length_of_rod, price_of_each_length):
        length_array = [i for i in range(length_of_rod+1)]
        price_of_each_length.insert(0, 0)
        dp = [[0 for i in range(lenght_of_rod+1)] for j in range(lenght_of_rod+1)]

        for i in range(1, length_of_rod+1):
            for j in range(1, length_of_rod+1):
                if length_array[i] > length_array[j]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(price_of_each_length[i]+dp[i][j-i], dp[i-1][j])
        
        return dp[-1][-1]

if __name__=="__main__":
    t = int(input())

    while t>0:
        t-=1

        lenght_of_rod = int(input())
        price_of_each_length = list(map(int, input().strip().split()))

        print(Solution.max_selling_price(lenght_of_rod, price_of_each_length))